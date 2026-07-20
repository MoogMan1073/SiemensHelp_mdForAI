---
title: "Using S7-1500T Kinematics functions (S7-1500T)"
package: TFTOSMCKinenUS
topics: 284
devices: [S7-1500T]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Using S7-1500T Kinematics functions (S7-1500T)

This section contains information on the following topics:

- [Overview of functions (S7-1500T)](#overview-of-functions-s7-1500t)
- [S7-1500T Motion Control KinPlus (S7-1500T)](#s7-1500t-motion-control-kinplus-s7-1500t)
- [Mapping kinematics in the project (S7-1500T)](#mapping-kinematics-in-the-project-s7-1500t)
- [Kinematics functions (S7-1500T)](#kinematics-functions-s7-1500t)
- [3D visualization (S7-1500T)](#3d-visualization-s7-1500t)
- [Commissioning (S7-1500T)](#commissioning-s7-1500t)
- [Diagnostics (S7-1500T)](#diagnostics-s7-1500t)
- [Kinematics trace (S7-1500T)](#kinematics-trace-s7-1500t)
- [Calibration (S7-1500T)](#calibration-s7-1500t)
- [Tags of the technology object data blocks (S7-1500T)](#tags-of-the-technology-object-data-blocks-s7-1500t)

## Overview of functions (S7-1500T)

This section contains information on the following topics:

- [Kinematics systems for handling tasks (S7-1500T)](#kinematics-systems-for-handling-tasks-s7-1500t)
- [Kinematics technology object with up to 4 interpolating kinematics axes (S7-1500T)](#kinematics-technology-object-with-up-to-4-interpolating-kinematics-axes-s7-1500t)
- [Motion control instructions for kinematics control (S7-1500T)](#motion-control-instructions-for-kinematics-control-s7-1500t)
- [Functions in STEP 7 (S7-1500T)](#functions-in-step-7-s7-1500t)
- [Configuration limits for kinematics systems (S7-1500T)](#configuration-limits-for-kinematics-systems-s7-1500t)

### Kinematics systems for handling tasks (S7-1500T)

Kinematics are user-programmable mechanical systems in which multiple mechanically coupled axes produce the motion of a working point. The S7‑1500T technology CPUs provide functions for controlling kinematics systems, e.g. for handling tasks, with the kinematics technology object. Typical applications include:

- Pick &amp; Place
- Installation
- Palletizing

The kinematics control panel and extensive online and diagnostic functions support straightforward commissioning of kinematics systems. The kinematics technology object is fully integrated in the system diagnostics of the S7-1500T CPU.

### Kinematics technology object with up to 4 interpolating kinematics axes (S7-1500T)

![Figure](images/121909341451_DV_resource.Stream@PNG-de-DE.png)

The kinematics technology object calculates motion setpoints for the tool center point (TCP) of the kinematics taking into account the dynamic settings. The kinematics technology object calculates the motion setpoints for the individual axes of the kinematics and vice versa from the current values of the axes using the kinematics transformation. The kinematics technology object outputs the axis-specific motion setpoints to the interconnected positioning axes.

The kinematics technology object provides the [kinematics transformation](#brief-description-of-the-kinematics-transformation-s7-1500t) for the predefined kinematics types on the system level. In the case of user-defined kinematics systems, you must provide the [user transformation](#user-transformation-without-jcs-s7-1500t) in a separate program.

You create the individual axes of the kinematics in the TIA Portal as "Positioning axis" or "Synchronous axis" technology objects. When you configure the kinematics technology object, you interconnect the axes in accordance with the configured kinematics type.

You can find an overview of the functions of the kinematics technology object in the section "[Motion control instructions for kinematics control](#motion-control-instructions-for-kinematics-control-s7-1500t)".

The graphic below shows the basic principle of operation of the kinematics technology object with up to four interpolating kinematics axes:

![Figure](images/165435267723_DV_resource.Stream@PNG-en-US.png)

#### Configuration

The following configurations are available in the kinematics technology object:

- Basic parameters

  - [Kinematics](#supported-kinematics-types-s7-1500t)
  - [Units of measure](#units-of-measure-s7-1500t)
- Interconnections

  - [Interconnecting kinematics axes](#configuring-and-interconnecting-kinematics-axes-s7-1500t)
  - [Mechanical axis coupling](#mechanical-axis-coupling-for-kinematics-types-with-up-to-four-interpolating-kinematics-axes-s7-1500t)
- [Geometry](#kinematics-types-s7-1500t)
- [Conveyor tracking](#conveyor-tracking-s7-1500t)
- Dynamics

  - [Presets and limits](#motion-dynamics-s7-1500t)
  - [Dynamic adaptation](#dynamic-adaptation-s7-1500t)
- Kinematics coordinate system, object coordinate systems and tools

  - [Coordinate systems and frames](#coordinate-systems-and-frames-s7-1500t-1)
  - [Kinematics types with up to four interpolating kinematics axes](#kinematics-types-with-up-to-four-interpolating-kinematics-axes-s7-1500t)
  - [Offset and rotation of the coordinate system](#offset-and-rotation-of-the-coordinate-system-s7-1500t)
- [Zones](#zone-monitoring-s7-1500t)
- [Job sequence](#job-sequence-s7-1500t)

### Motion control instructions for kinematics control (S7-1500T)

You execute the functions of the kinematics technology object using the Motion Control instructions in your user program or the TIA Portal (under "Technology object &gt; Commissioning").

The following table shows the motion control instructions that are supported by the kinematics technology object:

| Motion control instruction | Brief description |
| --- | --- |
| **Kinematics motions** |  |
| "[MC_GroupInterrupt](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_groupinterrupt-interrupt-motion-execution-v8-s7-1500t)" | Interrupt motion execution |
| "[MC_GroupContinue](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_groupcontinue-continue-motion-execution-v8-s7-1500t)" | Continue motion execution |
| "[MC_GroupStop](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_groupstop-stop-motion-v8-s7-1500t)" | Stop motion |
| "[MC_MoveLinearAbsolute](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_movelinearabsolute-position-kinematics-with-linear-path-motion-v8-s7-1500t)" | Position kinematics with linear path motion |
| "[MC_MoveLinearRelative](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_movelinearrelative-relative-positioning-of-kinematics-with-linear-path-motion-v8-s7-1500t)" | Relative positioning of kinematics with linear path motion |
| "[MC_MoveCircularAbsolute](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_movecircularabsolute-position-kinematics-with-circular-path-motion-v8-s7-1500t)" | Position kinematics with circular path motion |
| "[MC_MoveCircularRelative](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_movecircularrelative-relative-positioning-of-kinematics-with-circular-path-motion-v8-s7-1500t)" | Relative positioning of kinematics with circular path motion |
| "[MC_MoveDirectAbsolute](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_movedirectabsolute-absolute-movement-of-kinematics-with-synchronous-point-to-point-motion-v8-s7-1500t)" | Absolute movement of kinematics with synchronous "point-to-point" motion |
| "[MC_MoveDirectRelative](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_movedirectrelative-relative-movement-of-kinematics-with-synchronous-point-to-point-motion-v8-s7-1500t)" | Relative movement of kinematics with synchronous "point-to-point" motion |
| "[MC_TrackConveyorBelt](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_trackconveyorbelt-start-conveyor-tracking-v8-s7-1500t)" | Start conveyor tracking |
| "[MC_KinematicsMotionSimulation](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_kinematicsmotionsimulation-v8-s7-1500t)" | Start/end simulation of kinematics |
| **Zones** |  |
| "[MC_DefineWorkspaceZone](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_defineworkspacezone-define-workspace-zone-v8-s7-1500t)" | Define workspace zone |
| "[MC_DefineKinematicsZone](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_definekinematicszone-define-kinematics-zone-v8-s7-1500t)" | Define kinematics zone |
| "[MC_SetWorkspaceZoneActive](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_setworkspacezoneactive-activate-workspace-zone-v8-s7-1500t)" | Activate workspace zone |
| "[MC_SetWorkspaceZoneInactive](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_setworkspacezoneinactive-deactivate-workspace-zone-v8-s7-1500t)" | Deactivate workspace zone |
| "[MC_SetKinematicsZoneActive](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_setkinematicszoneactive-activate-kinematics-zone-v8-s7-1500t)" | Activate kinematics zone |
| "[MC_SetKinematicsZoneInactive](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_setkinematicszoneinactive-deactivate-kinematics-zone-v8-s7-1500t)" | Deactivate kinematics zone |
| **Tools** |  |
| "[MC_DefineTool](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_definetool-redefine-tool-v8-s7-1500t)" | Redefine tool |
| "[MC_SetTool](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_settool-change-active-tool-v8-s7-1500t)" | Change active tool |
| **Coordinate systems** |  |
| "[MC_SetOcsFrame](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_setocsframe-redefine-object-coordinate-systems-v8-s7-1500t)" | Redefine object coordinate systems |
| "[MC_KinematicsTransformation](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_kinematicstransformation-convert-axis-coordinates-to-cartesian-coordinates-v8-s7-1500t)" | Convert axis coordinates to Cartesian coordinates |
| "[MC_InverseKinematicsTransformation](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_inversekinematicstransformation-convert-cartesian-coordinates-to-axis-coordinates-v8-s7-1500t)" | Convert Cartesian coordinates to axis coordinates |

### Functions in STEP 7 (S7-1500T)

The following table shows the functions supported by the kinematics technology object in STEP 7:

| Functions in the TIA Portal | Brief description |
| --- | --- |
| [Kinematics control panel](#commissioning-s7-1500t) | - Active homing of the kinematics axes - Jog kinematics in WCS or OCS - Jog individual kinematics axes in MCS - Jog joints in the JCS |
| [Diagnostics](#diagnostics-s7-1500t) | Monitor and observe status and error messages of the kinematics technology object |
| [Kinematics trace](#kinematics-trace-s7-1500t) | - 3D visualization of the current motion of the tool center point (TCP) and the object coordinate systems (OCS) - Record, play back and save kinematics motions - Exporting and importing recordings |
| [Calibration](#calibration-s7-1500t) | - Determine exact position of object coordinate systems - Define workspace zones - Move tool center point offline in the 3D view using the directional pad - Move real kinematics online with the kinematics control panel |

### Configuration limits for kinematics systems (S7-1500T)

#### Motion control resources

Each CPU offers a defined set of "[Motion Control resources](S7-1500-S7-1500T%20Motion%20Control%20Overview%20%28S7-1500%2C%20S7-1500T%29.md#configuration-limits-s7-1500-s7-1500t)". For information on the total Motion Control resources available, refer to the technical specifications of the utilized CPU.

You can find an overview of the Motion Control resources of a CPU in the TIA Portal under "Tools &gt; Resources".

#### Extended Motion Control resources (S7-1500T)

In addition to the Motion Control resources of the interconnected axes, a kinematics technology object utilizes 30 "Extended Motion Control resources". For information on the maximum number of usable kinematics systems, refer to the technical specifications of the utilized CPU.

You can find the technical specifications of the S7-15xxT CPUs in the respective manual.

#### Application cycle

As the number of technology objects used increases, the computing time needed by the CPU to process the technology objects increases. The Motion Control application cycle can be adapted according to the number of technology objects used.

## S7-1500T Motion Control KinPlus (S7-1500T)

This section contains information on the following topics:

- [Product description "S7-1500T Motion Control KinPlus" (S7-1500T)](#product-description-s7-1500t-motion-control-kinplus-s7-1500t)
- [Kinematics technology object with more than 4 interpolating kinematics axes (S7-1500T)](#kinematics-technology-object-with-more-than-4-interpolating-kinematics-axes-s7-1500t)
- [SIMATIC Memory Card S7-1500T Motion Control KinPlus (S7-1500T)](#simatic-memory-card-s7-1500t-motion-control-kinplus-s7-1500t)
- [Version overview for "S7-1500T Motion Control KinPlus" (S7-1500T)](#version-overview-for-s7-1500t-motion-control-kinplus-s7-1500t)

### Product description "S7-1500T Motion Control KinPlus" (S7-1500T)

The Motion Control package "S7-1500T Motion Control KinPlus" enables you to control kinematics with 5 or 6 interpolating axes. These functions are not included in the firmware of a technology CPU due to export law.

#### Supported kinematics types

"S7-1500T Motion Control KinPlus" extends the kinematics technology object to include the following kinematics types:

- Cartesian portal with 2 orientations A, B
- 6-axis articulated arm with central hand
- Delta picker with 2 orientations A, B
- User-defined kinematics 3D with 3 orientations

#### Supported CPUs

"S7-1500T Motion Control KinPlus" can be used on the following CPUs:

- CPU 1507D TF with SINAMICS S120 Integrated
- CPU 1518T-4 PN/DP
- CPU 1518TF-4 PN/DP

Simulation with PLCSIM and PLCSIM Advanced is not supported.

#### How it works

The Motion Control package "S7-1500T Motion Control KinPlus" contains the full Motion Control firmware with the function extensions. The Motion Control functions for kinematics with up to 4 axes and all other Motion Control functions, such as homing or synchronous operation, are also loaded from the Motion Control package "S7-1500T Motion Control KinPlus".

The Motion Control package must be copied to a SIMATIC Memory Card of the type "S7-1500T Motion Control KinPlus". The firmware with the function extensions is loaded from this card in runtime.

![How it works](images/154297668235_DV_resource.Stream@PNG-en-US.png)

#### Type of delivery

The SIMATIC Memory Card for "S7-1500T Motion Control KinPlus" is available with the following storage capacity:

| Product | Article number |
| --- | --- |
| S7-1500T Motion Control KinPlus **2 GB** | 6ES7 954-8LP80-0AA0 |
| S7-1500T Motion Control KinPlus **32 GB** | 6ES7 954-8LT80-0AA0 |

Motion Control package "S7-1500T Motion Control KinPlus" is available as a software download via Online Software Delivery (OSD).

| Product | Article number |
| --- | --- |
| S7-1500T Motion Control KinPlus package as software download | 6ES7 823-0KE01-1AA0 |

#### Important export information

Due to existing export restrictions for software, with respect to certain controller functions (more than 4 interpolating axes), the European/German export list classifies the product "S7-1500T Motion Control KinPlus" as a dual-use good with label AL=2D002 and ECCN=N.

When using "S7-1500T Motion Control KinPlus", special attention must be paid that the obligation to obtain authorization also exists when components requiring authorization are exported as part of service delivery, spare parts delivery and software upgrade/software update delivery. This applies, in particular, when the software has been exported by the machine manufacture after installation in the machine.

This can lead to severe restrictions on providing services due to the length of the official authorization process.

General information:

For certain components, an obligation exists to obtain authorization for reexport according to U.S. law. This must also be heeded. Information on the obligation to obtain authorization for delivered components can be found in the delivery documents:

Goods labeled with AL not equal to N are subject to European or German export authorization when being exported from the EU. Goods labeled with ECCN not equal to N are subject to U.S. reexport authorization.

Even without a label, or with label AL=N or ECCN=N, authorization may be required due to the final whereabouts and purpose for which the goods are to be used.

In the event of a purchase agreement, the fulfillment of the agreement on the part of Siemens is subject to there being no obstacle to fulfillment due to national or international foreign trade law or embargos and/or other sanctions.

Customers are subsequently responsible for the lawful handling.

### Kinematics technology object with more than 4 interpolating kinematics axes (S7-1500T)

If a SIMATIC Memory Card with the Motion Control package "S7-1500T Motion Control KinPlus" is plugged into the CPU, the kinematics technology object calculates the motion setpoints for the tool center point for kinematics with more than 4 kinematics axes. The kinematics technology object calculates the motion setpoints for the individual axes of the kinematics and vice versa from the current values of the axis using the kinematics transformation. The dynamic specifications are included in all calculations. The kinematics technology object outputs the axis-specific motion setpoints to the interconnected positioning or synchronous axes.

For the predefined kinematics types, the [kinematic transformation](#kinematics-transformation-s7-1500t) is part of the kinematics technology object. For the user-defined kinematics 3D with 3 orientations, you need to provide the kinematics transformation in a separate program.

You create the individual axes of the kinematics in the TIA Portal as "Positioning axis" or "Synchronous axis" type technology objects. When you configure the kinematics technology object, you interconnect the axes in accordance with the configured kinematics type.

The following graphic shows the basic function of the kinematics technology object when using S7-1500T Motion Control KinPlus:

![Figure](images/166648227851_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Mechanical axis couplings |
| ② | Offsets  Inverted direction of movement  Transformation |
| ③ | Status, joint traversing range limits |

For kinematics with more than 4 kinematics axes, the joint coordinate system (JCS) represents the mechanical positions of the kinematics joints, while the MCS displays the axis positions. The joint coordinates can be specified as target coordinates for sPTP motions.

#### Configuration

In the kinematics technology object, the following configurations are available for kinematics types with more than 4 kinematics axes:

- Basic parameters

  - [Kinematics](#supported-kinematics-types-s7-1500t)
  - [Units of measure](#units-of-measure-s7-1500t)
- Interconnections

  - [Interconnecting kinematics axes](#configuring-and-interconnecting-kinematics-axes-s7-1500t)
  - [Mechanical axis coupling](#mechanical-axis-coupling-for-kinematics-types-with-more-than-four-interpolating-kinematics-axes-s7-1500t)
  - [Joints](#joints-s7-1500t)
- [Geometry](#defining-the-zone-geometry-s7-1500t)
- [Conveyor tracking](#conveyor-tracking-s7-1500t)
- Dynamics

  - [Presets and limits](#configuring-dynamics-for-the-kinematics-and-the-orientation-motion-s7-1500t)
  - [Dynamic adaptation](#dynamic-adaptation-s7-1500t)
- Kinematics coordinate system, object coordinate systems and tools

  - [Coordinate systems and frames](#coordinate-systems-and-frames-s7-1500t)
  - [Kinematics types with more than four kinematics axes](#kinematics-types-with-more-than-four-kinematics-axes-s7-1500t)
  - [Offset and rotation of the coordinate system](#offset-and-rotation-of-the-coordinate-system-s7-1500t)
- [Zones](#configuring-zones-s7-1500t)
- [Job sequence](#job-sequence-s7-1500t)

#### Motion Control instructions

All Motion Control instructions supported by the kinematics technology object can also be used for kinematics with more than 4 interpolating axes.

You can find more information under [Motion control instructions for kinematics control](#motion-control-instructions-for-kinematics-control-s7-1500t).

#### Functions in STEP 7

The following table shows the functions supported by S7-1500T Motion Control KinPlus in STEP 7:

| Functions in the TIA Portal | Brief description |
| --- | --- |
| [Kinematics control panel](#commissioning-s7-1500t) | - Active homing of the kinematics axes - Jog kinematics in WCS or OCS - Jog individual kinematics axes in MCS - Jog joints in the JCS |
| [Diagnostics](#diagnostics-s7-1500t) | Monitor and observe status and error messages of the kinematics technology object |
| [Kinematics trace](#kinematics-trace-s7-1500t) | - 3D visualization of the current motion of the tool center point (TCP) and the object coordinate systems (OCS) - Record, play back and save kinematics motions - Exporting and importing recordings |
| [Calibration](#calibration-s7-1500t) | - Determine exact position of object coordinate systems - Define workspace zones - Move tool center point offline in the 3D view using the directional pad - Move real kinematics online with the kinematics control panel |

### SIMATIC Memory Card S7-1500T Motion Control KinPlus (S7-1500T)

The SIMATIC Memory Card with the Motion Control package "S7-1500T Motion Control KinPlus" is marked with "S7-1500T MC KinPlus".

![Figure](images/158380598155_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | Slider for setting write protection:  - Slider up: not write-protected - Slider down: write-protected |
| ② | Memory size |
| ③ | Article number |
| ④ | Serial number |
| ⑤ | Production version |

The card can contain the Motion Control package "S7-1500T Motion Control KinPlus" and all files that are also on a normal SIMATIC Memory Card.

You can find more information about using the SIMATIC Memory Card in the function manual "[Structure and Use of the CPU Memory](https://support.industry.siemens.com/cs/ww/en/view/59193101)".

#### Enable Motion Control package "S7-1500T Motion Control KinPlus"

The SIMATIC Memory Card does not contain a Motion Control package "S7-1500T Motion Control KinPlus" in the following situations:

- The card is still unused.
- All versions have been deleted.
- The card has been formatted via the TIA Portal or the CPU display.

**Procedure**

The required Motion Control package "S7-1500T Motion Control KinPlus" with the file name "6ES7 823-0KI20-1AA0 V08.00.00.upd" is available as an OSD download.

1. Load the zip file containing the Motion Control package "S7-1500T Motion Control KinPlus".
2. Create the folder "\MCRC\" on the SIMATIC Memory Card.
3. Copy the file "6ES7 823-0KI20-1AA0 V08.00.00.upd" into the folder "\MCRC\" ("Motion Control Runtime Component") on the SIMATIC Memory Card. Copy the file to the SIMATIC Memory Card using a card reader or the SIMATIC web server. You can only use the file on a SIMATIC Memory Card with the label "MC KinPlus".
4. To activate the Motion Control package on the CPU, insert the SIMATIC Memory Card into the SIMATIC CPU. After POWER OFF → POWER ON of the CPU, the firmware extension is loaded and can be used as long as the card is inserted.

#### Show loaded Motion Control package

To check if the firmware extension "S7-1500T Motion Control KinPlus" has been loaded successfully, check the current Motion Control package.

You can find the version and type of the loaded Motion Control package via the following options:

- Under Online and Diagnostics &gt; General in the Motion Control Package Information area.
- In the diagnostic buffer in the event description for the loaded version
- In the display of the CPU under Overview &gt; Motion Control Package Information
- In the web server on the page Diagnostics &gt; Motion Control Package Information

If the Motion Control package "S7-1500T Motion Control KinPlus" is successfully loaded, "Package name: MC KinPlus" is displayed. The version and internal version of the Motion Control package is also displayed. If "Package name: MC Base" is displayed, the Motion Control package "S7-1500T Motion Control KinPlus" is not loaded.

#### Upgrade the Motion Control package

To upgrade the Motion Control package, copy the new UPD file into the folder "\MCRC\". The UPD file with the highest version from the folder "\MCRC\" is always loaded during the startup of the CPU. The version of the Motion Control package is included in the file name. The newest version is always loaded if there are several versions of the Motion Control package "S7-1500T Motion Control KinPlus" on the card.

#### Delete data on the card

To preserve the possibility of restoring an earlier version, save the existing file on another data medium before deleting it.

To free up memory on the SIMATIC Memory Card, delete Motion Control package files with earlier versions if you have copied different versions of the Motion Control package to the card.

#### Format SIMATIC Memory Card

Formatting the SIMATIC Memory Card deletes the Motion Control package "S7-1500T Motion Control KinPlus".

Before formatting the SIMATIC Memory Card, save the Motion Control package file on an external data medium.

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Memory card unusable**   Formatting the SIMATIC Memory Card via Windows applications makes it unusable.  Format the memory card exclusively via the TIA Portal or the display of the CPU. |  |

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Motion Control package "S7-1500T Motion Control KinPlus" deleted**  If you select the option to format the SIMATIC Memory Card when restoring the factory settings for the module, the Motion Control package "S7-1500T Motion Control KinPlus" is deleted.  Before you restore the factory settings for the module and format the SIMATIC Memory Card, save the Motion Control package file on an external data medium. |  |

#### CPU replacement

If you replace the CPU, you only have to plug the SIMATIC Memory Card "S7-1500T Motion Control KinPlus" into a new device with compatible firmware. You can find the version overview in the "[Kinematics technology object with more than 4 interpolating kinematics axes](#kinematics-technology-object-with-more-than-4-interpolating-kinematics-axes-s7-1500t)" section.

### Version overview for "S7-1500T Motion Control KinPlus" (S7-1500T)

The following table shows with which firmware version of the CPU and with which version of the Motion Control package "S7-1500T Motion Control KinPlus" can be used.

| CPU firmware version | Version Motion Control package "S7-1500T Motion Control KinPlus" |
| --- | --- |
| V3.1 | V8.0 |
| V3.0 | V7.0 |

## Mapping kinematics in the project (S7-1500T)

This section contains information on the following topics:

- [Term definition (S7-1500T)](#term-definition-s7-1500t)
- [Legend for representation of the kinematics (S7-1500T)](#legend-for-representation-of-the-kinematics-s7-1500t)
- [Coordinate systems and frames (S7-1500T)](#coordinate-systems-and-frames-s7-1500t)
- [Supported kinematics types (S7-1500T)](#supported-kinematics-types-s7-1500t)
- [Units of measure (S7-1500T)](#units-of-measure-s7-1500t)
- [Configuring and interconnecting kinematics axes (S7-1500T)](#configuring-and-interconnecting-kinematics-axes-s7-1500t)
- [Mechanical axis coupling (S7-1500T)](#mechanical-axis-coupling-s7-1500t)
- [Joints (S7-1500T)](#joints-s7-1500t)
- [Kinematics types (S7-1500T)](#kinematics-types-s7-1500t)
- [Kinematics transformation (S7-1500T)](#kinematics-transformation-s7-1500t)

### Term definition (S7-1500T)

#### Kinematics

Kinematics are user-programmable mechanical systems in which multiple mechanically coupled axes produce the motion of a working point.

#### Kinematics axes

Kinematics axes are the axes of the kinematics motion. You connect each kinematics axis with a positioning axis/synchronous axis technology object.

#### Kinematics zero point (KZP)

The coordinate origin of the kinematics coordinate system (KCS) is the KZP. You configure the geometry parameters of the kinematics starting from the KZP.

#### Zero point of the flange coordinate system (FNP)

The coordinate origin of the flange coordinate system (FCS) is the FNP. Starting from the FNP, you define, for example, the flange zones of the kinematics.

#### Tool center point (TCP)

The coordinate origin of the tool coordinate system (TCS) is the tool center point or TCP. The TCP is the operating point of the kinematics.

#### Degrees of freedom of kinematics

The degrees of freedom of kinematics are the dimensions in which the tool can move. 2D kinematics systems move the tool in the xz plane and thus have 2 translational degrees of freedom. 3D kinematics systems move the tool in xyz space and thus have 3 translational degrees of freedom. The optional orientation of the tool is 1 to 3 more degrees of freedom (rotations around the z, y and x axes).

#### Machine coordinate system (MCS)

The MCS contains the position data of the interconnected kinematics axes and thus combines up to six one-dimensional systems in one system.

#### Joint coordinate system (JCS)

The JCS contains the geometric positions of the kinematics joints. Joints can perform linear or rotary movements.

#### Job sequence

The job sequence of the kinematics technology object is the memory to which motion-related Motion Control jobs are entered as pending, waiting jobs. The job sequence allows the calculation of a velocity profile over several jobs.

#### AxesGroup

Kinematics-related Motion Control instructions have the input parameter "AxesGroup". Because the kinematics technology object groups the kinematics axes, you assign the kinematics technology object directly to the input parameter "AxesGroup".

#### Joint position space

Depending on the kinematics type, a kinematics can reach Cartesian coordinates via various joint positions. The [kinematics type](#kinematics-types-s7-1500t) defines the possible joint positions and the positive and negative joint position spaces. The joint position spaces are limited by the respective transformation areas.

#### Joint traversing range

The joint traversing range defines the minimum and maximum traversing position of a joint.

#### Target joint position range

A target joint position range defines the number of revolutions of a joint.

### Legend for representation of the kinematics (S7-1500T)

The following table shows the graphic elements and symbols used in the display of kinematics and coordinate systems:

| Graphic element | Meaning |
| --- | --- |
| ![Figure](images/158493456395_DV_resource.Stream@PNG-de-DE.png) | Basis of kinematics |
| ![Figure](images/158497505419_DV_resource.Stream@PNG-de-DE.png) | Kinematics arm |
| ![Figure](images/158497740043_DV_resource.Stream@PNG-de-DE.png) | Kinematics deflected from zero position |
| ![Figure](images/158497859467_DV_resource.Stream@PNG-de-DE.png) | Active rotary axis |
| ![Figure](images/158498017291_DV_resource.Stream@PNG-de-DE.png) | - Passive joint - Axis guide |
| ![Figure](images/158498136715_DV_resource.Stream@PNG-de-DE.png) | Active linear axis |
| ![Figure](images/158498281739_DV_resource.Stream@PNG-de-DE.png) | Rotary axis on the tool adapter |
| ![Figure](images/158659376651_DV_resource.Stream@PNG-de-DE.png) | Swivel axis |
| ![Figure](images/158498362763_DV_resource.Stream@PNG-de-DE.png) | Tool adapter |
| ![Figure](images/158498405387_DV_resource.Stream@PNG-de-DE.png) | Tool (gripper) |
| ![Figure](images/158498529035_DV_resource.Stream@PNG-de-DE.png) | Coordinate axis set up out of the mapping plane |
| ![Figure](images/158498512011_DV_resource.Stream@PNG-de-DE.png) | Coordinate axis set up into the mapping plane |
| ![Figure](images/158498584459_DV_resource.Stream@PNG-de-DE.png) | Color x axis |
| ![Figure](images/158498639883_DV_resource.Stream@PNG-de-DE.png) | Color y axis |
| ![Figure](images/158498669707_DV_resource.Stream@PNG-de-DE.png) | Color z axis |

### Coordinate systems and frames (S7-1500T)

This section contains information on the following topics:

- [Coordinate systems and frames (S7-1500T)](#coordinate-systems-and-frames-s7-1500t-1)
- [Kinematics types with up to four interpolating kinematics axes (S7-1500T)](#kinematics-types-with-up-to-four-interpolating-kinematics-axes-s7-1500t)
- [Kinematics types with more than four kinematics axes (S7-1500T)](#kinematics-types-with-more-than-four-kinematics-axes-s7-1500t)

#### Coordinate systems and frames (S7-1500T)

A handling task involves many objects, e.g. kinematics systems, tools, pallets and products. You describe these objects and their relative positions with coordinate systems and frames. The kinematics technology object calculates all motions for the tool center point (TCP).

##### Coordinate systems

The kinematics technology object uses the following right-handed Cartesian coordinate systems according to DIN 66217:

- World coordinate system (WCS)
- Kinematics coordinate system (KCS)
- Flange coordinate system (FCS)
- Tool coordinate system (TCS)
- Object coordinate systems (OCS)

The following graphic shows the relative position of the coordinate systems using a workspace example:

![Coordinate systems](images/158898281355_DV_resource.Stream@PNG-de-DE.png)

The position of the FCS and the TCS in the zero position of the kinematics is defined differently for the following kinematics types:

- [Kinematics types with up to four interpolating kinematics axes](#kinematics-types-with-up-to-four-interpolating-kinematics-axes-s7-1500t)
- [Kinematics types with more than four kinematics axes](#kinematics-types-with-more-than-four-kinematics-axes-s7-1500t)

##### World coordinate system (WCS)

The WCS is the fixed coordinate system of the environment or workspace of the kinematics. The zero point of the WCS is the reference point for objects and motions on the kinematics technology object. Starting from the zero point of the WCS (e.g. corner of a workspace), you define the position of the objects using frames.

##### Kinematics coordinate system (KCS)

The KCS is connected to the kinematics. The position of the KCS within the kinematics is specified for each predefined kinematics type. The coordinate origin of the KCS is the kinematics zero point (KZP). You configure the geometry parameters of the kinematics starting from the KZP.

You configure the position of the KCS in the WCS using the KCS frame.

##### Object coordinate system (OCS)

The OCS is a user-defined coordinate system. With an OCS, for example, you define the position of a pallet in the workspace. You define the position of the OCS in the WCS with an OCS frame. You can define up to 3 OCS frames which are active at the same time.

![Object coordinate system (OCS)](images/158898110731_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | OCS frame |

##### Frames

Frames specify the offset and rotation of one coordinate system relative to another coordinate system.

The following table shows the frames for the kinematics technology object:

| Frame | Description |
| --- | --- |
| KCS frame | Position of the kinematics coordinate system (KCS) in the world coordinate system (WCS) |
| Transformation frame | Position of the flange coordinate system (FCS) in the KCS  The transformation frame results from the kinematics transformation and is displayed in the "&lt;TO&gt;.FlangeInKcs" tag of the technology object. |
| Tool frame | Position of the tool coordinate system (TCS) in the FCS |
| OCS1..3 frame | Position of the object coordinate systems 1 to 3 (OCS1..3) in the WCS |

#### Kinematics types with up to four interpolating kinematics axes (S7-1500T)

##### Flange coordinate system (FCS)

The FCS is attached to the tool adapter (flange) of the kinematics. As a result, the position of the FCS changes with kinematics motions.

The position of the FCS in the zero position of the kinematics results from the configuration of the geometry parameters of the kinematics. The kinematics technology object calculates the transformation frame from the geometry parameters.

The transformation frame describes the position of the FCS in the KCS. The z axis of the FCS always points in the negative z direction of the KCS. A rotation of the FCS around z of the KCS is possible for kinematics types with orientation.

The following graphic shows the positions of the FCS and KCS and the transformation frame using the "Cylindrical robot" kinematics example:

![Flange coordinate system (FCS)](images/158824366091_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | KCS frame |
| ② | Transformation frame |

##### Tool coordinate system (TCS) and tool center point (TCP)

The TCS is attached to the FCS and defines the tool center point (TCP) in the coordinate origin. The TCP is the operating point of the tool. The kinematics motions always refer to the TCP (with reference to WCS/OCS). You define the position of the TCS in the FCS using a tool frame.

You can define tool frames for up to three tools, of which only one tool and one tool frame is active at the same time. The procedure for the definition of tool frames is described in the section ["Defining tool frames"](#define-tool-frames-s7-1500t).

The position of the TCS is defined at the target position reached for kinematics types with up to 4 interpolating axes as follows:

- The x direction of the TCS is the same as the x direction of the target position.
- The y direction of the TCS is opposite to the y direction of the target position.
- The z direction of the TCS always points in the negative z direction of the target position.

The following graphic shows the position of the TCS and the TCP in the workspace:

![Tool coordinate system (TCS) and tool center point (TCP)](images/158824361867_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | Tool frame |

The following graphic shows the position of the TCS before and after a kinematics motion:

![Tool coordinate system (TCS) and tool center point (TCP)](images/158645484555_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | TCS at initial position |
| ② | Kinematics motion to target position |
| ③ | TCS at the target position reached |

For kinematics types with orientation, the orientation is negative relative to the TCS and positive relative to the TCP or WCS.

#### Kinematics types with more than four kinematics axes (S7-1500T)

##### Flange coordinate system (FCS)

The FCS is attached to the tool adapter (flange) of the kinematics. As a result, the position of the FCS changes with kinematics motions.

The position of the FCS in the zero position of the kinematics results from the configuration of the geometry parameters of the kinematics. The kinematics technology object calculates the transformation frame from the geometry parameters.

The x axis of the FCS is defined in the outward direction of the flange normal vector. This means that the x axis of the FCS is also in the direction of the tool length vector if the tool frame of the TCS is defined without rotation.

In contrast to kinematics with up to four interpolating kinematics axes, the z axis of the FCS does not always point in the negative direction of the KCS.

The following graphic shows the positions of the FCS and KCS and the transformation frame of a kinematics with five kinematics axes using the "Delta picker 3D with 2 orientations A, B" kinematics as an example:

![Flange coordinate system (FCS)](images/158950591755_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | KCS frame |
| ② | Transformation frame |

The following graphic show the alignment of the FCS at other joint positions of the kinematics:

![Flange coordinate system (FCS)](images/158950595979_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | KCS frame |
| ② | Transformation frame |

![Flange coordinate system (FCS)](images/158950600203_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | KCS frame |
| ② | Transformation frame |
| ③ | Pivot |

##### Tool coordinate system (TCS - Tool Coordinate System) and tool center point (TCP - Tool Center Point)

The TCS is attached to the FCS and defines the tool center point (TCP) in the coordinate origin. The TCP is the operating point of the tool. The kinematics motions always refer to the TCP (with reference to WCS/OCS). You define the position of the TCS in the FCS using a tool frame.

You can define tool frames for up to three tools, of which only one tool and one tool frame is active at the same time. The procedure for the definition of tool frames is described in the section ["Defining tool frames"](#define-tool-frames-s7-1500t).

The position of the TCS is defined at the target position reached for kinematics types with more than 4 interpolating axes as follows:

- The x direction of the TCS is the same as the x direction of the target position.
- The y direction of the TCS is the same as the y direction of the target position.
- The z direction of the TCS is the same as the z direction of the target position.

The following graphic shows the position of the TCS and the TCP in the workspace:

![Tool coordinate system (TCS - Tool Coordinate System) and tool center point (TCP - Tool Center Point)](images/158950642827_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | Tool frame |

The following graphic shows the position of the TCS before and after a kinematics motion:

![Tool coordinate system (TCS - Tool Coordinate System) and tool center point (TCP - Tool Center Point)](images/158281630987_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | TCS at initial position |
| ② | Kinematics motion to target position |
| ③ | TCS at the target position reached |

### Supported kinematics types (S7-1500T)

The type of the mechanical system and the number of the axes determine the kinematics type. The mechanically coupled axes produce the motion of the tool center point (TCP). Depending on the kinematics type, you configure the kinematics using appropriate geometry parameters.

The kinematics technology object supports the following kinematics types:

| Category | Kinematics type |
| --- | --- |
| **Predefined kinematics systems** |  |
| [Cartesian portal](#cartesian-portal-s7-1500t) | Cartesian portal 2D |
| Cartesian portal 2D with orientation |  |
| Cartesian portal 3D |  |
| Cartesian portal 3D with orientation |  |
| Cartesian portal 3D with 2 orientations A, B<sup> 1)</sup> |  |
| [Roller picker](#roller-picker-s7-1500t) | Roller picker 2D |
| Roller picker 2D with orientation |  |
| Roller picker 3D (vertical) |  |
| Roller picker 3D with orientation (vertical) |  |
| Roller picker 3D with orientation (horizontal) |  |
| [SCARA](#scara-s7-1500t) | SCARA 2D with orientation |
| SCARA 3D with orientation |  |
| [Articulated arm](#articulated-arm-s7-1500t) | Articulated arm 2D |
| Articulated arm 2D with orientation |  |
| Articulated arm 3D |  |
| Articulated arm 3D with orientation |  |
| 6-axis articulated arm with central hand<sup> 1)</sup> |  |
| [Delta picker](#delta-picker-s7-1500t) | Delta picker 2D |
| Delta picker 2D with orientation |  |
| Delta picker 3D |  |
| Delta picker 3D with orientation |  |
| Delta picker 3D with 2 orientations A, B<sup> 1)</sup> |  |
| [Cylindrical robot](#cylindrical-robot-s7-1500t) | Cylindrical robot 3D |
| Cylindrical robot 3D with orientation |  |
| [Tripod](#tripod-s7-1500t) | Tripod 3D |
| Tripod 3D with orientation |  |
| **User-defined kinematics systems** |  |
| [User-defined kinematics systems](#user-defined-kinematics-systems-s7-1500t) | User-defined 2D |
| User-defined 2D with orientation A |  |
| User-defined 3D |  |
| User-defined 3D with orientation A |  |
| User-defined 3D with 3 orientations <sup>1)</sup> |  |
| <sup>1) </sup>S7-1500T Motion Control KinPlus |  |

### Units of measure (S7-1500T)

Select the units of measure available for the technology object from the drop-down lists.

Setting or changing the units of measurement affects the parameter values:

- Display of parameter values in the technology data block
- Assignment of parameters in the user program
- Input and display of the position and velocity in the TIA Portal

All information and displays correspond to the selected unit of measure.

The set units are displayed in the "&lt;TO&gt;.Units" tag structure of the technology object. The tag structure is described in the "["Units" tag (kinematics)](#units-tag-kinematics-s7-1500t)" section.

**Position and velocity**

The following table shows the supported units of measure for position and velocity of linear axes:

| Position | Velocity |
| --- | --- |
| nm, μm, mm<sup>1)</sup>, m, km | mm/s<sup>1)</sup>, mm/min, mm/h, m/s, m/min, m/h, km/min, km/h |
| in, ft, mi | in/s, in/min, ft/s, ft/min, mi/h |
| <sup>1)</sup> Six decimal places when the option box "Use position values with higher resolution" is selected. |  |

The following table shows the supported units of measure for angle and angular velocity of rotational axes:

| Angle | Angular velocity |
| --- | --- |
| °<sup>1)</sup>, rad | °/s<sup>1)</sup>, °/min, rad/s, rad/min |
| <sup>1)</sup> Six decimal places when the option box "Use position values with higher resolution" is selected. |  |

**Acceleration**

The acceleration is set accordingly as the position/s² (angle/s²) unit of measure.

**Jerk**

The jerk is set as the position/s³ (angle/s³) unit of measure.

#### Units of measure of the axes and the kinematics technology object

The technology objects always transfer values without units of measure.

For example, if you set [mm] for an axis and [m] for the kinematics technology object, the kinematics technology object miscalculates the position values of the linear axis in [m]. If, in this example, the kinematics technology object outputs a setpoint for a one-meter motion, the axis only moves by one millimeter.

The kinematics technology object outputs linear and rotary setpoints to the interconnected axes according to the kinematics type. The kinematics technology object does not check the axis type of the interconnected axis (linear or rotary).

Configure the units of measure as follows:

- Configure the interconnected technology objects as linear or rotary axes according to the kinematics type.
- Configure the same linear/rotary units of measure for the axes interconnected according to the kinematics type as for the kinematics technology object.
- Configure the same units of measure on the interconnected axes for all linear axes and for all rotary axes.

#### Position values with higher resolution

If you select the "Use position values with higher resolution" check box in the configuration of the positioning axis, synchronous axis, external encoder and kinematics technology objects, six decimal places are available in the selected unit, instead of the standard three. Due to the LREAL format, the representable position and angle range in [mm] and [°] is limited to +/- 1.0E09. You can then only use the units mm, mm/s, ° and °/s. If you have previously configured other units, these will automatically be changed to the unit "mm, mm/s, ° or °/s".

The following values are reduced by a factor of 1000 for position values with a higher resolution:

- Displayable position range
- Displayable angular range
- Mechanical gear ratio
- Numerical traversing range with regard to long-term stability
- Dynamic values for velocity, acceleration and deceleration

### Configuring and interconnecting kinematics axes (S7-1500T)

This section contains information on the following topics:

- [Brief description (S7-1500T)](#brief-description-s7-1500t)
- [Configuring kinematics axes (S7-1500T)](#configuring-kinematics-axes-s7-1500t)
- [Interconnecting kinematics axes (S7-1500T)](#interconnecting-kinematics-axes-s7-1500t)

#### Brief description (S7-1500T)

You can interconnect a kinematics technology object with positioning axes and synchronous axes. There must be a clear reference between the kinematics technology object and the interconnected axes. You cannot use a second kinematics technology object with already interconnected axes.

Depending on the kinematics type, you need 2 to 6 positioning axes or synchronous axes, which you interconnect with the kinematics.

Depending on the kinematics type, the following kinematics axes are relevant:

| Kinematics type | Kinematics axis |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| A1 | A2 | A3 | A4 | A5<sup> 1)</sup> | A6<sup> 1)</sup> |  |
| 2D | ✓ | ✓ | - | - | - | - |
| 2D with orientation | ✓ | ✓ | - | ✓ | - | - |
| 3D | ✓ | ✓ | ✓ | - | - | - |
| 3D with orientation | ✓ | ✓ | ✓ | ✓ | - | - |
| 3D with 2 orientations A, B<sup> 1)</sup> | ✓ | ✓ | ✓ | ✓ | ✓ | - |
| 3D with 3 orientations<sup> 1)</sup> | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 6-axis articulated arm with central hand<sup> 1)</sup> |  |  |  |  |  |  |
| ✓ Relevant  -  Not relevant   <sup> 1)</sup> Only with S7-1500T Motion Control KinPlus |  |  |  |  |  |  |

#### Configuring kinematics axes (S7-1500T)

This section contains information on the following topics:

- [Brief description (S7-1500T)](#brief-description-s7-1500t-1)
- [Modulo setting (S7-1500T)](#modulo-setting-s7-1500t)
- [Axis in simulation/virtual axis (S7-1500T)](#axis-in-simulationvirtual-axis-s7-1500t)

##### Brief description (S7-1500T)

Configure the following basic parameters of the axes depending on the kinematics used:

- Select the axis type according to the kinematics axes for the [kinematics type](#kinematics-types-s7-1500t) used
- Set [Modulo setting](#modulo-setting-s7-1500t) according to the kinematics type used or the interconnected kinematics axis

The following additional basic parameters are relevant for the interconnected kinematics axes:

- [Axis in simulation/virtual axis](#axis-in-simulationvirtual-axis-s7-1500t)
- [Units of measure](#units-of-measure-s7-1500t)

##### Modulo setting (S7-1500T)

###### Modulo setting

The kinematics technology object itself has no modulo setting. When you interconnect axes with active modulo setting to the kinematics technology object, the modulo range of the axes must cover at least the traversing range of the kinematics.

For the kinematics types with up to 4 interpolating axes, the zero position of the axis must correspond to the zero position of the kinematics axis. The Modulo range of the kinematics axes A1, A2 and A3 cannot be changed during a kinematics motion.

For the Cartesian orientations, you can specify an angle greater than 360°. A relative motion traverses this angle. An absolute motion maps this angle in the following ranges:

- A = -180° to 179.999°

The following ranges for the orientation are defined in addition for kinematics types with more than four interpolating kinematics axes:

- B = -90° to 90°
- C = -180° to 179,999°

For kinematics types with more than four interpolating kinematics axes, the "Modulo" setting should not be enabled for the axes A4, A5 and A6.

##### Axis in simulation/virtual axis (S7-1500T)

###### Axis in simulation/virtual axis

You can also interconnect the kinematics technology object with [axes in simulation](Using%20S7-1500-S7-1500T%20Axis%20functions%20%28S7-1500%2C%20S7-1500T%29.md#axis-in-simulation-s7-1500-s7-1500t) and [virtual axes](Using%20S7-1500-S7-1500T%20Axis%20functions%20%28S7-1500%2C%20S7-1500T%29.md#virtual-axis-s7-1500-s7-1500t).

#### Interconnecting kinematics axes (S7-1500T)

Interconnect the axes of kinematics in the "Interconnections" configuration window.

##### Kinematics axes

In the drop-down lists, select the desired axes depending on the [kinematics type](#kinematics-types-s7-1500t). Positioning axes and synchronous axes which are already created in the project are shown in the drop-down lists. Axes that are already interconnected are also visible in the drop-down lists but cannot be interconnected twice.

No provision is made for changing the interconnection of the axes during operation.

You directly call the configuration of the selected technology object using the ![Kinematics axes](images/134670054155_DV_resource.Stream@PNG-de-DE.png) button. Configure the interconnected technology objects [according to the kinematics type](#configuring-kinematics-axes-s7-1500t).

### Mechanical axis coupling (S7-1500T)

This section contains information on the following topics:

- [Mechanical axis coupling for kinematics types with up to four interpolating kinematics axes. (S7-1500T)](#mechanical-axis-coupling-for-kinematics-types-with-up-to-four-interpolating-kinematics-axes-s7-1500t)
- [Mechanical axis coupling for kinematics types with more than four interpolating kinematics axes (S7-1500T)](#mechanical-axis-coupling-for-kinematics-types-with-more-than-four-interpolating-kinematics-axes-s7-1500t)
- [Tags: Mechanical axis coupling (S7-1500T)](#tags-mechanical-axis-coupling-s7-1500t)

#### Mechanical axis coupling for kinematics types with up to four interpolating kinematics axes. (S7-1500T)

If the position of a kinematics axis changes due to the motion of another kinematics axis, these two axes are mechanically coupled. Mechanical couplings between two kinematics axes can arise for reasons of construction. For example, if the kinematics axis A4 of the "SCARA" kinematics is coupled to the spindle of a linear axis, the orientation changes due to the motion of the linear axis.

> **Note**
>
> If you set a mechanical axis coupling for a first axis to a second axis, the setting "Modulo" must not be activated for the first axis.

The kinematics transformation compensates for the mechanical couplings with a compensation factor. You specify the mechanical couplings and respective compensation factor depending on the kinematics type during configuration of the kinematics.

You can configure the mechanical axis coupling for the following kinematics types:

- [SCARA 2D with orientation](#scara-2d-with-orientation-s7-1500t)
- [SCARA 3D with orientation](#scara-3d-with-orientation-s7-1500t)
- [Articulated arm 2D](#articulated-arm-2d-s7-1500t)
- [Articulated arm 2D with orientation](#articulated-arm-2d-with-orientation-s7-1500t)
- [Articulated arm 3D](#articulated-arm-3d-s7-1500t)
- [Articulated arm 3D with orientation](#articulated-arm-3d-with-orientation-s7-1500t)
- [Cylindrical robot 3D with orientation](#cylindrical-robot-3d-with-orientation-s7-1500t)

You can find additional information on the setting and the compensation factor in the description of the kinematics type used.

#### Mechanical axis coupling for kinematics types with more than four interpolating kinematics axes (S7-1500T)

Mechanical axis couplings of two axes mean that when the "&lt;TO&gt;.AxisCoupling.N[1].CausingAxis" axis moves by a distance or an angle, the position of another joint also changes without the coupled axis "&lt;TO&gt;.AxisCoupling.N[1].AffectedAxis" or the motor of the axis. The motor encoder of the coupled axis "&lt;TO&gt;.AxisCoupling.N[1].AffectedAxis" does not detect any change in position.

##### Configuring the mechanical axis coupling

If there are mechanical axis couplings, configure them in the "Interconnections" configuration window of the kinematics.

The coupling factor defines the position change of the tracked joint in relation to the position change of the moved axis.

The coupling factor &lt;TO&gt;.AxisCoupling.N[1..5].Factor defines the position change of the coupled axis "&lt;TO&gt;.AxisCoupling.N[1].AffectedAxis" in relation to the position change of the coupled axis "&lt;TO&gt;.AxisCoupling.N[1].CausingAxis".

The coupling factor is defined as a quotient, but the two position items do not need to be identical. The position changes are specified in a numerical value (without unit) of the position unit of the kinematics axis.

![Configuring the mechanical axis coupling](images/158065754763_DV_resource.Stream@PNG-en-US.png)

**Example 1**

When the axis A4 is moved by +90°, the joint J4 is moved by +90° and joint J5 is moved by 9° along with it, even though axis A5 does not move. This results in a coupling factor between axis A4 and axis A5 of:

![Configuring the mechanical axis coupling](images/152883976203_DV_resource.Stream@PNG-en-US.png)

**Example 2**

When the axis A4 is moved by 90°, the joint J4 is moved by 90°. The joint J5 is not affected. There is no mechanical coupling between axis A4 and axis A5.

**Example 3**

When the axis A4 is moved by 90°, the joint J4 is moved by 90° and joint J5 is also moved by -0.9 mm, even though axis A5 does not move. This results in a coupling factor between axis A4 and axis A5 of:

![Configuring the mechanical axis coupling](images/152884031883_DV_resource.Stream@PNG-en-US.png)

> **Note**
>
> The coupling factor for kinematics with joint coordinate system (JCS) behaves inversely to the compensation factor of kinematics without joint coordinate system.

##### Determining coupling factors

You have the following options to determine the coupling factors:

- Determination based on the mechanical data of the kinematics
- Detection of the position change at the affected axis via an external measuring system with movement of the axis "&lt;TO&gt;.AxisCoupling.N[1..5].CausingAxis"
- Determination based on position change of the affected joint

**Determination based on position change of the affected joint**

Follow these steps to determine the coupling factor using the position change of the affected joint:

1. Move the affected joint into the zero position.
2. Move the coupled joint via the assigned axis by a defined distance or an angle, e.g. by 5°. The axis moves by 5° in this case when the direction of movement of the joint is not inverted.
3. Jog the axis "&lt;TO&gt;.AxisCoupling.N[1..5].CausingAxis" so that the coupled axis is moved again in the mechanical zero position without the motor of the affected axis moving.
4. You calculate the axis coupling factor from the moved position change of the axis "&lt;TO&gt;.AxisCoupling.N[1..5].CausingAxis" from step 3 and the known position change of the coupled axis "&lt;TO&gt;.AxisCoupling.N[1..5].AffectedAxis" (5°) from step 2.

> **Note**
>
> **Traversing coupled axis with sPTP motion**
>
> For coupled axes with coupling factor ≠ 1, the traversing of joints in the JCS with an sPTP motion can result in compensation motions of the coupled axes.

> **Note**
>
> **Jogging joints in the JCS**
>
> For coupled axes with coupling factor ≠ 1, the jogging of joints in the JCS can result in an unwanted position change of the coupled axes.

#### Tags: Mechanical axis coupling (S7-1500T)

For the mechanical axis coupling for kinematics types with more than four interpolating kinematics axes, the following tags of the kinematics technology object are relevant:

| Tag | Description |
| --- | --- |
| **Configuration of the mechanical axis coupling** |  |
| &lt;TO&gt;.AxisCoupling.N[1..5].Enable | Enabling/disabling the mechanical axis coupling |
| &lt;TO&gt;.AxisCoupling.N[1..5].CausingAxis | Coupling axis |
| &lt;TO&gt;.AxisCoupling.N[1..5].AffectedAxis | Coupled axis |
| &lt;TO&gt;.AxisCoupling.N[1..5].Factor | Coupling factor |

### Joints (S7-1500T)

This section contains information on the following topics:

- [Joint coordinate system (JCS) (S7-1500T)](#joint-coordinate-system-jcs-s7-1500t)
- [Configuring joints (S7-1500T)](#configuring-joints-s7-1500t)
- [Tags: Joints (S7-1500T)](#tags-joints-s7-1500t)

#### Joint coordinate system (JCS) (S7-1500T)

The joint coordinate system (JCS) represents the real mechanical positions of the kinematics joints.

##### Functions

The JCS offers the following functions:

- Display current positions, velocities and accelerations of the joints of a kinematics
- Direct movement of the joints of a kinematics without moving mechanically coupled joints
- Traversing range limit of the joints by defining a [joint traversing range](#define-joint-traversing-range-s7-1500t)
- Specification of the joint position ranges of a kinematics system on sPTP jobs
- Setting of zero point and counting direction of the joints

##### Setpoint calculation at the kinematics

The following diagram shows the kinematics transformation, the calculation of the joint coordinates (in the JCS) and the calculation of the axis coordinates (in the MCS):

![Setpoint calculation at the kinematics](images/156126771595_DV_resource.Stream@PNG-en-US.png)

#### Configuring joints (S7-1500T)

This section contains information on the following topics:

- [Configuring joints (S7-1500T)](#configuring-joints-s7-1500t-1)
- [Inverting the joint direction (S7-1500T)](#inverting-the-joint-direction-s7-1500t)
- [Define joint traversing range (S7-1500T)](#define-joint-traversing-range-s7-1500t)
- [Monitoring of the joint traversing range (S7-1500T)](#monitoring-of-the-joint-traversing-range-s7-1500t)
- [Defining an offset (S7-1500T)](#defining-an-offset-s7-1500t)

##### Configuring joints (S7-1500T)

Configure the joints of the kinematics in the "Joints" configuration window.

##### Inverting the joint direction (S7-1500T)

The defined directions of movement of the joints of a kinematics are described in the section "[Kinematics types](#kinematics-types-s7-1500t)". These directions of movement are used in the kinematics transformation.

The direction of movement of the joints can be defined for different mechanics inversely to the defined directions of movement of the kinematics types.

If the direction of travel of a joint of the real kinematics is inverse to the direction of travel of the joint defined in the kinematics type from Siemens, select the check box "Direction inverted" for the joint.

The inversion of the direction of movement is calculated by the technology object after the kinematics transformation.

The following diagram shows an example of a kinematics 6-axis articulated arm with central hand, where the inverse direction of movement is required for the joint J1:

![Figure](images/158917667851_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | Definition of the direction of motion on the kinematics type |
| ② | Definition of the direction of movement at the kinematics used |
| ③ | Positive direction of movement joint 1 |
| ④ | Negative direction of movement joint 1 |

> **Note**
>
> Then check whether the direction of movement of the joint matches the direction of movement of the kinematics axis, e.g. by jogging in the MCS. If the direction of the joint and the axis direction are inverse, invert the encoder and drive direction of the kinematics axis.

##### Define joint traversing range (S7-1500T)

The joint traversing range defines the permitted traversing range of a kinematics joint. By defining the joint traversing range, you prevent a mechanical endstop or joint positions from being approached when these are not permitted.

In the "Joints" configuration window, define the joint traversing range by entering the lower and upper limits.

Configure the limits of the joint traversing range in such a way that the joint has a sufficient deceleration distance and comes to a standstill in the permissible traversing range.

> **Note**
>
> The software limit switches of the kinematics axes are independent of the configured joint traversing range. You can define the joint traversing range greater than, equal to or less than the axis traversing range.

##### Monitoring of the joint traversing range (S7-1500T)

Depending on the job, monitoring of the joint traversing range is already active when the job is issued or becomes active during the active job.

| Job | Checking of the joint coordinates during the motion preparation in the MC_LookAhead | Cyclic checking of the joint coordinates during the active job |
| --- | --- | --- |
| - [MC_MoveLinearAbsolute](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_movelinearabsolute-position-kinematics-with-linear-path-motion-v8-s7-1500t) - [MC_MoveLinearRelative](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_movelinearrelative-relative-positioning-of-kinematics-with-linear-path-motion-v8-s7-1500t) - [MC_MoveCircularAbsolute](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_movecircularabsolute-position-kinematics-with-circular-path-motion-v8-s7-1500t) - [MC_MoveCircularRelative](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_movecircularrelative-relative-positioning-of-kinematics-with-circular-path-motion-v8-s7-1500t) | - | ✓ |
| - [MC_MoveDirectAbsolute](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_movedirectabsolute-absolute-movement-of-kinematics-with-synchronous-point-to-point-motion-v8-s7-1500t) - [MC_MoveDirectRelative](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_movedirectrelative-relative-movement-of-kinematics-with-synchronous-point-to-point-motion-v8-s7-1500t) | ✓ | ✓ |
| Single axis job | - | - |

###### Alarm response when leaving the joint position area

When a joint crosses the upper or lower limit of the joint traversing range, the 820 technology alarm is output. The kinematics motion is canceled, and the axes stop with the maximum dynamic values configured for the axes (alarm response: Stop with maximum dynamic values of the axes).

To return to the joint traversing range, move the joint via a single-axis job, e.g. with an "[MC_MoveAbsolute](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_moveabsolute-position-axis-absolutely-v8-s7-1500-s7-1500t)", "[MC_MoveRelative](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_moverelative-position-axis-relatively-v8-s7-1500-s7-1500t)", or "[MC_MoveJog](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_movejog-move-axis-in-jog-mode-v8-s7-1500-s7-1500t)" job.

##### Defining an offset (S7-1500T)

The offset describes the difference of the defined zero position of the joint of the [kinematics type](#kinematics-types-s7-1500t) and the mechanical zero position of the joint at the kinematics used.

If the zero position of the mechanics axis does not match the zero position of the kinematics type, configure an offset.

**Example**

The joint J2 is in the mechanical zero position. This mechanical zero position deviates by 30° in positive direction of rotation from the defined zero position of the kinematics type. The defined zero position of the kinematics type used for the kinematics transformation is staggered by -30°. The offset is configured with "&lt;TO&gt;.Joint.J[2].Offset" = -30°.

![Figure](images/156111240075_DV_resource.Stream@PNG-en-US.png)

> **Note**
>
> When homing the associated kinematics axis, ensure that the mechanical zero point of the joint matches the position 0.0 of the kinematics axis.

#### Tags: Joints (S7-1500T)

When configuring the joints for kinematics types with more than four interpolating kinematics axes, the following tags of the kinematics technology object are relevant:

| Tag | Description |
| --- | --- |
| **Configuration of joints** |  |
| &lt;TO&gt;.Joint.J[1..6].InverseDirection | Invert direction of movement |
| &lt;TO&gt;.Joint.J[1..6].Offset | Difference between the defined zero position of the joint of the [kinematics type](#kinematics-types-s7-1500t) and the mechanical zero position of the joint at the kinematics used |
| &lt;TO&gt;.Joint.J[1..6].LowerLimit | Lower limit of the joint traversing range |
| &lt;TO&gt;.Joint.J[1..6].UpperLimit | Upper limit of the joint traversing range |
| **Setpoints of the kinematics motion for the joints** |  |
| &lt;TO&gt;.JointData.J[1..6].Acceleration | Current acceleration setpoint |
| &lt;TO&gt;.JointData.J[1..6].Position | Current position setpoint |
| &lt;TO&gt;.JointData.J[1..6].Velocity | Current velocity setpoint |

### Kinematics types (S7-1500T)

This section contains information on the following topics:

- [Cartesian portal (S7-1500T)](#cartesian-portal-s7-1500t)
- [Roller picker (S7-1500T)](#roller-picker-s7-1500t)
- [SCARA (S7-1500T)](#scara-s7-1500t)
- [Articulated arm (S7-1500T)](#articulated-arm-s7-1500t)
- [Delta picker (S7-1500T)](#delta-picker-s7-1500t)
- [Cylindrical robot (S7-1500T)](#cylindrical-robot-s7-1500t)
- [Tripod (S7-1500T)](#tripod-s7-1500t)
- [User-defined kinematics systems (S7-1500T)](#user-defined-kinematics-systems-s7-1500t)

#### Cartesian portal (S7-1500T)

This section contains information on the following topics:

- [Cartesian portal 2D (S7-1500T)](#cartesian-portal-2d-s7-1500t)
- [Cartesian portal 2D with orientation (S7-1500T)](#cartesian-portal-2d-with-orientation-s7-1500t)
- [Cartesian portal 3D (S7-1500T)](#cartesian-portal-3d-s7-1500t)
- [Cartesian portal 3D with orientation (S7-1500T)](#cartesian-portal-3d-with-orientation-s7-1500t)
- [Cartesian portal 3D with 2 orientations A, B (S7-1500T)](#cartesian-portal-3d-with-2-orientations-a-b-s7-1500t)
- [Tags: Cartesian portal (S7-1500T)](#tags-cartesian-portal-s7-1500t)

##### Cartesian portal 2D (S7-1500T)

The "Cartesian portal 2D" kinematics support 2 axes and 2 degrees of freedom. The following graphic shows the principal configuration and the typical working area of the kinematics:

![Figure](images/158539381003_DV_resource.Stream@PNG-de-DE.png)

The kinematics consists of 2 orthogonal linear axes A1 and A2. The axes enclose a rectangular working range.

###### Coordinate systems and zero position

The graphic below shows the following in the front view:

- The position of the axes and the coordinate systems KCS and FCS
- The zero position of the kinematics
- The positive deflection of the kinematics is indicated (dashed)

![Coordinate systems and zero position](images/158539872907_DV_resource.Stream@PNG-de-DE.png)

|  |  |  |
| --- | --- | --- |
| ![Coordinate systems and zero position](images/158499650955_DV_resource.Stream@PNG-de-DE.png) | Zero position of the kinematics |  |
| L1 | With axis A1 in the zero position:  Distance of the FCS to the KZP in x direction of the KCS |  |
| L2 | With axis A2 in the zero position:  Distance of the FCS to the KZP and flange length LF in z direction of the KCS |  |
| LF | Flange length before the FCS in the z direction of the KCS |  |
| ![Coordinate systems and zero position](images/158499655179_DV_resource.Stream@PNG-de-DE.png) | Deflection of the kinematics |  |
| x<sub>1</sub> | Deflection of axis A1 in the positive x direction |  |
| z<sub>1</sub> | Deflection of axis A2 in the positive z direction |  |
| [Legend for representation of the kinematics](#legend-for-representation-of-the-kinematics-s7-1500t) |  |  |

The kinematics coordinate system (KCS) with the kinematics zero point (KZP) is located at the base of the kinematics. The flange coordinate system (FCS) is located at distance LF from the zero position of axis A2.

The position 0.0 on the respective interconnected technology object defines the zero position of axes A1 and A2. You define the position of the FCS with axes A1 and A2 in the zero position using lengths L1 and L2. You shift the FCS in the negative z direction of the KCS using length LF.

###### Transformation area

The kinematics transformation covers the entire [traversing range](#traversing-range-and-transformation-area-s7-1500t) of the axes.

###### Joint position space

No arm positioning spaces for the kinematics.

##### Cartesian portal 2D with orientation (S7-1500T)

The "Cartesian portal 2D with orientation" kinematics supports 3 axes and 3 degrees of freedom. The following graphic shows the principal configuration and the typical working area of the kinematics:

![Figure](images/158539878411_DV_resource.Stream@PNG-de-DE.png)

The kinematics consists of the following axes:

- 2 orthogonal linear axes A1 and A2
- 1 rotary axis A4 with rotation around z in the KCS

The linear axes enclose a rectangular working area. The kinematics axis A4 enables rotation of the tool around z in the KCS.

###### Coordinate systems and zero position

The graphic below shows the following in the front view:

- The position of the axes and the coordinate systems KCS and FCS
- The zero position of the kinematics
- The positive deflection of the kinematics is indicated (dashed)

![Coordinate systems and zero position](images/158540037515_DV_resource.Stream@PNG-de-DE.png)

|  |  |  |
| --- | --- | --- |
| ![Coordinate systems and zero position](images/158499650955_DV_resource.Stream@PNG-de-DE.png) | Zero position of the kinematics |  |
| L1 | With axis A1 in the zero position:  Distance of the FCS to the KZP in x direction of the KCS |  |
| L2 | With axis A2 in the zero position:  Distance of the FCS to the KZP and flange length LF in z direction of the KCS |  |
| LF | Flange length before the FCS in the z direction of the KCS |  |
| ![Coordinate systems and zero position](images/158499655179_DV_resource.Stream@PNG-de-DE.png) | Deflection of the kinematics |  |
| x<sub>1</sub> | Deflection of axis A1 in the positive x direction |  |
| z<sub>1</sub> | Deflection of axis A2 in the positive z direction |  |
| [Legend for representation of the kinematics](#legend-for-representation-of-the-kinematics-s7-1500t) |  |  |

The kinematics coordinate system (KCS) with the kinematics zero point (KZP) is located at the base of the kinematics. The flange coordinate system (FCS) is located at distance LF from the zero position of axis A2.

The position 0.0 on the respective interconnected technology object defines the zero position of axes A1 and A2. You define the position of the FCS with axes A1 and A2 in the zero position using lengths L1 and L2. You shift the FCS in the negative z direction of the KCS using length LF. In the zero position of axis A4, the x axis of the FCS points in the direction of the x axis of the KCS.

###### Transformation area

The kinematics transformation covers the entire [traversing range](#traversing-range-and-transformation-area-s7-1500t) of the axes.

###### Joint position space

No arm positioning spaces for the kinematics.

##### Cartesian portal 3D (S7-1500T)

The "Cartesian portal 3D" kinematics supports 3 axes and 3 degrees of freedom. The following graphic shows the principal configuration and the typical working area of the kinematics:

![Figure](images/158540043019_DV_resource.Stream@PNG-de-DE.png)

The kinematics consists of 3 orthogonal linear axes A1, A2 and A3. The linear axes enclose a rectangular working area.

###### Coordinate systems and zero position

The graphic below shows the following in the front view (xz plane):

- The position of the axes and the coordinate systems KCS and FCS
- The zero position of the kinematics
- The positive/negative deflection of the axes A1 and A3 is indicated (dashed)

![Coordinate systems and zero position](images/158540138123_DV_resource.Stream@PNG-de-DE.png)

|  |  |  |
| --- | --- | --- |
| ![Coordinate systems and zero position](images/158499650955_DV_resource.Stream@PNG-de-DE.png) | Zero position of the kinematics |  |
| L1 | With axis A1 in the zero position:  Distance of the FCS to the KZP in x direction of the KCS |  |
| L3 | With axis A3 in the zero position:  Distance of the FCS to the KZP and flange length LF in z direction of the KCS |  |
| LF | Flange length before the FCS in the z direction of the KCS |  |
| ![Coordinate systems and zero position](images/158499655179_DV_resource.Stream@PNG-de-DE.png) | Deflection of the kinematics |  |
| x<sub>1</sub> | Deflection of axis A1 in the positive x direction |  |
| z<sub>1</sub> | Deflection of axis A3 in the positive z direction |  |
| [Legend for representation of the kinematics](#legend-for-representation-of-the-kinematics-s7-1500t) |  |  |

The graphic below shows the following in the top view (xy plane):

- The position of the axes and the coordinate systems KCS and FCS
- The zero position of the kinematics
- The positive/negative deflection of the axes A1 and A2 is indicated (dashed)

![Coordinate systems and zero position](images/158540143627_DV_resource.Stream@PNG-de-DE.png)

|  |  |  |
| --- | --- | --- |
| ![Coordinate systems and zero position](images/158499650955_DV_resource.Stream@PNG-de-DE.png) | Zero position of the kinematics |  |
| L1 | With axis A1 in the zero position:  Distance of the FCS to the KZP in x direction of the KCS |  |
| L2 | With axis A2 in the zero position:  Distance of the FCS to the KZP in y direction of the KCS |  |
| ![Coordinate systems and zero position](images/158499655179_DV_resource.Stream@PNG-de-DE.png) | Deflection of the kinematics |  |
| x<sub>1</sub> | Deflection of axis A1 in the positive x direction |  |
| y<sub>1</sub> | Deflection of axis A2 in the negative y direction |  |
| [Legend for representation of the kinematics](#legend-for-representation-of-the-kinematics-s7-1500t) |  |  |

The kinematics coordinate system (KCS) with the kinematics zero point (KZP) is located at the base of the kinematics. The flange coordinate system (FCS) is located at distance LF from the zero position of axis A2.

Position 0.0 on the respective interconnected technology object defines the zero position of axes A1, A2, and A3. You define the position of the FCS with axes A1, A2, and A3 in the zero position using lengths L1, L2 and L3. You shift the FCS in the negative z direction of the KCS using length LF.

###### Transformation area

The kinematics transformation covers the entire [traversing range](#traversing-range-and-transformation-area-s7-1500t) of the axes.

###### Joint position space

No arm positioning spaces for the kinematics.

##### Cartesian portal 3D with orientation (S7-1500T)

The "Cartesian portal 3D with orientation" kinematics supports 4 axes and 4 degrees of freedom. The following graphic shows the principal configuration and the typical working area of the kinematics:

![Figure](images/158540149131_DV_resource.Stream@PNG-de-DE.png)

The kinematics consists of the following axes:

- 3 orthogonal linear axes A1, A2 and A3
- 1 rotary axis A4 with rotation around z in the KCS

The linear axes enclose a rectangular working area. The kinematics axis A4 enables rotation of the tool around z in the KCS.

###### Coordinate systems and zero position

The graphic below shows the following in the front view (xz plane):

- The position of the axes and the coordinate systems KCS and FCS
- The zero position of the kinematics
- The positive/negative deflection of the axes A1 and A3 is indicated (dashed)

![Coordinate systems and zero position](images/158540282635_DV_resource.Stream@PNG-de-DE.png)

|  |  |  |
| --- | --- | --- |
| ![Coordinate systems and zero position](images/158499650955_DV_resource.Stream@PNG-de-DE.png) | Zero position of the kinematics |  |
| L1 | With axis A1 in the zero position:  Distance of the FCS to the KZP in x direction of the KCS |  |
| L3 | With axis A3 in the zero position:  Distance of the FCS to the KZP and flange length LF in z direction of the KCS |  |
| LF | Flange length before the FCS in the z direction of the KCS |  |
| ![Coordinate systems and zero position](images/158499655179_DV_resource.Stream@PNG-de-DE.png) | Deflection of the kinematics |  |
| x<sub>1</sub> | Deflection of axis A1 in the positive x direction |  |
| z<sub>1</sub> | Deflection of axis A3 in the positive z direction |  |
| [Legend for representation of the kinematics](#legend-for-representation-of-the-kinematics-s7-1500t) |  |  |

The graphic below shows the following in the top view (xy plane):

- The position of the axes and the coordinate systems KCS and FCS
- The zero position of the kinematics
- The positive/negative deflection of the axes A1 and A2 is indicated (dashed)

![Coordinate systems and zero position](images/158540288139_DV_resource.Stream@PNG-de-DE.png)

|  |  |  |
| --- | --- | --- |
| ![Coordinate systems and zero position](images/158499650955_DV_resource.Stream@PNG-de-DE.png) | Zero position of the kinematics |  |
| L1 | With axis A1 in the zero position:  Distance of the FCS to the KZP in x direction of the KCS |  |
| L2 | With axis A2 in the zero position:  Distance of the FCS to the KZP in y direction of the KCS |  |
| ![Coordinate systems and zero position](images/158499655179_DV_resource.Stream@PNG-de-DE.png) | Deflection of the kinematics |  |
| x<sub>1</sub> | Deflection of axis A1 in the positive x direction |  |
| y<sub>1</sub> | Deflection of axis A2 in the negative y direction |  |
| [Legend for representation of the kinematics](#legend-for-representation-of-the-kinematics-s7-1500t) |  |  |

The kinematics coordinate system (KCS) with the kinematics zero point (KZP) is located at the base of the kinematics. The flange coordinate system (FCS) is located at distance LF from the zero position of axis A2.

Position 0.0 on the respective interconnected technology object defines the zero position of axes A1, A2, and A3. You define the distances of the zero positions of the axes A1, A2 and A3 to the kinematics zero point using the lengths L1, L2 and L3. You shift the FCS in the negative z direction of the KCS using length LF. In the zero position of axis A4, the x axis of the FCS points in the direction of the x axis of the KCS.

###### Transformation area

The kinematics transformation covers the entire [traversing range](#traversing-range-and-transformation-area-s7-1500t) of the axes.

###### Joint position space

No arm positioning spaces for the kinematics.

##### Cartesian portal 3D with 2 orientations A, B (S7-1500T)

The "Cartesian portal 3D with 2 orientations A, B" kinematics supports 5 axes and 5 degrees of freedom. For this kinematics type, you need the Motion Control package ["S7-1500T Motion Control KinPlus"](#s7-1500t-motion-control-kinplus-s7-1500t).

The following graphic shows the principal configuration and the typical working area of the kinematics:

![Figure](images/158544837643_DV_resource.Stream@PNG-de-DE.png)

The kinematics consists of the following axes:

- 3 orthogonal linear axes A1, A2 and A3
- One rotary axis A4 rotating around the z axis of the KCS
- One rotary swivel axis A5, which rotates around the y axis of the KCS in the kinematics zero position.

The linear axes enclose a rectangular working area.

###### Coordinate systems and zero position

The graphic below shows the following in the front view (xz plane):

- The position of the axes and the coordinate systems KCS and FCS
- The zero position of the kinematics
- The positive deflection of axes A1 and A3 and the negative deflection of axis A5 are indicated (dashed)

![Coordinate systems and zero position](images/158158155275_DV_resource.Stream@PNG-de-DE.png)

|  |  |  |
| --- | --- | --- |
| ![Coordinate systems and zero position](images/158499650955_DV_resource.Stream@PNG-de-DE.png) | Zero position of the kinematics |  |
| L1 | With axis A1 in the zero position:  Distance of the zero position of axis A1 to the KZP in the x direction of the KCS |  |
| L3 | With axis A3 in the zero position:  Distance of the zero position of axis A3 to the KZP in the z direction of the KCS. |  |
| LF | Flange length before the FCS in the x direction of the FCS |  |
| L4 | Distance of the joint points of rotational axis A4 and swivel axis A5 in the x direction of the KCS in the kinematics zero position |  |
| ![Coordinate systems and zero position](images/158499655179_DV_resource.Stream@PNG-de-DE.png) | Deflection of the kinematics |  |
| x<sub>1</sub> | Deflection of axis A1 in the positive x direction |  |
| z<sub>1</sub> | Deflection of axis A3 in the positive z direction |  |
| α5 | Negative deflection of swivel axis A5 when α5 = -45° |  |
| [Legend for representation of the kinematics](#legend-for-representation-of-the-kinematics-s7-1500t) |  |  |

The graphic below shows the following in the top view (xy plane):

- The position of the axes and the coordinate systems KCS and FCS
- The zero position of the kinematics
- The positive/negative deflection of the axes A1 and A2 is indicated (dashed)

![Coordinate systems and zero position](images/158199746955_DV_resource.Stream@PNG-de-DE.png)

|  |  |  |
| --- | --- | --- |
| ![Coordinate systems and zero position](images/158499650955_DV_resource.Stream@PNG-de-DE.png) | Zero position of the kinematics |  |
| L1 | With axis A1 in the zero position:  Distance of axis A3/A4 to the KZP in the x direction of the KCS |  |
| L2 | With axis A2 in the zero position:  Distance of the FCS to the KZP in the y direction of the KCS in the kinematics zero position. If axis A4 has been moved, the distance between KZP and FCS is no longer L2. |  |
| ![Coordinate systems and zero position](images/158499655179_DV_resource.Stream@PNG-de-DE.png) | Deflection of the kinematics |  |
| x<sub>1</sub> | Deflection of axis A1 in the positive x direction |  |
| y<sub>1</sub> | Deflection of axis A2 in the negative y direction |  |
| [Legend for representation of the kinematics](#legend-for-representation-of-the-kinematics-s7-1500t) |  |  |

The kinematics coordinate system (KCS) with the kinematics zero point (KZP) is located at the base of the kinematics. The flange coordinate system (FCS) is located at a distance from axis A5 in the negative z direction of the KCS.

Position 0.0 on the respective interconnected technology object defines the zero position of axes A1, A2, and A3. You define the distances of the zero positions of axes A1, A2, and A3 to the kinematics zero point using lengths L1, L2, and L3. You can also move the zero position of axes A1, A2, and A3 and the associated joints J1, J2, and J3 with [joint offsets](#defining-an-offset-s7-1500t). You shift the FCS in the negative z direction of the KCS using length LF.

In the zero position, the FCS is aligned in the following Cartesian position:

- x = L1 + L4
- y = L2
- z = L3-LF
- A = 0°
- B = 90°
- C = 0

In the zero position of axes A4 and A5, the x axis of the FCS points in the opposite direction of the z axis of the KCS. The y axis of the FCS points in the same direction as the y axis of the KCS. The z axis of the FCS points in the same direction as the x axis of the KCS.

###### Direction of travel of the joints

The following figure shows the direction of travel of the joints defined in the kinematics type.

![Direction of travel of the joints](images/171231498251_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | Front view |
| ② | Top view |
| ![Direction of travel of the joints](images/168814121867_DV_resource.Stream@PNG-de-DE.png) | Positive direction of rotation of the joints |

If the direction of travel of a joint of the real kinematics is inverse to the direction of travel of the joint defined in the kinematics type from Siemens, you must [invert the joint direction](#inverting-the-joint-direction-s7-1500t) in the configuration.

###### Transformation area

The kinematics transformation covers the entire [traversing range](#traversing-range-and-transformation-area-s7-1500t) of the axes.

###### Joint position space

No arm positioning spaces for the kinematics.

##### Tags: Cartesian portal (S7-1500T)

###### Cartesian portal 2D

You can define the 2D kinematics using the following tags of the technology object:

| Tags | Values | Description |
| --- | --- | --- |
| &lt;TO&gt;.Kinematics.TypeOfKinematics | 1 | Cartesian portal 2D |
| 2 | Cartesian portal 2D with orientation |  |
| &lt;TO&gt;.Kinematics.Parameter[1] | -1.0E12 to 1.0E12 | Distance L1 of the zero position of axis A1 to the kinematics zero point (KZP) in the x direction of the kinematics coordinate system (KCS) |
| &lt;TO&gt;.Kinematics.Parameter[2] | -1.0E12 to 1.0E12 | Distance LF of the FCS to axis A2 in the negative z direction of the KCS |
| &lt;TO&gt;.Kinematics.Parameter[3] | -1.0E12 to 1.0E12 | Distance L2 of the zero position of axis A2 to the KZP in the z direction of the KCS |

###### Cartesian portal 3D

You can define the 3D kinematics using the following tags of the technology object:

| Tags | Values | Description |
| --- | --- | --- |
| &lt;TO&gt;.Kinematics.TypeOfKinematics | 3 | Cartesian portal 3D |
| 4 | Cartesian portal 3D with orientation |  |
| 26 | Cartesian portal 3D with 2 orientations A, B |  |
| &lt;TO&gt;.Kinematics.Parameter[1] | -1.0E12 to 1.0E12 | Distance L1 of the zero position of axis A1 to the KZP in the x direction of the KCS |
| &lt;TO&gt;.Kinematics.Parameter[2] | -1.0E12 to 1.0E12 | Distance L2 of the zero position of axis A2 to the KZP in the y direction of the KCS |
| &lt;TO&gt;.Kinematics.Parameter[3] | -1.0E12 to 1.0E12 | - Distance LF of the FCS to axis A3 in the negative z direction of the KCS - Cartesian portal 3D with 2 orientations A, B:   Distance LF of the FCS to axis A5 |
| &lt;TO&gt;.Kinematics.Parameter[4] | -1.0E12 to 1.0E12 | Distance L3 of the zero position of axis A3 to the KZP in the z direction of the KCS |
| &lt;TO&gt;.Kinematics.Parameter[5] | -1.0E12 to 1.0E12 | Distance L4 of the joint points of rotational axis A4 and swivel axis A5 in the x direction of the KCS in the kinematics zero position<sup>1)</sup> |
| <sup>1) </sup>Only relevant for kinematics type "Cartesian portal 3D with 2 orientations A, B" |  |  |

---

**See also**

[Tags of the kinematics technology object (S7-1500T)](#tags-of-the-kinematics-technology-object-s7-1500t)

#### Roller picker (S7-1500T)

This section contains information on the following topics:

- [Roller picker 2D (S7-1500T)](#roller-picker-2d-s7-1500t)
- [Roller picker 2D with orientation (S7-1500T)](#roller-picker-2d-with-orientation-s7-1500t)
- [Roller picker 3D (vertical) (S7-1500T)](#roller-picker-3d-vertical-s7-1500t)
- [Roller picker 3D with orientation (vertical) (S7-1500T)](#roller-picker-3d-with-orientation-vertical-s7-1500t)
- [Roller picker 3D with orientation (horizontal) (S7-1500T)](#roller-picker-3d-with-orientation-horizontal-s7-1500t)
- [Tags: Roller picker (S7-1500T)](#tags-roller-picker-s7-1500t)

##### Roller picker 2D (S7-1500T)

The kinematics "Roller picker 2D" supports 2 axes and 2 degrees of freedom. The following graphic shows the principal configuration and the typical working area of the kinematics:

![Figure](images/158535449099_DV_resource.Stream@PNG-de-DE.png)

The kinematics consists of 2 rotary axes A1 and A2 and a system of guide rollers. If both axes A1 and A2 rotate with the same velocity in the same direction, the flange moves horizontally in x direction of the KCS. If both axes A1 and A2 rotate with the same velocity in opposite directions, the flange moves vertically in z direction of the KCS. The kinematics enables a rectangular working area.

###### Coordinate systems and zero position

The graphic below shows the following in the front view:

- The position of the axes and the coordinate systems KCS and FCS
- The zero position of the kinematics
- The deflection of the kinematics is indicated (dashed)

![Coordinate systems and zero position](images/158535443595_DV_resource.Stream@PNG-de-DE.png)

|  |  |  |
| --- | --- | --- |
| ![Coordinate systems and zero position](images/158499650955_DV_resource.Stream@PNG-de-DE.png) | Zero position of the kinematics |  |
| L1 | With zero position of the axes A1 and A2:  Distance of the FCS to the KZP in x direction of the KCS |  |
| L2 | With zero position of the axes A1 and A2:  Distance of the FCS to the KZP and flange length LF in z direction of the KCS |  |
| LF | Flange length before the FCS in the z direction of the KCS |  |
| R1 | Cam radius for axis A1 |  |
| R2 | Cam radius for axis A2 |  |
| ![Coordinate systems and zero position](images/158499655179_DV_resource.Stream@PNG-de-DE.png) | Deflection of the kinematics |  |
| x<sub>1</sub> | Deflection of the kinematics in the positive x direction |  |
| z<sub>1</sub> | Deflection of the kinematics in the positive z direction |  |
| [Legend for representation of the kinematics](#legend-for-representation-of-the-kinematics-s7-1500t) |  |  |

The kinematics coordinate system (KCS) with the kinematics zero point (KZP) is located at the base of the kinematics. The flange coordinate system (FCS) is located between axes A1 and A2.

The position 0.0 on the respective interconnected technology object defines the zero position of the axes A1 and A2. You define the position of the FCS for zero position of the axes A1 and A2 using lengths L1 and L2. Use the length LF to move the FCS in negative z direction of the KCS.

###### Transformation area

The kinematics transformation covers the entire [traversing range](#traversing-range-and-transformation-area-s7-1500t) of the axes.

###### Joint position space

No arm positioning space for the kinematics.

##### Roller picker 2D with orientation (S7-1500T)

The kinematics "Roller picker 2D with orientation" supports 3 axes and 3 degrees of freedom. The following graphic shows the principal configuration and the typical working area of the kinematics:

![Figure](images/158535838603_DV_resource.Stream@PNG-de-DE.png)

The kinematics consists of a system made up of guide rollers and the following axes:

- 2 rotary axes A1 and A2
- 1 rotary axis A4 with rotation around z in the KCS

If both axes A1 and A2 rotate with the same velocity in the same direction, the flange moves horizontally in x direction of the KCS. If both axes A1 and A2 rotate with the same velocity in opposite directions, the flange moves vertically in z direction of the KCS. The kinematics enables a rectangular working area. The kinematics axis A4 enables rotation of the tool around z in the KCS.

###### Coordinate systems and zero position

The graphic below shows the following in the front view:

- The position of the axes and the coordinate systems KCS and FCS
- The zero position of the kinematics
- The deflection of the kinematics is indicated (dashed)

![Coordinate systems and zero position](images/158535844107_DV_resource.Stream@PNG-de-DE.png)

|  |  |  |
| --- | --- | --- |
| ![Coordinate systems and zero position](images/158499650955_DV_resource.Stream@PNG-de-DE.png) | Zero position of the kinematics |  |
| L1 | With axes A1 and A2 in the zero position:  Distance of the FCS to the KZP in x direction of the KCS |  |
| L2 | With axes A1 and A2 in the zero position:  Distance of the FCS to the KZP and flange length LF in z direction of the KCS |  |
| LF | Flange length before the FCS in the z direction of the KCS |  |
| R1 | Cam radius for axis A1 |  |
| R2 | Cam radius for axis A2 |  |
| ![Coordinate systems and zero position](images/158499655179_DV_resource.Stream@PNG-de-DE.png) | Deflection of the kinematics |  |
| x<sub>1</sub> | Deflection of the kinematics in the positive x direction |  |
| z<sub>1</sub> | Deflection of the kinematics in the positive z direction |  |
| [Legend for representation of the kinematics](#legend-for-representation-of-the-kinematics-s7-1500t) |  |  |

The kinematics coordinate system (KCS) with the kinematics zero point (KZP) is located at the base of the kinematics. The flange coordinate system (FCS) is located between axes A1 and A2.

The position 0.0 on the respective interconnected technology object defines the zero position of the axes A1 and A2. You define the position of the FCS with axes A1 and A2 in the zero position using lengths L1 and L2. You shift the FCS in the negative z direction of the KCS using length LF. At the zero position of axis A4, the x axis of the FCS points in the direction of the x axis of the KCS.

###### Transformation area

The kinematics transformation covers the entire [traversing range](#traversing-range-and-transformation-area-s7-1500t) of the axes.

###### Joint position space

No arm positioning spaces for the kinematics.

##### Roller picker 3D (vertical) (S7-1500T)

The kinematics "Roller picker 3D (vertical)" supports 3 axes and 3 degrees of freedom. The following graphic shows the principal configuration and the typical working area of the kinematics:

![Figure](images/158535911819_DV_resource.Stream@PNG-de-DE.png)

The kinematics consists of a system made up of guide rollers and the following axes:

- 2 rotary axes A1 and A2
- 1 linear axis A3 in y direction of the KCS

If both axes A1 and A2 rotate with the same velocity in the same direction, the flange moves horizontally in x direction of the KCS. If both axes A1 and A2 rotate with the same velocity in opposite directions, the flange moves vertically in z direction of the KCS. The linear portal axis A3 moves the system of guide rollers horizontally in y direction of the KCS. The kinematics enables a cuboid working area.

###### Coordinate systems and zero position

The graphic below shows the following in the front view (xz plane):

- The position of the axes and the coordinate systems KCS and FCS
- The zero position of the kinematics
- The deflection of the kinematics is indicated (dashed)

![Coordinate systems and zero position](images/158535900811_DV_resource.Stream@PNG-de-DE.png)

|  |  |  |
| --- | --- | --- |
| ![Coordinate systems and zero position](images/158499650955_DV_resource.Stream@PNG-de-DE.png) | Zero position of the kinematics |  |
| L1 | With zero position of the axes A1 and A2:  Distance of the FCS to the KZP in x direction of the KCS |  |
| L3 | With zero position of the axes A1 and A2:  Distance of the FCS to the KZP and flange length LF in z direction of the KCS |  |
| LF | Flange length before the FCS in the z direction of the KCS |  |
| R1 | Cam radius for axis A1 |  |
| R2 | Cam radius for axis A2 |  |
| ![Coordinate systems and zero position](images/158499655179_DV_resource.Stream@PNG-de-DE.png) | Deflection of the kinematics |  |
| x<sub>1</sub> | Deflection of the kinematics in the positive x direction |  |
| z<sub>1</sub> | Deflection of the kinematics in the positive z direction |  |
| [Legend for representation of the kinematics](#legend-for-representation-of-the-kinematics-s7-1500t) |  |  |

The graphic below shows the following in the top view (xy plane):

- The position of the axes and the coordinate systems KCS and FCS
- The zero position of the kinematics
- The deflection of the kinematics is indicated (dashed)

![Coordinate systems and zero position](images/158535906315_DV_resource.Stream@PNG-de-DE.png)

|  |  |  |
| --- | --- | --- |
| ![Coordinate systems and zero position](images/158499650955_DV_resource.Stream@PNG-de-DE.png) | Zero position of the kinematics |  |
| L1 | With zero position of the axes A1 and A2:  Distance of the FCS to the KZP in x direction of the KCS |  |
| L2 | At zero position of the axis A3:  Distance of the FCS to the KZP in y direction of the KCS |  |
| R1 | Cam radius for axis A1 |  |
| R2 | Cam radius for axis A2 |  |
| ![Coordinate systems and zero position](images/158499655179_DV_resource.Stream@PNG-de-DE.png) | Deflection of the kinematics |  |
| x<sub>1</sub> | Deflection of the kinematics in the positive x direction |  |
| y<sub>1</sub> | Deflection of the kinematics in the positive y direction |  |
| [Legend for representation of the kinematics](#legend-for-representation-of-the-kinematics-s7-1500t) |  |  |

The kinematics coordinate system (KCS) with the kinematics zero point (KZP) is located at the base of the kinematics. The flange coordinate system (FCS) is located between axes A1 and A2.

The position 0.0 on the respective interconnected technology object defines the zero position of the axes A1, A2 and A3. You define the position of the FCS for zero position of the axes A1, A2 and A3 using lengths L1, L2 and L3 . You shift the FCS in the negative z direction of the KCS using length LF.

###### Transformation area

The kinematics transformation covers the entire [traversing range](#traversing-range-and-transformation-area-s7-1500t) of the axes.

###### Joint position space

No arm positioning spaces for the kinematics.

##### Roller picker 3D with orientation (vertical) (S7-1500T)

The kinematics "Roller picker 3D with orientation (vertical)" supports 4 axes and 4 degrees of freedom. The following graphic shows the principal configuration and the typical working area of the kinematics:

![Figure](images/158536017931_DV_resource.Stream@PNG-de-DE.png)

The kinematics consists of a system made up of guide rollers and the following axes:

- 2 rotary axes A1 and A2
- 1 linear axis A3 in the y direction of the KCS
- 1 rotary axis A4 with rotation around z in the KCS

If both axes A1 and A2 rotate with the same velocity in the same direction, the flange moves horizontally in x direction of the KCS. If both axes A1 and A2 rotate with the same velocity in opposite directions, the flange moves vertically in z direction of the KCS. Linear portal axis A3 moves the system of guide rollers horizontally in the y direction of the KCS. The kinematics enables a cuboid working area. Kinematics axis A4 enables rotation of the tool around z in the KCS.

###### Coordinate systems and zero position

The graphic below shows the following in the front view (xz plane):

- The position of the axes and the coordinate systems KCS and FCS
- The zero position of the kinematics
- The deflection of the kinematics is indicated (dashed)

![Coordinate systems and zero position](images/158535930123_DV_resource.Stream@PNG-de-DE.png)

|  |  |  |
| --- | --- | --- |
| ![Coordinate systems and zero position](images/158499650955_DV_resource.Stream@PNG-de-DE.png) | Zero position of the kinematics |  |
| L1 | With axes A1 and A2 in the zero position:  Distance of the FCS to the KZP in x direction of the KCS |  |
| L3 | With axes A1 and A2 in the zero position:  Distance of the FCS to the KZP and flange length LF in z direction of the KCS |  |
| LF | Flange length before the FCS in the z direction of the KCS |  |
| R1 | Cam radius for axis A1 |  |
| R2 | Cam radius for axis A2 |  |
| ![Coordinate systems and zero position](images/158499655179_DV_resource.Stream@PNG-de-DE.png) | Deflection of the kinematics |  |
| x<sub>1</sub> | Deflection of the kinematics in the positive x direction |  |
| z<sub>1</sub> | Deflection of the kinematics in the positive z direction |  |
| [Legend for representation of the kinematics](#legend-for-representation-of-the-kinematics-s7-1500t) |  |  |

The graphic below shows the following in the top view (xy plane):

- The position of the axes and the coordinate systems KCS and FCS
- The zero position of the kinematics
- The deflection of the kinematics is indicated (dashed)

![Coordinate systems and zero position](images/158535935627_DV_resource.Stream@PNG-de-DE.png)

|  |  |  |
| --- | --- | --- |
| ![Coordinate systems and zero position](images/158499650955_DV_resource.Stream@PNG-de-DE.png) | Zero position of the kinematics |  |
| L1 | With axes A1 and A2 in the zero position:  Distance of the FCS to the KZP in x direction of the KCS |  |
| L2 | With axis A3 in the zero position:  Distance of the FCS to the KZP in y direction of the KCS |  |
| R1 | Cam radius for axis A1 |  |
| R2 | Cam radius for axis A2 |  |
| ![Coordinate systems and zero position](images/158499655179_DV_resource.Stream@PNG-de-DE.png) | Deflection of the kinematics |  |
| x<sub>1</sub> | Deflection of the kinematics in the positive x direction |  |
| y<sub>1</sub> | Deflection of the kinematics in the positive y direction |  |
| [Legend for representation of the kinematics](#legend-for-representation-of-the-kinematics-s7-1500t) |  |  |

The kinematics coordinate system (KCS) with the kinematics zero point (KZP) is located at the base of the kinematics. The flange coordinate system (FCS) is located between axes A1 and A2.

The position 0.0 on the respective interconnected technology object defines the zero position of the axes A1, A2 and A3. You define the distance of the zero position of axis A3 to the KZP in the y direction of the KCS using length L2.

You define the position of the FCS with axes A1 and A2 in the zero position using lengths L1 and L3. You shift the FCS in the negative z direction of the KCS using length LF. In the zero position of axis A4, the x axis of the FCS points in the direction of the x axis of the KCS.

###### Transformation area

The kinematics transformation covers the entire [traversing range](#traversing-range-and-transformation-area-s7-1500t) of the axes.

###### Joint position space

No arm positioning spaces for the kinematics.

##### Roller picker 3D with orientation (horizontal) (S7-1500T)

The kinematics "Roller picker 3D with orientation (horizontal)" supports 4 axes and 4 degrees of freedom. The following graphic shows the principal configuration and the typical working area of the kinematics:

![Figure](images/158536098443_DV_resource.Stream@PNG-de-DE.png)

The kinematics consists of a system made up of guide rollers and the following axes:

- 2 rotary axes A1 and A2
- 1 linear axis A3 in z direction of the KCS
- 1 rotary axis A4 with rotation around z in the KCS

If both axes A1 and A2 rotate with the same velocity in the same direction, the flange moves horizontally in x direction of the KCS. If both axes A1 and A2 rotate with the same velocity in opposite directions, the flange moves horizontally in y direction of the KCS. The linear portal axis A3 moves the system of guide rollers vertically in z direction of the KCS. The kinematics enables a cuboid working area. The kinematics axis A4 enables rotation of the tool around z in the KCS.

###### Coordinate systems and zero position

The graphic below shows the following in the front view (xz plane):

- The position of the axes and the coordinate systems KCS and FCS
- The zero position of the kinematics
- The deflection of the kinematics is indicated (dashed)

![Coordinate systems and zero position](images/158536092939_DV_resource.Stream@PNG-de-DE.png)

|  |  |  |
| --- | --- | --- |
| ![Coordinate systems and zero position](images/158499650955_DV_resource.Stream@PNG-de-DE.png) | Zero position of the kinematics |  |
| L1 | With zero position of the axes A1 and A2:  Distance of the FCS to the KZP in x direction of the KCS |  |
| L3 | At zero position of the axis A3:  Distance of the FCS to the KZP and flange length LF in z direction of the KCS |  |
| LF | Flange length before the FCS in the z direction of the KCS |  |
| R1 | Cam radius for axis A1 |  |
| R2 | Cam radius for axis A2 |  |
| ![Coordinate systems and zero position](images/158499655179_DV_resource.Stream@PNG-de-DE.png) | Deflection of the kinematics |  |
| x<sub>1</sub> | Deflection of the kinematics in the positive x direction |  |
| z<sub>1</sub> | Deflection of the kinematics in the positive z direction |  |
| [Legend for representation of the kinematics](#legend-for-representation-of-the-kinematics-s7-1500t) |  |  |

The graphic below shows the following in the top view (xy plane):

- The position of the axes and the coordinate systems KCS and FCS
- The zero position of the kinematics
- The deflection of the kinematics is indicated (dashed)

![Coordinate systems and zero position](images/158536023435_DV_resource.Stream@PNG-de-DE.png)

|  |  |  |
| --- | --- | --- |
| ![Coordinate systems and zero position](images/158499650955_DV_resource.Stream@PNG-de-DE.png) | Zero position of the kinematics |  |
| L1 | With zero position of the axes A1 and A2:  Distance of the FCS to the KZP in x direction of the KCS |  |
| L2 | With zero position of the axes A1 and A2:  Distance of the FCS to the KZP in y direction of the KCS |  |
| R1 | Cam radius for axis A1 |  |
| R2 | Cam radius for axis A2 |  |
| ![Coordinate systems and zero position](images/158499655179_DV_resource.Stream@PNG-de-DE.png) | Deflection of the kinematics |  |
| x<sub>1</sub> | Deflection of the kinematics in the positive x direction |  |
| y<sub>1</sub> | Deflection of the kinematics in the positive y direction |  |
| [Legend for representation of the kinematics](#legend-for-representation-of-the-kinematics-s7-1500t) |  |  |

The kinematics coordinate system (KCS) with the kinematics zero point (KZP) is located at the base of the kinematics. The flange coordinate system (FCS) is located between axes A1 and A2.

The position 0.0 on the respective interconnected technology object defines the zero position of the axes A1, A2 and A3. You define the distance of the zero position of the axis A3 to the KZP in y direction of the KCS using length L2.

You define the position of the FCS for zero position of the axes A1 and A2 using lengths L1 and L3. You shift the FCS in the negative z direction of the KCS using length LF. At the zero position of axis A4, the x axis of the FCS points in the direction of the x axis of the KCS.

###### Transformation area

The kinematics transformation covers the entire [traversing range](#traversing-range-and-transformation-area-s7-1500t) of the axes.

###### Joint position space

No arm positioning spaces for the kinematics.

##### Tags: Roller picker (S7-1500T)

###### Roller picker 2D

You define the 2D delta picker kinematics systems using the following tags of the technology object:

| Tags | Values | Description |
| --- | --- | --- |
| &lt;TO&gt;.Kinematics.TypeOfKinematics | 5 | Roller picker 2D |
| 6 | Roller picker 2D with orientation |  |
| &lt;TO&gt;.Kinematics.Parameter[1] | -1.0E12 to 1.0E12 | With zero position of the axes A1 and A2:  Distance L1 of the FCS to the KZP in x direction of the kinematics coordinate system (KCS) |
| &lt;TO&gt;.Kinematics.Parameter[2] | 0.001 to 1.0E12 | Cam radius R1 for axis 1 |
| &lt;TO&gt;.Kinematics.Parameter[3] | 0.001 to 1.0E12 | Cam radius R2 for axis 2 |
| &lt;TO&gt;.Kinematics.Parameter[4] | -1.0E12 to 1.0E12 | Flange length LF before the flange coordinate system (FCS) in the negative z direction of the KCS |
| &lt;TO&gt;.Kinematics.Parameter[5] | -1.0E12 to 1.0E12 | With zero position of the axes A1 and A2:  Distance L2 of the FCS to the KZP in z direction of the KCS |

###### Roller picker 3D

You define the 3D roller picker kinematics systems using the following tags of the technology object:

| Tags | Values | Description |  |
| --- | --- | --- | --- |
| &lt;TO&gt;.Kinematics.TypeOfKinematics | 7 | Roller picker 3D (vertical) |  |
| 8 | Roller picker 3D with orientation (vertical) |  |  |
| 9 | Roller picker 3D with orientation (horizontal) |  |  |
| &lt;TO&gt;.Kinematics.Parameter[1] | -1.0E12 to 1.0E12 | With zero position of the axes A1 and A2:  Distance L1 of the FCS to the KZP in x direction of the KCS |  |
| &lt;TO&gt;.Kinematics.Parameter[2] | 0.001 to 1.0E12 | Cam radius R1 for axis 1 |  |
| &lt;TO&gt;.Kinematics.Parameter[3] | 0.001 to 1.0E12 | Cam radius R2 for axis 2 |  |
| &lt;TO&gt;.Kinematics.Parameter[4] | -1.0E12 to 1.0E12 | Flange length LF before the FCS in the negative z direction of the KCS |  |
| &lt;TO&gt;.Kinematics.Parameter[5] | -1.0E12 to 1.0E12 | Roller picker vertical | Distance L2 of the zero position of the axis A3 to the KZP in y direction of the KCS |
| Roller picker horizontal | With zero position of the axes A1 and A2:  Distance L2 of the FCS to the kinematics zero point (KZP) in y direction of the KCS |  |  |
| &lt;TO&gt;.Kinematics.Parameter[6] | -1.0E12 to 1.0E12 | Roller picker vertical | With zero position of the axes A1 and A2:  Distance L3 of the FCS to the KZP in z direction of the KCS |
| Roller picker horizontal | Distance L3 of the zero position of the axis A3 to the KZP in z direction of the KCS |  |  |

#### SCARA (S7-1500T)

This section contains information on the following topics:

- [SCARA 2D with orientation (S7-1500T)](#scara-2d-with-orientation-s7-1500t)
- [SCARA 3D with orientation (S7-1500T)](#scara-3d-with-orientation-s7-1500t)
- [Tags: SCARA (S7-1500T)](#tags-scara-s7-1500t)

##### SCARA 2D with orientation (S7-1500T)

The kinematics "SCARA 2D with orientation (swivel axis)" supports 3 axes and 3 degrees of freedom. The axes are configured as serial kinematics.

The following graphic shows the principal configuration and the typical working area of the kinematics:

![Figure](images/158505285131_DV_resource.Stream@PNG-de-DE.png)

The kinematics consists of the following axes:

- 1 rotary axis A1 with rotation around the z axis of the kinematics coordinate system (KCS)
- 1 linear axis A2 in the z direction of the KCS
- 1 rotary axis A4 with rotation around z in the KCS

The kinematics consists of a base and an articulated arm for horizontal alignment which are connected by a revolute joint (axis A1). A linear stroke axis (axis A2) is fastened to the end of the articulated arm for the vertical alignment. The tool is fastened to the end of the linear axis. The kinematics axis A4 enables rotation of the tool around z in the KCS.

###### Coordinate systems and zero position

The graphic below shows the following in the side view (xz plane):

- The position of the axes and the coordinate systems KCS and FCS
- The zero position of the kinematics
- The positive/negative deflection of the kinematics is indicated (dashed)

![Coordinate systems and zero position](images/166607145867_DV_resource.Stream@PNG-de-DE.png)

|  |  |  |
| --- | --- | --- |
| ![Coordinate systems and zero position](images/158499650955_DV_resource.Stream@PNG-de-DE.png) | Zero position of the kinematics |  |
| L1 | Distance of the axis A1 to the KZP in z direction of the KCS |  |
| L2 | Distance of the axis A1 to the FCS in x direction of the KCS |  |
| LF | Distance of the FCS to the axis A1 in z direction of the FCS |  |
| ![Coordinate systems and zero position](images/158499655179_DV_resource.Stream@PNG-de-DE.png) | Deflection of the kinematics |  |
| z<sub>1</sub> | Deflection of the axis A2 in negative direction |  |
| [Legend for representation of the kinematics](#legend-for-representation-of-the-kinematics-s7-1500t) |  |  |

The graphic below shows the following in the top view (xy plane):

- The position of the axes and the coordinate systems KCS and FCS
- The zero position of the kinematics
- The positive/negative deflection of the kinematics is indicated (dashed)

![Coordinate systems and zero position](images/158505330187_DV_resource.Stream@PNG-de-DE.png)

|  |  |  |
| --- | --- | --- |
| ![Coordinate systems and zero position](images/158499650955_DV_resource.Stream@PNG-de-DE.png) | Zero position of the kinematics |  |
| ![Coordinate systems and zero position](images/158499655179_DV_resource.Stream@PNG-de-DE.png) | Deflection of the kinematics |  |
| α1 | Deflection of the axis A1 in positive direction when α1 = 30.0°  Deflection of the axis A1 in negative direction when α1 = -60.0° |  |
| [Legend for representation of the kinematics](#legend-for-representation-of-the-kinematics-s7-1500t) |  |  |

The KCS with the kinematics zero point (KZP) is located at the base of the kinematics. The flange coordinate system (FCS) is located at the end of the articulated arm.

The following table shows the zero position of the axes:

| Axis | Zero position |
| --- | --- |
| A1 | The articulated arm points in the x direction of the KCS. |
| A2 | The axis A2 is at the position 0.0 of the interconnected technology object. |
| A4 | With axis A1 in the zero position, the x axis of the FCS points in the direction of the x axis of the KCS. |

###### Compensation of mechanical axis couplings

You can configure a mechanical axis coupling of axis A4 to axis A2 for the kinematics. The kinematics transformation compensates for the configured mechanical axis coupling. The axis coupling between axis A4 and axis A2 is implemented as a leadscrew pitch. With a compensation factor of 1.0, 360.0° on axis A4 corresponds to a distance of -1.0 mm on axis A2.

###### Transformation area

The kinematics transformation covers the following [traversing range](#traversing-range-and-transformation-area-s7-1500t) of the axes:

- Axis A1: -180.0° ≤ α1 &lt; 180.0°
- Axis A2: No limit
- Axis A4: No limit

  An angle greater than 360° can be defined for the orientation. But coordinate A of the tool center point (TCP) is mapped in the range -180° to +180°.

You can process these kinematics only with the Motion Control instructions "MC_MoveDirectAbsolute" and "MC_MoveDirectRelative" or single-axis jobs.

###### Joint position space

No arm positioning spaces for the kinematics.

##### SCARA 3D with orientation (S7-1500T)

The kinematics "SCARA (Selective Compliance Assembly Robot Arm) 3D with orientation" supports 4 axes and 4 degrees of freedom. The axes are configured as serial kinematics.

The following graphic shows the principal configuration and the typical working area of the kinematics:

![Figure](images/158506070283_DV_resource.Stream@PNG-de-DE.png)

The kinematics consists of the following axes:

- 1 rotary axis A1 with rotation around the z axis of the kinematics coordinate system (KCS)
- 1 rotary axis A2 at distance L2 to A1 with rotation around z of the KCS
- 1 linear axis A3 at distance L3 to A2 with motion in z direction of the KCS
- 1 rotary axis A4 with rotation around z in the KCS

The kinematics consists of a base and two levers for horizontal alignment which are connected by revolute joints (axis A1 and A2). A linear axis (axis A3) is fastened to the end of the articulated arm for the vertical alignment. The tool is fastened to the end of the linear axis. The kinematics axis A4 enables rotation of the tool around z in the KCS.

###### Coordinate systems and zero position

The graphic below shows the following in the side view (xz plane):

- The position of the axes and the coordinate systems KCS and FCS
- The zero position of the kinematics

![Coordinate systems and zero position](images/166664154891_DV_resource.Stream@PNG-de-DE.png)

|  |  |  |
| --- | --- | --- |
| ![Coordinate systems and zero position](images/158499650955_DV_resource.Stream@PNG-de-DE.png) | Zero position of the kinematics |  |
| L1 | Distance of the axis A1 to the KZP in z direction of the KCS |  |
| L2 | Distance of the axis A2 to the axis A1 in x direction of the KCS |  |
| L3 | Distance of the axis A3 to the axis A2 in x direction of the KCS |  |
| LF | Distance of the FCS to the axis A2 in z direction of the FCS |  |
| ![Coordinate systems and zero position](images/158499655179_DV_resource.Stream@PNG-de-DE.png) | Deflection of the kinematics |  |
| z<sub>1</sub> | Deflection of the axis A3 in the positive direction |  |
| [Legend for representation of the kinematics](#legend-for-representation-of-the-kinematics-s7-1500t) |  |  |

The graphic below shows the following in the top view (xy plane):

- The position of the axes and the coordinate systems KCS and FCS
- The zero position of the kinematics
- The positive/negative deflection of the kinematics is indicated (dashed)

![Coordinate systems and zero position](images/158506234123_DV_resource.Stream@PNG-de-DE.png)

|  |  |  |
| --- | --- | --- |
| ![Coordinate systems and zero position](images/158499650955_DV_resource.Stream@PNG-de-DE.png) | Zero position of the kinematics |  |
| ![Coordinate systems and zero position](images/158499655179_DV_resource.Stream@PNG-de-DE.png) | Deflection of the kinematics in the positive direction when α1 = 30.0° with a positive joint position when α2 = 75.0°  Deflection of the kinematics in the negative direction when α1 = -60.0° with a negative joint position when α2 = -45.0° |  |
| α1 | Deflection of the axis A1 in positive direction when α1 = 30.0°  Deflection of the axis A1 in negative direction when α1 = -60.0° |  |
| α2 | The deflection of axis A2 in the positive direction when α2 = 75.0° produces a positive joint position.  The deflection of axis A2 in the negative direction when α2 = -45.0° produces a negative joint position. |  |
| [Legend for representation of the kinematics](#legend-for-representation-of-the-kinematics-s7-1500t) |  |  |

The KCS with the kinematics zero point (KZP) is located at the base of the kinematics. The flange coordinate system (FCS) is located at the end of the axis A3.

The following table shows the zero position of the axes:

| Axis | Zero position |
| --- | --- |
| A1 and A2 | The kinematics is elongated in the x<sub>KCS</sub> direction. |
| A3 | The FCS is located at distance L1-LF from the KCS in z direction. |
| A4 | With axes A1 and A2 in the zero position, the x axis of the FCS points in the direction of the x axis of the KCS. |

###### Compensation of mechanical axis couplings

You can configure the following mechanical coupled axes for the kinematics:

- Mechanical coupling of axis A1 to axis A2
- Mechanical coupling of axis A4 to axis A3

The kinematics transformation compensates for the configured mechanical axis couplings. With a compensation factor &gt; 0.0, the kinematics transformation assumes that a positive motion of the axis A1 leads to a negative motion on the axis A2. The axis coupling between axis A4 and axis A3 is implemented as a leadscrew pitch. With a compensation factor of 1.0, 360.0° on axis A4 corresponds to a distance of -1.0 mm on axis A3.

###### Transformation area

The kinematics transformation covers the following [traversing range](#traversing-range-and-transformation-area-s7-1500t) of the axes:

- Axis A1: -180.0° ≤ α1 ≤ 180.0°
- Axis A2: -180.0° ≤ α2 ≤ 180.0°
- Axis A3: No limit
- Axis A4: No limit

  An angle greater than 360° can be defined for the orientation. But coordinate A of the tool center point (TCP) is mapped in the range -180° to +180°.

> **Note**
>
> **Singularity**
>
> The kinematics has [singularities](#singularities-s7-1500t).

A singularity occurs when the zero point of the flange coordinate system (FCS) is located on the z axis of the kinematics coordinate system (KCS). Inverse transformation is not possible in this area. This position may result, e.g. in the event of suspended installation if the lengths L2 and L3 are the same size.

The graphic below shows examples of a movement in the direction of the singularity:

![Transformation area](images/158506239243_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ![Transformation area](images/156065229195_DV_resource.Stream@PNG-de-DE.png) | Permissible joint position |
| ![Transformation area](images/156065233419_DV_resource.Stream@PNG-de-DE.png) | Folded position  Inner singularity at L2 = L3 |

###### Joint position space

The following table shows the possible arm positioning spaces of the kinematics:

| Tag |  |  | Data type | Values | W | Description |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| StatusKinematics. |  |  | TO_Struct_Kinematics_StatusKinematics |  |  |  |  |
|  | Valid |  | BOOL | - | RON | Validity of the transformation values |  |
| FALSE | Invalid |  |  |  |  |  |  |
| TRUE | Valid |  |  |  |  |  |  |
| LinkConstellation |  | DWORD | 0 to n | RON | Joint position space |  |  |
|  | Bit 0 | - | - | - | Position axis 1 |  |  |
| 0 | Not relevant |  |  |  |  |  |  |
| 1 | Not relevant |  |  |  |  |  |  |
| Bit 1 | - | - | - | Position axis 2 Angle α2 of axis A2 positive/negative taking into consideration the mechanical axis coupling |  |  |  |
| 0 | α2 positive |  |  |  |  |  |  |
| 1 | α2 negative |  |  |  |  |  |  |
| Bit 2 | - | - | - | Position axis 3 |  |  |  |
| 0 | Not relevant |  |  |  |  |  |  |
| 1 | Not relevant |  |  |  |  |  |  |
| Bit 3 … 31 | - | - | - | Not relevant |  |  |  |

##### Tags: SCARA (S7-1500T)

###### SCARA 2D

You define the SCARA 2D kinematics using the following tags of the technology object:

| Tags | Values | Description |
| --- | --- | --- |
| &lt;TO&gt;.Kinematics.TypeOfKinematics | 20 | SCARA 2D with orientation |
| &lt;TO&gt;.Kinematics.Parameter[1] | -1.0E12 to 1.0E12 | Distance of the axis A1 from the kinematics zero point in z direction of the kinematics coordinate system (KCS) |
| &lt;TO&gt;.Kinematics.Parameter[2] | -1.0E12 to 1.0E12 | Distance L2 of the axis A2 from the axis A4 in x direction of the KCS |
| &lt;TO&gt;.Kinematics.Parameter[3] | 0.001 to 1.0E12 | Distance of the flange coordinate system from the axis A2 in the negative z direction of the KCS |
| &lt;TO&gt;.Kinematics.Parameter[4] | - | Mechanical axis coupling of axis A4 to A2 present/not present |
| 0 | Not present |  |
| 1 | Present |  |
| &lt;TO&gt;.Kinematics.Parameter[5] | -1.0E12 to 1.0E12 | Compensation factor of axis A4 to axis A2 |

###### SCARA 3D

You define the SCARA 3D kinematics using the following tags of the technology object:

| Tags | Values | Description |
| --- | --- | --- |
| &lt;TO&gt;.Kinematics.TypeOfKinematics | 10 | SCARA 3D with orientation |
| &lt;TO&gt;.Kinematics.Parameter[1] | -1.0E12 to 1.0E12 | Distance of the axis A1 from the kinematics zero point in z direction of the kinematics coordinate system (KCS) |
| &lt;TO&gt;.Kinematics.Parameter[2] | 0.001 to 1.0E12 | Distance L2 of the axis A2 from the axis A1 in x direction of the KCS |
| &lt;TO&gt;.Kinematics.Parameter[3] | - | Mechanical axis coupling of axis A1 to axis A2 present/not present |
| 0 | Not present |  |
| 1 | Present |  |
| &lt;TO&gt;.Kinematics.Parameter[4] | -1.0E12 to 1.0E12 | Compensation factor of axis A1 to axis A2 |
| &lt;TO&gt;.Kinematics.Parameter[5] | 0.001 to 1.0E12 | Distance L3 of the axis A3 from the axis A2 in x direction of the KCS |
| &lt;TO&gt;.Kinematics.Parameter[6] | - | Mechanical axis coupling of axis A4 to axis A3 present/not present |
| 0 | Not present |  |
| 1 | Present |  |
| &lt;TO&gt;.Kinematics.Parameter[7] | -1.0E12 to 1.0E12 | Compensation factor of axis A4 to axis A3 |
| &lt;TO&gt;.Kinematics.Parameter[8] | -1.0E12 to 1.0E12 | Distance of the flange coordinate system from the axis A2 in the negative z direction of the KCS |

#### Articulated arm (S7-1500T)

This section contains information on the following topics:

- [Articulated arm 2D (S7-1500T)](#articulated-arm-2d-s7-1500t)
- [Articulated arm 2D with orientation (S7-1500T)](#articulated-arm-2d-with-orientation-s7-1500t)
- [Articulated arm 3D (S7-1500T)](#articulated-arm-3d-s7-1500t)
- [Articulated arm 3D with orientation (S7-1500T)](#articulated-arm-3d-with-orientation-s7-1500t)
- [6-axis articulated arm with central hand (S7-1500T)](#6-axis-articulated-arm-with-central-hand-s7-1500t)
- [Tags: Articulated arm (S7-1500T)](#tags-articulated-arm-s7-1500t)

##### Articulated arm 2D (S7-1500T)

The kinematics "Articulated arm 2D" supports 2 axes and 2 degrees of freedom. The axes are configured as serial kinematics with forced coupling of the flange system.

The following graphic shows the principal configuration and the typical working area of the kinematics:

![Figure](images/158527165963_DV_resource.Stream@PNG-de-DE.png)

The kinematics consists of the following axes:

- 1 rotary axis A1 with the distances L1 in z direction of the KCS and L2 in x direction of the KCS to the kinematics zero point
- 1 rotary axis A2 at distance L3 to axis A1

The kinematics consists of a base and articulated arms, which are connected by revolute joints (axes A1, A2). Axes A1 and A2 move the articulated arm in the xz plane. Through a forced coupling between the axes and the flange system, the z axis of the FCS always points in the negative z direction of the KCS.

###### Coordinate systems and zero position

The graphic below shows the following in the side view:

- The position of the axes and of the forced coupler point
- The position of coordinate systems KCS and FCS
- The zero position of the kinematics
- The positive/negative deflection of the kinematics is indicated (dashed)

![Coordinate systems and zero position](images/166664362507_DV_resource.Stream@PNG-de-DE.png)

|  |  |  |
| --- | --- | --- |
| ① | Forced coupler point |  |
| ![Coordinate systems and zero position](images/158499650955_DV_resource.Stream@PNG-de-DE.png) | Zero position of the kinematics |  |
| L1 | Distance of the axis A1 to the kinematics zero point (KZP) in z direction of the KCS |  |
| L2 | Distance of the axis A1 to the KZP in x direction of the KCS |  |
| L3 | Distance of the axis A2 to the axis A1 in x direction of the KCS |  |
| L4 | Distance of the forced coupler point to the axis A2 in x direction of the KCS |  |
| LF | Distance of the FCS to the forced coupler point in z direction of the FCS |  |
| ![Coordinate systems and zero position](images/158499655179_DV_resource.Stream@PNG-de-DE.png) | Deflection of the kinematics |  |
| α1 | Positive deflection of the axis A1 when α1 = 45.0°  Negative deflection of the axis A1 when α1 = -60.0° |  |
| α2 | The deflection of the axis A2 in the positive direction when α2 = 45.0° produces a positive joint position.  The deflection of the axis A2 in negative direction when α2 = -15.0° produces a negative joint position. |  |
| [Legend for representation of the kinematics](#legend-for-representation-of-the-kinematics-s7-1500t) |  |  |

The kinematics coordinate system (KCS) with the kinematics zero point (KZP) is located at the base of the kinematics. You define the position of the axis A1 relative to the KZP using lengths L1 and L2. The axis A2 is located at distance L3 in x direction of the KCS from the axis A1.

The flange coordinate system (FCS) is located at the following distances from the axis A2 and the forced coupler point:

- Distance L4 to the axis A2 in x direction of the KCS
- Distance LF to the forced coupler point in the negative z direction of the KCS

The axis A2 and the flange system are force-coupled. With the force coupling, the z axis of the FCS always points in negative z direction of the KCS. The forced coupler point is located at distance L4 in x direction of the KCS from the axis A2.

The following table shows the zero position of the axes:

| Axis | Zero position |
| --- | --- |
| A1 | Length L3 points in x direction of the KCS. |
| A2 | At zero position of the axis A1, the length L4 points in x direction of the KCS. |

###### Compensation of mechanical axis couplings

For the kinematics, you can configure a mechanical axis coupling of axis A1 to axis A2. The kinematics transformation compensates for the configured mechanical axis coupling. With a compensation factor &gt; 0.0, the kinematics transformation assumes that a positive motion of the axis A1 leads to a negative motion on the axis A2.

###### Transformation area

The kinematics transformation covers the following [traversing range](#traversing-range-and-transformation-area-s7-1500t) of the axes:

- Axis A1: -180.0° ≤ α1 &lt; 180.0°
- Axis A2: -180.0° ≤ α2 &lt; 180.0°

> **Note**
>
> **Singularity**
>
> The kinematics has outer [singularities](#singularities-s7-1500t).

###### Joint position space

The following table shows the possible arm positioning spaces of the kinematics:

| Tag |  |  | Data type | Values | W | Description |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| StatusKinematics. |  |  | TO_Struct_Kinematics_StatusKinematics |  |  |  |  |
|  | Valid |  | BOOL | - | RON | Validity of the transformation values |  |
| FALSE | Invalid |  |  |  |  |  |  |
| TRUE | Valid |  |  |  |  |  |  |
| LinkConstellation |  | DWORD | 0 to n | RON | Joint position space |  |  |
|  | Bit 0 | - | - | - | Position axis 1 |  |  |
| 0 | Not relevant |  |  |  |  |  |  |
| 1 | Not relevant |  |  |  |  |  |  |
| Bit 1 | - | - | - | Position axis 2  Angle α2 of axis A2 positive/negative taking into consideration the mechanical axis coupling |  |  |  |
| 0 | α2 positive |  |  |  |  |  |  |
| 1 | α2 negative |  |  |  |  |  |  |
| Bit 2 | - | - | - | Position axis 3 |  |  |  |
| 0 | Not relevant |  |  |  |  |  |  |
| 1 | Not relevant |  |  |  |  |  |  |
| Bit 3 … 31 | - | - | - | Not relevant |  |  |  |

##### Articulated arm 2D with orientation (S7-1500T)

The kinematics "Articulated arm 2D with orientation" supports 3 axes and 3 degrees of freedom. The axes are configured as serial kinematics with forced coupling of the flange system.

The following graphic shows the principal configuration and the typical working area of the kinematics:

![Figure](images/158527201803_DV_resource.Stream@PNG-de-DE.png)

The kinematics consists of the following axes:

- 1 rotary axis A1 with the distances L1 in z direction of the KCS and L2 in x direction of the KCS to the kinematics zero point
- 1 rotary axis A2 at distance L3 to axis A1
- 1 rotary axis A4 with rotation around z in the KCS at a distance L4 in x direction of the KCS to axis A2

The kinematics consists of a base and articulated arms, which are connected by revolute joints (axes A1, A2). Axes A1 and A2 move the articulated arm in the xz plane. Through a forced coupling between the axes and the flange system, the z axis of the FCS always points in the negative z direction of the KCS. The kinematics axis A4 enables rotation of the tool around z in the KCS.

###### Coordinate systems and zero position

The graphic below shows the following in the side view:

- The position of the axes and of the forced coupler point
- The position of coordinate systems KCS and FCS
- The zero position of the kinematics
- The positive/negative deflection of the kinematics is indicated (dashed)

![Coordinate systems and zero position](images/166675596427_DV_resource.Stream@PNG-de-DE.png)

|  |  |  |
| --- | --- | --- |
| ① | Forced coupler point |  |
| ![Coordinate systems and zero position](images/158499650955_DV_resource.Stream@PNG-de-DE.png) | Zero position of the kinematics |  |
| L1 | Distance of the axis A1 to the kinematics zero point (KZP) in z direction of the KCS |  |
| L2 | Distance of the axis A1 to the KZP in x direction of the KCS |  |
| L3 | Distance of the axis A2 to the axis A1 in x direction of the KCS |  |
| L4 | Distance of the forced coupler point to the axis A2 in x direction of the KCS |  |
| LF | Distance of the FCS to the forced coupler point in z direction of the FCS |  |
| ![Coordinate systems and zero position](images/158499655179_DV_resource.Stream@PNG-de-DE.png) | Deflection of the kinematics |  |
| α1 | Positive deflection of the axis A1 when α1 = 45.0°  Negative deflection of the axis A1 when α1 = -60.0° |  |
| α2 | The deflection of the axis A2 in the positive direction when α2 = 45.0° produces a positive joint position.  The deflection of the axis A2 in negative direction when α2 = -15.0° produces a negative joint position. |  |
| [Legend for representation of the kinematics](#legend-for-representation-of-the-kinematics-s7-1500t) |  |  |

The kinematics coordinate system (KCS) with the kinematics zero point (KZP) is located at the base of the kinematics. You define the position of the axis A1 relative to the KZP using lengths L1 and L2. The axis A2 is located at distance L3 in x direction of the KCS from the axis A1.

The flange coordinate system (FCS) is located at the following distances from the axis A2 and the forced coupler point:

- Distance L4 to the axis A2 in x direction of the KCS
- Distance LF to the forced coupler point in the negative z direction of the KCS

The axis A2 and the flange system are force-coupled. With the force coupling, the z axis of the FCS always points in negative z direction of the KCS. The forced coupler point is located at distance L4 in x direction of the KCS from the axis A2.

The following table shows the zero position of the axes:

| Axis | Zero position |
| --- | --- |
| A1 | Length L3 points in x direction of the KCS. |
| A2 | At zero position of the axis A1, the length L4 points in x direction of the KCS. |
| A4 | At the zero position of axis A1 and A2, the x axis of the FCS points in the direction of the x axis of the KCS. |

###### Compensation of mechanical axis couplings

For the kinematics, you can configure a mechanical axis coupling of axis A1 to axis A2. The kinematics transformation compensates for the configured mechanical axis coupling. With a compensation factor &gt; 0.0, the kinematics transformation assumes that a positive motion of the axis A1 leads to a negative motion on the axis A2.

###### Transformation area

The kinematics transformation covers the following [traversing range](#traversing-range-and-transformation-area-s7-1500t) of the axes:

- Axis A1: -180.0° ≤ α1 &lt; 180.0°
- Axis A2: -180.0° ≤ α2 &lt; 180.0°
- Axis A4: No limit

  An angle greater than 360° can be defined for the orientation. But coordinate A of the tool center point (TCP) is mapped in the range -180° to +180°.

> **Note**
>
> **Singularity**
>
> The kinematics has outer [singularities](#singularities-s7-1500t).

###### Joint position space

The following table shows the possible arm positioning spaces of the kinematics:

| Tag |  |  | Data type | Values | W | Description |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| StatusKinematics. |  |  | TO_Struct_Kinematics_StatusKinematics |  |  |  |  |
|  | Valid |  | BOOL | - | RON | Validity of the transformation values |  |
| FALSE | Invalid |  |  |  |  |  |  |
| TRUE | Valid |  |  |  |  |  |  |
| LinkConstellation |  | DWORD | 0 to n | RON | Joint position space |  |  |
|  | Bit 0 | - | - | - | Position axis 1 |  |  |
| 0 | Not relevant |  |  |  |  |  |  |
| 1 | Not relevant |  |  |  |  |  |  |
| Bit 1 | - | - | - | Position axis 2  Angle α2 of axis A2 positive/negative taking into consideration the mechanical axis coupling |  |  |  |
| 0 | α2 positive |  |  |  |  |  |  |
| 1 | α2 negative |  |  |  |  |  |  |
| Bit 2 | - | - | - | Position axis 3 |  |  |  |
| 0 | Not relevant |  |  |  |  |  |  |
| 1 | Not relevant |  |  |  |  |  |  |
| Bit 3 … 31 | - | - | - | Not relevant |  |  |  |

##### Articulated arm 3D (S7-1500T)

The kinematics "Articulated arm 3D" supports 3 axes and 3 degrees of freedom. The axes are configured as serial kinematics with forced coupling of the flange system.

The following graphic shows the principal configuration and the typical working area of the kinematics:

![Figure](images/158527206923_DV_resource.Stream@PNG-de-DE.png)

The kinematics consists of the following axes:

- 1 rotary axis A1 with rotation around the z axis of the kinematics coordinate system (KCS)
- 1 rotary axis A2 with the distances L1 in z direction of the KCS and L2 in x direction of the KCS to the kinematics zero point
- 1 rotary axis A3 at distance L3 to axis A2

The kinematics consists of a base and articulated arms, which are connected by revolute joints (axes A1, A2 and A3). Axis A1 rotates the kinematics horizontally around the base. Axes A2 and A3 move the articulated arm. The kinematics enables an approximately spherical working area. Through a forced coupling between the axes and the flange system, the z axis of the FCS always points in the negative z direction of the KCS.

###### Coordinate systems and zero position

The graphic below shows the following in the side view (xz plane):

- The position of the axes and of the forced coupler point
- The position of coordinate systems KCS and FCS
- The zero position of the axes
- The positive/negative deflection of the axes A2 and A3 is indicated (dashed)

![Coordinate systems and zero position](images/166675817355_DV_resource.Stream@PNG-de-DE.png)

|  |  |  |
| --- | --- | --- |
| ① | Forced coupler point |  |
| ![Coordinate systems and zero position](images/158499650955_DV_resource.Stream@PNG-de-DE.png) | Zero position of the kinematics |  |
| L1 | Distance of the axis A2 to the kinematics zero point (KZP) in z direction of the KCS |  |
| L2 | Distance of the axis A2 to the KZP in x direction of the KCS |  |
| L3 | Distance of the axis A3 to the axis A2 in x direction of the KCS |  |
| L4 | Distance of the forced coupler point to the axis A3 in x direction of the KCS |  |
| LF | Distance of the FCS to the forced coupler point in z direction of the FCS |  |
| ![Coordinate systems and zero position](images/158499655179_DV_resource.Stream@PNG-de-DE.png) | Deflection of the kinematics |  |
| α2 | Positive deflection of the axis A2 when α2 = 45.0°  Negative deflection of the axis A2 when α2 = -60.0° |  |
| α3 | The deflection of the A3 in the positive direction when α3 = 45.0° produces a positive joint position.  The deflection of the A3 in negative direction when α3 = -15.0° produces a negative joint position. |  |
| [Legend for representation of the kinematics](#legend-for-representation-of-the-kinematics-s7-1500t) |  |  |

The graphic below shows the following in the top view (xy plane):

- The position of the axes and the coordinate systems KCS and FCS
- The zero position of the kinematics
- The positive/negative deflection of the kinematics is indicated (dashed)

![Coordinate systems and zero position](images/158527212043_DV_resource.Stream@PNG-de-DE.png)

|  |  |  |
| --- | --- | --- |
| ![Coordinate systems and zero position](images/158499650955_DV_resource.Stream@PNG-de-DE.png) | Zero position of the kinematics |  |
| ![Coordinate systems and zero position](images/158499655179_DV_resource.Stream@PNG-de-DE.png) | Deflection of the kinematics |  |
| α1 | Positive deflection of the axis A1 when α1 = 30.0°  Negative deflection of the axis A1 when α1 = -60.0° |  |
| [Legend for representation of the kinematics](#legend-for-representation-of-the-kinematics-s7-1500t) |  |  |

The KCS with the kinematics zero point (KZP) is located at the base of the kinematics. You define the position of the axis A2 relative to the KZP using lengths L1 and L2. The axis A3 is located at distance L3 in x direction of the KCS from the axis A2.

The flange coordinate system (FCS) is located at the following distances from the axis A3 and the forced coupler point:

- Distance L4 to the axis A3 in x direction of the KCS
- Distance LF to the forced coupler point in the negative z direction of the KCS

The axis A3 and the flange system are force-coupled. With the force coupling, the z axis of the FCS always points in negative z direction of the KCS. The forced coupler point is located at distance L4 in x direction of the KCS from the axis A3.

The following table shows the zero position of the axes:

| Axis | Zero position |
| --- | --- |
| A1 | The articulated arms of the kinematics point in the x direction of the KCS. |
| A2 | At zero position of the axis A1, the length L3 points in x direction of the KCS. |
| A3 | At zero position of the axes A1 and A2, the length L4 points in x direction of the KCS. |

###### Compensation of mechanical axis couplings

You can configure a mechanical axis coupling of axis A2 to axis A3 for the kinematics. The kinematics transformation compensates for the configured mechanical axis coupling. With a compensation factor &gt; 0.0, the kinematics transformation assumes that a positive motion of the axis A2 leads to a negative motion on the axis A3.

###### Transformation area

The kinematics transformation covers the following [traversing range](#traversing-range-and-transformation-area-s7-1500t) of the axes:

- Axis A1: -180.0° ≤ α1 &lt; 180.0°
- Axis A2: -180.0° ≤ α2 &lt; 180.0°
- Axis A3: -180.0° ≤ α3 &lt; 180.0°

> **Note**
>
> **Singularity**
>
> The kinematics has [singularities](#singularities-s7-1500t).

A singularity occurs when the zero point of the flange coordinate system (FCS) is located on the z axis of the kinematics coordinate system (KCS). Inverse transformation is not possible in this area.

The graphic below shows examples of singularities and permissible joint positions:

![Transformation area](images/166676050571_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ![Transformation area](images/156065229195_DV_resource.Stream@PNG-de-DE.png) | Permissible joint position |
| ![Transformation area](images/156065233419_DV_resource.Stream@PNG-de-DE.png) | Inner singularity |

###### Joint position space

The following table shows the possible arm positioning spaces of the kinematics:

| Tag |  |  | Data type | Values | W | Description |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| StatusKinematics. |  |  | TO_Struct_Kinematics_StatusKinematics |  |  |  |  |
|  | Valid |  | BOOL | - | RON | Validity of the transformation values |  |
| FALSE | Invalid |  |  |  |  |  |  |
| TRUE | Valid |  |  |  |  |  |  |
| LinkConstellation |  | DWORD | 0 to n | RON | Joint position space |  |  |
|  | Bit 0 | - | - | - | Position axis 1  Angle α1 of axis A1 in the front/rear area (standard area/overhead area) |  |  |
| 0 | The zero point of the FCS is located in the front area (standard area) of the joint position lines for the axis A1.  α1 = arctan(y<sub>FCS</sub>/x<sub>FCS</sub>) |  |  |  |  |  |  |
| 1 | The zero point of the FCS is located in the rear area (overhead area) of the joint position lines for the axis A1.  α1 = -arctan(y<sub>FCS</sub>/x<sub>FCS</sub>) |  |  |  |  |  |  |
| Bit 1 | - | - | - | Position axis 2 |  |  |  |
| 0 | Not relevant |  |  |  |  |  |  |
| 1 | Not relevant |  |  |  |  |  |  |
| Bit 2 | - | - | - | Position axis 3  Angle α3 of axis A3 positive/negative taking into consideration the mechanical axis coupling |  |  |  |
| 0 | α3 positive |  |  |  |  |  |  |
| 1 | α3 negative |  |  |  |  |  |  |
| Bit 3 … 31 | - | - | - | Not relevant |  |  |  |

##### Articulated arm 3D with orientation (S7-1500T)

The kinematics "Articulated arm 3D with orientation" supports 4 axes and 4 degrees of freedom. The axes are configured as serial kinematics with forced coupling of the flange system.

The following graphic shows the principal configuration and the typical working area of the kinematics:

![Figure](images/158527240203_DV_resource.Stream@PNG-de-DE.png)

The kinematics consists of the following axes:

- 1 rotary axis A1 with rotation around the z axis of the kinematics coordinate system (KCS)
- 1 rotary axis A2 with the distances L1 in z direction of the KCS and L2 in x direction of the KCS to the kinematics zero point
- 1 rotary axis A3 at distance L3 to axis A2
- 1 rotary axis A4 with rotation around z in the KCS at a distance L4 in x direction of the KCS to axis A3

The kinematics consists of a base and articulated arms, which are connected by revolute joints (axes A1, A2 and A3). Axis A1 rotates the kinematics horizontally around the base. Axes A2 and A3 move the articulated arm. The kinematics enables an approximately spherical working area. Through a forced coupling between the axes and the flange system, the z axis of the FCS always points in the negative z direction of the KCS. The kinematics axis A4 enables rotation of the tool around z in the KCS.

###### Coordinate systems and zero position

The graphic below shows the following in the side view (xz plane):

- The position of the axes and of the forced coupler point
- The position of coordinate systems KCS and FCS
- The zero position of the kinematics
- The positive/negative deflection of the kinematics is indicated (dashed)

![Coordinate systems and zero position](images/166676412299_DV_resource.Stream@PNG-de-DE.png)

|  |  |  |
| --- | --- | --- |
| ① | Forced coupler point |  |
| ![Coordinate systems and zero position](images/158499650955_DV_resource.Stream@PNG-de-DE.png) | Zero position of the kinematics |  |
| L1 | Distance of the axis A2 to the kinematics zero point (KZP) in z direction of the KCS |  |
| L2 | Distance of the axis A2 to the KZP in x direction of the KCS |  |
| L3 | Distance of the axis A3 to the axis A2 in x direction of the KCS |  |
| L4 | Distance of the forced coupler point to the axis A3 in x direction of the KCS |  |
| LF | Distance of the FCS to the forced coupler point in z direction of the FCS |  |
| ![Coordinate systems and zero position](images/158499655179_DV_resource.Stream@PNG-de-DE.png) | Deflection of the kinematics |  |
| α2 | Positive deflection of the axis A2 when α2 = 45.0°  Negative deflection of the axis A2 when α2 = -60.0° |  |
| α3 | The deflection of the A3 in the positive direction when α3 = 45.0° produces a positive joint position.  The deflection of the A3 in negative direction when α3 = -15.0° produces a negative joint position. |  |
| [Legend for representation of the kinematics](#legend-for-representation-of-the-kinematics-s7-1500t) |  |  |

The graphic below shows the following in the top view (xy plane):

- The position of the axes
- The position of coordinate systems KCS and FCS
- The zero position of the kinematics
- The positive/negative deflection of the kinematics is indicated (dashed)

![Coordinate systems and zero position](images/158527250443_DV_resource.Stream@PNG-de-DE.png)

|  |  |  |
| --- | --- | --- |
| ![Coordinate systems and zero position](images/158499650955_DV_resource.Stream@PNG-de-DE.png) | Zero position of the kinematics |  |
| ![Coordinate systems and zero position](images/158499655179_DV_resource.Stream@PNG-de-DE.png) | Deflection of the kinematics |  |
| α1 | Positive deflection of the axis A1 when α1 = 30.0°  Negative deflection of the axis A1 when α1 = -60.0° |  |
| [Legend for representation of the kinematics](#legend-for-representation-of-the-kinematics-s7-1500t) |  |  |

The KCS with the kinematics zero point (KZP) is located at the base of the kinematics. You define the position of the axis A2 relative to the KZP using lengths L1 and L2. The axis A3 is located at distance L3 in x direction of the KCS from the axis A2.

The flange coordinate system (FCS) is located at the following distances from the axis A3 and the forced coupler point:

- Distance L4 to the axis A3 in x direction of the KCS
- Distance LF to the forced coupler point in the negative z direction of the KCS

The axis A3 and the flange system are force-coupled. With the force coupling, the z axis of the FCS always points in negative z direction of the KCS. The forced coupler point is located at distance L4 in x direction of the KCS from the axis A3.

The following table shows the zero position of the axes:

| Axis | Zero position |
| --- | --- |
| A1 | The articulated arms of the kinematics point in the x direction of the KCS. |
| A2 | At zero position of the axis A1, the length L3 points in x direction of the KCS. |
| A3 | At zero position of the axes A1 and A2, the length L4 points in x direction of the KCS. |
| A4 | At zero position of the axes A1, A2 and A3, the x axis of the FCS points in the direction of the x axis of the KCS. |

###### Compensation of mechanical axis couplings

You can configure a mechanical axis coupling of axis A2 to axis A3 for the kinematics. The kinematics transformation compensates for the configured mechanical axis coupling. With a compensation factor &gt; 0.0, the kinematics transformation assumes that a positive motion of the axis A2 leads to a negative motion on the axis A3.

###### Transformation area

The kinematics transformation covers the following [traversing range](#traversing-range-and-transformation-area-s7-1500t) of the axes:

- Axis A1: -180.0° ≤ α1 &lt; 180.0°
- Axis A2: -180.0° ≤ α2 &lt; 180.0°
- Axis A3: -180.0° ≤ α3 &lt; 180.0°
- Axis A4: No limit

  An angle greater than 360° can be defined for the orientation. But coordinate A of the tool center point (TCP) is mapped in the range -180° to +180°.

> **Note**
>
> **Singularity**
>
> The kinematics has [singularities](#singularities-s7-1500t).

A singularity occurs when the zero point of the flange coordinate system (FCS) is located on the z axis of the kinematics coordinate system (KCS). Inverse transformation is not possible in this area.

The graphic below shows examples of singularities and permissible joint positions:

![Transformation area](images/166676050571_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ![Transformation area](images/156065229195_DV_resource.Stream@PNG-de-DE.png) | Permissible joint position |
| ![Transformation area](images/156065233419_DV_resource.Stream@PNG-de-DE.png) | Inner singularity |

###### Joint position space

The following table shows the possible arm positioning spaces of the kinematics:

| Tag |  |  | Data type | Values | W | Description |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| StatusKinematics. |  |  | TO_Struct_Kinematics_StatusKinematics |  |  |  |  |
|  | Valid |  | BOOL | - | RON | Validity of the transformation values |  |
| FALSE | Invalid |  |  |  |  |  |  |
| TRUE | Valid |  |  |  |  |  |  |
| LinkConstellation |  | DWORD | 0 to n | RON | Joint position space |  |  |
|  | Bit 0 | - | - | - | Position axis 1  Angle α1 of axis A1 in the front/rear area (standard area/overhead area) |  |  |
| 0 | The zero point of the FCS is located in the front area (standard area) of the joint position lines for the axis A1.  α1 = arctan(y<sub>FCS</sub>/x<sub>FCS</sub>) |  |  |  |  |  |  |
| 1 | The zero point of the FCS is located in the rear area (overhead area) of the joint position lines for the axis A1.  α1 = -arctan(y<sub>FCS</sub>/x<sub>FCS</sub>) |  |  |  |  |  |  |
| Bit 1 | - | - | - | Position axis 2 |  |  |  |
| 0 | Not relevant |  |  |  |  |  |  |
| 1 | Not relevant |  |  |  |  |  |  |
| Bit 2 | - | - | - | Position axis 3  Angle α3 of axis A3 positive/negative taking into consideration the mechanical axis coupling |  |  |  |
| 0 | α3 positive |  |  |  |  |  |  |
| 1 | α3 negative |  |  |  |  |  |  |
| Bit 3 … 31 | - | - | - | Not relevant |  |  |  |

##### 6-axis articulated arm with central hand (S7-1500T)

The kinematics "6-axis articulated arm with central hand" supports 6 axes and 6 degrees of freedom. The axes are configured as serial kinematics. For this kinematics type you need the Motion Control package "[S7-1500T Motion Control KinPlus](#s7-1500t-motion-control-kinplus-s7-1500t)".

The following graphic shows the principal configuration and the typical working area of the kinematics:

![Figure](images/158529590411_DV_resource.Stream@PNG-de-DE.png)

The kinematics consists of the following axes (output state):

- 1 rotary axis A1 with rotation around the z axis of the kinematics coordinate system (KCS)
- 1 rotary axis A2 with the distances L1 in z direction of the KCS and L2 in x direction of the KCS to the kinematics zero point
- 1 rotary axis A3 at distance L3 to axis A2
- 1 rotary axis A4 with the distance L5 in z direction of the KCS to the axis A3 with rotation around x
- 1 rotary axis A5 with the distances L4 in x direction of the KCS and L5 in z direction of the KCS to the axis A3 with rotation around y
- 1 rotary axis A6 with distance LF to axis A5 with rotation around x

The kinematics consists of a base and articulated arms, which are connected by revolute joints (axes A1, A2 and A3). Axis A1 rotates the kinematics horizontally around the base. Axes A2 and A3 move the articulated arm. The kinematics enables an approximately spherical working area.

The axes A4, A5 and A6 form the central hand. This means that the axes A4, A5 and A6 intersect at one point. This point is referred to as the manual root point.

###### Coordinate systems and zero position

The graphic below shows the following in the side view (xz plane):

- The position of the axes
- The position of coordinate systems KCS and FCS
- The zero position of the kinematics

  > **Note**
  >
  > **Singularity**
  >
  > Note that the zero position represents a singularity.
- The positive/negative deflection of the kinematics is indicated (dashed)

![Coordinate systems and zero position](images/166677794059_DV_resource.Stream@PNG-de-DE.png)

|  |  |  |
| --- | --- | --- |
| ① | Manual root point |  |
| ② | Joint position line for the joint |  |
| ![Coordinate systems and zero position](images/158499650955_DV_resource.Stream@PNG-de-DE.png) | Zero position of the kinematics |  |
| L1 | Distance of the axis A2 to the kinematics zero point (KZP) in z direction of the KCS |  |
| L2 | Distance of the axis A2 to the KZP in x direction of the KCS |  |
| L3 | Distance of the axis A3 to the axis A2 in x direction of the KCS |  |
| L4 | Distance of the manual root point to the axis A3 in x direction of the KCS |  |
| L5 | Distance of the manual root point to the axis A3 in z direction of the KCS |  |
| LF | Distance of the FCS to the manual root point in x direction of the KCS |  |
| ![Coordinate systems and zero position](images/158499655179_DV_resource.Stream@PNG-de-DE.png) | Deflection of the kinematics |  |
| α2 | Positive deflection of the axis A2 when α2 = 45.0°  Negative deflection of the axis A2 when α2 = -60.0° |  |
| α3 | The deflection of the A3 in the positive direction when α3 = 45.0° produces a positive joint position.  The deflection of the A3 in negative direction when α3 = -15.0° produces a negative joint position. |  |
| α5 | The deflection of the axis A5 in negative direction when α5 = -60.0° or α5 = -75.0°produces a negative joint position. |  |
| [Legend for representation of the kinematics](#legend-for-representation-of-the-kinematics-s7-1500t) |  |  |

The graphic below shows the following in the top view (xy plane):

- The position of the axes
- The position of coordinate systems KCS and FCS
- The zero position of the kinematics
- The positive/negative deflection of the kinematics is indicated (dashed)

![Coordinate systems and zero position](images/158917683467_DV_resource.Stream@PNG-de-DE.png)

|  |  |  |
| --- | --- | --- |
| ① | Manual root point |  |
| ![Coordinate systems and zero position](images/158499650955_DV_resource.Stream@PNG-de-DE.png) | Zero position of the kinematics |  |
| ![Coordinate systems and zero position](images/158499655179_DV_resource.Stream@PNG-de-DE.png) | Deflection of the kinematics |  |
| α1 | Positive deflection of the axis A1 when α1 = 30.0°  Negative deflection of the axis A1 when α1 = -45.0° |  |
| α4 | Positive deflection of the axis A4 when α4 = 90.0° |  |
| α6 | Negative deflection of the axis A6 when α6 = -90.0° |  |
| [Legend for representation of the kinematics](#legend-for-representation-of-the-kinematics-s7-1500t) |  |  |

The KCS with the kinematics zero point (KZP) is located at the base of the kinematics. With zero position of the axes A1, A2, A3 and A5, the kinematics is extended in x direction of the KCS.

You can use the lengths L1 to L5 and the flange length LF to define the zero position of the flange coordinate system (FCS) at zero position of the kinematics. Since there is no forced coupling between the kinematics axes and the flange system, the coordinate axes of the FCS at the zero position of the kinematics point in the same direction as the coordinate axes of the KCS.

The following table shows the zero position of the axes:

| Axis | Zero position |
| --- | --- |
| A1 | The articulated arms of the kinematics point in the x direction of the KCS. |
| A2 | At zero position of the axis A1, the length L3 points in x direction of the KCS. |
| A3 | At zero position of the axes A1 and A2, the length L4 points in the x direction of the KCS and length L5 points in the z direction of the KCS. |
| A5 | At zero position of the axes A1, A2 and A3, the length LF points in the x direction of KCS. |
| A4, A6 | At zero position of the axes A1, A2, A3 and A5, the x, y and z axes of FCS point in the direction of the x, y and z axes of KCS. |

###### Direction of travel of the joints

The following figure shows the direction of travel of the joints defined in the kinematics type.

![Direction of travel of the joints](images/168813080843_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ![Direction of travel of the joints](images/168814121867_DV_resource.Stream@PNG-de-DE.png) | Positive direction of rotation of the joints |

If the direction of travel of a joint of the real kinematics is inverse to the direction of travel of the joint defined in the kinematics type from Siemens, you must [invert the joint direction](#inverting-the-joint-direction-s7-1500t) in the configuration.

###### Transformation area

The kinematics transformation covers the following [traversing range](#traversing-range-and-transformation-area-s7-1500t) of the axes:

- Axis A[1..6]: -180.0° ≤ α[1..6] &lt; 180.0°

To traverse outside these traversing range definitions, you can use, for example, the Motion Control instructions "[MC_MoveLinearAbsolute](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_movelinearabsolute-position-kinematics-with-linear-path-motion-v8-s7-1500t)" or "[MC_MoveDirectAbsolute](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_movedirectabsolute-absolute-movement-of-kinematics-with-synchronous-point-to-point-motion-v8-s7-1500t)" and "[MC_MoveDirectRelative](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_movedirectrelative-relative-movement-of-kinematics-with-synchronous-point-to-point-motion-v8-s7-1500t)" with "TurnJoint[1..6]" ≠ 1.

> **Note**
>
> **Modulo functionality**
>
> Do not use the setting "Modulo" for the axes A1 to A6.

> **Note**
>
> **Singularity**
>
> The kinematics has [singularities](#singularities-s7-1500t).

Singularity is present in the following cases:

- The axis A4 is located on the z axis of the KCS and rotates around the z axis of the KCS (A1 and A4 are collinear).
- The axis A5 is located on the z axis of the KCS and rotates around the z axis of the KCS (A1 and A5 are collinear).
- The axis A6 is located on the z axis of the KCS and rotates around the z axis of the KCS or the x axis of the FCS is located on the z axis of the KCS (A1 and A6 are collinear).
- The axes A4 and A6 rotate in opposite directions around the same axis when α5 = 0.0° (A4 and A6 are collinear).

Inverse transformation is not possible in these cases.

The graphic below shows examples of singularities and permissible joint positions:

![Transformation area](images/166699074443_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ![Transformation area](images/156065229195_DV_resource.Stream@PNG-de-DE.png) | Permissible joint position |
| ![Transformation area](images/156065233419_DV_resource.Stream@PNG-de-DE.png) | Inner singularity |

###### Joint position space

The joint position space of the kinematics "6-axis articulated arm with central hand" is defined by the joint positions from the kinematics transformation. The joint position space thus describes the geometric joint positions of the kinematics.

When using mechanical axis couplings, inverted joint directions or joint offsets, the joint position space is not defined by the absolute joint positions "&lt;TO&gt;.JointData.J[1..6].Position" or the axis positions "&lt;TO&gt;.AxesData.A[1..6].Position".

The following example shows the geometric joint position on joint 5:

![Joint position space](images/158877968011_DV_resource.Stream@PNG-de-DE.png)

**Case 1:** No joint inversion and no joint offset is defined. The joint position corresponds to the geometric joint position (from the transformation), thus -45°. Bit 4 in the "&lt;TO&gt;StatusKinematics.LinkConstellation" tag is TRUE, because the geometric joint position is -45°.

**Case 2:** The inverted traversing direction is configured for joint 5. The kinematics has exactly the same geometric joint position as in Case 1. However, due to the inverted traversing direction, the joint position is +45°. Bit 4 in the "&lt;TO&gt;StatusKinematics.LinkConstellation" tag is thus also TRUE in this case, because the geometric joint position (from the transformation) is -45°.

**Working areas**

The following graphics show the overhead area ① and the standard area ②:

![Joint position space](images/159495093131_DV_resource.Stream@PNG-de-DE.png)

Example "A" shows the kinematics with joint J1 in the zero position. The wrist point is located in the standard area. In example "B", joint J1 is rotated by -180.0°. With the rotated joint J1, the standard area and the overhead area are also rotated.

The following table shows the possible arm positioning spaces of the kinematics:

| Tag |  |  | Data type | Values | W | Description |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| StatusKinematics. |  |  | TO_Struct_Kinematics_StatusKinematics |  |  |  |  |
|  | Valid |  | BOOL | - | RON | Validity of the transformation values |  |
| FALSE | Invalid |  |  |  |  |  |  |
| TRUE | Valid |  |  |  |  |  |  |
| LinkConstellation |  | DWORD | 0 … n | RON | Joint position space |  |  |
|  | Bit 0 | - | - | - | Geometric joint position joint J1 |  |  |
| 0 | The manual root point is located in the front area (standard area) or on the joint position lines for joint J1. |  |  |  |  |  |  |
| 1 | The manual root point is located in the rear area (overhead area) of the joint position lines for joint J1. |  |  |  |  |  |  |
| Bit 1 | - | - | - | Geometric joint position joint J2 |  |  |  |
| 0 | Not relevant |  |  |  |  |  |  |
| 1 | Not relevant |  |  |  |  |  |  |
| Bit 2 | - | - | - | Geometric joint position joint J3 |  |  |  |
| 0 | The wrist point is in one of the following positions:  - On the joint position line for joint J3 - In the standard area (bit 0 = 0), above the joint position line for joint J3 - In the overhead area (bit 0 = 1), below the joint position line for joint J3 |  |  |  |  |  |  |
| 1 | The wrist point is in one of the following positions:  - In the standard area (bit 0 = 0), below the joint position line for joint J3 - In the overhead area (bit 0 = 1), above the joint position line for joint J3 |  |  |  |  |  |  |
| Bit 3 | - | - | - | Geometric joint position joint J4 |  |  |  |
| 0 | Not relevant |  |  |  |  |  |  |
| 1 | Not relevant |  |  |  |  |  |  |
| Bit 4 | - | - | - | Geometric joint position joint J5 |  |  |  |
| 0 | α5 positive |  |  |  |  |  |  |
| 1 | α5 negative or α5 = 0° |  |  |  |  |  |  |
| Bit 5 | - | - | - | Geometric joint position joint J6 |  |  |  |
| 0 | Not relevant |  |  |  |  |  |  |
| 1 | Not relevant |  |  |  |  |  |  |
| Bit 6 … 31 | - | - | - | Not relevant |  |  |  |

Bits 1, 3, 5 and 6 … 31 in the "&lt;TO&gt;StatusKinematics.LinkConstellation" tag are not programmable on the motion control instructions "MC_MoveDirectAbsolute" or "MC_MoveDirectRelative". A setting is reported as an impermissible value for the target joint position space ("ErrorID" = 16#80D2).

**Examples**

The following examples show various joint position spaces for the same Cartesian position of the kinematics "6-axis articulated arm with central hand". There are no configured offsets or inversions in the example. The tool center point in the FCS is configured as follows: x = 60 mm, y = 0 mm, z = -100 mm, A = 0°, B = 90°, C = 0°.

| Symbol | Meaning |
| --- | --- |
| **LinkConstellation**  **= 16#0000_0000:**     ![Joint position space](images/159341692811_DV_resource.Stream@PNG-de-DE.png) | **LinkConstellation**  **= 16#0000_0001:**     ![Joint position space](images/159341696907_DV_resource.Stream@PNG-de-DE.png) |
| **LinkConstellation**  **= 16#0000_0004:**     ![Joint position space](images/159361989003_DV_resource.Stream@PNG-de-DE.png) | **LinkConstellation**  **= 16#0000_0005:**     ![Joint position space](images/159361993099_DV_resource.Stream@PNG-de-DE.png) |
| **LinkConstellation**  **= 16#0000_0010:**     ![Joint position space](images/159361997195_DV_resource.Stream@PNG-de-DE.png) | **LinkConstellation**  **= 16#0000_0011:**     ![Joint position space](images/159362039691_DV_resource.Stream@PNG-de-DE.png) |
| **LinkConstellation**  **= 16#0000_0014:**     ![Joint position space](images/159362043787_DV_resource.Stream@PNG-de-DE.png) | **LinkConstellation**  **= 16#0000_0015:**     ![Joint position space](images/159362047883_DV_resource.Stream@PNG-de-DE.png) |

##### Tags: Articulated arm (S7-1500T)

###### Articulated arm 2D

You define the 2D articulated arm kinematics systems using the following tags of the technology object:

| Tags | Values | Description |
| --- | --- | --- |
| &lt;TO&gt;.Kinematics.TypeOfKinematics | 11 | Articulated arm 2D |
| 12 | Articulated arm 2D with orientation |  |
| &lt;TO&gt;.Kinematics.Parameter[1] | -1.0E12 to 1.0E12 | Distance L1 of the axis A1 to the kinematics zero point in z direction of the kinematics coordinate system (KCS) |
| &lt;TO&gt;.Kinematics.Parameter[2] | -1.0E12 to 1.0E12 | Distance L2 of the axis A1 to the kinematics zero point in x direction of the KCS |
| &lt;TO&gt;.Kinematics.Parameter[3] | 0.001 to 1.0E12 | Arm length L3 between the axes A1 and A2 |
| &lt;TO&gt;.Kinematics.Parameter[4] | - | Mechanical axis coupling of axis A1 to axis A2 present/not present |
| 0 | Not present |  |
| 1 | Present |  |
| &lt;TO&gt;.Kinematics.Parameter[5] | -1.0E12 to 1.0E12 | Compensation factor of axis A1 to axis A2 |
| &lt;TO&gt;.Kinematics.Parameter[6] | 0.001 to 1.0E12 | Side length L4 between A2 and positive coupling point |
| &lt;TO&gt;.Kinematics.Parameter[7] | -1.0E12 to 1.0E12 | Distance LF of the flange coordinate system (FCS) from the forced coupler point in the negative z direction of the KCS |

###### Articulated arm 3D

You define the 3D articulated arm kinematics systems using the following tags of the technology object:

| Tags | Values | Description |
| --- | --- | --- |
| &lt;TO&gt;.Kinematics.TypeOfKinematics | 13 | Articulated arm 3D |
| 14 | Articulated arm 3D with orientation |  |
| &lt;TO&gt;.Kinematics.Parameter[1] | -1.0E12 to 1.0E12 | Distance L1 of the axis A2 to the kinematics zero point in z direction of the KCS |
| &lt;TO&gt;.Kinematics.Parameter[2] | 0.0 to 1.0E12 | Distance L2 of the axis A2 to the kinematics zero point in x direction of the KCS |
| &lt;TO&gt;.Kinematics.Parameter[3] | 0.001 to 1.0E12 | Arm length L3 between the axes A2 and A3 |
| &lt;TO&gt;.Kinematics.Parameter[4] | - | Mechanical axis coupling of axis A2 to A3 present/not present |
| 0 | Not present |  |
| 1 | Present |  |
| &lt;TO&gt;.Kinematics.Parameter[5] | -1.0E12 to 1.0E12 | Compensation factor of axis A2 to axis A3 |
| &lt;TO&gt;.Kinematics.Parameter[6] | 0.001 to 1.0E12 | Arm length L4 between the axis A3 and positive coupler point |
| &lt;TO&gt;.Kinematics.Parameter[7] | -1.0E12 to 1.0E12 | Distance LF of the FCS from the forced coupler point in the negative z direction of the KCS |

###### 6-axis articulated arm with central hand

You define the kinematics "6-axis articulated arm with central hand" via the following tags of the technology object:

| Tags | Values | Description |
| --- | --- | --- |
| &lt;TO&gt;.Kinematics.TypeOfKinematics | 25 | 6-axis articulated arm with central hand |
| &lt;TO&gt;.Kinematics.Parameter[1] | -1.0E12 to 1.0E12 | Distance L1 of the axis A2 to the kinematics zero point in z direction of the KCS |
| &lt;TO&gt;.Kinematics.Parameter[2] | 0.0 to 1.0E12 | Distance L2 of the axis A2 to the kinematics zero point in x direction of the KCS |
| &lt;TO&gt;.Kinematics.Parameter[3] | 0.001 to 1.0E12 | Distance L3 of the axis A3 to the axis A2 in x direction of the KCS |
| &lt;TO&gt;.Kinematics.Parameter[4] | 0.001 to 1.0E12 | Distance L4 of the manual root point to the axis A3 in x direction of the KCS |
| &lt;TO&gt;.Kinematics.Parameter[5] | -1.0E12 to 1.0E12 | Distance LF of the FCS to the manual root point in x direction of the KCS |
| &lt;TO&gt;.Kinematics.Parameter[6] | -1.0E12 to 1.0E12 | Distance L5 of the manual root point to the axis A3 in z direction of the KCS |

#### Delta picker (S7-1500T)

This section contains information on the following topics:

- [Delta picker 2D (S7-1500T)](#delta-picker-2d-s7-1500t)
- [Delta picker 2D with orientation (S7-1500T)](#delta-picker-2d-with-orientation-s7-1500t)
- [Delta picker 3D (S7-1500T)](#delta-picker-3d-s7-1500t)
- [Delta picker 3D with orientation (S7-1500T)](#delta-picker-3d-with-orientation-s7-1500t)
- [Delta picker 3D with 2 orientations A, B (S7-1500T)](#delta-picker-3d-with-2-orientations-a-b-s7-1500t)
- [Permissible joint position for delta picker (S7-1500T)](#permissible-joint-position-for-delta-picker-s7-1500t)
- [Tags: Delta picker (S7-1500T)](#tags-delta-picker-s7-1500t)

##### Delta picker 2D (S7-1500T)

The kinematics "Delta picker 2D" supports 2 axes and 2 degrees of freedom. The axes are configured as parallel kinematics.

The following graphic shows the principal configuration and the typical working area of the kinematics:

![Figure](images/158530788363_DV_resource.Stream@PNG-de-DE.png)

The kinematics consists of 2 rotary axes A1 and A2.

The kinematics is modeled suspended. The kinematics consists of an upper connecting plate, two upper arms, connecting rods and a lower connecting plate. The axes for moving the arms (axes A1, A2) are fastened to the upper connecting plate. The upper arms and the connecting rods connect the upper and lower connecting plates.

The tool is suspended from the lower connecting plate.

The parallelogram structures of the connecting rods keep the lower connecting plate parallel to the xy plane of the KCS.

###### Coordinate systems and zero position

The graphic below shows the following in the front view:

- The position of the axes and the coordinate systems KCS and FCS
- The zero position of the kinematics
- The deflection of the kinematics is indicated (dashed)

![Coordinate systems and zero position](images/158531087883_DV_resource.Stream@PNG-de-DE.png)

|  |  |  |
| --- | --- | --- |
| ![Coordinate systems and zero position](images/158499650955_DV_resource.Stream@PNG-de-DE.png) | Zero position of the kinematics |  |
| D1 | Distance of the axes from the center of the upper connecting plate (radius of the upper connecting plate) |  |
| D2 | Distance of the hinge points of the connecting rods to the middle of the lower connecting plate (radius of the lower connecting plate) |  |
| L1 | Length of the upper arms |  |
| L2 | Length of the connecting rods |  |
| D1, D2, L1 and L2 are identical for the two arms of the kinematics. |  |  |
| LF | Flange length before the FCS in the z direction of the KCS |  |
| ![Coordinate systems and zero position](images/158499655179_DV_resource.Stream@PNG-de-DE.png) | Deflection of the kinematics  The motion of the axes in the positive direction is the outward rotation of the upper arms. |  |
| α1 | Deflection of the axis A1 in the negative direction when α1 = -45.0° |  |
| α2 | Deflection of the axis A2 in the positive direction when α2 = 88.0° |  |
| [Legend for representation of the kinematics](#legend-for-representation-of-the-kinematics-s7-1500t) |  |  |

The kinematics coordinate system (KCS) with the kinematics zero point (KZP) is located at the center point of the upper connecting plate. The axes A1 and A2 are at distance D1 from the common center point (kinematics zero point).

The flange coordinate system (FCS) is located on the bottom of the lower connecting plate with equal distance D2 to the hinge points of each arm. You shift the FCS in the negative z direction of the KCS using length LF.

In the zero position of the axes A1 and A2, the upper arms point in the negative z direction of the KCS.

###### Transformation area

Only the outwardly bent [joint position](#permissible-joint-position-for-delta-picker-s7-1500t) is permitted for the arms of the kinematics. You cannot traverse the axes beyond the extended position of the arms.

> **Note**
>
> **Singularity**
>
> The kinematics has outer [singularities](#singularities-s7-1500t).

##### Delta picker 2D with orientation (S7-1500T)

The kinematics "Delta picker 2D with orientation" supports 3 axes and 3 degrees of freedom. The axes are configured as parallel kinematics.

The following graphic shows the principal configuration and the typical working area of the kinematics:

![Figure](images/158531093003_DV_resource.Stream@PNG-de-DE.png)

The kinematics consists of the following axes:

- 2 rotary axes A1, A2
- 1 rotary axis A4 with rotation around z in the KCS

The kinematics is modeled suspended. The kinematics consists of an upper connecting plate, two upper arms, connecting rods and a lower connecting plate. The axes for moving the arms (axes A1, A2) are fastened to the upper connecting plate. The upper arms and the connecting rods connect the upper and lower connecting plates.

The tool is suspended from the lower connecting plate.

The parallelogram structures of the connecting rods keep the lower connecting plate parallel to the xy plane of the KCS. The kinematics axis A4 enables rotation of the tool around z in the KCS.

###### Coordinate systems and zero position

The graphic below shows the following in the front view:

- The position of the axes and the coordinate systems KCS and FCS
- The zero positions of the axes A1 and A4
- The deflection of the kinematics is indicated (dashed)

![Coordinate systems and zero position](images/158531098123_DV_resource.Stream@PNG-de-DE.png)

|  |  |  |
| --- | --- | --- |
| ![Coordinate systems and zero position](images/158499650955_DV_resource.Stream@PNG-de-DE.png) | Zero position of the kinematics |  |
| D1 | Distance of the axes from the center of the upper connecting plate (radius of the upper connecting plate) |  |
| D2 | Distance of the joint points of the connecting rods to the middle of the lower connecting plate (radius of the lower connecting plate) |  |
| L1 | Length of the upper arms |  |
| L2 | Length of the connecting rods |  |
| D1, D2, L1 and L2 are identical for the two arms of the kinematics. |  |  |
| LF | Flange length before the FCS in the z direction of the KCS |  |
| ![Coordinate systems and zero position](images/158499655179_DV_resource.Stream@PNG-de-DE.png) | Deflection of the kinematics  The motion of the axes in the positive direction is the outward rotation of the upper arms. |  |
| α1 | Deflection of the axis A1 in the negative direction when α1 = -45.0° |  |
| α2 | Deflection of the axis A2 in the positive direction when α2 = 88.0° |  |
| [Legend for representation of the kinematics](#legend-for-representation-of-the-kinematics-s7-1500t) |  |  |

The kinematics coordinate system (KCS) with the kinematics zero point (KZP) is located at the center point of the upper connecting plate. The axes A1 and A2 are at distance D1 from the common center point (kinematics zero point).

The flange coordinate system (FCS) is located in the center point of the lower connecting plate with equal distance D2 to the joint points of each arm. You shift the FCS in the negative z direction of the KCS using length LF.

In the zero position of the axes A1 and A2, the upper arms point in the negative z direction of the KCS. At the zero position of axis A4, the x axis of the FCS points in the direction of the x axis of the KCS.

###### Transformation area

Only the outwardly bent [joint position](#permissible-joint-position-for-delta-picker-s7-1500t) is permitted for the arms of the kinematics. You cannot traverse the axes beyond the extended position of the arms.

> **Note**
>
> **Singularity**
>
> The kinematics has outer [singularities](#singularities-s7-1500t).

##### Delta picker 3D (S7-1500T)

The kinematics "Delta picker 3D" supports 3 axes and 3 degrees of freedom. The axes are configured as parallel kinematics.

The following graphic shows the principal configuration and the typical working area of the kinematics:

![Figure](images/158531233803_DV_resource.Stream@PNG-de-DE.png)

The kinematics consists of 3 rotary axes A1, A2 and A3.

The kinematics is modeled suspended. The kinematics consists of an upper connecting plate, three upper arms, connecting rods and a lower connecting plate. The axes for moving the arms (axes A1, A2 and A3) are fastened to the upper connecting plate. The upper arms and the connecting rods connect the upper and lower connecting plates.

The tool is suspended from the lower connecting plate.

The parallelogram structures of the connecting rods keep the lower connecting plate parallel to the xy plane of the KCS.

###### Coordinate systems and zero position

The graphic below shows the following in the top view (xy plane):

- The position of the kinematics coordinate system (KCS)
- The angles of the axes A1, A2 and A3 to one another

![Coordinate systems and zero position](images/158531128843_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| β1 | Angle between the axes A1 and A2 |
| β2 | Angle between the axes A2 and A3 |
| [Legend for representation of the kinematics](#legend-for-representation-of-the-kinematics-s7-1500t) |  |

The following graphic shows the top view of the position of the flange coordinate system (FCS) in the xy plane of the lower connecting plate:

![Coordinate systems and zero position](images/158531228683_DV_resource.Stream@PNG-de-DE.png)

The graphic below shows the following in the front view (xz plane):

- The position of the axis A1 and the coordinate systems KCS and FCS
- The zero position of the axis A1
- The positive/negative deflection of the axis A1 is indicated (dashed)

![Coordinate systems and zero position](images/158531133963_DV_resource.Stream@PNG-de-DE.png)

|  |  |  |
| --- | --- | --- |
| ![Coordinate systems and zero position](images/158499650955_DV_resource.Stream@PNG-de-DE.png) | Zero position of the kinematics |  |
| D1 | Distance of the axes from the center of the upper connecting plate (radius of the upper connecting plate) |  |
| D2 | Distance of the hinge points of the connecting rods to the middle of the lower connecting plate (radius of the lower connecting plate) |  |
| L1 | Length of the upper arms |  |
| L2 | Length of the connecting rods |  |
| D1, D2, L1 and L2 are identical for the three arms of the kinematics. |  |  |
| LF | Flange length before the FCS in the z direction of the KCS |  |
| ![Coordinate systems and zero position](images/158499655179_DV_resource.Stream@PNG-de-DE.png) | Deflection of the kinematics  The motion of the axes in the positive direction is the outward rotation of the upper arms. |  |
| α1 | Deflection of the axis A1 in negative direction when α1 = -50.0°  Deflection of the axis A1 in positive direction when α1 = 90.0° |  |
| [Legend for representation of the kinematics](#legend-for-representation-of-the-kinematics-s7-1500t) |  |  |

The KCS with the kinematics zero point (KZP) is located at the center point of the upper connecting plate. The axes A1, A2 and A3 are at distance D1 from the common center point (kinematics zero point).

The FCS is located in the center on the bottom of the lower connecting plate with equal distance D2 to the hinge points of each arm. You shift the FCS in the negative z direction of the KCS using length LF.

In the zero position of the axes A1, A2 and A3, the upper arms point in the negative z direction of the KCS.

###### Transformation area

Only the outwardly bent [joint position](#permissible-joint-position-for-delta-picker-s7-1500t) is permitted for the arms of the kinematics. You cannot traverse the axes beyond the extended position of the arms.

> **Note**
>
> **Singularity**
>
> The kinematics has outer [singularities](#singularities-s7-1500t).

##### Delta picker 3D with orientation (S7-1500T)

The kinematics "Delta picker 3D with orientation" supports 4 axes and 4 degrees of freedom. The axes are configured as parallel kinematics.

The following graphic shows the principal configuration and the typical working area of the kinematics:

![Figure](images/158531238923_DV_resource.Stream@PNG-de-DE.png)

The kinematics consists of the following axes:

- 3 rotary axes A1 A2 and A3
- 1 rotary axis A4 with rotation around z in the KCS

The kinematics is modeled suspended. The kinematics consists of an upper connecting plate, three upper arms, connecting rods and a lower connecting plate. The axes for moving the arms (axes A1, A2 and A3) are fastened to the upper connecting plate. The upper arms and the connecting rods connect the upper and lower connecting plates.

The tool is attached to the lower connecting plate.

The parallelogram structures of the connecting rods keep the lower connecting plate parallel to the xy plane of the KCS. The kinematics axis A4 enables rotation of the tool around z in the KCS.

###### Coordinate systems and zero position

The graphic below shows the following in the top view (xy plane):

- The position of the kinematics coordinate system (KCS)
- The angles of the axes A1, A2 and A3 to one another

![Coordinate systems and zero position](images/158531128843_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| β1 | Angle between the axes A1 and A2 |
| β2 | Angle between the axes A2 and A3 |
| [Legend for representation of the kinematics](#legend-for-representation-of-the-kinematics-s7-1500t) |  |

The following graphic shows the top view of the position of the flange coordinate system (FCS) in the xy plane of the lower connecting plate:

![Coordinate systems and zero position](images/158500744971_DV_resource.Stream@PNG-de-DE.png)

The graphic below shows the following in the front view (xz plane):

- The position of the axis A1 and the coordinate systems KCS and FCS
- The zero positions of the axes A1 and A4
- The positive/negative deflection of the axis A1 is indicated (dashed)

![Coordinate systems and zero position](images/158531308043_DV_resource.Stream@PNG-de-DE.png)

|  |  |  |
| --- | --- | --- |
| ![Coordinate systems and zero position](images/158499650955_DV_resource.Stream@PNG-de-DE.png) | Zero position of the kinematics |  |
| D1 | Distance of the axes from the center of the upper connecting plate (radius of the upper connecting plate) |  |
| D2 | Distance of the joint points of the connecting rods to the middle of the lower connecting plate (radius of the lower connecting plate) |  |
| L1 | Length of the upper arms |  |
| L2 | Length of the connecting rods |  |
| D1, D2, L1 and L2 are identical for the three arms of the kinematics. |  |  |
| LF | Flange length before the FCS in the z direction of the KCS |  |
| ![Coordinate systems and zero position](images/158499655179_DV_resource.Stream@PNG-de-DE.png) | Deflection of the kinematics  The motion of the axes in the positive direction is the outward rotation of the upper arms. |  |
| α1 | Deflection of the axis A1 in negative direction when α1 = -50.0°  Deflection of the axis A1 in positive direction when α1 = 90.0° |  |
| [Legend for representation of the kinematics](#legend-for-representation-of-the-kinematics-s7-1500t) |  |  |

The KCS with the kinematics zero point (KZP) is located at the center point of the upper connecting plate. The axes A1, A2 and A3 are at distance D1 from the common center point (kinematics zero point).

The FCS is located in the center point on the bottom of the lower connecting plate with equal distance D2 to the joint points of each arm. You shift the FCS in the negative z direction of the KCS using length LF.

In the zero position of the axes A1, A2 and A3, the upper arms point in the negative z direction of the KCS. At the zero position of axis A4, the x axis of the FCS points in the direction of the x axis of the KCS.

###### Transformation area

Only the outwardly bent [joint position](#permissible-joint-position-for-delta-picker-s7-1500t) is permitted for the arms of the kinematics. You cannot traverse the axes beyond the extended position of the arms.

> **Note**
>
> **Singularity**
>
> The kinematics has outer [singularities](#singularities-s7-1500t).

##### Delta picker 3D with 2 orientations A, B (S7-1500T)

The kinematics "Delta picker 3D with 2 orientations A, B" supports 5 axes and 5 degrees of freedom. The axes are configured as parallel kinematics. For this kinematics type, you need the Motion Control package ["S7-1500T Motion Control KinPlus"](#s7-1500t-motion-control-kinplus-s7-1500t).

The following graphic shows the principal configuration and the typical working area of the kinematics:

![Figure](images/158533509643_DV_resource.Stream@PNG-de-DE.png)

The kinematics consists of the following axes:

- 3 rotary axes A1 A2 and A3
- One rotary swivel axis A4 which rotates around the z axis of the KCS in the kinematics zero position.
- One rotary swivel axis A5, which rotates around the y axis of the KCS in the kinematics zero position.

The kinematics is modeled suspended. The kinematics consists of an upper connecting plate, three upper arms, connecting rods and a lower connecting plate. The axes for moving the arms (axes A1, A2 and A3) are fastened to the upper connecting plate. The upper arms and the connecting rods connect the upper and lower connecting plates.

The parallelogram structures of the connecting rods keep the lower connecting plate parallel to the xy plane of the KCS.

The rotary axis A4 and the swivel axis A5 are mounted on the lower connecting plate. The motors of the axes A4 and A5 can be mounted on the upper connecting plate or below the lower connecting plate. If the motors are mounted on the upper connecting plate, then the axes A4 and A5 are moved via a mechanical shaft, which is mounted between the two connecting plates.

The tool is attached to the swivel axis A5.

###### Coordinate systems and zero position

The graphic below shows the following in the top view (xy plane):

- The position of the kinematics coordinate system (KCS)
- The angles of the axes A1, A2 and A3 to one another

![Coordinate systems and zero position](images/158533518091_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| β1 | Angle between the axes A1 and A2 |
| β2 | Angle between the axes A2 and A3 |
| [Legend for representation of the kinematics](#legend-for-representation-of-the-kinematics-s7-1500t) |  |

The following graphic shows the bottom view of the position of the flange coordinate system (FCS) in the xy plane of the lower connecting plate:

![Coordinate systems and zero position](images/158533650315_DV_resource.Stream@PNG-de-DE.png)

The graphic below shows the following in the front view (xz plane):

- The position of the axis A1 and the coordinate systems KCS and FCS
- The zero positions of the axes A1 and A4
- The positive/negative deflection of the axis A1 is indicated (dashed)

![Coordinate systems and zero position](images/158533513867_DV_resource.Stream@PNG-de-DE.png)

|  |  |  |
| --- | --- | --- |
| ![Coordinate systems and zero position](images/155189952779_DV_resource.Stream@PNG-de-DE.png) | Zero position of the kinematics |  |
| D1 | Distance of the axes from the center of the upper connecting plate (radius of the upper connecting plate) |  |
| D2 | Distance of the joint points of the connecting rods to the middle of the lower connecting plate (radius of the lower connecting plate) |  |
| L1 | Length of the upper arms |  |
| L2 | Length of the connecting rods |  |
| L3 | Distance of the swivel axis from the lower connecting plate in the negative z direction of the KCS |  |
| L4 | Distance of the joint points of rotary axis A4 and swivel axis A5 in the x direction of the KCS in the kinematics zero position |  |
| D1, D2, L1 and L2 are identical for the three arms of the kinematics. |  |  |
| LF | Distance LF from the joint point of swivel axis A5 to the FCS in the negative x direction of the FCS |  |
| ![Coordinate systems and zero position](images/155190021131_DV_resource.Stream@PNG-de-DE.png) | Deflection of the kinematics  The motion of the axes A1, A2 and A3 in positive direction is that of the rotation outward of the upper arms. |  |
| α1 | Deflection of the axis A1 in negative direction when α1 = -50.0°  Deflection of the axis A1 in positive direction when α1 = 90.0° |  |
| [Legend for representation of the kinematics](#legend-for-representation-of-the-kinematics-s7-1500t) |  |  |

The KCS with the kinematics zero point (KZP) is located at the center point of the upper connecting plate. The axes A1, A2 and A3 are at distance D1 from the common center point (kinematics zero point).

At the zero position of the kinematics, the FCS is oriented with A = 0°, B = 90° and C = 0°.

In the zero position of the axes A1, A2 and A3, the upper arms point in the negative z direction of the KCS. At the zero position of axes A4 and A5, the x axis of the FCS points in the negative direction of the z axis of the KCS.

###### Direction of travel of the joints

The following figure shows the direction of travel of the joints defined in the kinematics type.

![Direction of travel of the joints](images/169000164363_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | Front view |
| ② | Side view |
| ![Direction of travel of the joints](images/168814121867_DV_resource.Stream@PNG-de-DE.png) | Positive direction of rotation of the joints |

If the direction of travel of a joint of the real kinematics is inverse to the direction of travel of the joint defined in the kinematics type from Siemens, you must [invert the joint direction](#inverting-the-joint-direction-s7-1500t) in the configuration.

###### Transformation area

Only the outwardly bent [joint position](#permissible-joint-position-for-delta-picker-s7-1500t) is permitted for the arms of the kinematics. You cannot traverse the axes beyond the extended position of the arms.

> **Note**
>
> **Singularity**
>
> The kinematics has outer [singularities](#singularities-s7-1500t).

##### Permissible joint position for delta picker (S7-1500T)

Only the outwardly bent joint position is permitted for the arms of the delta picker kinematics. The graphic below shows examples of permissible and impermissible joint positions for the transformation:

![Figure](images/158531313163_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ![Figure](images/156065229195_DV_resource.Stream@PNG-de-DE.png) | Permissible joint position |
| ![Figure](images/156065233419_DV_resource.Stream@PNG-de-DE.png) | Invalid joint position for the transformation |

##### Tags: Delta picker (S7-1500T)

###### Delta picker 2D

You define the 2D delta picker kinematics using the following tags of the technology object:

| Tags | Values | Description |
| --- | --- | --- |
| &lt;TO&gt;.Kinematics.TypeOfKinematics | 15 | Delta picker 2D |
| 16 | Delta picker 2D with orientation |  |
| &lt;TO&gt;.Kinematics.Parameter[1] | 0.0 to 1.0E12 | Distance D1 (radius of the upper connecting plate) |
| &lt;TO&gt;.Kinematics.Parameter[2] | 0.001 to 1.0E12 | Length L1 of the upper arms |
| &lt;TO&gt;.Kinematics.Parameter[3] | 0.001 to 1.0E12 | Length L2 of connecting rods |
| &lt;TO&gt;.Kinematics.Parameter[4] | 0.0 to 1.0E12 | Distance D2 (radius of the lower connecting plate) |
| &lt;TO&gt;.Kinematics.Parameter[5] | -1.0E12 to 1.0E12 | Distance LF of the FCS to the lower connecting plate in the negative z direction of the KCS |

###### Delta picker 3D

You define the 3D delta picker kinematics using the following tags of the technology object:

| Tags | Values | Description |
| --- | --- | --- |
| &lt;TO&gt;.Kinematics.TypeOfKinematics | 17 | Delta picker 3D |
| 18 | Delta picker 3D with orientation |  |
| 27 | Delta picker 3D with 2 orientations A, B |  |
| &lt;TO&gt;.Kinematics.Parameter[1] | 0.0 to 1.0E12 | Distance D1 (radius of the upper connecting plate) |
| &lt;TO&gt;.Kinematics.Parameter[2] | 0.001 to 1.0E12 | Length L1 of the upper arms |
| &lt;TO&gt;.Kinematics.Parameter[3] | 0.001 to 1.0E12 | Length L2 of connecting rods |
| &lt;TO&gt;.Kinematics.Parameter[4] | 0.0 to 1.0E12 | Distance D2 (radius of the lower connecting plate) |
| &lt;TO&gt;.Kinematics.Parameter[5] | 90.001° to 179.998° | Angle β1 between the axes A1 and A2 |
| &lt;TO&gt;.Kinematics.Parameter[6] | 90.001° to 179.998° | Angle β2 between the axes A2 and A3 |
| &lt;TO&gt;.Kinematics.Parameter[7] | -1.0E12 to 1.0E12 | - Distance LF of the FCS to the lower connecting plate in the negative z direction of the KCS - Delta picker 3D with 2 orientations A, B:   Distance LF from pivot point of swivel axis A5 to FCS in negative x direction of FCS |
| &lt;TO&gt;.Kinematics.Parameter[8] | 0.001 to 1.0E12 | Distance L3 of the swivel axis to the lower connecting plate in the negative z direction of the KCS at zero position of the kinematics<sup> 1)</sup> |
| &lt;TO&gt;.Kinematics.Parameter[9] | 0.001 to 1.0E12 | Distance L4 of the hinge points of the rotary axis A4 to swivel axis A5 in x direction of the KCS at zero position of the kinematics<sup> 1)</sup> |
| <sup>1) </sup>Only relevant for kinematics type "Delta picker 3D with 2 orientations A, B" |  |  |

#### Cylindrical robot (S7-1500T)

This section contains information on the following topics:

- [Cylindrical robot 3D (S7-1500T)](#cylindrical-robot-3d-s7-1500t)
- [Cylindrical robot 3D with orientation (S7-1500T)](#cylindrical-robot-3d-with-orientation-s7-1500t)
- [Tags: Cylindrical robot (S7-1500T)](#tags-cylindrical-robot-s7-1500t)

##### Cylindrical robot 3D (S7-1500T)

The kinematics "Cylindrical robot 3D" supports 3 axes and 3 degrees of freedom. The axes are configured as serial kinematics.

The following graphic shows the principal configuration and the typical working area of the kinematics:

![Figure](images/158502641419_DV_resource.Stream@PNG-de-DE.png)

The kinematics consists of the following axes:

- 1 rotary axis A1 with rotation around the z axis of the kinematics coordinate system (KCS)
- 1 linear axis A2 in z direction of the KCS
- 1 linear axis A3 in x direction of the KCS

The kinematics consists of a base, a supporting column and a jib. Axis A1 rotates the supporting column with jib around the base. Axis A2 moves the jib vertically. Axis A3 moves the flange system horizontally on the jib. The kinematics enables a cylindrical working area.

###### Coordinate systems and zero position

The graphic below shows the following in the side view (xz plane):

- The position of the axes and the coordinate systems KCS and FCS
- The zero positions of the axes A1 and A2
- The deflection of the kinematics is indicated (dashed)

![Coordinate systems and zero position](images/158503687947_DV_resource.Stream@PNG-de-DE.png)

|  |  |  |
| --- | --- | --- |
| ![Coordinate systems and zero position](images/158499650955_DV_resource.Stream@PNG-de-DE.png) | Zero position of the axes A1 and A2 |  |
| L1 | At zero position of the axis A2:  Distance of the FCS to the kinematics zero point (KZP) and flange length LF in z direction of the KCS |  |
| LF | Flange length before the FCS in the z direction of the KCS |  |
| x<sub>1</sub> | Positive deflection of the axis A3  At the zero position of axis A3, the z axis of the FCS is located on the z axis of the KCS. For mechanical reasons, the kinematics shown cannot approach the zero position of the axis A3. |  |
| ![Coordinate systems and zero position](images/158499655179_DV_resource.Stream@PNG-de-DE.png) | Deflection of the kinematics |  |
| x<sub>2</sub> | Positive deflection of the axis A3 |  |
| z<sub>1</sub> | Positive deflection of the axis A2 |  |
| [Legend for representation of the kinematics](#legend-for-representation-of-the-kinematics-s7-1500t) |  |  |

The graphic below shows the following in the top view (xy plane):

- The position of the axes and the coordinate systems KCS and FCS
- The zero position of the kinematics
- The positive/negative deflection of the kinematics is indicated (dashed)

![Coordinate systems and zero position](images/158502953739_DV_resource.Stream@PNG-de-DE.png)

|  |  |  |
| --- | --- | --- |
| ![Coordinate systems and zero position](images/158499650955_DV_resource.Stream@PNG-de-DE.png) | Zero position of the kinematics |  |
| L2 | Distance of the axis A3 from the KZP in y direction of the KCS (negative value here) |  |
| ![Coordinate systems and zero position](images/158499655179_DV_resource.Stream@PNG-de-DE.png) | Deflection of the kinematics |  |
| α1 | Positive deflection of the axis A1 when α1 = 30°  Negative deflection of the axis A1 when α1 = -75° |  |
| [Legend for representation of the kinematics](#legend-for-representation-of-the-kinematics-s7-1500t) |  |  |

The KCS with the kinematics zero point (KZP) is located at the base of the kinematics. You define the distance of the zero position of axis A2 in z direction of the KCS from the KZP using length L1. You define the distance of the axis A3 from the KZP in y direction of the KCS using length L2.

The flange coordinate system (FCS) is located on the axis A3, shifted by the length LF in negative z direction of the KCS.

The following table shows the zero position of the axes:

| Axis | Zero position |
| --- | --- |
| A1 | The jib with the axis A3 points in x<sub>KCS</sub> direction. |
| A2 | The axis A2 is at the position 0.0 of the interconnected technology object. |
| A3 | The axis A3 is at the position 0.0 of the interconnected technology object. |

###### Transformation area

The kinematics transformation covers the following [traversing range](#traversing-range-and-transformation-area-s7-1500t) of the axes:

- Axis A1: -180.0° ≤ α1 &lt; 180.0°
- Axis A2: No limit
- Axis A3: No limit

> **Note**
>
> **Singularity**
>
> The kinematics has [singularity](#singularities-s7-1500t).

A singularity occurs when the zero point of the flange coordinate system (FCS) is located on the z axis of the kinematics coordinate system (KCS). Inverse transformation is not possible in this area. This position may result, e.g. if the length L2 is 0.0 due to the design.

The graphic below shows examples of permissible and impermissible joint positions for the transformation:

![Transformation area](images/158502958859_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ![Transformation area](images/156065229195_DV_resource.Stream@PNG-de-DE.png) | Permissible joint position |
| ![Transformation area](images/156065233419_DV_resource.Stream@PNG-de-DE.png) | Singularity at L2 = 0.0 |

###### Joint position space

The following table shows the possible arm positioning spaces of the kinematics:

| Tag |  |  | Data type | Values | W | Description |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| StatusKinematics. |  |  | TO_Struct_Kinematics_StatusKinematics |  |  |  |  |
|  | Valid |  | BOOL | - | RON | Validity of the transformation values |  |
| FALSE | Invalid |  |  |  |  |  |  |
| TRUE | Valid |  |  |  |  |  |  |
| LinkConstellation |  | DWORD | 0 to n | RON | Joint position space |  |  |
|  | Bit 0 | - | - | - | Position axis 1 |  |  |
| 0 | Not relevant |  |  |  |  |  |  |
| 1 | Not relevant |  |  |  |  |  |  |
| Bit 1 | - | - | - | Position axis 2 |  |  |  |
| 0 | Not relevant |  |  |  |  |  |  |
| 1 | Not relevant |  |  |  |  |  |  |
| Bit 2 | - | - | - | Angle α3 of axis A3 positive/negative taking into consideration the mechanical axis coupling |  |  |  |
| 0 | α3 positive |  |  |  |  |  |  |
| 1 | α3 negative |  |  |  |  |  |  |
| Bit 3 … 31 | - | - | - | Not relevant |  |  |  |

##### Cylindrical robot 3D with orientation (S7-1500T)

The kinematics "Cylindrical robot 3D with orientation" supports 4 axes and 4 degrees of freedom. The axes are configured as serial kinematics.

The following graphic shows the principal configuration and the typical working area of the kinematics:

![Figure](images/158502963979_DV_resource.Stream@PNG-de-DE.png)

The kinematics consists of the following axes:

- 1 rotary axis A1 with rotation around the z axis of the kinematics coordinate system (KCS)
- 1 linear axis A2 in z direction of the KCS
- 1 linear axis A3 in x direction of the KCS
- 1 rotary axis A4 with rotation around z in the KCS

The kinematics consists of a base, a supporting column and a jib. Axis A1 rotates the supporting column with jib around the base. Axis A2 moves the jib vertically. Axis A3 moves the flange system horizontally on the jib. The kinematics enables a cylindrical working area. The kinematics axis A4 enables rotation of the tool around z in the KCS.

###### Coordinate systems and zero position

The graphic below shows the following in the side view (xz plane):

- The position of the axes and the coordinate systems KCS and FCS
- The zero positions of the axes A1 and A2
- The deflection of the kinematics is indicated (dashed)

![Coordinate systems and zero position](images/158504098955_DV_resource.Stream@PNG-de-DE.png)

|  |  |  |
| --- | --- | --- |
| ![Coordinate systems and zero position](images/158499650955_DV_resource.Stream@PNG-de-DE.png) | Zero position of the kinematics |  |
| L1 | With axis A2 in the zero position:  Distance of the FCS to the kinematics zero point (KZP) and flange length LF in z direction of the KCS |  |
| LF | Flange length before the FCS in the z direction of the KCS |  |
| x<sub>1</sub> | Positive deflection of the axis A3  At the zero position of axis A3, the z axis of the FCS is located on the z axis of the KCS. For mechanical reasons, the kinematics shown cannot approach the zero position of the axis A3. |  |
| ![Coordinate systems and zero position](images/158499655179_DV_resource.Stream@PNG-de-DE.png) | Deflection of the kinematics |  |
| x<sub>2</sub> | Positive deflection of the axis A3 |  |
| z<sub>1</sub> | Positive deflection of the axis A2 |  |
| [Legend for representation of the kinematics](#legend-for-representation-of-the-kinematics-s7-1500t) |  |  |

The graphic below shows the following in the top view (xy plane):

- The position of the axes and the coordinate systems KCS and FCS
- The zero position of the kinematics
- The positive/negative deflection of the kinematics is indicated (dashed)

![Coordinate systems and zero position](images/158503045899_DV_resource.Stream@PNG-de-DE.png)

|  |  |  |
| --- | --- | --- |
| ![Coordinate systems and zero position](images/158499650955_DV_resource.Stream@PNG-de-DE.png) | Zero position of the kinematics |  |
| L2 | Distance of the axis A3 to the KZP in y direction of the KCS (negative value in this case) |  |
| ![Coordinate systems and zero position](images/158499655179_DV_resource.Stream@PNG-de-DE.png) | Deflection of the kinematics |  |
| α1 | Positive deflection of the axis A1 when α1 = 30°  Negative deflection of the axis A1 when α1 = -75° |  |
| [Legend for representation of the kinematics](#legend-for-representation-of-the-kinematics-s7-1500t) |  |  |

The KCS with the kinematics zero point (KZP) is located at the base of the kinematics. You define the distance of the zero position of axis A2 in z direction of the KCS from the KZP using length L1. You define the distance of the axis A3 from the KZP in y direction of the KCS using length L2.

The flange coordinate system (FCS) is located on the axis A3, shifted by the length LF in negative z direction of the KCS.

The following table shows the zero position of the axes:

| Axis | Zero position |
| --- | --- |
| A1 | The jib with the axis A3 points in x<sub>KCS</sub> direction. |
| A2 | The axis A2 is at the position 0.0 of the interconnected technology object. |
| A3 | The axis A3 is at the position 0.0 of the interconnected technology object. |
| A4 | With axis A1 in the zero position, the x axis of the FCS points in the direction of the x axis of the KCS. |

###### Compensation of mechanical axis couplings

You can configure a mechanical axis coupling of axis A4 to axis A2 for the kinematics. The kinematics transformation compensates for the configured mechanical axis coupling. The axis coupling between axis A4 and axis A2 is implemented as a leadscrew pitch. With a compensation factor of 1.0, 360.0° on axis A4 corresponds to a distance of -1.0 mm on axis A2.

###### Transformation area

The kinematics transformation covers the following [traversing range](#traversing-range-and-transformation-area-s7-1500t) of the axes:

- Axis A1: -180.0° ≤ α1 &lt; 180.0°
- Axis A2: No limit
- Axis A3: No limit
- Axis A4: No limit

  An angle greater than 360° can be defined for the orientation. But coordinate A of the tool center point (TCP) is mapped in the range -180° to +180°.

> **Note**
>
> **Singularity**
>
> The kinematics has [singularity](#singularities-s7-1500t).

A singularity occurs when the zero point of the flange coordinate system (FCS) is located on the z axis of the kinematics coordinate system (KCS). Inverse transformation is not possible in this area. This position may result, e.g. if the length L2 is 0.0 due to the design.

The graphic below shows examples of permissible and impermissible joint positions for the transformation:

![Transformation area](images/158502958859_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ![Transformation area](images/156065229195_DV_resource.Stream@PNG-de-DE.png) | Permissible joint position |
| ![Transformation area](images/156065233419_DV_resource.Stream@PNG-de-DE.png) | Singularity at L2 = 0.0 |

###### Joint position space

The following table shows the possible arm positioning spaces of the kinematics:

| Tag |  |  | Data type | Values | W | Description |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| StatusKinematics. |  |  | TO_Struct_Kinematics_StatusKinematics |  |  |  |  |
|  | Valid |  | BOOL | - | RON | Validity of the transformation values |  |
| FALSE | Invalid |  |  |  |  |  |  |
| TRUE | Valid |  |  |  |  |  |  |
| LinkConstellation |  | DWORD | 0 to n | RON | Joint position space |  |  |
|  | Bit 0 | - | - | - | Position axis 1 |  |  |
| 0 | Not relevant |  |  |  |  |  |  |
| 1 | Not relevant |  |  |  |  |  |  |
| Bit 1 | - | - | - | Position axis 2 |  |  |  |
| 0 | Not relevant |  |  |  |  |  |  |
| 1 | Not relevant |  |  |  |  |  |  |
| Bit 2 | - | - | - | Angle α3 of axis A3 positive/negative taking into consideration the mechanical axis coupling |  |  |  |
| 0 | α3 positive |  |  |  |  |  |  |
| 1 | α3 negative |  |  |  |  |  |  |
| Bit 3 … 31 | - | - | - | Not relevant |  |  |  |

##### Tags: Cylindrical robot (S7-1500T)

###### Cylindrical robot 3D

You define the "Cylindrical robot 3D" kinematics using the following tags of the technology object:

| Tags | Values | Description |
| --- | --- | --- |
| &lt;TO&gt;.Kinematics.TypeOfKinematics | 21 | Cylindrical robot 3D |
| &lt;TO&gt;.Kinematics.Parameter[1] | -1.0E12 to 1.0E12 | Distance L1 of the zero position of the axis A2 to the kinematics zero point in z direction of the kinematics coordinate system (KCS) |
| &lt;TO&gt;.Kinematics.Parameter[2] | -1.0E12 to 1.0E12 | Distance L2 between the axes A2 and A3 in y direction of the KCS |
| &lt;TO&gt;.Kinematics.Parameter[3] | -1.0E12 to 1.0E12 | Distance of the flange coordinate system from the axis A3 in the negative z direction of the KCS |

###### Cylindrical robot 3D with orientation

You define the "Cylindrical robot 3D with orientation" kinematics using the following tags of the technology object:

| Tags | Values | Description |
| --- | --- | --- |
| &lt;TO&gt;.Kinematics.TypeOfKinematics | 22 | Cylindrical robot 3D with orientation |
| &lt;TO&gt;.Kinematics.Parameter[1] | -1.0E12 to 1.0E12 | Distance L1 of the zero position of the axis A2 to the kinematics zero point in z direction of the KCS |
| &lt;TO&gt;.Kinematics.Parameter[2] | -1.0E12 to 1.0E12 | Distance L2 between the axes A2 and A3 in y direction of the KCS |
| &lt;TO&gt;.Kinematics.Parameter[3] | -1.0E12 to 1.0E12 | Distance of the flange coordinate system from the axis A3 in the negative z direction of the KCS |
| &lt;TO&gt;.Kinematics.Parameter[4] | - | Mechanical axis coupling of axis A4 to A2 present/not present |
| 0 | Not present |  |
| 1 | Present |  |
| &lt;TO&gt;.Kinematics.Parameter[5] | -1.0E12 to 1.0E12 | Compensation factor of axis A4 to axis A2 |

#### Tripod (S7-1500T)

This section contains information on the following topics:

- [Tripod 3D (S7-1500T)](#tripod-3d-s7-1500t)
- [Tripod 3D with orientation (S7-1500T)](#tripod-3d-with-orientation-s7-1500t)
- [Tags: Tripod (S7-1500T)](#tags-tripod-s7-1500t)

##### Tripod 3D (S7-1500T)

The kinematics "Tripod 3D" supports 3 axes and 3 degrees of freedom. The axes are configured as parallel kinematics.

The following graphic shows the principal configuration and the typical working area of the kinematics:

![Figure](images/158500750091_DV_resource.Stream@PNG-de-DE.png)

The kinematics consists of 3 linear axes A1, A2 and A3.

The kinematics is modeled suspended and consists of an upper connecting plate, 3 arms and a lower connecting plate. The axes for the motion of the arms consist of rails with sliding carriages. The rails with the sliding carriages are fastened to the upper connecting plate. Connecting rods connect the sliding carriages to the lower connecting plate. The tool is suspended from the lower connecting plate. The parallelogram structures of the connecting rods keep the lower connecting plate parallel to the xy plane of the KCS.

###### Coordinate systems and zero position

The graphic below shows the following in the top view (xy plane):

- The position of the kinematics coordinate system (KCS)
- The angles of the axes A1, A2 and A3 to one another

![Coordinate systems and zero position](images/158500491531_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| β1 | Angle between the axes A1 and A2 |
| β2 | Angle between the axes A2 and A3 |
| [Legend for representation of the kinematics](#legend-for-representation-of-the-kinematics-s7-1500t) |  |

The following graphic shows the top view of the position of the flange coordinate system (FCS) in the xy plane of the lower connecting plate:

![Coordinate systems and zero position](images/158500744971_DV_resource.Stream@PNG-de-DE.png)

The graphic below shows the following in the front view (xz plane):

- The position of the axis A1 and the coordinate systems KCS and FCS
- The zero position of the axis A1
- The positive deflection of the axis A1 is indicated (dashed)

![Coordinate systems and zero position](images/158500739851_DV_resource.Stream@PNG-de-DE.png)

|  |  |  |
| --- | --- | --- |
| ![Coordinate systems and zero position](images/158499650955_DV_resource.Stream@PNG-de-DE.png) | Zero position of the kinematics |  |
| D1 | Distance of the upper hinge points of the connecting rods to the center of the upper connecting plate |  |
| D2 | Distance of the lower hinge points of the connecting rods to the center of the lower connecting plate |  |
| L1 | Length of the connecting rods |  |
| LF | Flange length before the FCS in the z direction of the KCS |  |
| γ | Angle between the upper connecting plate (xy plane of the KCS) and the rail of the axis A1 (0.0° ≤ γ &lt; 90.0°) |  |
| D1, D2, L1 and γ are identical for the three arms of the kinematics. |  |  |
| ![Coordinate systems and zero position](images/158499655179_DV_resource.Stream@PNG-de-DE.png) | Deflection of the kinematics with deflection of the axis A1 in positive direction |  |
| [Legend for representation of the kinematics](#legend-for-representation-of-the-kinematics-s7-1500t) |  |  |

The KCS with the kinematics zero point (KZP) is located at the center point of the upper connecting plate. The kinematics zero point is centered relative to the zero positions of the axes A1, A2 and A3.

The FCS is located in the center point of the lower connecting plate with identical distance D2 to the joint points of each connecting rod. You shift the FCS in the negative z direction of the KCS using length LF.

At the zero position, axes A1, A2 and A3 are in the xy plane of the KCS.

###### Transformation area

The kinematics transformation covers the following [traversing range](#traversing-range-and-transformation-area-s7-1500t) of the axes:

- Axes A1, A2 and A3: 0.0 ≤ Travel distance

> **Note**
>
> **Singularity**
>
> The kinematics has outer [singularities](#singularities-s7-1500t).

###### Joint position space

No arm positioning spaces for the kinematics.

##### Tripod 3D with orientation (S7-1500T)

The kinematics "Tripod 3D with orientation" supports 4 axes and 4 degrees of freedom. The axes are configured as parallel kinematics.

The following graphic shows the principal configuration and the typical working area of the kinematics:

![Figure](images/158500793611_DV_resource.Stream@PNG-de-DE.png)

The kinematics consists of the following axes:

- 3 linear axes A1, A2 and A3
- 1 rotary axis A4 with rotation around z in the KCS

The kinematics is modeled suspended and consists of an upper connecting plate, 3 arms and a lower connecting plate. The axes for the motion of the arms consist of rails with sliding carriages. The rails with the sliding carriages are fastened to the upper connecting plate. Connecting rods connect the sliding carriages to the lower connecting plate. The tool is suspended from the lower connecting plate. The parallelogram structures of the connecting rods keep the lower connecting plate parallel to the xy plane of the KCS. The kinematics axis A4 enables rotation of the tool around z in the KCS.

###### Coordinate systems and zero position

The graphic below shows the following in the top view (xy plane):

- The position of the kinematics coordinate system (KCS)
- The angles of the axes A1, A2 and A3 to one another

![Coordinate systems and zero position](images/158500491531_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| β1 | Angle between the axes A1 and A2 |
| β2 | Angle between the axes A2 and A3 |
| [Legend for representation of the kinematics](#legend-for-representation-of-the-kinematics-s7-1500t) |  |

The following graphic shows the top view of the position of the flange coordinate system (FCS) in the xy plane of the lower connecting plate:

![Coordinate systems and zero position](images/158500744971_DV_resource.Stream@PNG-de-DE.png)

The graphic below shows the following in the side view:

- The position of the axis A1 and the coordinate systems KCS and FCS
- The zero position of the axis A1
- The positive deflection of the axis A1 is indicated (dashed)

![Coordinate systems and zero position](images/158500798731_DV_resource.Stream@PNG-de-DE.png)

|  |  |  |
| --- | --- | --- |
| ![Coordinate systems and zero position](images/158499650955_DV_resource.Stream@PNG-de-DE.png) | Zero position of the kinematics |  |
| D1 | Distance of the upper joint points of the connecting rods to the center of the upper connecting plate |  |
| D2 | Distance of the lower joint points of the connecting rods to the center of the lower connecting plate |  |
| L1 | Length of the connecting rods |  |
| LF | Flange length before the FCS in the z direction of the KCS |  |
| γ | Angle between the upper connecting plate (xy plane of the KCS) and the rail of the axis A1 (0.0° ≤ γ &lt; 90.0°) |  |
| D1, D2, L1 and γ are identical for the three arms of the kinematics. |  |  |
| ![Coordinate systems and zero position](images/158499655179_DV_resource.Stream@PNG-de-DE.png) | Deflection of the kinematics with deflection of the axis A1 in positive direction |  |
| [Legend for representation of the kinematics](#legend-for-representation-of-the-kinematics-s7-1500t) |  |  |

The KCS with the kinematics zero point (KZP) is located at the center point of the upper connecting plate. The kinematics zero point is centered relative to the zero positions of the axes A1, A2 and A3.

The FCS is located in the center point of the lower connecting plate with identical distance D2 to the joint points of each connecting rod. You shift the FCS in the negative z direction of the KCS using length LF.

At the zero position, axes A1, A2 and A3 are in the xy plane of the KCS. At the zero position of axis A4, the x axis of the FCS points in the direction of the x axis of the KCS.

###### Transformation area

The kinematics transformation covers the following [traversing range](#traversing-range-and-transformation-area-s7-1500t) of the axes:

- Axes A1, A2 and A3: 0.0 ≤ Travel distance
- Axis A4: No limit

  An angle greater than 360° can be defined for the orientation. But coordinate A of the tool center point (TCP) is mapped in the range -180° to +180°.

> **Note**
>
> **Singularity**
>
> The kinematics has outer [singularities](#singularities-s7-1500t).

###### Joint position space

No arm positioning spaces for the kinematics.

##### Tags: Tripod (S7-1500T)

You define the tripod kinematics using the following tags of the technology object:

| Tags | Values | Description |
| --- | --- | --- |
| &lt;TO&gt;.Kinematics.TypeOfKinematics | 23 | Tripod 3D |
| 24 | Tripod 3D with orientation |  |
| &lt;TO&gt;.Kinematics.Parameter[1] | 0.0 to 1.0E12 | Distance D1 (radius of the upper connecting plate) |
| &lt;TO&gt;.Kinematics.Parameter[2] | 0.001 to 1.0E12 | Length L1 of connecting rods |
| &lt;TO&gt;.Kinematics.Parameter[3] | 0.0° to 89.999° | Angle γ between the linear axes and the x-y plane of the kinematics coordinate system |
| &lt;TO&gt;.Kinematics.Parameter[4] | 0.0 to 1.0E12 | Distance D2 (radius of the lower connecting plate) |
| &lt;TO&gt;.Kinematics.Parameter[5] | 90.001° to 179.998° | Angle β1 between the axes A1 and A2 |
| &lt;TO&gt;.Kinematics.Parameter[6] | 90.001° to 179.998° | Angle β2 between the axes A2 and A3 |
| &lt;TO&gt;.Kinematics.Parameter[7] | -1.0E12 to 1.0E12 | Distance of the flange coordinate system from the lower connecting plate in the negative z direction of the kinematics coordinate system |

#### User-defined kinematics systems (S7-1500T)

This section contains information on the following topics:

- [Brief description of user-defined kinematics (S7-1500T)](#brief-description-of-user-defined-kinematics-s7-1500t)
- [Tags: User-defined kinematics systems (S7-1500T)](#tags-user-defined-kinematics-systems-s7-1500t)

##### Brief description of user-defined kinematics (S7-1500T)

You can configure user-defined kinematics systems with corresponding axis interconnections:

- User-defined 2D
- User-defined 2D with orientation A
- User-defined 3D
- User-defined 3D with orientation A
- User-defined 3D with 3 orientations

The configuration supports you in a user-defined kinematics as follows:

- You interconnect the kinematics axes under "Technology object &gt; Configuration &gt; Interconnections".
- You define the transformation parameters under "Technology object &gt; Configuration &gt; Geometry". Up to 32 tags for defining the geometry of your kinematics are available on the system level.

You have to program the user transformation of the Cartesian positions and the axis positions and axis dynamics. Predefined interfaces are available on the system level. The function of the user transformation is different for kinematics with and without JCS:

- [User transformation without JCS](#user-transformation-without-jcs-s7-1500t)
- [User transformation with JCS](#user-transformation-with-jcs-s7-1500t)

##### Tags: User-defined kinematics systems (S7-1500T)

You configure the user-defined kinematics systems using the following tags of the technology object:

| Tag | Values | Description |
| --- | --- | --- |
| &lt;TO&gt;.Kinematics.TypeOfKinematics | 31 | User-defined 2D |
| 32 | User-defined 2D with orientation A |  |
| 33 | User-defined 3D |  |
| 34 | User-defined 3D with orientation A |  |
| 36 | User-defined 3D with 3 orientations |  |
| &lt;TO&gt;.Kinematics.Parameter[1..32] | - | Up to 32 user-specific parameters |

### Kinematics transformation (S7-1500T)

This section contains information on the following topics:

- [Brief description of the kinematics transformation (S7-1500T)](#brief-description-of-the-kinematics-transformation-s7-1500t)
- [Transformation for predefined kinematics systems (S7-1500T)](#transformation-for-predefined-kinematics-systems-s7-1500t)
- [Transformation for user-defined kinematics systems (S7-1500T)](#transformation-for-user-defined-kinematics-systems-s7-1500t)
- [Tags: Kinematics transformation (S7-1500T)](#tags-kinematics-transformation-s7-1500t)

#### Brief description of the kinematics transformation (S7-1500T)

The kinematics transformation is the conversion between the Cartesian coordinates of the kinematics motion and the setpoints for the individual kinematics axes:

- Forward transformation

  Calculation of the Cartesian coordinates from the axis positions of the kinematics axes
- Inverse transformation

  Calculation of the axis positions of the kinematics axes from the Cartesian coordinates

The kinematics transformation converts the position values and the dynamic values (velocity, acceleration).

The kinematics technology object provides the kinematics transformation for the predefined kinematics types on the system level. In the case of user-defined kinematics systems, you must calculate the [user transformation](#user-transformation-without-jcs-s7-1500t) in its own program.

#### Transformation for predefined kinematics systems (S7-1500T)

This section contains information on the following topics:

- [Reference points (S7-1500T)](#reference-points-s7-1500t)
- [Traversing range and transformation area (S7-1500T)](#traversing-range-and-transformation-area-s7-1500t)
- [Joint position spaces (kinematics-dependent) (S7-1500T)](#joint-position-spaces-kinematics-dependent-s7-1500t)
- [Singularities (S7-1500T)](#singularities-s7-1500t)

##### Reference points (S7-1500T)

The kinematics transformation uses the following reference points:

- Kinematics zero point (KZP)
- Zero positions of the kinematics axes
- Tool center point (TCP)

The positive direction of the axes for the kinematics transformation is dependent on the [kinematics type](#kinematics-types-s7-1500t). Configure the positive direction on the positioning axis/synchronous axis technology object corresponding to the positive direction of the axis in the kinematics.

###### Zero positions of the kinematics axes

The position 0.0 on the positioning axis/synchronous axis technology object defines the zero position of the kinematics axis. Reference the axes in such a way that the axes indicate the position 0.0 in the zero position of the kinematics. The zero position of the kinematics depends on the [kinematics type](#kinematics-types-s7-1500t).

##### Traversing range and transformation area (S7-1500T)

The transformation area is the area of the axis positions that the kinematics transformation covers. The kinematics type defines the transformation area for the individual kinematics axes. You will find information on the transformation area in the description of the individual [kinematics systems](#kinematics-types-s7-1500t).

The hardware and software limit switches of an axis define the maximum traversing range and the working area. The working area of a kinematics axis can be greater than or less than the transformation area depending on the axis configuration:

- Working area &gt; Transformation area

  When a kinematics axis exits the transformation area during a kinematics motion, the kinematics technology object outputs the technology alarm 803. The kinematics motion is aborted and the axes stop with the maximum dynamic values configured for the axes (alarm reaction: Stop with maximum dynamic values of the axes).
- Working area ≤ Transformation area

  When a kinematics axis runs into the software limit switch, the positioning axis/synchronous axis technology object outputs the technology alarm 533. The axis stops with the maximum dynamic values configured for the axis (alarm reaction: Stop with maximum dynamic values). When the axis is stopped, the kinematics technology object outputs the technology alarm 801. The kinematics motion is aborted and the axes stop with the maximum dynamic values configured for the axes (alarm reaction: Stop with maximum dynamic values of the axes).

The following graphic shows the relationship between the working area of the axis and the transformation area:

![Figure](images/158835190923_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | Mechanical end stop |
| ② | Hardware limit switch for positioning axis/synchronous axis technology object |
| ③ | Software limit switch for positioning axis/synchronous axis technology object |
| ④ | Maximum traversing range of the axis |
| ⑤ | Working area of the axis |
| ⑥ | Transformation area  (here working area &gt; transformation area) |

##### Joint position spaces (kinematics-dependent) (S7-1500T)

Depending on the kinematics type, a kinematics system can reach Cartesian coordinates via various joint positions. The [kinematics type](#kinematics-types-s7-1500t) defines the possible joint positions and the positive and negative joint position space. The joint positioning spaces are limited by the respective transformation areas. In addition, with the "Delta picker" kinematics type there are further limitations due to invalid joint positions and [singularities](#singularities-s7-1500t) with the kinematics types "articulated arm", "SCARA 3D" and "cylindrical robot". Also note the resulting constructional limitations due to the installation location of the kinematics.

The kinematics technology object indicates the current joint position in the "&lt;TO&gt;.StatusKinematics.LinkConstellation" tag.

The kinematics system cannot exit the joint position space during a linear or circular motion. You can change the arm positioning space using single-axis motions and synchronous "point-to-point" motion (sPTP motion).

###### Example: Kinematics type SCARA 3D

A "SCARA 3D" kinematics is to relocate an object from one pallet to another pallet. Due to a wall, the kinematics system cannot reach the second pallet without the axis A2 changing the joint position space.

The figure below shows the kinematics in the top view (xy plane):

![Example: Kinematics type SCARA 3D](images/158835661835_DV_resource.Stream@PNG-de-DE.png)

|  |  |  |
| --- | --- | --- |
| ![Example: Kinematics type SCARA 3D](images/158499650955_DV_resource.Stream@PNG-de-DE.png) | Zero position of the kinematics |  |
| ![Example: Kinematics type SCARA 3D](images/158499655179_DV_resource.Stream@PNG-de-DE.png) | Deflection of the kinematics in the positive direction when α1 = 45.0° with positive joint position when α2 = 120.0°  Deflection of the kinematics in the negative direction when α1 = -45.0° with negative joint position when α2 = -120.0° |  |
| α1 | Deflection of the axis A1 in positive direction when α1 = 45.0°  Deflection of the axis A1 in the negative direction when α1 = -45.0° |  |
| α2 | The deflection of the axis A2 in the positive direction when α2 = 120.0° produces a positive joint position.  The deflection of the axis A2 in negative direction when α2 = -120.0° produces a negative joint position. |  |
| [Legend for representation of the kinematics](#legend-for-representation-of-the-kinematics-s7-1500t) |  |  |

###### Example: "Articulated arm 3D" kinematics type

A kinematics "Articulated arm 3D" should move one object from one storage location to another. The kinematics cannot reach the second storage location because of the ceiling without axis A3 changing the arm positioning space.

The figure below shows the kinematics in the side view (xz plane):

![Example: "Articulated arm 3D" kinematics type](images/158835678859_DV_resource.Stream@PNG-de-DE.png)

|  |  |  |
| --- | --- | --- |
| ![Example: "Articulated arm 3D" kinematics type](images/158499650955_DV_resource.Stream@PNG-de-DE.png) | Zero position of the kinematics |  |
| ![Example: "Articulated arm 3D" kinematics type](images/158499655179_DV_resource.Stream@PNG-de-DE.png) | Deflection of the kinematics in the positive direction when α2 = 10.0° with positive joint position when α3 = 35.0°  Deflection of the kinematics in the negative direction when α2 = -15.0° with negative joint position when α3 = -75.0° |  |
| α2 | Deflection of the axis A2 in the positive direction when α2 = 10.0°  Deflection of the axis A2 in negative direction when α2 = -15.0° |  |
| α3 | The deflection of the A3 in the positive direction when α3 = 35.0° produces a positive joint position.  The deflection of the A3 in negative direction when α3 = -75.0° produces a negative joint position. |  |
| [Legend for representation of the kinematics](#legend-for-representation-of-the-kinematics-s7-1500t) |  |  |

###### Example: Kinematics type "cylindrical robot"

A kinematics "Cylindrical robot" should move an object from one storage location to another. The kinematics cannot reach the second storage location without axis A3 changing the arm positioning space.

The figure below shows the kinematics in the top view (xy plane):

![Example: Kinematics type "cylindrical robot"](images/158835683083_DV_resource.Stream@PNG-de-DE.png)

|  |  |  |
| --- | --- | --- |
| ![Example: Kinematics type "cylindrical robot"](images/158499650955_DV_resource.Stream@PNG-de-DE.png) | Zero position of the kinematics |  |
| ![Example: Kinematics type "cylindrical robot"](images/158499655179_DV_resource.Stream@PNG-de-DE.png) | Deflection of the kinematics in positive direction when α1 = 30.0°  Deflection of the kinematics in the negative direction when α1 = -75.0° |  |
| α1 | Deflection of the axis A1 in positive direction when α1 = 30.0°  Deflection of the axis A1 in the negative direction when α1 = -75.0° |  |
| [Legend for representation of the kinematics](#legend-for-representation-of-the-kinematics-s7-1500t) |  |  |

##### Singularities (S7-1500T)

Depending on the kinematics type, inverse transformation Cartesian coordinates are possible, which cannot be clearly converted into axis positions of the kinematics axes. The Cartesian coordinates at which this behavior occurs are referred to as singularities.

###### Inner singularities

The inner singularity occurs when the zero point of the flange coordinate system (FCS) is located on the z-axis of the kinematics coordinate system (KCS). The following kinematics have inner singularities:

- Articulated arm 3D
- Articulated arm 3D with orientation
- 6-axis articulated arm with central hand
- SCARA 3D with orientation
- Cylindrical robot 3D
- Cylindrical robot 3D with orientation

**Inner singularity using the articulated arm 3D as an example**

![Inner singularities](images/158917769739_DV_resource.Stream@PNG-de-DE.png)

In the vicinity of the inner singularity, a path motion without dynamic adaptation will result in an overrun of the dynamics of the kinematics axis A1 and the kinematics axis A4. This causes the entire kinematics to rotate with an overrun of the dynamics.

###### Outer singularities

An outer singularity occurs when one or more arms of the kinematics are completely extended or folded. The following kinematics have outer singularities:

- Articulated arm 2D
- Articulated arm 2D with orientation
- Articulated arm 3D
- Articulated arm 3D with orientation
- 6-axis articulated arm with central hand
- SCARA 3D with orientation
- Delta picker 2D
- Delta picker 2D with orientation
- Delta picker 3D
- Delta picker 3D with orientation
- Delta picker 3D with 2 orientations A, B
- Tripod 3D
- Tripod 3D with orientation

In the vicinity of these singularities a path motion without dynamic adaptation will result in an overrun of the dynamics at the kinematics axes, which can result in oscillations of the entire kinematics as well as excessive forces being applied.

**Extended position using the articulated arm 3D as an example**

![Outer singularities](images/158917773707_DV_resource.Stream@PNG-de-DE.png)

The articulated arm is fully extended and the flange is at the external limit of the maximum possible working range.

**Folded position using the articulated arm 3D as an example**

![Outer singularities](images/158917777675_DV_resource.Stream@PNG-de-DE.png)

The articulated arm is completely folded.

###### Behavior in the vicinity of a singularity

In the vicinity of a singularity a path motion without dynamic adaptation results in overruns of the dynamics. This means one or more kinematics axes can move at very high speed and accelerate or decelerate with excessive force. The size of the area in which this behavior occurs depends on the kinematics used.

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Overrun of the dynamics in the vicinity of a singularity**  An overrun of the dynamics in the vicinity of a singularity can result in the following damage:  - Personal injury, for example, caused by products or machine parts coming loose - Machine damages, for example, through overload of the mechanical components   Take into account the preventive measures described in this section to prevent this behavior. |  |

A path motion through a singularity is not possible. The technology alarm 803 "Error during calculation of the transformation" is output (alarm response: Stop with maximum dynamic values of the axes).

The kinematics system reduces the overruns of the dynamics caused by setpoints to the maximum dynamics of the axis. The reduction of the overruns of the dynamics can result in an unpredictable axis motion.

When the dynamic limits of the kinematics axes are exceeded, this is displayed at the affected kinematics axis with the tag "&lt;TO&gt;.StatusKinematicsMotion" and the technology alarm 511 "Dynamic limit is violated by the kinematics motion" is triggered. The technology alarm 511 does not trigger an alarm response and the kinematics motion is not stopped.

**Affected kinematics motions**

An overrun of the dynamics in the vicinity of a singularity only occurs for path motions without dynamic adaptation.

An overrun of the dynamics due to a singularity does not occur for the following motions:

- Synchronous point-to-point motion
- Motions in the MCS through the kinematics control panel

**Dynamic adaptation in the vicinity of singularities**

With movement in the vicinity of singularities with dynamic adaptation without segmentation of the path, dynamics can be significantly limited over the entire motion. Therefore, with motions in the vicinity of singularities, use the dynamic adaptation with segmentation of the path.

###### Preventive measures to prevent the behavior

By applying the following preventive measures, you can avoid a path motion without dynamic adaptation in the vicinity of a singularity:

1. Avoid the use of conveyor tracking in the vicinity of a singularity. Dynamic adaptation cannot be used in any phase of the conveyor tracking.
2. Activate [Dynamic adaptation](#configuring-dynamics-for-the-kinematics-and-the-orientation-motion-s7-1500t) for linear or circular motions that are not part of the phases of conveyor tracking.
3. To limit the working area of the kinematics, use zone monitoring or software limit switches at the kinematics axes.
4. Control with the kinematics control panel

   - Move the kinematics in the MCS.
   - In the WCS or OCS, avoid the "Jog" mode.

     The dynamic adaptation is not active in the kinematics control panel. The dynamic limits of the kinematics axes are not taken into account during a kinematics motion with the kinematics control panel.
   - Up to technology version V5.0 of the kinematics technology object: In the WCS or OCS, avoid using the "Jog to target position" mode.

     The dynamic adaptation is not active in the kinematics control panel. The dynamic limits of the kinematics axes are not taken into account during a kinematics motion with the kinematics control panel.
   - As of technology version V5.0 and higher: Move the kinematics to the "Jog to target position" mode in the WCS or OCS using the kinematics control panel.

     "Dynamic adaptation without segmentation of the path" is permanently active in the "Jog to target position" mode, and the dynamic limits of the kinematics axes are taken into account.

###### Determining the area with overrun of the dynamics for articulated arm 3D

To empirically determine the area in which overruns of the dynamics occur due to a singularity, use the following functions:

- Kinematics diagnostics
- Kinematics control panel
- Trace
- Virtual or simulated axes

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Deliberately traveling into the singularity**  The following damage may occur due to overruns of the dynamics in the vicinity of a singularity:  - Personal injury, for example, caused by products or machine parts coming loose - Machine damages, for example, through overload of the mechanical components   Do **not** determine the areas with overrun in the dynamics by moving the actual kinematics.  You **must** configure all kinematics axes as "virtual axis" or "axis in simulation". |  |

**Requirements**

- All kinematics axes are configured as virtual or simulated axes. The kinematics are interconnected.
- The geometry of the kinematics is configured to match the real kinematics.
- The dynamics for kinematics and all kinematics axes are configured.
- The permitted dynamics are known from the application.
- The tool center point is located at the origin of the FCS.

**Determining the distance to the inner singularity**

1. Configure a Trace with the following signals:

   - &lt;TOKinematics&gt;.A[1..6].Velocity
   - &lt;TOKinematics&gt;.A[1..6].Acceleration
   - &lt;TOKinematics&gt;.FlangeInKcs.x.Position
   - &lt;TOKinematics&gt;.FlangeInKcs.y.Position
   - &lt;TOKinematics&gt;.FlangeInKcs.z.Position
2. Open the diagnostics of the kinematics and arrange it next to the kinematics control panel.
3. Set the kinematics control panel as follows:

   - Operating mode: Jog
   - Coordinate system: WCS
   - Path velocity: Maximum required path velocity for the process
4. Make sure that all kinematics axes are configured as virtual axes or axes in simulation.
5. Jog the kinematics to a position from which the inner singularity could be reached.
6. Jog the kinematics backward a little (e.g. 1 mm) in y direction so that you can jog slightly past the singularity.
7. Jog the kinematics with maximum path velocity in x direction past the inner singularity and record the signals in the Trace.

   ![Determining the area with overrun of the dynamics for articulated arm 3D](images/158917794443_DV_resource.Stream@PNG-de-DE.png)

   | Symbol | Meaning |
   | --- | --- |
   | ![Determining the area with overrun of the dynamics for articulated arm 3D](images/158917809419_DV_resource.Stream@PNG-de-DE.png) | Jog forward and backward in x direction |
   | ![Determining the area with overrun of the dynamics for articulated arm 3D](images/158917814539_DV_resource.Stream@PNG-de-DE.png) | Jog backward in y direction |
8. Gradually increase the distance in y direction to the inner singularity. Repeat step 7.

   ![Determining the area with overrun of the dynamics for articulated arm 3D](images/158917800331_DV_resource.Stream@PNG-de-DE.PNG)

   The recorded Trace shows the dynamics of the axis A1 at different distances of the FCS to the inner singularity.
9. Determine the distance on the y-axis at which the dynamics of the kinematics axis A1 is permissible for your process.

   This distance corresponds to the radius of a cylinder around the z axis of the KCS in which overruns of the dynamics occur and the flange must not be moved.

> **Note**
>
> **Validity of the determined distance**
>
> The determined distance only applies to a kinematics with the configured geometry and dynamics.

> **Note**
>
> **Valid tool**
>
> Configure the tool once again so that the tool matches your application.

###### Limiting the working area with zone monitoring

The Cartesian space that must be excluded from the working area results from the determined distance.

You can find a description of the zone monitoring in section "[Zone monitoring](#zone-monitoring-s7-1500t)".

1. Define a cylindrical blocked zone or signal zone around the z-axis of the KCS:

   - Length z: Entire working area of the kinematics
   - Radius: Determined distance
   - x: Position of the KZP in x direction of the WCS
   - y: Position of the KZP in y direction of the WCS

   | Signal zone | Blocked zone |
   | --- | --- |
   | Useful in case of a major shift of the TCP from the origin of the FCS in x or y direction and when using conveyor tracking | Useful in case of a minor shift of the TCP from the origin of the FCS in x or y direction  Not very useful when using conveyor tracking |
   | Individually programmed stop reaction when: - Flange zone violates signal zone - Signal zone violated by TCP | Automatic stop reaction when: - Flange zone violates blocked zone - Blocked zone violated by TCP |
2. Define a spherical flange zone:

   - Radius: Distance required for the stop reaction
   - CS: FCS
   - x: 0.0
   - y: 0.0
   - z: 0.0

   ![Limiting the working area with zone monitoring](images/158917804299_DV_resource.Stream@PNG-de-DE.png)
3. When you are using a signal zone, program a stop reaction for the kinematics and any other axes, if necessary.

> **Note**
>
> **Extended position and folded position**
>
> You can also use this procedure to determine the area of the overruns of the dynamics in extended and folded positions and then limit the working area of the kinematics with zones.

---

**See also**

[Brief description of synchronous "point-to-point" motion (S7-1500T)](#brief-description-of-synchronous-point-to-point-motion-s7-1500t)

#### Transformation for user-defined kinematics systems (S7-1500T)

This section contains information on the following topics:

- [User transformation without JCS (S7-1500T)](#user-transformation-without-jcs-s7-1500t)
- [User transformation with JCS (S7-1500T)](#user-transformation-with-jcs-s7-1500t)
- [MC_Transformation [OB98] (S7-1500T)](#mc_transformation-ob98-s7-1500t)
- [Program example for a user-defined kinematics systems (S7-1500T)](#program-example-for-a-user-defined-kinematics-systems-s7-1500t)

##### User transformation without JCS (S7-1500T)

Unlike for predefined kinematics types, you must calculate the transformation for user-defined kinematics systems in your own program. Like for predefined kinematics types, the kinematics technology object performs the following tasks:

- Processing of Motion Control instructions
- Monitoring functions
- Communication with the interconnected axes

You program the user transformation of the Cartesian coordinates and the axis-specific setpoints in the MC_Transformation organization block. This programming includes the transformation of the positions and the dynamic values (velocity, acceleration). You freely define the parameters of a user-defined kinematics system in the tags of the kinematics technology object "&lt;TO&gt;.Kinematics.Parameter[1..32]" or under "Technology object &gt; Configuration &gt; Geometry".

When you add the MC_Transformation in the TIA Portal, the system data block "TransformationParameter" is automatically created under "Program blocks &gt; System blocks &gt; Program resources". In the properties of the organization block under "General &gt; Transformation", the MC_Transformation indicates the number of the system data block "TransformationParameter". You write and read the axis-specific data or the Cartesian data of the kinematics to be transformed in the system data block "TransformationParameter".

With the technology version V5.0, longer runtimes of the MC_Interpolator arise during user transformation. With longer runtimes of the MC_Interpolator, the runtimes of the organization blocks with lower priority are extended.

> **Note**
>
> **Disable system performance improvement**
>
> If you are using user-defined kinematics, clear the "Improve system performance" check box in the MC_LookAhead properties under "General &gt; Multi-core processor".

###### Programming

The graphic below shows the interfaces and the interaction of system performance and user transformation:

![Programming](images/168642312203_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ![Programming](images/156518746763_DV_resource.Stream@PNG-de-DE.png) | Processing by user program |
| ![Programming](images/156518750987_DV_resource.Stream@PNG-de-DE.png) | System performance |

The kinematics technology object automatically calls the MC_Transformation. The MC_Transformation contains the following start information:

- Kinematics technology object that calls the MC_Transformation
- Required direction of the transformation (forward or inverse transformation)
- Processing context of the transformation (current motion or motion planning)
- Pointer to the system data block "TransformationParameter" (VARIANT)

You evaluate this status information in your user program. In MC_Transformation, you program the algorithms for the calculation of the axis-specific data or the Cartesian data of all user-defined kinematics systems. You read the kinematics parameters needed for this from the tags of the "&lt;TO&gt;.Kinematics.Parameter[1..32]" technology object. You write the result of the calculation to the "TransformationParameter" interface.

The transformation parameters are then applied automatically to the kinematics technology object and processed further. The kinematics technology object outputs the setpoints to the kinematics axes.

You can configure and apply the user-defined transformation with multiple kinematics technology objects on a PLC. To differentiate in MC_Transformation between the different kinematics technology objects, use the input "KinematicsObject".

##### User transformation with JCS (S7-1500T)

Unlike for predefined kinematics types, you must calculate the transformation for user-defined kinematics systems in your own program. Like for predefined kinematics types, the kinematics technology object performs the following tasks:

- Processing of Motion Control instructions
- Monitoring functions
- Communication with the interconnected axes

You program the user transformation of the Cartesian coordinates and the joint-specific setpoints in the MC_Transformation organization block without considering inversions and offsets. If the joint directions of movement or the joint zero positions of the kinematics used do not correspond to the programmed user transformation, there are two ways to adapt them:

1. Retain the user transformation. Invert the affected joint directions of movement and joint zero positions in the "Joints" configuration window of the kinematics technology object. In this case, the joint-specific parameters "AxisData" in the system data block "Transformation" are not equal to the joint coordinates ("JointData"). The technology object performs this calculation automatically through the configured offsets and inversions.
2. Change the programmed user transformation in such a way that the calculated joint-specific setpoints from the transformation correspond to the joint coordinate system of the kinematics. In this case, the "AxisData" parameters in the "Transformation" system data block are equal to the joint coordinates ("JointData"). It is not necessary to configure the joint offset.

This programming includes the transformation of the positions and the dynamic values (velocity, acceleration). You freely define the parameters of a user-defined kinematics system in the tags of the kinematics technology object "&lt;TO&gt;.Kinematics.Parameter[1..32]" or under "Technology object &gt; Configuration &gt; Geometry".

When you add the MC_Transformation in the TIA Portal, the system data block "TransformationParameter" is automatically created under "Program blocks &gt; System blocks &gt; Program resources". In the properties of the organization block under "General &gt; Transformation", the MC_Transformation indicates the number of the system data block "TransformationParameter". You write and read the joint-specific data or the Cartesian data of the kinematics to be transformed in the system data block "TransformationParameter".

With the technology version V5.0, longer runtimes of the MC_Interpolator arise during user transformation. With longer runtimes of the MC_Interpolator, the runtimes of the organization blocks with lower priority are extended.

> **Note**
>
> **Disable system performance improvement**
>
> If you are using user-defined kinematics, clear the "Improve system performance" check box in the MC_LookAhead properties under "General &gt; Multi-core processor".

###### Programming

The graphic below shows the interfaces and the interaction of system performance and user transformation in a kinematics with used JCS:

![Programming](images/162907210891_DV_resource.Stream@PNG-en-US.png)

The kinematics technology object automatically calls the MC_Transformation. The MC_Transformation contains the following start information:

- Kinematics technology object that calls the MC_Transformation
- Required direction of the transformation (forward or inverse transformation)
- Processing context of the transformation (current motion or motion planning)
- Pointer to the system data block "TransformationParameter" (VARIANT)

You evaluate this status information in your user program. In MC_Transformation, you program the algorithms for the calculation of the axis-specific data or the Cartesian data of all user-defined kinematics systems. You read the kinematics parameters needed for this from the tags of the "&lt;TO&gt;.Kinematics.Parameter[1..32]" technology object. You write the result of the calculation to the "TransformationParameter" interface.

The transformation parameters are then applied automatically to the kinematics technology object and processed further. The kinematics technology object outputs the setpoints to the kinematics axes.

You can configure and apply the user-defined transformation with multiple kinematics technology objects on a PLC. To differentiate in MC_Transformation between the different kinematics technology objects, use the input "KinematicsObject".

> **Note**
>
> **Inverse transformation**
>
> In the inverse transformation, only the basic joint range "TurnJoint" = 0 needs to be programmed. The technology object automatically calculates the sPTP motions for the joint position ranges outside of the basic joint range "TurnJoint" ≠ 0.

##### MC_Transformation [OB98] (S7-1500T)

###### Reference declaration for system data block "TransformationParameter"

You must specify a reference to the data type for the system data block "TransformationParameter" in the MC_Transformation. For this purpose, you specify a tag with the following data type in the "Temp" area of the block interface:

"REF_TO TO_Struct_TransformationParameter_V2"

To enable access to the system data block "TransformationParameter", assign the data type "TO_Struct_TransformationParameter_V2" using the following casting command:

#P ?= #TransformationParameters;

The declaration is described in a [program example](#program-example-for-a-user-defined-kinematics-systems-s7-1500t).

###### Block call

The MC_Transformation is called in the [Motion Control application cycle](S7-1500-S7-1500T%20Motion%20Control%20Overview%20%28S7-1500%2C%20S7-1500T%29.md#process-response-s7-1500-s7-1500t) according to the configured priority. When the MC_Transformation is called, the kinematics technology object assigns its parameters:

| Parameter | Declaration | Data type | Default value | Description |  |
| --- | --- | --- | --- | --- | --- |
| KinematicsObject | INPUT | DB_ANY | - | Kinematics technology object for which the MC_Transformation calculates the transformation when called. |  |
| ExecutionContext | INPUT | DINT | - | Processing context of the MC_Transformation OB |  |
| 0 | MOTION_EXECUTION  Calculation of the axis setpoints in the motion execution in the MC_Interpolator. The calculated values are necessary for the current motion control. |  |  |  |  |
| 1 | NON_MOTION_EXECUTION  The transformation is necessary for the motion planning (currently no motion). |  |  |  |  |
| TransformationType | INPUT | DINT | - | Calculation called for |  |
| 0 | Forward transformation  Calculation of the Cartesian parameters from the axis positions |  |  |  |  |
| 1 | Inverse transformation  Calculation of the axis-specific parameters from the Cartesian parameters |  |  |  |  |
| TransformationParameters | InOut | VARIANT | - | Pointer to the system data block "TransformationParameter" |  |
| FunctionResult | OUTPUT | DINT | - | Return value of the MC_Transformation to the kinematics technology object |  |
| 0 | Calculation performed and parameters output |  |  |  |  |
| ≠ 0 | Error during calculation (user-defined)  If an error occurs during the calculation, the kinematics technology object stops the motion. The kinematics technology object outputs a technology alarm with the error ID as an accompany value and deletes the job sequence.  The value can be greater than or less than zero. |  |  |  |  |

###### Priority

You configure the priority of the MC_Transformation in the properties of the organization block under "General &gt; Attributes &gt; Priority". For the priority you can set values from 17 to 25 (default setting 25):

- The priority of MC_Transformation must be at least one level lower than the priority of MC_Servo.
- The priority of MC_Transformation must be at least one level higher than the priority of MC_Interpolator.

###### Tags of the system data block "TransformationParameter"

The following table shows the tags in the system data block "TransformationParameter":

> **Note**
>
> If JCS is used, the "AxisData" tags are to be interpreted as joint-specific setpoints.

| Tag |  | Data type | Description |  |
| --- | --- | --- | --- | --- |
| AxisData. |  | STRUCT_ Transformation AxisData_V2 | JCS not used:  Axis-specific parameters | JCS used:  Joint-specific parameters without consideration of inversions and offsets |
|  | a1Position | LREAL | Position setpoint of the axis A1 | Position setpoint of the joint J1 |
| a1Velocity | LREAL | Velocity setpoint of the axis A1 | Velocity setpoint of the joint J1 |  |
| a1Acceleration | LREAL | Acceleration setpoint of the axis A1 | Acceleration setpoint of the joint J1 |  |
| a2Position | LREAL | Position setpoint of the axis A2 | Position setpoint of the joint J2 |  |
| a2Velocity | LREAL | Velocity setpoint of the axis A2 | Velocity setpoint of the joint J2 |  |
| a2Acceleration | LREAL | Acceleration setpoint of the axis A2 | Acceleration setpoint of the joint J2 |  |
| a3Position | LREAL | Position setpoint of the axis A3 | Position setpoint of the joint J3 |  |
| a3Velocity | LREAL | Velocity setpoint of the axis A3 | Velocity setpoint of the joint J3 |  |
| a3Acceleration | LREAL | Acceleration setpoint of the axis A3 | Acceleration setpoint of the joint J3 |  |
| a4Position | LREAL | Position setpoint of the axis A4 | Position setpoint of the joint J4 |  |
| a4Velocity | LREAL | Velocity setpoint of the axis A4 | Velocity setpoint of the joint J4 |  |
| a4Acceleration | LREAL | Acceleration setpoint of the axis A4 | Acceleration setpoint of the joint J4 |  |
| a5Position | LREAL | Position setpoint of the axis A5 | Position setpoint of the joint J5 |  |
| a5Velocity | LREAL | Velocity setpoint of the axis A5 | Velocity setpoint of the joint J5 |  |
| a5Acceleration | LREAL | Acceleration setpoint of the axis A5 | Acceleration setpoint of the joint J5 |  |
| a6Position | LREAL | Position setpoint of the axis A6 | Position setpoint of the joint J6 |  |
| a6Velocity | LREAL | Velocity setpoint of the axis A6 | Velocity setpoint of the joint J6 |  |
| a6Acceleration | LREAL | Acceleration setpoint of the axis A6 | Acceleration setpoint of the joint J6 |  |
| CartesianData |  | STRUCT_ Transformation CartesianData_V2 | Cartesian parameters and joint position space |  |
|  | xPosition | LREAL | x position |  |
| xVelocity | LREAL | x velocity |  |  |
| xAcceleration | LREAL | x acceleration |  |  |
| yPosition | LREAL | y position |  |  |
| yVelocity | LREAL | y velocity |  |  |
| yAcceleration | LREAL | y acceleration |  |  |
| zPosition | LREAL | z position |  |  |
| zVelocity | LREAL | z velocity |  |  |
| zAcceleration | LREAL | z acceleration |  |  |
| aPosition | LREAL | A-position (orientation) |  |  |
| aVelocity | LREAL | A velocity (orientation) |  |  |
| aAcceleration | LREAL | A acceleration (orientation) |  |  |
| bPosition | LREAL | B position (orientation) |  |  |
| bVelocity | LREAL | B velocity (orientation) |  |  |
| bAcceleration | LREAL | B acceleration (orientation) |  |  |
| cPosition | LREAL | C position (orientation) |  |  |
| cVelocity | LREAL | C velocity (orientation) |  |  |
| cAcceleration | LREAL | C acceleration (orientation) |  |  |
| LinkConstellation | DWORD | Joint position space |  |  |

##### Program example for a user-defined kinematics systems (S7-1500T)

An example of user transformation in the [MC_Transformation](#mc_transformation-ob98-s7-1500t) of a 2D kinematics with the name "KinematicsUserDefined2D" is described below. For these kinematics, two transformation parameters were defined under "Technology object &gt; Configuration &gt; Geometry".

The interaction of system performance and user transformation is displayed in the figure in section "[User transformation without JCS](#user-transformation-without-jcs-s7-1500t)".

The following table shows the declaration of the tags used:

| Tag | Declaration | Data type | Description |  |
| --- | --- | --- | --- | --- |
| KinematicsObject | Input | DB_ANY | Reference to the technology object |  |
| TransformationType | Input | DInt | Transformation direction |  |
| 0 | Forward transformation |  |  |  |
| 1 | Inverse transformation |  |  |  |
| FunctionResult | Output | DInt | Transformation result |  |
| 0 | Successful |  |  |  |
| &lt; 0 | Error |  |  |  |
| TransformationParameters | InOut | Variant | Reference to the system data block "TransformationParameter" in the MC_Transformation |  |
| P | Temp | REF_TO TO_Struct_TransformationParameter_V2 | Temporary tag for the casting command |  |
| GearRatioA1 | Temp | LReal | Temporary tag for read the defined transformation parameters |  |
| GearRatioA2 | Temp | LReal | Temporary tag for read the defined transformation parameters |  |
| InvalidCast | Constant | DInt | Return value for an unsuccessful casting command |  |

The program example is structured as follows:

- Casting command for access to the system data block "TransformationParameter"
- Evaluation of the technology object
- Read the defined transformation parameters
- Evaluation of the transformation direction
- Calculation of the Cartesian coordinates from the axis positions of the kinematics axes (forward transformation)
- Calculation of the axis positions of the kinematics axes from the Cartesian coordinates (backward transformation)

First, the example program is explained step by step. The program code is summarized in the section "Program example".

###### Casting command for access to the system data block "TransformationParameter"

The casting command enables access the transformation parameters defined in the configuration.

The variant pointer is passed on to the temporary tag using the casting command.

#P ?= #TransformationParameters;

It is then tested whether the casting command was successful. This means that the specified InOut tag "TransformationParameters" has the expected structure of type "TO_Struct_TransformationParameter_V1".

If the casting command was not successful, the calculation is canceled and the tag "FunctionResult" gets the value "InvalidCast".

IF #P = NULL THEN

    #FunctionResult := #InvalidCast;

    RETURN;

END_IF;

###### Evaluation of the technology object

An IF query is used to evaluate whether the user-defined kinematics requires the transformation defined below.

IF #KinematicsObject = "KinematicsUserDefined2D" THEN

###### Read the defined transformation parameters

First, the transformation parameters defined in the configuration are read out. Two gears ratios were defined in this example.

#GearRatioA1 := "KinematicsUserDefined2D".Kinematics.Parameter[1];

    #GearRatioA2 := "KinematicsUserDefined2D".Kinematics.Parameter[2];

###### Evaluation of the transformation direction

The transformation direction is evaluated in the next step. If the tag "TransformationType" has the value "0", the forward transformation is calculated. If the tag has the value "1", the backward transformation is calculated.

IF #TransformationType = 0 THEN

###### Calculation of the Cartesian coordinates from the axis positions of the kinematics axes (forward transformation)

In the forward transformation, Cartesian data (position, velocity and acceleration) are calculated from the axis data. The forward transformation is first calculated in x direction and then in z direction.

#P^.CartesianData.xPosition := #P^.AxisData.a1Position * #GearRatioA1;

        #P^.CartesianData.xVelocity := #P^.AxisData.a1Velocity * #GearRatioA1;

        #P^.CartesianData.xAcceleration := #P^.AxisData.a1Acceleration * #GearRatioA1;

        #P^.CartesianData.zPosition := #P^.AxisData.a2Position * #GearRatioA2;

        #P^.CartesianData.zVelocity := #P^.AxisData.a2Velocity * #GearRatioA2;

        #P^.CartesianData.zAcceleration := #P^.AxisData.a2Acceleration * #GearRatioA2;

The specification of the arm positioning space is not required in this example. The corresponding tag is set to zero.

#P^.CartesianData.LinkConstellation := 16#0000;

If the transformation is successful, the tag "FunctionResult" receives the value "0".

#FunctionResult := 0;

###### Calculation of the axis positions of the kinematics axes from the Cartesian coordinates (backward transformation)

In the backward transformation, axis data (position, velocity and acceleration) are calculated from the Cartesian data. The backward transformation is first calculated for axis A1 and then for axis A2.

ELSIF #TransformationType = 1 THEN

        #P^.AxisData.a1Position := #P^.CartesianData.xPosition / #GearRatioA1;

        #P^.AxisData.a1Velocity := #P^.CartesianData.xVelocity / #GearRatioA1;

        #P^.AxisData.a1Acceleration := #P^.CartesianData.xAcceleration / #GearRatioA1;

        #P^.AxisData.a2Position := #P^.CartesianData.zPosition / #GearRatioA2;

        #P^.AxisData.a2Velocity := #P^.CartesianData.zVelocity / #GearRatioA2;

        #P^.AxisData.a2Acceleration := #P^.CartesianData.zAcceleration / #GearRatioA2;

If the transformation is successful, the tag "FunctionResult" receives the value "0".

#FunctionResult := 0;

    END_IF;

END_IF;

###### Program example

The program example is summarized with Commentary in the following section:

SCL

//Caste of the variant "TransformationParameters" to the referenced datatype

//"TO_Struct_TransformationParameter_V2".

//This has to be done in order to access the variant pointer, which references

//the "TransformationParameters" where the "AxisData" and "CartesianData" for

//the calculation of user transformation are stored.

#P ?= #TransformationParameters;

//Check if cast of "TransformationParameters" was successfull. Otherwise abort calculation.

IF #P = NULL THEN

    #FunctionResult := #InvalidCast;

    RETURN;

END_IF;

//Check if "KinematicsUserDefined2D" needs transformation.

IF #KinematicsObject = "KinematicsUserDefined2D" THEN

    //Read the user defined cartesian parameters.

    #GearRatioA1 := "KinematicsUserDefined2D".Kinematics.Parameter[1];

    #GearRatioA2 := "KinematicsUserDefined2D".Kinematics.Parameter[2];

    //Calculate the forward transformation "AxisData" -&gt; "CartesianData".

    //The system fills the "AxisData" of "TransformationParameters" with values.

    //To calculate the "CartesianData" evaluate "AxisData".

    IF #TransformationType = 0 THEN

        //Calculate the position, velocity and acceleration component for the x-vector.

        #P^.CartesianData.xPosition := #P^.AxisData.a1Position * #GearRatioA1;

        #P^.CartesianData.xVelocity := #P^.AxisData.a1Velocity * #GearRatioA1;

        #P^.CartesianData.xAcceleration := #P^.AxisData.a1Acceleration * #GearRatioA1;

        //Calculate the position, velocity and acceleration component for the z-vector.

        #P^.CartesianData.zPosition := #P^.AxisData.a2Position * #GearRatioA2;

        #P^.CartesianData.zVelocity := #P^.AxisData.a2Velocity * #GearRatioA2;

        #P^.CartesianData.zAcceleration := #P^.AxisData.a2Acceleration * #GearRatioA2;

        //Link constellation can be set to 0 here, hence it is not needed.

        #P^.CartesianData.LinkConstellation := 16#0000;

        //Transformation was successfull.

        #FunctionResult := 0;

    //Calculate the backward transformation "CartesianData" -&gt; "AxisData".

    //The system fills the "CartesianData" of "TransformationParameters" with values.

    //To calculate the "AxisData" evaluate "CartesianData".

    ELSIF #TransformationType = 1 THEN

        //Calculate the position, velocity and acceleration component for the first axis.

        #P^.AxisData.a1Position := #P^.CartesianData.xPosition / #GearRatioA1;

        #P^.AxisData.a1Velocity := #P^.CartesianData.xVelocity / #GearRatioA1;

        #P^.AxisData.a1Acceleration := #P^.CartesianData.xAcceleration / #GearRatioA1;

        //Calculate the position, velocity and acceleration component for the second axis.

        #P^.AxisData.a2Position := #P^.CartesianData.zPosition / #GearRatioA2;

        #P^.AxisData.a2Velocity := #P^.CartesianData.zVelocity / #GearRatioA2;

        #P^.AxisData.a2Acceleration := #P^.CartesianData.zAcceleration / #GearRatioA2;

        //Transformation was successfull.

        #FunctionResult := 0;

    END_IF;

END_IF;

###### Check the validity of the transformation/cartesian values

Check the "&lt;TO&gt;.StatusKinematics.Valid" bit cyclically, e.g. in the MC_PostServo. If "&lt;TO&gt;.StatusKinematics.Valid" shows the value "FALSE", then the Cartesian values are invalid. In this case, initiate a stop action, for example, with the Motion Control instruction "MC_GroupStop".

Check the setpoint specification of the Cartesian values and the programmed user transformation.

#### Tags: Kinematics transformation (S7-1500T)

The following tags of the kinematics technology object are relevant for the kinematics transformation:

| Tag | Description |  |
| --- | --- | --- |
| **Status values** |  |  |
| &lt;TO&gt;.StatusKinematics.Valid | TRUE | Transformation/Cartesian values valid |
| FALSE | Transformation/Cartesian values invalid |  |
| &lt;TO&gt;.StatusKinematics.LinkConstellation | Joint position space |  |
| &lt;TO&gt;.FlangeInKcs | Current transformation frame (with dynamics, setpoint reference) |  |

## Kinematics functions (S7-1500T)

This section contains information on the following topics:

- [Offset and rotation of the coordinate system (S7-1500T)](#offset-and-rotation-of-the-coordinate-system-s7-1500t)
- [Zone monitoring (S7-1500T)](#zone-monitoring-s7-1500t)
- [Overview of kinematics motions (S7-1500T)](#overview-of-kinematics-motions-s7-1500t)
- [Moving a kinematics in a linear manner (S7-1500T)](#moving-a-kinematics-in-a-linear-manner-s7-1500t)
- [Moving a kinematics in a circular manner (S7-1500T)](#moving-a-kinematics-in-a-circular-manner-s7-1500t)
- [Moving a kinematics with a synchronous "point-to-point" motion (S7-1500T)](#moving-a-kinematics-with-a-synchronous-point-to-point-motion-s7-1500t)
- [Conveyor Tracking (S7-1500T)](#conveyor-tracking-s7-1500t)
- [Set kinematics to simulation mode (S7-1500T)](#set-kinematics-to-simulation-mode-s7-1500t)

### Offset and rotation of the coordinate system (S7-1500T)

This section contains information on the following topics:

- [Brief description of offset and rotation (S7-1500T)](#brief-description-of-offset-and-rotation-s7-1500t)
- [Define KCS/OCS frame (S7-1500T)](#define-kcsocs-frame-s7-1500t)
- [Define tool frames (S7-1500T)](#define-tool-frames-s7-1500t)
- [Tags: Coordinate systems and frames (S7-1500T)](#tags-coordinate-systems-and-frames-s7-1500t)

#### Brief description of offset and rotation (S7-1500T)

You can define the following frames in the configuration for a technology object kinematics:

| Frame | Description |
| --- | --- |
| KCS frame | Position of the kinematics coordinate system (KCS) in the world coordinate system (WCS) |
| OCS1..3 frame | Position of the object coordinate systems 1 to 3 (OCS1..3) in the WCS |
| Tool frame | Position of the tool coordinate system (TCS) in the FCS |

The position of the frames is determined by the offset and the rotation in the reference coordinate system.

##### Offset

You use the shift to define the position of the zero point of a coordinate system or a zone within the reference coordinate system. You specify the offset in Cartesian coordinates.

The following table shows the definition of the offset:

| Value in the frame | Description |
| --- | --- |
| x | Shift in the x direction in the reference coordinate system |
| y | Shift in the y direction in the reference coordinate system |
| z | Shift in the z direction in the reference coordinate system |

##### Rotation

You use the rotation to define the orientation of a coordinate system or a zone within the reference coordinate system. The rotation is made up of three successive individual rotations around the axes of the coordinate system which you define using three Euler angles. The individual rotations depend on each other.

The following graphic shows the three successive rotations using a cuboid zone as an example:

![Rotation](images/158922977675_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | Rotation A |
| ② | Rotation B |
| ③ | Rotation C |

The following table shows the definition of the rotations:

| Rotation | Description |
| --- | --- |
| Rotation A | Euler angle of the first rotation  A positive angle corresponds to a clockwise rotation around the z axis of the coordinate system.  The coordinate system rotated once consists of the axes x', y' and z. |
| Rotation B | Euler angle of the second rotation  A positive angle corresponds to a clockwise rotation around the rotated y' axis.  The coordinate system rotated twice consists of the axes x'', y' and z'. |
| Rotation C | Euler angle of the third rotation  A positive angle corresponds to a clockwise rotation around the rotated x'' axis.  The coordinate system rotated three times consists of the axes x'', y'' and z''. The x'', y'' and z'' axes correspond to the x, y and z axes of the rotated coordinate system or of the rotated zone. |

#### Define KCS/OCS frame (S7-1500T)

##### Define KCS/OCS frame offline

In the following configuration windows, you configure the position of the KCS/OCS frames in the world coordinate system (WCS):

- You configure the position of the KCS in the WCS in the "Kinematics coordinate system" configuration window.
- You configure the position of the OCS in the WCS in the "Object coordinate system" configuration window.

**Select object coordinate system (OCS)**

In the "Object coordinate system" configuration window, select the object coordinate system to be defined in the "Object coordinate system (OCS)" drop-down list. You can define up to three tool object coordinate systems.

**Enter offset and rotation**

To define a frame, enter the values for the offset and rotation. Since the kinematics types support different numbers of degrees of freedom, enter only the values that are relevant and permissible for your kinematics type.

The following table shows you the values that you can specify during configuration (✓) and their valid value ranges.

| Kinematics type | KCS/OCS frame |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Offset |  |  | Rotation |  |  |  |
| x | y | z | A | B | C |  |
| **2D** | ✓ | 0.0 | ✓ | 0.0 | ✓  -180.0° to 179.999° | 0.0 |
| **2D with orientation** | ✓ | 0.0<sup>1)</sup> | ✓ | 0.0<sup>2)</sup> | 0.0 | 0.0 |
| **3D** | ✓ | ✓ | ✓ | ✓  -180.0° to 179.999° | ✓  -90.0° to 90.0° | ✓  -180.0° to 179.999° |
| **3D with orientation** | ✓ | ✓ | ✓ | ✓  -180.0° to 179.999° | 0.0 | 0.0 |
| **3D with 2 orientations A, B** | ✓ | ✓ | ✓ | ✓  -180.0° to 179.999° | 0.0 | 0.0 |
| **3D with 3 orientations** | ✓ | ✓ | ✓ | ✓  -180.0° to 179.999° | ✓  -90.0° to 90.0° | ✓  -180.0° to 179.999° |
| **6-axis articulated arm with central hand** |  |  |  |  |  |  |
| <sup>1)</sup> For the kinematics type "SCARA 2D", an offset in the y direction is permissible.   <sup>2)</sup> For the kinematics type "SCARA 2D", a rotation around A is permissible.  Value = 0.0: Offset/rotation not permitted or not relevant |  |  |  |  |  |  |

##### Calibrate OCS

[Calibration](#calibration-s7-1500t) enables you to determine the exact position of an OCS in the WCS in online or offline mode or check an OCS already defined in the WCS.

##### Define OCS frames with Motion Control instructions

With the "[MC_SetOcsFrame](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_setocsframe-v8-s7-1500t)" Motion Control instruction, you define the position of an object coordinate system (OCS) in relation to the world coordinate system (WCS).

#### Define tool frames (S7-1500T)

##### Define tool frames offline

In the "Tools" configuration window, you configure the tool frames and also the position of the tool center point (TCP) of the tools in the flange coordinate system (FCS). You can define up to three tools.

**Select tool**

Select the tool to be defined in the "Tool" drop-down list. You can define up to three tools.

**Enter offset and rotation**

To define a frame, enter the values for the offset and rotation. Since the kinematics types support different numbers of degrees of freedom, enter only the values that are relevant and permissible for your kinematics type.

The following table shows you the values that you can specify during configuration (✓) and their valid value ranges.

| Kinematics type | Tool frame |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Offset |  |  | Rotation |  |  |  |
| x | y | z | A | B | C |  |
| **2D** | ✓ | 0.0 | ✓ | 0.0 | 0.0 | 0.0 |
| **2D with orientation** | 0.0 | 0.0 | ✓ | ✓  -180.0° to 179.999° | 0.0 | 0.0 |
| **3D** | ✓ | ✓ | ✓ | 0.0 | 0.0 | 0.0 |
| **3D with orientation** | ✓ | ✓ | ✓ | ✓  -180.0° to 179.999° | 0.0 | 0.0 |
| **3D with 2 orientations A, B** | ✓ | ✓ | ✓ | 0.0 | ✓  -180.0° to 179.999° | 0.0 |
| **3D with 3 orientations** | ✓ | ✓ | ✓ | ✓  -180.0° to 179.999° | ✓  -90.0° to 90.0° | ✓  -180.0° to 179.999° |
| **6-axis articulated arm with central hand** |  |  |  |  |  |  |
| Value = 0.0: Offset/rotation not permitted |  |  |  |  |  |  |

##### Define tool frame with Motion Control instructions

You can use the "[MC_DefineTool](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_definetool-redefine-tool-v8-s7-1500t)" Motion Control instruction to redefine the tool frame of tool 1.

##### Example

**Tool frame with a kinematics "Delta picker 3D with 2 orientations A, B"**

The following example shows a possible definition of the tool frame with a kinematics "Delta picker 3D with 2 orientations A, B". The tool is rotated by B = -90° in relation to the FCS and is shifted in direction x and z.

![Example](images/158951033355_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | Tool frame |

#### Tags: Coordinate systems and frames (S7-1500T)

The following tags of the kinematics technology object are relevant for coordinate systems and frames:

| Tag | Description |
| --- | --- |
| **Configuration** |  |
| &lt;TO&gt;.KcsFrame | KCS frame  x, y, z, A, B, C |
| &lt;TO&gt;.OcsFrame[1..3] | OCS frame  x, y, z, A, B, C |
| &lt;TO&gt;.Tool[1..3] | Tool frame  x, y, z, A, B, C |
| **Status values** |  |
| &lt;TO&gt;.Tcp | Position of the tool center point (TCP), TCP frame in the world coordinate system (WCS).  x, y, z, A, B, C |
| &lt;TO&gt;.TcpInWcs | Parameter for tool center point in the world coordinate system  x, y, z, A, B, C |
| &lt;TO&gt;.TcpInOcs[1..3] | Parameter for the tool center point (TCP) in the Object Coordinate Systems 1 to 3 (OCS)  x, y, z, A, B, C |
| &lt;TO&gt;.FlangeInKcs | Parameter for the flange coordinate system (FCS) in the kinematics coordinate system (KCS)  x, y, z, A, B, C |
| &lt;TO&gt;.StatusOcsFrame[1..3] | Display of the OCS frames  x, y, z, A, B, C |

### Zone monitoring (S7-1500T)

This section contains information on the following topics:

- [Brief description of zone monitoring (S7-1500T)](#brief-description-of-zone-monitoring-s7-1500t)
- [Configuring zones (S7-1500T)](#configuring-zones-s7-1500t)
- [Zone violation (S7-1500T)](#zone-violation-s7-1500t)
- [Retracting after a zone violation (S7-1500T)](#retracting-after-a-zone-violation-s7-1500t)
- [Tags: Zone monitoring (S7-1500T)](#tags-zone-monitoring-s7-1500t)

#### Brief description of zone monitoring (S7-1500T)

The zone monitoring has the following purposes:

- Protection from collisions with mechanical installations
- Triggering of process-related actions (signal zones)

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Inappropriate use of zone monitoring**  Zone monitoring is not suitable for preventing personal injury.  1. Implement suitable protective measures to prevent personal injury, e.g. protective fences or safety doors. 2. Use safety functions for safe monitoring of the kinematics, for example, with SIMATIC Safe Kinematics. |  |

##### Zones

Zones are geometric bodies you can use to describe and subdivide the workspace of a kinematics system. You can configure the following zones on the kinematics technology object:

- **Workspace zones**

  Workspace zones describe the environment of a kinematics system. You can configure the following zone types as workspace zones for the kinematics technology object:

  - Work zone

    With work zones, you limit the possible travel space of the kinematics or define several possible work areas.
  - Signal zone

    Signal zones are areas within the traversing space of the kinematics. Signal zones indicate the following:

    • Kinematics zone is entering the signal zones

    • Kinematics zone is located in the signal zone
  - Blocked zone

    Blocked zones are areas within the traversing space of the kinematics in which a kinematics zone must not enter (e.g. control cabinet, protective wall).
- **Kinematics zones**

  Kinematics zones envelope the end point of a kinematics system (flange or tool).

  Kinematics zones are related to the working point/flange of a kinematics and move with the kinematics. The zone monitoring checks the kinematics zones for penetration with workspace zones. With kinematics zones, you expand the monitored area beyond the tool center point (TCP). The tool center point (TCP) is permanently defined as the first kinematics zone (&lt;TO&gt;.KinematicsZone[1]) and always activated.

  You can configure the following zone types as kinematics zones for the kinematics technology object:

  - Tool zone

    Tool zones envelope the tool or parts of the tool.
  - Flange zone

    Flange zones envelope the flange or parts of the flange.

The following example shows how the zone types of a kinematics are used:

![Zones](images/158920012299_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| **Workspace zones** |  |
| ![Zones](images/150608080139_DV_resource.Stream@PNG-de-DE.png) | Work zone |
| ![Zones](images/150608084363_DV_resource.Stream@PNG-de-DE.png) | Signal zone |
| ![Zones](images/150608088587_DV_resource.Stream@PNG-de-DE.png) | Blocked zone |
| **Kinematics zones** |  |
| ![Zones](images/158927078539_DV_resource.Stream@PNG-de-DE.png) | Flange zone and tool zone |

---

**See also**

[Zones status (S7-1500T)](#zones-status-s7-1500t)
  
[Tags: Zone monitoring (S7-1500T)](#tags-zone-monitoring-s7-1500t)
  
[Configuring a workspace zone offline (S7-1500T)](#configuring-a-workspace-zone-offline-s7-1500t)
  
[Configuring kinematics zones offline (S7-1500T)](#configuring-kinematics-zones-offline-s7-1500t)
  
[Zones (S7-1500T)](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#zones-s7-1500t-4)
  
[SIMATIC Safe Kinematics](https://support.industry.siemens.com/cs/ww/en/view/109801883)

#### Configuring zones (S7-1500T)

This section contains information on the following topics:

- [Configuring zones (S7-1500T)](#configuring-zones-s7-1500t-1)
- [Configuring a workspace zone offline (S7-1500T)](#configuring-a-workspace-zone-offline-s7-1500t)
- [Configuring kinematics zones offline (S7-1500T)](#configuring-kinematics-zones-offline-s7-1500t)
- [Defining the zone geometry (S7-1500T)](#defining-the-zone-geometry-s7-1500t)
- [Defining the offset and rotation in the reference coordinate system (S7-1500T)](#defining-the-offset-and-rotation-in-the-reference-coordinate-system-s7-1500t)
- [Activating zone monitoring (S7-1500T)](#activating-zone-monitoring-s7-1500t)

##### Configuring zones (S7-1500T)

You have the following options to define workspace zones:

- Via the "Zones" configuration window, you can [Configuring a workspace zone offline](#configuring-a-workspace-zone-offline-s7-1500t).
- Via the [Calibration](#calibration-s7-1500t) configuration window, you can define workspace zones in online and offline mode.
- With the Motion Control instruction ["MC_DefineWorkspaceZone"](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_defineworkspacezone-define-workspace-zone-v8-s7-1500t), you define a workspace zone during runtime.

You have the following options to define kinematics zones:

- Via the "Zones" configuration window, you can [Configuring kinematics zones offline](#configuring-kinematics-zones-offline-s7-1500t).
- With the Motion Control instruction ["MC_DefineKinematicsZone"](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_definekinematicszone-define-kinematics-zone-v8-s7-1500t), you define a kinematics zone during runtime.

###### "Zones" configuration window

The "Zones" configuration window is divided into the following areas:

- Graphic view

  The workspace zones or the kinematics zones, which you define in the tabular editor, are displayed in the graphic view. You operate the 3D visualization via the toolbar. For more information about operating the toolbar and the graphic display, refer to the section "[3D visualization](#3d-visualization-s7-1500t)".
- Tabular editor of the workspace zones

  You [configure the workspace zones](#configuring-a-workspace-zone-offline-s7-1500t) here.
- Tabular editor of the kinematics zones
- You [configure the kinematics zones](#configuring-kinematics-zones-offline-s7-1500t) here.

###### Online view

When you click on the ![Online view](images/134636636043_DV_resource.Stream@PNG-de-DE.png) symbol, values of the workspace zones and the kinematics zones at the current point in time are read back from the CPU. When you click the ![Online view](images/134692367371_DV_resource.Stream@PNG-de-DE.png) icon in the "Number" column, two additional rows are displayed. The additional rows contain the following values:

- ![Online view](images/134692378763_DV_resource.Stream@PNG-de-DE.png) Start values of the CPU
- ![Online view](images/134692757643_DV_resource.Stream@PNG-de-DE.png) Start values in project

  You can edit these values. If you want to apply the change, load the changes from the project into the device.

##### Configuring a workspace zone offline (S7-1500T)

You can configure up to 10 workspace zones in the kinematics configuration window under "Extended parameters &gt; Zones &gt; Workspace zones".

1. In the "Status" column, select whether [zone monitoring](#activating-zone-monitoring-s7-1500t) for the zone should be active or inactive after loading into the device.
2. In the "Zone type" column, select whether the zone is a work zone, signal zone or blocked zone.

   - **Work zone**

     You can specify several work zones.

     Only one work zone can be activated at a given time. If no work zone is activated, the entire traversing space of the kinematics is regarded as the work area.

     Kinematics zones must be located within work zones.
   - **Signal zone**

     You can specify several signal zones. Multiple signal zones can be activated at the same time.

     Signal zones can be located outside the work zone to some extent.
   - **Blocked zone**

     You can specify several blocked zones. Multiple blocked zones can be activated at the same time.

     Blocked zones can be located outside the work zone to some extent.
3. In the "Geometry" column, select whether the zone is a sphere, a cuboid or a cylinder.
4. Configure the [zone geometry](#defining-the-zone-geometry-s7-1500t).
5. In the "KS" column, select the coordinate system in which the zone is defined.

   You can select the following coordinate systems:

   - WCS (world coordinate system)
   - OCS1 (object coordinate system 1)
   - OCS2 (object coordinate system 2)
   - OCS3 (object coordinate system 3)

   If you create the zone in an OCS, the zone moves together with the OCS.
6. Enter the [offset and rotation of the zero point](#defining-the-offset-and-rotation-in-the-reference-coordinate-system-s7-1500t) of the zone.

   The offset of the zone to the zero point of the WCS or OCS remains constant.

##### Configuring kinematics zones offline (S7-1500T)

You can configure up to 9 kinematics zones in the kinematics configuration window under "Extended parameters &gt; Zones &gt; Kinematics zones".

1. In the "Status" column, select whether [zone monitoring](#activating-zone-monitoring-s7-1500t) for the zone should be active or inactive after loading into the device.
2. In the "Geometry" column, select whether the zone is a sphere, a cuboid or a cylinder.
3. Configure the [zone geometry](#defining-the-zone-geometry-s7-1500t).
4. In the "KS" column, select the coordinate system in which the zone is defined.

   You can select the following coordinate systems:

   - If you select TCS, the zone envelops the tool or parts of it and moves with the tool (TCP).
   - If you select FCS, the zone envelops the flange or parts of it and moves with the flange.
5. Enter the [offset and rotation of the zero point](#defining-the-offset-and-rotation-in-the-reference-coordinate-system-s7-1500t) of the zone.

   The offset of the zone to the zero point of the TCS or FCS remains constant.

**Tool changeover**

If you wish to define and use more than one tool, check whether the dimensions of a tool zone are suitable for all tools and envelop them. Otherwise, create a separate zone for each of the tools dimensioned differently.

###### Example of tool zone

You define tool zones in the tool coordinate system (TCS). The following graphic shows a spherical tool zone:

![Example of tool zone](images/158923840395_DV_resource.Stream@PNG-de-DE.png)

###### Example of flange zone

You define flange zones in the flange coordinate system (FCS). The following graphic shows a cylindrical flange zone:

![Example of flange zone](images/158923845515_DV_resource.Stream@PNG-de-DE.png)

In this example, a shift by the height of the flange zone in negative z direction of the FCS has been defined.

##### Defining the zone geometry (S7-1500T)

You can configure zones with the following geometric bodies:

- ![Figure](images/158890048907_DV_resource.Stream@PNG-de-DE.png) Sphere
- ![Figure](images/158890040715_DV_resource.Stream@PNG-de-DE.png) Cuboid
- ![Figure](images/158890044811_DV_resource.Stream@PNG-de-DE.png) Cylinder

###### Sphere

You define a sphere starting from the zero point using the radius:

![Sphere](images/158924055435_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| r | Radius of the sphere |

**Configuration**

1. Select the ![Sphere](images/158890048907_DV_resource.Stream@PNG-de-DE.png) icon in the "Geometry" column.
2. Enter the radius in the "Radius" column.

**Motion Control instructions**

In the Motion Control instructions "MC_DefineWorkspaceZone" and "MC_DefineKinematicsZone", specify the zone geometry in these parameters:

| Parameter | Value |
| --- | --- |
| GeometryType | 1 |
| GeometryParameter[1] | Radius of the sphere |

###### Cuboid

You define a cuboid starting from the zero point using the edge lengths in x, y and z direction:

![Cuboid](images/158924060555_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| Lx | Edge length in x direction of the zone coordinate system |
| Ly | Edge length in y direction of the zone coordinate system |
| Lz | Edge length in z direction of the zone coordinate system |

**Configuration**

1. Select the ![Cuboid](images/158890040715_DV_resource.Stream@PNG-de-DE.png) icon in the "Geometry" column.
2. Enter the edge lengths in the following columns:

   - In the "Length x" column, edge length in x direction of the zone coordinate system
   - In the "Length y" column, edge length in y direction of the zone coordinate system
   - In the "Length z" column, edge length in z direction of the zone coordinate system

**Motion Control instructions**

In the Motion Control instructions "MC_DefineWorkspaceZone" and "MC_DefineKinematicsZone", specify the zone geometry in these parameters:

| Parameter | Value |
| --- | --- |
| GeometryType | 0 |
| GeometryParameter[1] | Edge length in x direction of the zone coordinate system |
| GeometryParameter[2] | Edge length in y direction of the zone coordinate system |
| GeometryParameter[3] | Edge length in z direction of the zone coordinate system |

###### Cylinder

You define a cylinder starting from the zero point using the radius of the base and the cylinder height:

![Cylinder](images/158924065675_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| r | Radius of the base of the cylinder |
| Lz | Height of the cylinder |

**Configuration**

1. Select the ![Cylinder](images/158890044811_DV_resource.Stream@PNG-de-DE.png) icon in the "Geometry" column.
2. Enter the height of the cylinder in the "Length z" column.
3. Enter the radius of the base in the "Radius" column.

**Motion Control instructions**

In the Motion Control instructions "MC_DefineWorkspaceZone" and "MC_DefineKinematicsZone", specify the zone geometry in these parameters:

| Parameter | Value |
| --- | --- |
| GeometryType | 2 |
| GeometryParameter[1] | Radius of the base of the cylinder |
| GeometryParameter[2] | Height of the cylinder |

##### Defining the offset and rotation in the reference coordinate system (S7-1500T)

Define the offset and rotation of the geometric body starting from the zero point of the reference coordinate system as follows:

1. Define the offset of the zone by entering the following values:

   - x: Offset of the zone in the x direction
   - y: Offset of the zone in the y direction
   - z: Offset of the zone in the z direction
2. Define the rotation of the zone by entering the following values:

   (Not relevant for a spherical zone)

   - A: Enter a value between -180.0° and 179.999° for the rotation of the zone around the z axis.
   - B: Enter a value between -90.0° and 90.0° for the rotation of the zone around the y axis.
   - C: Enter a value between -180.0° and 179.999° for the rotation of the zone around the x axis.

###### Defining the position and rotation in a Motion Control instruction

In the Motion Control instructions "MC_DefineWorkspaceZone" and "MC_DefineKinematicsZone", specify the offset and rotation in the "Frame" parameter.

##### Activating zone monitoring (S7-1500T)

Note the following when activating zone monitoring for work zones:

- Only one work zone can be active at a given time.
- If no work zone is activated, the entire traversing space of the kinematics is regarded as the work area.

###### Configuring the status offline

You activate or deactivate zone monitoring for a defined zone in the tabular editor in the "Zones" configuration window. In the "Column" status, select whether the zone should be active or inactive after loading into the device.

###### Activating and deactivating zone monitoring online

You can activate and deactivate zones online in your user program using the following Motion Control instructions:

- [MC_SetWorkspaceZoneActive: Activate workspace zone V8](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_setworkspacezoneactive-activate-workspace-zone-v8-s7-1500t)
- [MC_SetWorkspaceZoneInactive: Deactivate workspace zone V8](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_setworkspacezoneinactive-deactivate-workspace-zone-v8-s7-1500t)
- [MC_SetKinematicsZoneActive: Activate kinematics zone V8](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_setkinematicszoneactive-activate-kinematics-zone-v8-s7-1500t)
- [MC_SetKinematicsZoneInactive: Deactivate kinematics zone V8](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_setkinematicszoneinactive-deactivate-kinematics-zone-v8-s7-1500t)

#### Zone violation (S7-1500T)

The zone monitoring checks all activated workspace zones (work zones, signal zones, blocked zones) for collision with all activated kinematics zones (flange zones, tool zones, TCP). The zone monitoring monitors the zones for all motions of the kinematics system:

- Kinematics motions via the user program or kinematics control panel
- Single axis motions via the user program or axis control panel

The status of the zone monitoring is indicated in the [diagnostics](#zones-status-s7-1500t) and in the [tags](#tags-zone-monitoring-s7-1500t) of the kinematics technology object.

If the zone monitoring detects a zone violation by a kinematics motion, the following reactions occur:

| Zone violation | Reaction | Description |
| --- | --- | --- |
| Exiting the work zone | Alarm with stop | The kinematics technology object outputs technology alarm 806 (alarm response: Stop without leaving the path). The kinematics motion is stopped. The kinematics leaves the zone by the length of the deceleration distance at a minimum. |
| Entering a signal zone | Alarm without stop | The kinematics technology object outputs a technology alarm 807 (no alarm response). The kinematics motion will be continued. |
| Entering a blocked zone | Alarm with stop | The kinematics technology object outputs a technology alarm 806 (alarm response: Stop without leaving the path). The kinematics motion is stopped. The kinematics violates the zone by the length of the brake path at a minimum. All jobs in the job sequence are canceled. |

The kinematics technology object outputs a technology alarm following zone violations by single axis motions. The positioning axis/synchronous axis technology object outputs a technology alarm. The single axis motion is not aborted. You can abort the single axis motion in the application.

In addition to the zones of the kinematics technology object, you can limit the travel space of the kinematics as follows:

- Software limit switches at the axes
- Joint traversing ranges

#### Retracting after a zone violation (S7-1500T)

Once you have acknowledged the technology alarm on the kinematics technology object, you can move the kinematics system again.

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Zone monitoring for violated zone deactivated after acknowledgment**  After you have acknowledged the technology alarm on the kinematics technology object, the zone monitoring is deactivated for the violated zone until the kinematics exits the violated blocked zone / signal zone or enters the violated work zone again. You can move the kinematics in all directions including again into the violated blocked zone / signal zone or from the work zone.  Take into consideration the travel direction when retracting the kinematics. |  |

Monitor retraction in the application. The zone monitoring status is still displayed in the data block technology object.

After the kinematics has exited the violated blocked zone / signal zone again or entered the violated work zone again, zone monitoring is activated again for this zone. A new technology alarm is therefore triggered when the zone is violated again.

#### Tags: Zone monitoring (S7-1500T)

The following tags of the kinematics technology object are relevant for the zone monitoring:

| Tag | Description |
| --- | --- |
| **Zone configuration** |  |
| &lt;TO&gt;.WorkspaceZone[1..10] | Configuration of the workspace zones |
| &lt;TO&gt;.KinematicsZone[2..10] | Configuration of the kinematics zones  The &lt;TO&gt;.KinematicsZone[1] zone is the tool center point (TCP) and is always activated. |
| **Status values** |  |
| &lt;TO&gt;.StatusWorkspaceZone[1..10] | Status of the workspace zones |
| &lt;TO&gt;.StatusKinematicsZone[2..10] | Status of the kinematics zones |
| &lt;TO&gt;.StatusZoneMonitoring.WorkingZones | Display of violated work zones  Bit numbers 0 to 9 correspond to the configured zone numbers. |
| &lt;TO&gt;.StatusZoneMonitoring.BlockedZones | Display of violated blocked zones  Bit numbers 0 to 9 correspond to the configured zone numbers. |
| &lt;TO&gt;.StatusZoneMonitoring.SignalizingZones | Display of approached signal zones  Bit numbers 0 to 9 correspond to the configured zone numbers. |
| &lt;TO&gt;.StatusZoneMonitoring.KinematicsZones | Display of kinematics zones that violate workspace zones  Bit number 0 indicates the monitoring status of the TCP. Bit numbers 1 to 9 correspond to the configured zone numbers. |

### Overview of kinematics motions (S7-1500T)

This section contains information on the following topics:

- [Brief description of overview of kinematics motions (S7-1500T)](#brief-description-of-overview-of-kinematics-motions-s7-1500t)
- [Introduction to the programming of the kinematics motions (S7-1500T)](#introduction-to-the-programming-of-the-kinematics-motions-s7-1500t)
- [Define target position (S7-1500T)](#define-target-position-s7-1500t)
- [Motion status and remaining distance (S7-1500T)](#motion-status-and-remaining-distance-s7-1500t)
- [Interrupting, continuing and stopping kinematics motions (S7-1500T)](#interrupting-continuing-and-stopping-kinematics-motions-s7-1500t)
- [Motion dynamics (S7-1500T)](#motion-dynamics-s7-1500t)
- [Motion preparation using multiple jobs (S7-1500T)](#motion-preparation-using-multiple-jobs-s7-1500t)
- [Interaction of kinematics motions and single axis motions (S7-1500T)](#interaction-of-kinematics-motions-and-single-axis-motions-s7-1500t)
- [Tags: Kinematics motions (S7-1500T)](#tags-kinematics-motions-s7-1500t)

#### Brief description of overview of kinematics motions (S7-1500T)

With kinematics motions, you move the kinematics through the three-dimensional space and rotate the kinematics with up to three orientations. Plan the kinematics motion in advance. Take into consideration the following:

- Reachable points of the kinematics
- Zones
- Transformation areas
- Joint position spaces
- Joint traversing ranges
- Software limit switches of axes

##### Motion types

The following motion types are available:

- [Linear motion](#moving-a-kinematics-in-a-linear-manner-s7-1500t)

  You can move the kinematics linearly to a defined target position with a linear motion.
- [Circular motion](#moving-a-kinematics-in-a-circular-manner-s7-1500t)

  You can move the kinematics using a defined circular path with a circular motion.
- [sPTP motion](#moving-a-kinematics-with-a-synchronous-point-to-point-motion-s7-1500t)

  With a synchronous "point-to-point" motion (sPTP motion), you can move a kinematics time- and motion-optimized, bypass singularities or change joint position spaces. The kinematics does not follow a specified path. The single-axis motions, which move the kinematics axes synchronously, are calculated from the start and target positions.
- [Conveyor tracking](#conveyor-tracking-s7-1500t)

  With conveyor tracking, the kinematics can follow an object on a moving conveyor belt.
- Orientation motion

  The orientation motion is the motion of the Cartesian orientation and is performed at the same time as the path motion. When motions are smoothed, the orientation motion is also smoothed. When the circular motion stops, the orientation motion also stops.

##### Reference coordinate system

The target position and the target orientation you specify for a kinematics motion can relate to different coordinate systems, e.g. the world coordinate system (WCS) or an object coordinate system (OCS).

#### Introduction to the programming of the kinematics motions (S7-1500T)

You can use Motion Control instructions in the user program to transmit jobs to the technology object. You can find an overview of the Motion Control instructions for the kinematics technology object in the section "[Motion control instructions for kinematics control](#motion-control-instructions-for-kinematics-control-s7-1500t)".

You configure the job with the input parameters of the Motion Control instructions. The current job status is indicated in the output parameters.

Because the kinematics technology object groups the kinematics axes, you assign the kinematics technology object directly to the input parameter "AxesGroup".

You cannot enable the kinematics technology object itself using an "MC_Power" command or home it using an "MC_Home" job. For kinematics motions, the interconnected axes must be enabled ("MC_Power.Enable" = TRUE).

You can acknowledge errors of the kinematics technology object with an "MC_Reset" job or by restarting the technology object.

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Unexpected axis motions**  The kinematics can perform unexpected motions due to the incorrect configuration of the technology objects or parameter assignment of the motion control jobs.  This can cause the following damages:  - Personal injury, for example, caused by products or machine parts coming loose - Machine damages, for example, through overload of the mechanical components or collision between kinematics and machine components   Before you start the user program, implement the following preventive measures:  1. Check the correct configuration of all technology objects that are used for the motion sequence of the kinematics. 2. Check the correct parameter assignment of the motion control instructions. 3. Protect the configuration and user program against unauthorized access. |  |

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Overrun of the dynamics through singularities**  Overruns of the dynamics in the vicinity of a [singularity](#singularities-s7-1500t) can result in the following damages:   - Personal injury, for example, caused by products or machine parts coming loose - Machine damages, for example, through overload of the mechanical components   To prevent overruns of the dynamics in the vicinity of a singularity, implement the following preventive measures:  1. Avoid path motions without dynamic adaptation in the vicinity of a singularity. 2. Use blocked zones or software limit switches for kinematics motions in the vicinity of a singularity. 3. Avoid the use of conveyor tracking in the vicinity of a singularity. Dynamic adaptation cannot be used in any phase of the conveyor tracking. 4. Programming motions that are not part of the phases of conveyor tracking:    - For linear or circular motions, activate the [dynamic adaptation](#configuring-dynamics-for-the-kinematics-and-the-orientation-motion-s7-1500t).    - Use [synchronous "point-to-point" motions](#brief-description-of-synchronous-point-to-point-motion-s7-1500t). |  |

#### Define target position (S7-1500T)

You define the target position in a Motion Control instruction for a kinematics motion depending on the kinematics type.

##### Define offset and rotation

Enter the values according to the following specifications:

| Kinematics type | Target position |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Offset |  |  | Rotation |  |  |  |
| x | y | z | A | B | C |  |
| **2D** | ✓ | 0.0 | ✓ | 0.0 | 0.0 | 0.0 |
| **2D with orientation** | ✓ | 0.0 | ✓ | ✓  -180.0° to 179.999° | 0.0 | 0.0 |
| **3D** | ✓ | ✓ | ✓ | 0.0 | 0.0 | 0.0 |
| **3D with orientation** | ✓ | ✓ | ✓ | ✓  -180.0° to 179.999° | 0.0 | 0.0 |
| **3D with 2 orientations A, B** | ✓ | ✓ | ✓ | ✓  -180.0° to 179.999° | ✓  -90.0° to 90.0° | ✓  0.0 / -180.0° |
| **3D with 3 orientations** | ✓ | ✓ | ✓ | ✓  -180.0° to 179.999° | ✓  -90.0° to 90.0° | ✓  -180.0° to 179.999° |
| **6-axis articulated arm with central hand** |  |  |  |  |  |  |
| ✓ Value for offset/rotation configurable  Value = 0.0: Offset/rotation not permitted |  |  |  |  |  |  |

##### Examples

The following examples of a kinematics type with more than 4 interpolating kinematics axes show 4 different positions of the TCP at the target position reached. The target positions are configured in each case with the same shift, but with different rotation.

![Examples](images/159009180939_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① … ④ | Position in the WCS |

##### Orientation in path motion jobs for 3D kinematics with 2 orientations

You can move a 3D kinematics with 2 orientations to a Cartesian position with a differently configured orientation. The following figures show the kinematics with different joint positions at the same target position with different orientation of the TCP. The effective direction of the tool in x direction of the TCP is the same in both cases. However, due to the rotation C, the tool is rotated -180° around the x axis of the TCP.

![Orientation in path motion jobs for 3D kinematics with 2 orientations](images/158659880075_DV_resource.Stream@PNG-de-DE.png)

The following figure shows the orientation motion B in which joint J5 is moved beyond 0° and joint J4 is stationary. Since values greater than 90° for orientation B are not permitted, configure the Cartesian orientations as follows in order to move beyond the vertical position without rotating joint J4:

- A: By -180° (from 0° to -180° or also, e.g. from 20° to -160°)
- B: 90° when position of the TCP is vertical, decreasing to 0°
- C: -180°

Abrupt changes in orientations A and C do not lead to abrupt position changes on the joints or kinematics axes.

![Orientation in path motion jobs for 3D kinematics with 2 orientations](images/158957321227_DV_resource.Stream@PNG-de-DE.png)

#### Motion status and remaining distance (S7-1500T)

You can obtain the status and the remaining distance of a motion job from the parameters of the corresponding Motion Control instruction.

##### Status of a motion job

You can identify the status of a motion job based on the "Busy" and "Active" parameters. When the job is transmitted, the "Busy" parameter is set to TRUE and the job is added to the job sequence. As long as the job is still in the job sequence, the "Active" parameter is set to FALSE. As soon as the job is active in the motion control, the "Active" parameter is set to TRUE. If the motion job is completed, the parameters "Busy" and "Active"are set to FALSE and the parameter "Done" to TRUE.

All inactive jobs in the job sequence are recalculated if another motion job is added to the job sequence. The current job is also included in the new calculation so that the current job can be blended with the next job.

##### Remaining distance of a motion job

You can obtain the remaining distance of a motion job from the "RemainingDistance" parameter. If the motion is not being blended, the "RemainingDistance" parameter contains the distance to the target position on the path. If the active motion is being blended with the next motion, the "RemainingDistance" parameter contains the distance to the beginning of the blending segment on the path. If only the Cartesian orientation of the TCP is changed in a motion task, but the TCP is at the Cartesian coordinates x, y, z, then the "RemainingDistance" parameter has the value "-1.0".

With an sPTP motion job, the execution progress is displayed with the "ExecutionTimeStatus" parameter instead of the remaining path. The parameter value starts at "0.0" and increases incrementally in the course of job execution until the job is completed at "1.0".

##### Distance of linear and circular motion jobs

The status tag "&lt;TO&gt;.StatusPath.AccumulatedPathLength" contains the distance already covered by the TCP of all completed motion jobs and the current motion job.

The status tag "&lt;TO&gt;.StatusPath.TotalPathLength" contains the total path length of the TCP for all jobs in the job sequence.

The total path length is the sum of:

- Distance of all completed motion jobs
- Distance travelled of the active motion job
- Remaining distance of the motion job
- Calculated distance of all jobs in the job sequence

Distances based on the following motion jobs are not taken into account:

- Synchronous "point-to-point" motions (sPTP motion)

  Exception: Blending segment between path motion and sPTP motion
- Active conveyor tracking
- Pure orientation motions

If there are no jobs in the job sequence and the last motion job is completed, then "AccumulatedPathLength" and "TotalPathLength" are equal.

##### Resetting distances

To reset the tags "AccumulatedPathLength" and "TotalPathLength" to zero in the user program, use one of the following instructions:

- Call "MC_Reset" with "Restart = TRUE" for the kinematics.
- Call "MC_GroupStop" for the kinematics.

The two tags are automatically reset during the following actions.

- Operating state changes from STOP to RUN
- Startup after POWER ON of the CPU

##### Calculate remaining distance of all jobs of the job sequence

To determine the remaining distance of all jobs in the job sequence, subtract "AccumulatedPathLength" from "TotalPathLength".

Remaining distance of the job sequence = "TotalPathLength" - "AccumulatedPathLength"

**Example: Three linear motion jobs with smoothing**

![Calculate remaining distance of all jobs of the job sequence](images/158924249995_DV_resource.Stream@PNG-de-DE.png)

The starting point is point A. From point A, three linear path jobs are sent to points B, C and D. Blending is carried out in the second and third jobs. The path length is 0 mm at the beginning of the example. To simplify this, a 2D kinematics without orientation motion is used.

![Calculate remaining distance of all jobs of the job sequence](images/158924255115_DV_resource.Stream@PNG-de-DE.png)

![Calculate remaining distance of all jobs of the job sequence](images/158941220619_DV_resource.Stream@PNG-de-DE.png)

At time ①, the first linear motion job is started from point A to point B. The tag "AccumulatedPathLength" is 0.0 mm at the time ① because the kinematics is not yet moving. "TotalPathLength" outputs the distance 100.0 mm between point A and point B. After the TCP moves, the "AccumulatedPathLength" tag shows the distance already moved.

When the second linear motion job is issued at time ②, the distance to point B is added, taking into account the smoothing, and displayed in "TotalPathLength". The total path length is now 281.8 mm. The second linear motion job becomes active at time ③.

At time ④, the third linear motion job is sent to point D. The total path length of 363.5 mm between point A and point D is now displayed in "TotalPathLength" . The third linear motion job becomes active at time ⑤.

At the time ⑥, the TCP reaches point D and all motion jobs are completed. The "AccumulatedPathLength" corresponds to the "TotalPathLength", as no more motion jobs are processed in the job sequence.

#### Interrupting, continuing and stopping kinematics motions (S7-1500T)

You can interrupt and continue active kinematics motions or stop them and thus also cancel queued motion jobs.

##### Suspend kinematics motions

With the Motion Control instruction "[MC_GroupInterrupt](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_groupinterrupt-v8-s7-1500t)", you interrupt the execution of the motion on a kinematics technology object. With the "Mode" parameter, you specify the dynamic behavior. The kinematics can be stopped either with the dynamics of the motion job to be interrupted or with the maximum dynamics. When dynamic adaptation is activated, the dynamics of the motion can also be reduced so that the dynamic limits of the axes are not exceeded. The current path is not exited when the kinematics is stopped. If the kinematics is already at a standstill, the motion control is also interrupted for subsequent motion jobs.

The kinematics technology object is in "Interrupted" status (&lt;TO&gt;.StatusWord.X17).

##### Continue kinematics motions

With the Motion Control instruction "[MC_GroupContinue](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_groupcontinue-v8-s7-1500t)", you continue a kinematics motion that was previously interrupted with an "MC_GroupInterrupt" job. The kinematics motion can be continued if the kinematics has come to a standstill following the "MC_GroupInterrupt" job.

The "MC_GroupContinue" job only has an effect if the kinematics technology object is in "Interrupted" status (&lt;TO&gt;.StatusWord.X17).

##### Stop kinematics motions

With the Motion Control instruction "[MC_GroupStop](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_groupstop-v8-s7-1500t)", you stop the Motion Control of the kinematics technology object. In so doing, both the active motion job as well as all queued jobs in the job sequence are canceled and the job sequence is emptied. If the kinematics motion was already interrupted with an "MC_GroupInterrupt" job, this job is also canceled. As long as the "Execute" parameter is set to TRUE, the following kinematics jobs are rejected ("ErrorID" = 16#80CD).

With the "Mode" parameter, you specify the dynamic behavior. The kinematics can be stopped either with the dynamics of the motion job to be stopped or with the maximum dynamics. When dynamic adaptation is activated, the dynamics of the motion can also be reduced so that the dynamic limits of the axes are not exceeded. The current path is not exited when the kinematics is stopped.

---

**See also**

[Job sequence (S7-1500T)](#job-sequence-s7-1500t)

#### Motion dynamics (S7-1500T)

This section contains information on the following topics:

- [Brief description of motions dynamics (S7-1500T)](#brief-description-of-motions-dynamics-s7-1500t)
- [Configuring dynamics for the kinematics and the orientation motion (S7-1500T)](#configuring-dynamics-for-the-kinematics-and-the-orientation-motion-s7-1500t)
- [Configuring dynamics for the sPTP motion (S7-1500T)](#configuring-dynamics-for-the-sptp-motion-s7-1500t)
- [Dynamic adaptation (S7-1500T)](#dynamic-adaptation-s7-1500t)
- [Override (S7-1500T)](#override-s7-1500t)

##### Brief description of motions dynamics (S7-1500T)

Configure the following values in the "Dynamics" configuration window:

- Default values for the dynamics, the dynamic limits of the path motion and the orientation motion
- Default values for the dynamics of the sPTP motion
- Dynamic adaptation

##### Configuring dynamics for the kinematics and the orientation motion (S7-1500T)

###### Dynamic limits of the kinematics

The configured dynamic limits of the kinematics configured under "Technology object &gt; Configuration &gt; Extended parameters &gt; Dynamics" are taken into account during the motion execution. The dynamics of a motion can be restricted so that the dynamic limits of the kinematics are not exceeded. When you change the dynamic limits of the kinematics, the changes take effect immediately for the kinematics motion and orientation motion.

###### Dynamic limits of the kinematics axes

When a motion job is transmitted, the dynamic limits of the kinematics axes configured under "Technology object &gt; Configuration &gt; Extended parameters &gt; Limits &gt; Dynamic limits" are only taken into account when [dynamic adaptation](#dynamic-adaptation-s7-1500t) is active. The dynamics of the motion can be restricted so that the dynamic limits of the kinematics axes are not exceeded. Even when using dynamic adaptation, there may be slight overruns of the dynamic limits of the kinematics axes. Set the dynamics at the kinematics axes about 5% lower than their permitted limit. When you change the dynamic limits of the kinematics axes during an active motion, the changed values only take effect with the next motion job.

> **Note**
>
> **Dynamic adaptation in the user program**
>
> Dynamic adaptation is only active if it is activated in the user program.

> **Note**
>
> **Dynamic adaptation in "Jog" mode**
>
> The dynamic adaptation is not active in the kinematics control panel. The dynamic limits of the kinematics axes are not taken into account during a kinematics motion with the kinematics control panel.

> **Note**
>
> **Dynamic adaptation in "Jog to target position" mode**
>
> In the kinematics control panel, the dynamic adaptation is only effective as of technology V6.0 and the dynamic limits of the kinematic axes are taken into account. "Dynamic adaptation without segmentation of the path" is always used.

###### Configuring dynamic defaults for the kinematics motion

You specify the dynamic values (velocity, acceleration, jerk) of a kinematics motion for the corresponding Motion Control instruction. If you do not specify any dynamic values for motion jobs (default value "-1.0"), the dynamic defaults configured under "Technology object &gt; Configuration &gt; Extended parameters &gt; Dynamics" are used for the kinematics motion.

> **Note**
>
> If you change the dynamic defaults during an active motion, the changed values take effect only in the next motion job.

**Procedure**

1. Select the entry "Kinematics motion" in the "Settings for" drop-down list.
2. Enter the default values of the dynamics in the "Velocity", "Acceleration", "Deceleration" and "Jerk" fields.
3. To activate the default settings, set the dynamic factors at the Motion Control instructions to less than zero.
4. Define the default values of the dynamic limits in the "Maximum velocity", "Maximum acceleration", "Maximum deceleration" and "Maximum jerk" fields.

###### Configuring dynamic defaults for the orientation motion

> **Note**
>
> If you change the dynamic defaults during an active motion, the changed values take effect only in the next motion job.

**Procedure**

1. Select the entry "Orientation motion" in the "Settings for" drop-down list.
2. Enter the default values of the dynamics in the "Velocity", "Acceleration", "Deceleration" and "Jerk" fields.
3. Define the default values of the dynamic limits in the "Maximum velocity", "Maximum acceleration", "Maximum deceleration" and "Maximum jerk" fields.

##### Configuring dynamics for the sPTP motion (S7-1500T)

You specify the dynamic values (velocity, acceleration, jerk) of an sPTP motion for the corresponding Motion Control instruction. If you do not specify any dynamic values for motion jobs (default value "-1.0"), the dynamic defaults configured under "Technology object &gt; Configuration &gt; Extended parameters &gt; Dynamics" are used for the sPTP motion.

You specify the default settings of the dynamics of the synchronous "point-to-point" motion using factors. These factors each relate in percentage terms to the maximum values of velocity, acceleration, deceleration and jerk that you have configured for the individual axes under "Technology object &gt; Configuration &gt; Extended parameters &gt; Limits&gt; Dynamic limits".

###### Configuring dynamic defaults for the sPTP motion

> **Note**
>
> If you change the dynamic defaults during an active motion, the changed values take effect only in the next motion job.

**Procedure**

1. Select the entry "sPTP motion" in the "Settings for" drop-down list.
2. Enter the default values of the dynamics in the "Velocity factor", "Acceleration factor", "Deceleration factor" and "Jerk factor" fields.
3. To activate the default settings, set the dynamic factors at the Motion Control instructions "MC_MoveDirectRelative" or "MC_MoveDirectAbsolute" to less than zero.

##### Dynamic adaptation (S7-1500T)

When dynamic adaptation is activated, a velocity profile for the motion of the kinematics is calculated, which takes into account both the dynamic specifications or dynamic presettings and dynamic limits of the kinematic motion as well as the maximum velocity, maximum acceleration and maximum deceleration of the kinematics axes. In addition, the dynamic presets and dynamic limits for velocity, acceleration and deceleration of the orientation motion are taken into account.

The "&lt;TO&gt;.StatusPath.DynamicAdaption" tag displays the status of the dynamic adaptation.

> **Note**
>
> **Dynamic adaptation in the user program**
>
> Dynamic adaptation is only active if it is activated in the user program.

> **Note**
>
> **Dynamic adaptation in "Jog" mode**
>
> The dynamic adaptation is not active in the kinematics control panel. The dynamic limits of the kinematics axes are not taken into account during a kinematics motion with the kinematics control panel.

> **Note**
>
> **Dynamic adaptation in "Jog to target position" mode**
>
> In the kinematics control panel, the dynamic adaptation is only effective as of technology V6.0 and the dynamic limits of the kinematic axes are taken into account. "Dynamic adaptation without segmentation of the path" is always used.

The graphic below shows examples of a velocity curve with and without dynamic adaptation:

![Figure](images/158924541835_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ![Figure](images/158924546955_DV_resource.Stream@PNG-de-DE.png) | With dynamic adaptation |
| ![Figure](images/158924552203_DV_resource.Stream@PNG-de-DE.png) | Without dynamic adaptation |

###### Configuring dynamic adaptation

You set the dynamic adaptation under "Kinematics technology object &gt; Configuration &gt; Extended parameters &gt; Dynamics".

Select the default for the dynamic adaptation in the drop-down list.

- **Do not limit**

  The dynamic limits of the axes are not taken into consideration.
- **Limit with segmentation of the path**

  The path is divided into individual equidistant segments. For each of these segments, the velocity profile is calculated taking into consideration the dynamic limits of the kinematics axes which apply for individual sections of the motion. The dynamic response is therefore adapted for individual sections of a motion. Dynamic adaptation in the "Limit with segmentation of the path" mode requires a considerably higher computing time than in the "Limit without segmentation of the path" mode.
- **Limit without segmentation of the path**

  With dynamic adaptation without segmentation of the path, the velocity profile is calculated taking into consideration the dynamic limits of the kinematics axes which apply for the entire motion.

##### Override (S7-1500T)

You can specify a velocity override for the kinematics (&lt;TO&gt;.Override.Velocity) using the technology object data block.

- You can enter a value between 0% and 200% for a path motion.
- You can enter a value between 0% and 100% for an sPTP motion.

The velocity override acts on the velocity of the tool center point (TCP) along the path. If you change the velocity override of the kinematics, the change takes effect immediately for the kinematics motion and orientation motion.

The setpoint velocity of the motion is the velocity specified for the Motion Control instruction multiplied by the percentage value of the velocity override.

The axis-specific velocity override values do not take effect for kinematics motions.

#### Motion preparation using multiple jobs (S7-1500T)

This section contains information on the following topics:

- [Job sequence (S7-1500T)](#job-sequence-s7-1500t)
- [Blending kinematics motions with maximum rounding clearance (S7-1500T)](#blending-kinematics-motions-with-maximum-rounding-clearance-s7-1500t)
- [Dynamic behavior when motions are appended/blended (S7-1500T)](#dynamic-behavior-when-motions-are-appendedblended-s7-1500t)
- [Preliminary motion preparation (S7-1500T)](#preliminary-motion-preparation-s7-1500t)
- [Setting the motion preparation (S7-1500T)](#setting-the-motion-preparation-s7-1500t)

##### Job sequence (S7-1500T)

Motion-relevant jobs are entered in the job sequence of the kinematics technology object.

The following jobs enter the job sequence:

| Job | Brief description |
| --- | --- |
| **Kinematics motions** |  |
| [MC_MoveLinearAbsolute](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_movelinearabsolute-v8-s7-1500t) | Position kinematics with linear path motion |
| [MC_MoveLinearRelative](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_movelinearrelative-v8-s7-1500t) | Relative positioning of kinematics with linear path motion |
| [MC_MoveCircularAbsolute](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_movecircularabsolute-v8-s7-1500t) | Position kinematics with circular path motion |
| [MC_MoveCircularRelative](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_movecircularrelative-v8-s7-1500t) | Relative positioning of kinematics with circular path motion |
| [MC_MoveDirectAbsolute](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_movedirectabsolute-v8-s7-1500t) | Absolute movement of kinematics with synchronous "point-to-point" motion |
| [MC_MoveDirectRelative](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_movedirectrelative-v8-s7-1500t) | Relative movement of kinematics with synchronous "point-to-point" motion |
| **Zones** |  |
| [MC_DefineWorkspaceZone](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_defineworkspacezone-v8-s7-1500t) | Define workspace zone |
| [MC_DefineKinematicsZone](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_definekinematicszone-v8-s7-1500t) | Define kinematics zone |
| [MC_SetWorkspaceZoneActive](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_setworkspacezoneactive-v8-s7-1500t) | Activate workspace zone |
| [MC_SetWorkspaceZoneInactive](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_setworkspacezoneinactive-v8-s7-1500t) | Deactivate workspace zone |
| [MC_SetKinematicsZoneActive](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_setkinematicszoneactive-v8-s7-1500t) | Activate kinematics zone |
| [MC_SetKinematicsZoneInactive](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_setkinematicszoneinactive-v8-s7-1500t) | Deactivate kinematics zone |
| **Coordinate systems** |  |
| [MC_SetOcsFrame](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_setocsframe-v8-s7-1500t) | Redefine object coordinate systems |

###### Define maximum number of jobs

By default, the job sequence can contain up to five jobs. You can change the maximum number of jobs in the configuration window "Technology object &gt; Configuration &gt; Extended parameters &gt; Job sequence". The job sequence can contain a maximum of ten jobs.

> **Note**
>
> **Multiple jobs in the job sequence**
>
> The more jobs contained in the job sequence, the longer it takes to calculate the motion jobs.

###### Processing of jobs in the job sequence

The jobs are processed in the same order in which they were entered in the job sequence. The order of the jobs cannot be changed subsequently. If another motion job is added to the job sequence, all jobs in the job sequence will be recalculated. The kinematics motion jobs do not cancel each other.

The job sequence allows the calculation of a velocity profile over several jobs. The number of motion jobs to be considered depends on the type of motion jobs, e. g. sPTP motion, linear motion, circular motion, conveyor tracking. The current job is also included in the new calculation so that the current job can be blended as far as possible with the next job.

###### Status of the job sequence

The two tags for the status of the job sequence can be used to check whether the calculation of the jobs in the job sequence has been completed and whether the corresponding programmed motion jobs are being blended. If the number of prepared commands in the job sequence ("&lt;TO&gt;StatusMotionQueue.NumberOfPreparedCommands") matches the number of jobs in the job sequence ("&lt;TO&gt;.StatusMotionQueue.NumberOfCommands"), then the preparation of the motion is complete.

###### Interrupting and resuming job execution

You can also interrupt execution of the jobs with a "MC_GroupInterrupt" job, fill the job sequence and then continue execution with an "MC_GroupContinue" job. The behavior of the motion processing at the "MC_GroupContinue" differs as follows:

- If a "MC_GroupInterrupt" job is transmitted before the start of the motion, the kinematics motion jobs transmitted between the "MC_GroupInterrupt" and the "MC_GroupContinue" job are prepared. If the number of prepared commands in the job sequence ("&lt;TO&gt;StatusMotionQueue.NumberOfPreparedCommands") matches the number of jobs in the job sequence ("&lt;TO&gt;.StatusMotionQueue.NumberOfCommands"), then the preparation of the motion is complete. As soon as the motion preparation is completed, the "MC_GroupContinue" job immediately releases the motion execution without renewed preparation.
- If an active kinematics motion is stopped with a "MC_GroupInterrupt" job and continued with a "MC_GroupContinue" job, the kinematics motions in the job sequence are prepared again with the "MC_GroupContinue" job.

---

**See also**

["MotionQueue" tag (kinematics) (S7-1500T)](#motionqueue-tag-kinematics-s7-1500t)
  
[Interrupting, continuing and stopping kinematics motions (S7-1500T)](#interrupting-continuing-and-stopping-kinematics-motions-s7-1500t)

##### Blending kinematics motions with maximum rounding clearance (S7-1500T)

Multiple motions can be appended to one another, in which case the kinematics comes to a standstill between the individual motions. To achieve an uninterrupted Motion Control without standstill between the individual motion jobs, the individual motions can be blended and thus connected via geometric transitions.

You can configure the maximum rounding clearance of the kinematics motions from 0% to 100% of the distance. You can specify and move blending distances greater than half of the shorter path length.

###### Determine maximum rounding clearance

The maximum rounding clearance is determined depending on the following values:

- L0: Rounding clearance of the previous motion job
- L1: Path length of the first job to the rounding point.
- L2: Path length of the second job to the rounding point

The maximum rounding clearance is the smallest of the following values:

- L1 - L0
- "&lt;TO&gt;.Transition.FactorBlendingLength" / 100 * L1
- "&lt;TO&gt;.Transition.FactorBlendingLength" / 100 * L2

![Determine maximum rounding clearance](images/158925215371_DV_resource.Stream@PNG-en-US.png)

**Example: Equal distances between the points**

The distances between points A and B and points B and C are the same length. The kinematics is at a standstill.

| &lt;TO&gt;.Transition.FactorBlendingLength | Maximum rounding clearance ① |  | Description |
| --- | --- | --- | --- |
| 100.0 | L1 | ![Determine maximum rounding clearance](images/158924818571_DV_resource.Stream@PNG-de-DE.png) | The entire motion can be blended. The maximum rounding clearance corresponds to the distance between points A and B or B and C. |
| 50.0 | L1 * 0.5 | ![Determine maximum rounding clearance](images/158924813451_DV_resource.Stream@PNG-de-DE.png) | The maximum rounding clearance is reduced to half the distance between points A and B. |

**Example: Different distances between the points**

The distances between points A and B and points B and C are different in length. The distance between points A and B is less than the distance between points B and C. The kinematics is in standstill.

| &lt;TO&gt;.Transition.FactorBlendingLength | Maximum rounding clearance ① |  | Description |
| --- | --- | --- | --- |
| 100.0 | L1 | ![Determine maximum rounding clearance](images/158925041291_DV_resource.Stream@PNG-de-DE.png) | The maximum rounding clearance corresponds to the distance L1, as this is the shorter distance. |
| 50.0 | L1 * 0.5 | ![Determine maximum rounding clearance](images/158925046411_DV_resource.Stream@PNG-de-DE.png) | The maximum rounding clearance is calculated with half of L1, because L1 is the shorter distance. |

**Example: Previous job blended**

The example builds on the previous example. A linear motion to point D should be traversed. Point C should not be approached directly. The motion to point D should be done with maximum rounding clearance to point C. The previous motion job to point C is blended with rounding clearance L0.

| &lt;TO&gt;.Transition.FactorBlendingLength | Maximum rounding clearance ① |  | Description |
| --- | --- | --- | --- |
| 100.0 | L1 - L0 | ![Determine maximum rounding clearance](images/158925051531_DV_resource.Stream@PNG-de-DE.png) | The maximum rounding clearance corresponds to the distance L1 minus the rounding clearance from the previous motion. That is the shortest distance. |
| 50.0 | L2 * 0.5 | ![Determine maximum rounding clearance](images/158925210251_DV_resource.Stream@PNG-de-DE.png) | Half of L2 is the shortest distance and therefore the maximum rounding clearance. The rounding clearance of the previous motion is lower by a factor of 50% and does not reduce the maximum rounding clearance of the following motion as much as it does at 100%. |

###### Configure maximum rounding clearance

Up to technology version V5.0, the maximum rounding clearance is limited to 50% of the shorter distance. From technology version V6.0, you can configure the maximum rounding clearance. The default is 50% and therefore compatible with the technology versions &lt; V6.0.

The factor [%] is configured in the configuration window "Technology object &gt; Configuration &gt; Extended parameters &gt; Job sequence" or using the tag "&lt;TO&gt;.Transition.FactorBlendingLength" of the kinematics technology object. Change the factor in the user program before sending the motion jobs to the job sequence so that the change is effective.

The maximum rounding clearance is used when the value of the "TransitionParameter[1]" parameter is &lt; 0.0 or the specified value exceeds the maximum rounding clearance. The rounding clearance is limited to the maximum rounding clearance when the value of the "TransitionParameter[1]" is &gt; 0. If you have parameterized a smaller positive rounding clearance at the Motion Control instruction than the maximum rounding clearance, then the configured rounding clearance "TransitionParameter[1]" is effective.

The following table shows three possible configuration examples and their effect on the calculation of the maximum rounding clearance:

| Configuration example  "&lt;TO&gt;.Transition.FactorBlendingLength" | Effect |
| --- | --- |
| 0.0 | The rounding clearance is always zero. Blending is not possible with any motion. |
| 50.0 | The maximum rounding clearance is calculated from half of the shorter distance between the two motions. |
| 100.0 | The maximum rounding clearance is calculated from the shorter distance of the two motions and the rounding clearance of the previous motion.  You have the option of moving the kinematics with the maximum possible rounding clearances. |

##### Dynamic behavior when motions are appended/blended (S7-1500T)

You define the dynamic behavior for the transition of kinematics motions with the "BufferMode" and "DynamicAdaption" parameters.

Multiple motions can be appended to one another, in which case the kinematics comes to a standstill between the individual motions ("BufferMode" = 1). To achieve an uninterrupted motion, the individual motions can be blended with a blending segment. The consecutive motions can be blended at the lower velocity ("BufferMode" = 2) or at the higher velocity ("BufferMode" = 5).

###### Dynamic adaptation

With active dynamic adaptation with segmentation of the path ("DynamicAdaption" =1), the path of a motion job is divided into individual segments. For each of these segments, the velocity profile is calculated with consideration of the applicable limits. The dynamic response of the path is thus adapted for individual segments of a motion job. As a result, a higher traversing velocity can be reached section by section, thus reducing the traversing time of the motion .

With active dynamic adaptation ("DynamicAdaption"=1) without segmentation of the path, the velocity profile is calculated taking into account the limitations that apply to the entire motion job.

Dynamic adaptation in the "Limit with segmentation of the path" mode requires a considerably higher computing time than in the "Limit without segmentation of the path" mode.

When dynamic adaptation is activated, a velocity profile for the motion of the kinematics is calculated, which takes into account both the dynamic specifications or dynamic presettings and dynamic limits of the kinematic motion as well as the maximum velocity, maximum acceleration and maximum deceleration of the kinematics axes. In addition, the dynamic presets and dynamic limits for velocity, acceleration and deceleration of the orientation motion are taken into account.

##### Preliminary motion preparation (S7-1500T)

With technology version V5.0, the calculation of the motion preparation has changed. The motion preparation is calculated in the organization block (OB) MC_LookAhead and no longer in MC_Interpolator.

The jobs from the job sequence are prepared in advance with MC_LookAhead. The dynamic values for path motions and orientation motions are transferred to the job sequence. The dynamic values are only active when the job is executed.

For the motion processing, the current path motion job and the following path motion jobs (for sPTP-motions only the next motion job) must be taken into account so that the blending of path motions is possible. Path motions are first processed in MC_LookAhead and then take effect in MC_Interpolator. Motions with blending require a longer lead time and a longer reaction time.

You can change the velocity override during a path motion, which immediately changes the dynamics of the path motion.

In MC_Interpolator, less time is needed for motion preparation and you can set a shorter application cycle of MC_Servo.

The description of the organization blocks MC_Interpolator and MC_LookAhead can be found in the "[Organization blocks for Motion Control](S7-1500-S7-1500T%20Motion%20Control%20Overview%20%28S7-1500%2C%20S7-1500T%29.md#organization-blocks-for-motion-control-s7-1500-s7-1500t)" section of the "S7-1500/S7-1500T Motion Control overview" documentation.

##### Setting the motion preparation (S7-1500T)

The motion preparation is influenced by various factors.

To increase the available computing time of the MC_LookAhead, adjust the following settings:

- Application cycle:

  - Set a bigger application cycle.
  - Set a longer PN send clock.
- Increase the maximum cycle load for MC_LookAhead in the properties of the organization block under "General &gt; Multi-core processor". You can set values from 1% to 40% (default setting 20%) for the maximum cycle load.
- If you are not using user-defined kinematics, select the "Improve system performance" check box in the properties of MC_LookAhead  under "General &gt; Multi-core processor".
- Set the higher priority 16 for the MC_LookAhead.
- Reduce the percentage communication load in the CPU properties.
- If necessary for interpolation of cyclic cams, clear the "Improve system performance" check box in the properties of MC_Interpolator under "General &gt; Multi-core processor".

You have the following options for reducing the calculation time of the motion preparation:

- Use dynamic adaptation without segmentation of the path instead of dynamic adaptation with segmentation of the path.
- Reduce the maximum number of jobs in the job sequence.

The following measures are possible during programming of the jobs:

- So that blending of a currently active job with a newly issued subsequent job is possible, sufficient computing time must be available for preparation of the subsequent job. You can increase the available computing time using the following measures:

  - Select the smallest possible rounding clearance. Since the rounding clearance shortens the currently active job, there is less time for calculation of the subsequent job.
  - Reduce the traversing velocity.
  - Use jobs with the longest possible traversing length.
- If no motion job is active and the job sequence is empty, you can interrupt the processing of the jobs with an "MC_GroupInterrupt" job and fill the job sequence. Then continue the processing with an "MC_GroupContinue" job as soon as the motion preparation is complete. As a result, the number of prepared commands (&lt;TO&gt;.StatusMotionQueue.NumberOfPreparedCommands) corresponds to the number of queued jobs (&lt;TO&gt;.StatusMotionQueue.NumberOfCommands) in the job sequence.

#### Interaction of kinematics motions and single axis motions (S7-1500T)

Kinematics motions are only possible if no single axis motions are active on the kinematics axes. Single axis motions have an overriding effect on kinematics motions. The motion of the corresponding axis is overridden by the single-axis motion and the job sequence is cleared. The other kinematics axes stop with the maximum dynamics. Exception: The kinematics is in [simulation](#set-kinematics-to-simulation-mode-s7-1500t).

The following functions are permitted during an active kinematics motion:

- Torque reduction on the axes/Travel to fixed stop ("MC_TorqueLimiting")

  When the fixed stop is reached, the kinematics motion is aborted.
- Setting of an additive torque ("MC_TorqueAdditive")
- Setting of the upper and lower torque limit ("MC_TorqueRange")
- Sensor switchover ("MC_SetSensor")

The following functions are rejected during an active kinematics motion:

- Overlaid motion on the axes ("MC_MoveSuperimposed")
- Homing of the axes ("MC_Home")

#### Tags: Kinematics motions (S7-1500T)

The following technology object tags are relevant for motion control:

| Tag | Description |  |
| --- | --- | --- |
| **Status values** |  |  |
| &lt;TO&gt;.StatusWord | Status indicator for an active motion |  |
| &lt;TO&gt;.Tcp | Target coordinates x, y, z, A, B, C of the kinematics motion in the world coordinate system |  |
| &lt;TO&gt;.StatusPath.CoordSystem | Coordinate system of the active motion job |  |
| 0 | World coordinate system |  |
| 1, 2, 3 | Object coordinate system 1, 2, 3 |  |
| 100 | Machine coordinate system |  |
| 101 | Joint coordinate system<sup>1)</sup> |  |
| &lt;TO&gt;.StatusPath.Velocity | Current path velocity (setpoint reference) |  |
| &lt;TO&gt;.StatusPath.Acceleration | Current path acceleration (setpoint reference) |  |
| &lt;TO&gt;.StatusPath.OrientationVelocity | Resulting orientation velocity |  |
| &lt;TO&gt;.StatusPath.DynamicAdaption | Dynamic adaptation |  |
| 0 | No dynamic adaptation |  |
| 1 | Dynamic adaptation with segmentation of the path |  |
| 2 | Dynamic adaptation without segmentation of the path |  |
| &lt;TO&gt;.StatusPath.TotalPathLength | Total path length of linear and circular path motions  Sum of:  - Distance of all completed motion jobs - Distance travelled of the active motion job - Remaining distance of the motion job - Calculated distance of all jobs in the job sequence |  |
| &lt;TO&gt;.StatusPath.AccumulatedPathLength | Accumulated path length of linear and circular path motions  Sum of:  - Distance of all completed motion jobs - Distance travelled of the active motion job |  |
| &lt;TO&gt;.StatusMotionQueue.NumberOfCommands | Number of jobs in the job sequence |  |
| **Override** |  |  |
| &lt;TO&gt;.Override.Velocity | Velocity override |  |
| **Dynamic limits** |  |  |
| &lt;TO&gt;.DynamicLimits.Path.Velocity | Dynamic limitation for the maximum velocity of the path |  |
| &lt;TO&gt;.DynamicLimits.Path.Acceleration | Dynamic limitation for the maximum acceleration of the path |  |
| &lt;TO&gt;.DynamicLimits.Path.Deceleration | Dynamic limitation for the maximum deceleration of the path |  |
| &lt;TO&gt;.DynamicLimits.Path.Jerk | Dynamic limitation for the maximum jerk of the path |  |
| &lt;TO&gt;.DynamicLimits.Orientation.Velocity | Dynamic limitation for the maximum velocity of the Cartesian orientation |  |
| &lt;TO&gt;.DynamicLimits.Orientation.Acceleration | Dynamic limitation for the maximum acceleration of the Cartesian orientation |  |
| &lt;TO&gt;.DynamicLimits.Orientation.Deceleration | Dynamic limitation for the maximum deceleration of the Cartesian orientation |  |
| &lt;TO&gt;.DynamicLimits.Orientation.Jerk | Dynamic limitation for the maximum jerk of the Cartesian orientation |  |
| **Dynamic defaults** |  |  |
| &lt;TO&gt;.DynamicDefaults.Path.Velocity | Default setting of the velocity of the path |  |
| &lt;TO&gt;.DynamicDefaults.Path.Acceleration | Default setting of the acceleration of the path |  |
| &lt;TO&gt;.DynamicDefaults.Path.Deceleration | Default setting of the deceleration of the path |  |
| &lt;TO&gt;.DynamicDefaults.Path.Jerk | Default setting of the jerk of the path |  |
| &lt;TO&gt;.DynamicDefaults.Orientation.Velocity | Default setting of the velocity of the Cartesian orientation |  |
| &lt;TO&gt;.DynamicDefaults.Orientation.Acceleration | Default setting of the acceleration of the Cartesian orientation |  |
| &lt;TO&gt;.DynamicDefaults.Orientation.Deceleration | Default setting of the deceleration of the Cartesian orientation |  |
| &lt;TO&gt;.DynamicDefaults.Orientation.Jerk | Default setting of the jerk of the Cartesian orientation |  |
| &lt;TO&gt;.DynamicDefaults.DynamicAdaption | Default setting of the dynamic adaptation |  |
| 0 | No dynamic adaptation |  |
| 1 | Dynamic adaptation with segmentation of the path |  |
| 2 | Dynamic adaptation without segmentation of the path |  |
| &lt;TO&gt;.DynamicDefaults.MoveDirect.VelocityFactor | Factor for the velocity of the axis motions in relation to the respective maximum velocity of the axes with sPTP motion. |  |
| &lt;TO&gt;.DynamicDefaults.MoveDirect.AccelerationFactor | Factor for the acceleration of the axis motions in relation to the respective maximum acceleration of the axes with sPTP motion. |  |
| &lt;TO&gt;.DynamicDefaults.MoveDirect.DecelerationFactor | Factor for the deceleration of the axis motions in relation to the respective maximum deceleration of the axes with sPTP motion. |  |
| &lt;TO&gt;.DynamicDefaults.MoveDirect.JerkFactor | Factor for the jerk of the axis motions in relation to the respective maximum jerk of the axes with sPTP motion. |  |
| **Rounding clearance** |  |  |
| &lt;TO&gt;.Transition.FactorBlendingLength | Factor of the maximum rounding distance in percent [%]  The configuration takes place in "Technology object &gt; Configuration &gt; Extended parameters &gt; Job sequence".  Change the factor in the user program before sending the motion jobs to the job sequence so that the change is effective. |  |
| 0.0 | No blending possible |  |
| 50.0 | Default value |  |
| 100.0 | Blending possible with complete segment length or motion length |  |
| <sup>1)</sup> With up to four interpolating kinematics axes, the joint coordinate system is identical to the machine coordinate system. |  |  |

### Moving a kinematics in a linear manner (S7-1500T)

This section contains information on the following topics:

- [Brief description of linear motion (S7-1500T)](#brief-description-of-linear-motion-s7-1500t)
- [Defining the target position of the linear motion (S7-1500T)](#defining-the-target-position-of-the-linear-motion-s7-1500t)
- [Defining the dynamic response of the linear motion (S7-1500T)](#defining-the-dynamic-response-of-the-linear-motion-s7-1500t)
- [Defining the transition of linear motion (S7-1500T)](#defining-the-transition-of-linear-motion-s7-1500t)
- [Starting a linear motion job (S7-1500T)](#starting-a-linear-motion-job-s7-1500t)
- [Tags: Linear motion (S7-1500T)](#tags-linear-motion-s7-1500t)

#### Brief description of linear motion (S7-1500T)

You can move the kinematics linearly to a defined target position with a linear motion. With the Motion Control instruction "[MC_MoveLinearAbsolute](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_movelinearabsolute-position-kinematics-with-linear-path-motion-v8-s7-1500t)", you move a kinematics with a linear motion to an absolute position. With the Motion Control instruction "[MC_MoveLinearRelative](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_movelinearrelative-relative-positioning-of-kinematics-with-linear-path-motion-v8-s7-1500t)", you move a kinematics with a linear path relative to the position which was present at the start of the job processing.

You have the following options for the linear motion:

- [Define target position](#defining-the-target-position-of-the-linear-motion-s7-1500t)
- [Define dynamic response](#defining-the-dynamic-response-of-the-linear-motion-s7-1500t)
- [Define motion transition](#defining-the-transition-of-linear-motion-s7-1500t)
- [Start job](#starting-a-linear-motion-job-s7-1500t)
- [Show motion status and remaining distance](#motion-status-and-remaining-distance-s7-1500t)

#### Defining the target position of the linear motion (S7-1500T)

With the Motion Control instruction "MC_MoveLinearAbsolute", you move a kinematics with a linear motion to an absolute position. With the Motion Control instruction "MC_MoveLinearRelative", you move a kinematics with a linear path relative to the position which was present at the start of the job processing.

##### Parameter inputs

**Absolute target position**

You define the absolute target position of the linear motion with the following parameters of the Motion Control instruction "[MC_MoveLinearAbsolute](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_movelinearabsolute-position-kinematics-with-linear-path-motion-v8-s7-1500t)":

- With the "CoordSystem" parameter, you define the reference system for the target coordinates.
- With the "Position[1..4]" parameters, you define the x, y, z and A coordinates of the target position.
- With up to four interpolating kinematics axes:

  - With the "DirectionA" parameter, you define the direction of movement of the Cartesian orientation A.
- With more than four interpolating kinematics axes:

  - With the "Position[5..6]" parameters, you define the B and C coordinates of the target position.
  > **Note**
  >
  > **Orientation motion**
  >
  > The target orientation is always approached by the shortest distance. If the target orientation can be reached via two paths of equal length, motion is in the positive direction.

**Relative target position**

You define the relative target position of the linear motion with the following parameters of the Motion Control instruction "[MC_MoveLinearRelative](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_movelinearrelative-relative-positioning-of-kinematics-with-linear-path-motion-v8-s7-1500t)":

- With the "CoordSystem" parameter, you define the reference system for the target coordinates.
- With the "Distance[1..4]" parameters, you define the x, y, z and A coordinates of the target position.
- With more than four interpolating kinematics axes:

  - With the "Distance[5..6]" parameters, you define the B and C coordinates of the target position.
  > **Note**
  >
  > **Orientation motion**
  >
  > The target orientation is always approached by the shortest distance. If the target orientation can be reached via two paths of equal length, motion is in the positive direction.

#### Defining the dynamic response of the linear motion (S7-1500T)

You can define the dynamic response of the linear path motion at the corresponding Motion Control instruction. You can only define the dynamic response of the orientation motion in the configuration of the kinematics technology object.

##### Parameter inputs

You define the dynamics of the linear motion with the following parameters of the Motion Control instruction "[MC_MoveLinearAbsolute](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_movelinearabsolute-position-kinematics-with-linear-path-motion-v8-s7-1500t)" or "[MC_MoveLinearRelative](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_movelinearrelative-relative-positioning-of-kinematics-with-linear-path-motion-v8-s7-1500t)":

- With the "Velocity" parameter, you define the velocity.
- With the "Acceleration" parameter, you define the acceleration.
- With the "Deceleration" parameter, you define the deceleration.
- With the "Jerk" parameter, you define the jerk.
- With the "DynamicAdaption" parameter, you specify the dynamic adaptation of the path motion.

With the following configuration parameters under "Technology object &gt; Configuration &gt; Extended parameters &gt; Dynamics", you define the dynamic response of the orientation motion:

- Select the entry "Orientation motion" in the "Settings for" drop-down list.
- Define the velocity (&lt;TO&gt;.DynamicDefaults.Orientation.Velocity) in the field "Velocity".
- Define the acceleration (&lt;TO&gt;.DynamicDefaults.Orientation.Acceleration) in the field "Acceleration".
- Define the deceleration (&lt;TO&gt;.DynamicDefaults.Orientation.Deceleration) in the field "Deceleration".
- Define the jerk (&lt;TO&gt;.DynamicDefaults.Orientation.Jerk) in the field "Jerk".

##### Dynamic adaptation

The dynamic adaptation limits the path dynamics to the axis dynamics. When dynamic adaptation is activated, a velocity profile for the motion of the kinematics is calculated, which takes into account not only the dynamic specifications or dynamic defaults and the dynamic limits of the kinematic motion, but also the maximum velocity, maximum acceleration and maximum deceleration of the kinematics axes. In addition, the dynamic defaults and the dynamic limits for velocity, acceleration and deceleration of the orientation motion are taken into account.

**Use the configured default**

With the "DynamicAdaption" &lt; 0 parameter, the configured default is used. You configure the default value in the field "Limit path dynamics to axis dynamics" under "Technology object &gt; Configuration &gt; Extended parameters &gt; Dynamics" of the kinematics technology object (&lt;TO&gt;.DynamicDefaults.DynamicAdaption).

**Do not limit path dynamics to axis dynamics**

With the "DynamicAdaption" = 0 parameter, no dynamic adaptation is used for the linear motion.

**Limit path dynamics to axis dynamics with segmentation of the path**

With the "DynamicAdaption" = 1 parameter, the dynamic adaptation is used for the linear motion. The path of the linear motion is divided into individual segments. For each of these segments, the velocity profile is calculated with consideration of the applicable limits. The dynamic response of the path is thus adapted for individual segments of the linear motion. As a result, a higher traversing velocity is reached section by section and the traversing time of the linear motion is reduced.

Note that dynamic adaptation with segmentation of the path requires a considerably higher computing time than dynamic adaptation without segmentation of the path.

**Limit path dynamics to axis dynamics without segmentation of the path**

With the "DynamicAdaption" = 2 parameter, the dynamic adaptation is used for the linear motion. The velocity profile is calculated for the entire linear motion. The limitations which apply to the entire motion job are taken into consideration.

#### Defining the transition of linear motion (S7-1500T)

Multiple motions can be appended to one another, in which case the kinematics comes to a standstill between the individual motions. To achieve an uninterrupted Motion Control without standstill between the individual motion jobs, the individual motions can be blended with geometric transitions. You define the corresponding parameters at the new motion job (A2), into which the previous job (A1) is to be blended.

In the following examples, the various motion transitions are explained using an active linear motion (A1) and a subsequent linear motion (A2).

##### Parameter inputs

You define the transition to the active motion with the following parameters of the Motion Control instruction "[MC_MoveLinearAbsolute](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_movelinearabsolute-position-kinematics-with-linear-path-motion-v8-s7-1500t)" or "[MC_MoveLinearRelative](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_movelinearrelative-relative-positioning-of-kinematics-with-linear-path-motion-v8-s7-1500t)":

- With the "BufferMode" parameter, you define the mode of the motion transition.
- With the "TransitionParameter[1]" parameter, you define the rounding clearance.

##### Appending motion

With the "BufferMode" = 1 parameter, the linear motion is appended to the active motion. The active motion sequence (A1) is completed and the kinematics comes to a standstill. The linear motion (A2) is then executed.

![Appending motion](images/158925426059_DV_resource.Stream@PNG-de-DE.png)

In this case, the parameter "TransitionParameter[1]" is not relevant.

##### Blending motion

With the "BufferMode" = 2 parameter, the active motion is blended with the linear motion and the lower velocity of both jobs is used.

With the "BufferMode" = 5 parameter, the active motion is blended with the linear motion and the higher velocity of both jobs is used.

**Rounding clearance d &gt; 0.0**

With the "TransitionParameter[1]" &lt; 0.0 parameter, the active motion (A1) is blended with the linear motion (A2) as soon as the specified rounding clearance to the target position of the active motion is reached.

![Blending motion](images/158925431179_DV_resource.Stream@PNG-de-DE.png)

**Rounding clearance d = 0.0**

With the "TransitionParameter[1]" = 0.0 parameter, the linear motion is appended to the active motion as with "BufferMode" = 1. The active motion sequence (A1) is completed and the kinematics comes to a standstill. The linear motion (A2) is then executed.

![Blending motion](images/158926025099_DV_resource.Stream@PNG-de-DE.png)

**Rounding clearance d &lt; 0.0**

With the "TransitionParameter[1]" &lt; 0.0 parameter, the active motion (A1) is blended with the linear motion (A2) as soon as the maximum rounding clearance to the target position of the active motion is reached.

You configure the factor of the maximum rounding clearance under "Technology object &gt; Configuration &gt; Extended parameters &gt; Job sequence" (&lt;TO&gt;.Transition.FactorBlendingLength). In the following example, the maximum rounding clearance is limited to 50% of the shorter distance.

![Blending motion](images/158926030219_DV_resource.Stream@PNG-de-DE.png)

#### Starting a linear motion job (S7-1500T)

After the start of the linear motion job with "Execute" = TRUE, the job is added to the [job sequence](#job-sequence-s7-1500t). The processing status is indicated in the Motion Control instruction "[MC_MoveLinearAbsolute](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_movelinearabsolute-position-kinematics-with-linear-path-motion-v8-s7-1500t)" or. "[MC_MoveLinearRelative](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_movelinearrelative-relative-positioning-of-kinematics-with-linear-path-motion-v8-s7-1500t)" with the parameter "Busy" = TRUE. If the job is active, this is indicated with the parameter "Active" = TRUE and in the "&lt;TO&gt;.StatusWord.X8 (LinearCommand)" tag of the technology object.

As soon as the target position is reached or the linear motion is blended to the next motion, the job is completed. The status is indicated with the parameter "Done" = TRUE.

You can find more information in the section "[Motion status and remaining distance](#motion-status-and-remaining-distance-s7-1500t)".

#### Tags: Linear motion (S7-1500T)

The following technology object tags are relevant for motion control:

| Tag | Description |  |
| --- | --- | --- |
| **Status values** |  |  |
| &lt;TO&gt;.StatusWord | Status indicator for an active motion |  |
| &lt;TO&gt;.StatusWord.X8 (LinearCommand) | The value "TRUE" is set if a job for linear motion is active ("MC_MoveLinearAbsolute", "MC_MoveLinearRelative"). |  |
| &lt;TO&gt;.Tcp | Target coordinates x, y, z, A, B, C of the kinematics motion in the world coordinate system |  |
| &lt;TO&gt;.StatusPath.CoordSystem | Coordinate system of the active motion job |  |
| 0 | World coordinate system |  |
| 1, 2, 3 | Object coordinate system 1, 2, 3 |  |
| 100 | Machine coordinate system |  |
| 101 | Joint coordinate system<sup>1)</sup> |  |
| &lt;TO&gt;.StatusPath.Velocity | Current path velocity (setpoint reference) |  |
| &lt;TO&gt;.StatusPath.Acceleration | Current path acceleration (setpoint reference) |  |
| &lt;TO&gt;.StatusPath.OrientationVelocity | Resulting orientation velocity |  |
| &lt;TO&gt;.StatusPath.DynamicAdaption | Dynamic adaptation |  |
| 0 | No dynamic adaptation |  |
| 1 | Dynamic adaptation with segmentation of the path |  |
| 2 | Dynamic adaptation without segmentation of the path |  |
| &lt;TO&gt;.StatusPath.TotalPathLength | Total path length of linear and circular path motions  Sum of:  - Distance of all completed motion jobs - Distance travelled of the active motion job - Remaining distance of the motion job - Calculated distance of all jobs in the job sequence |  |
| &lt;TO&gt;.StatusPath.AccumulatedPathLength | Accumulated path length of linear and circular path motions  Sum of:  - Distance of all completed motion jobs - Distance travelled of the active motion job |  |
| &lt;TO&gt;.StatusMotionQueue.NumberOfCommands | Number of jobs in the job sequence |  |
| **Override** |  |  |
| &lt;TO&gt;.Override.Velocity | Velocity override |  |
| **Dynamic limits** |  |  |
| &lt;TO&gt;.DynamicLimits.Path.Velocity | Dynamic limitation for the maximum velocity of the path |  |
| &lt;TO&gt;.DynamicLimits.Path.Acceleration | Dynamic limitation for the maximum acceleration of the path |  |
| &lt;TO&gt;.DynamicLimits.Path.Deceleration | Dynamic limitation for the maximum deceleration of the path |  |
| &lt;TO&gt;.DynamicLimits.Path.Jerk | Dynamic limitation for the maximum jerk of the path |  |
| &lt;TO&gt;.DynamicLimits.Orientation.Velocity | Dynamic limitation for the maximum velocity of the Cartesian orientation |  |
| &lt;TO&gt;.DynamicLimits.Orientation.Acceleration | Dynamic limitation for the maximum acceleration of the Cartesian orientation |  |
| &lt;TO&gt;.DynamicLimits.Orientation.Deceleration | Dynamic limitation for the maximum deceleration of the Cartesian orientation |  |
| &lt;TO&gt;.DynamicLimits.Orientation.Jerk | Dynamic limitation for the maximum jerk of the Cartesian orientation |  |
| **Dynamic defaults** |  |  |
| &lt;TO&gt;.DynamicDefaults.Path.Velocity | Default setting of the velocity of the path |  |
| &lt;TO&gt;.DynamicDefaults.Path.Acceleration | Default setting of the acceleration of the path |  |
| &lt;TO&gt;.DynamicDefaults.Path.Deceleration | Default setting of the deceleration of the path |  |
| &lt;TO&gt;.DynamicDefaults.Path.Jerk | Default setting of the jerk of the path |  |
| &lt;TO&gt;.DynamicDefaults.Orientation.Velocity | Default setting of the velocity of the Cartesian orientation |  |
| &lt;TO&gt;.DynamicDefaults.Orientation.Acceleration | Default setting of the acceleration of the Cartesian orientation |  |
| &lt;TO&gt;.DynamicDefaults.Orientation.Deceleration | Default setting of the deceleration of the Cartesian orientation |  |
| &lt;TO&gt;.DynamicDefaults.Orientation.Jerk | Default setting of the jerk of the Cartesian orientation |  |
| &lt;TO&gt;.DynamicDefaults.DynamicAdaption | Default setting of the dynamic adaptation |  |
| 0 | No dynamic adaptation |  |
| 1 | Dynamic adaptation with segmentation of the path |  |
| 2 | Dynamic adaptation without segmentation of the path |  |
| **Rounding clearance** |  |  |
| &lt;TO&gt;.Transition.FactorBlendingLength | Factor of the maximum rounding clearance in percent [%]  The configuration takes place in "Technology object &gt; Configuration &gt; Extended parameters &gt; Job sequence".  Change the factor in the user program before sending the motion jobs to the job sequence so that the change is effective. |  |
| 0.0 | No blending possible |  |
| 50.0 | Default value |  |
| 100.0 | Blending possible with complete segment length or motion length |  |
| <sup>1)</sup> With up to four interpolating kinematics axes, the joint coordinate system is identical to the machine coordinate system. |  |  |

### Moving a kinematics in a circular manner (S7-1500T)

This section contains information on the following topics:

- [Brief description of circular motion (S7-1500T)](#brief-description-of-circular-motion-s7-1500t)
- [Defining the circular path of the circular motion (S7-1500T)](#defining-the-circular-path-of-the-circular-motion-s7-1500t)
- [Define the dynamic response of the circular motion (S7-1500T)](#define-the-dynamic-response-of-the-circular-motion-s7-1500t)
- [Define the transition of circular motion (S7-1500T)](#define-the-transition-of-circular-motion-s7-1500t)
- [Starting a circular motion job (S7-1500T)](#starting-a-circular-motion-job-s7-1500t)
- [Tags: Circular motion (S7-1500T)](#tags-circular-motion-s7-1500t)

#### Brief description of circular motion (S7-1500T)

You can move the kinematics using a defined circular path with a circular motion. With the Motion Control instruction "[MC_MoveCircularAbsolute](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_movecircularabsolute-position-kinematics-with-circular-path-motion-v8-s7-1500t)", you move a kinematics with a circular motion to an absolute position. With the Motion Control instruction "[MC_MoveCircularRelative](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_movecircularrelative-relative-positioning-of-kinematics-with-circular-path-motion-v8-s7-1500t)", you move a kinematics with a circular motion relative to the position which was present at the start of the job processing.

You have the following options for the circular motion:

- Define circular path:

  - [Define circular path via intermediate point and target position](#defining-the-circular-path-via-intermediate-point-and-target-position-s7-1500t)
  - [Define circular path via center point and angle](#defining-the-circular-path-via-center-point-and-angle-s7-1500t)
  - [Define circular path via radius and target position](#define-circular-path-via-radius-and-target-position-s7-1500t)
- [Define dynamic response](#define-the-dynamic-response-of-the-circular-motion-s7-1500t)
- [Define motion transition](#define-the-transition-of-circular-motion-s7-1500t)
- [Start job](#starting-a-circular-motion-job-s7-1500t)
- [Show motion status and remaining distance](#motion-status-and-remaining-distance-s7-1500t)

#### Defining the circular path of the circular motion (S7-1500T)

This section contains information on the following topics:

- [Defining the circular path via intermediate point and target position (S7-1500T)](#defining-the-circular-path-via-intermediate-point-and-target-position-s7-1500t)
- [Defining the circular path via center point and angle (S7-1500T)](#defining-the-circular-path-via-center-point-and-angle-s7-1500t)
- [Define circular path via radius and target position (S7-1500T)](#define-circular-path-via-radius-and-target-position-s7-1500t)

##### Defining the circular path via intermediate point and target position (S7-1500T)

With the Motion Control instruction "MC_MoveCircularAbsolute", you move a kinematics with a circular motion to an absolute position. With the Motion Control instruction "MC_MoveCircularRelative", you move a kinematics with a circular motion relative to the position which was present at the start of the job processing.

Specify an intermediate point on the circular path and the target position for the definition of the circular path. The circular path is calculated via the start position, the intermediate point and the target position. The kinematics can only traverse circular paths less than 360°.

With this mode of circular path definition, the kinematics can move in three-dimensional space:

![Figure](images/158943207435_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | Start position |
| ② | Intermediate point ("AuxPoint") |
| ③ | Target position ("EndPoint") |

When defining the intermediate point and target position, ensure that the information is consistent.

###### Parameter inputs

You define the circular path of the circular motion with the following parameters of the Motion Control instruction "[MC_MoveCircularAbsolute](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_movecircularabsolute-position-kinematics-with-circular-path-motion-v8-s7-1500t)" or "[MC_MoveCircularRelative](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_movecircularrelative-relative-positioning-of-kinematics-with-circular-path-motion-v8-s7-1500t)":

- With the "CircMode" parameter, you define the mode of the circular path definition. With "CircMode" = 0, you define the circular path via an intermediate point and the target position.
- With the "CoordSystem" parameter, you define the reference coordinate system.
- With the "AuxPoint[1..3]" parameters, you define the x, y and z coordinates of the intermediate point of the circular path in the reference coordinate system.
- With the parameter "EndPoint[1..4]", you define the x, y, z and A coordinates of the target position in the reference coordinate system.
- With up to four interpolating kinematics axes:

  - With the "DirectionA" parameter, you define the direction of movement of the Cartesian orientation A (only with "MC_MoveCircularAbsolute").
- With more than four interpolating kinematics axes:

  - With the parameter "EndPoint[5..6]", you define the B and C coordinates of the target position in the reference coordinate system.
  > **Note**
  >
  > **Orientation motion**
  >
  > The target orientation is always approached by the shortest distance. If the target orientation can be reached via two paths of equal length, motion is in the positive direction.

##### Defining the circular path via center point and angle (S7-1500T)

With the Motion Control instruction "MC_MoveCircularAbsolute", you move a kinematics with a circular motion to an absolute position. With the Motion Control instruction "MC_MoveCircularRelative", you move a kinematics with a circular motion relative to the position which was present at the start of the job processing.

Specify the intermediate point of the circular path and the angle for the definition of the circular path. Also define the main plane and the orientation of the circular path. The circular path and the target position are calculated via the defaults .

With this mode of circular path definition, the kinematics can also move circular paths with more than 360° in a main plane.

When defining the circle center and angle, ensure that the information is consistent.

###### Parameter inputs

You define the circular path of the circular motion with the following parameters of the Motion Control instruction "[MC_MoveCircularAbsolute](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_movecircularabsolute-position-kinematics-with-circular-path-motion-v8-s7-1500t)" or "[MC_MoveCircularRelative](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_movecircularrelative-relative-positioning-of-kinematics-with-circular-path-motion-v8-s7-1500t)":

- With the "CircMode" parameter, you define the mode of the circular path definition. With "CircMode" = 1, you define the circular path via the circle center and an angle in a main plane.
- With the "CoordSystem" parameter, you define the reference coordinate system.
- With the "AuxPoint[1..3]" parameters, you define the x, y and z coordinates of the center point of the circular path in the reference coordinate system.
- With the "EndPoint[4]" parameter, you define the A coordinates of the target position in the reference coordinate system.
- With up to four interpolating kinematics axes:

  - With the "DirectionA" parameter, you define the direction of movement of the Cartesian orientation A (only with "MC_MoveCircularAbsolute").
- With more than four interpolating kinematics axes:

  - With the parameter "EndPoint[5..6]", you define the B and C coordinates of the target position in the reference coordinate system.
  > **Note**
  >
  > **Orientation motion**
  >
  > The target orientation is always approached by the shortest distance. If the target orientation can be reached via two paths of equal length, motion is in the positive direction.
- With the "Arc" parameter, you define the angle of the circular path in the main plane.
- With the "CirclePlane" parameter, you define the main plane of the circular path in the reference coordinate system.
- With the "PathChoice" parameter, you define the orientation of the circular path in the reference coordinate system.

###### Main plane of the circular path

With the "CirclePlane" parameter, you define on which main plane of the reference coordinate system the circular path is to move:

- With the "CirclePlane" = 0 parameter, you define the xz plane of the reference coordinate system as the main plane.
- With the "CirclePlane" = 1 parameter, you define the yz plane of the reference coordinate system as the main plane.
- With the "CirclePlane" = 2 parameter, you define the xy plane of the reference coordinate system as the main plane.

###### Orientation of the circular path

There are two possible circular paths in the specified main plane. With the "PathChoice" parameter, you specify the direction in which the circular path should move:

- Use the positive direction of rotation with the "PathChoice" = 0 parameter.
- Use the negative direction of rotation using the "PathChoice" = 1 parameter.

In the following example, the xz plane is defined as the main plane:

![Orientation of the circular path](images/158943211659_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | Positive direction of rotation ("PathChoice" = 0) |
| ② | Target position of positive direction of rotation |
| ③ | Circle center |
| ④ | Start position |
| ⑤ | Target position of negative direction of rotation |
| ⑥ | Positive direction of rotation ("PathChoice" = 1) |
| α | Angle α = 135° |

The figure below shows the direction of rotation depending on the main planes:

![Orientation of the circular path](images/158943241483_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ![Orientation of the circular path](images/158943245707_DV_resource.Stream@PNG-de-DE.png) | Positive direction of rotation |
| ![Orientation of the circular path](images/158943249931_DV_resource.Stream@PNG-de-DE.png) | Negative direction of rotation |

##### Define circular path via radius and target position (S7-1500T)

With the Motion Control instruction "MC_MoveCircularAbsolute", you move a kinematics with a circular motion to an absolute position. With the Motion Control instruction "MC_MoveCircularRelative", you move a kinematics with a circular motion relative to the position which was present at the start of the job processing.

Specify the radius of the circular path and the target position for each definition of the circular path. Also define the main plane and the orientation of the circular path. The circular path is calculated via the defaults.

With this mode of circular path definition, the kinematics can only move circular paths less than 360° in a main plane.

When defining the radius and target position, ensure that the information is consistent.

###### Parameter inputs

You define the circular path of the circular motion with the following parameters of the Motion Control instruction "[MC_MoveCircularAbsolute](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_movecircularabsolute-position-kinematics-with-circular-path-motion-v8-s7-1500t)" or "[MC_MoveCircularRelative](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_movecircularrelative-relative-positioning-of-kinematics-with-circular-path-motion-v8-s7-1500t)":

- With the "CircMode" parameter, you define the mode of the circular path definition. With "CircMode" = 2, you define the circular path via the circle radius and the target position in a main plane.
- With the "CoordSystem" parameter, you define the reference coordinate system.
- With the parameter "EndPoint[1..4]", you define the x, y, z and A coordinates of the target position in the reference coordinate system.
- With up to four interpolating kinematics axes:

  - With the "DirectionA" parameter, you define the direction of movement of the Cartesian orientation A (only with "MC_MoveCircularAbsolute").
- With more than four interpolating kinematics axes:

  - With the parameter "EndPoint[5..6]", you define the B and C coordinates of the target position in the reference coordinate system.
  > **Note**
  >
  > **Orientation motion**
  >
  > The target orientation is always approached by the shortest distance. If the target orientation can be reached via two paths of equal length, motion is in the positive direction.
- With the "Radius" parameter, you define the radius of the circular path in the main plane.
- With the "CirclePlane" parameter, you define the main plane of the circular path in the reference coordinate system.
- With the "PathChoice" parameter, you define the orientation of the circular path in the reference coordinate system.

###### Main plane of the circular path

With the "CirclePlane" parameter, you define on which main plane of the reference coordinate system the circular path is to move:

- With the "CirclePlane" = 0 parameter, you define the xz plane of the reference coordinate system as the main plane.
- With the "CirclePlane" = 1 parameter, you define the yz plane of the reference coordinate system as the main plane.
- With the "CirclePlane" = 2 parameter, you define the xy plane of the reference coordinate system as the main plane.

###### Orientation of the circular path

Depending on the radius, up to four possible circular paths can occur in the specified main plane. With the "PathChoice" parameter, you specify how the circular path should move:

- Use the shorter positive circle segment with the "PathChoice" = 0 parameter.
- Use the shorter negative circle segment using the "PathChoice" = 1 parameter.
- Use the longer positive circle segment with the "PathChoice" = 2 parameter.
- Use the longer negative circle segment with the "PathChoice" = 3 parameter.

In the following example, the xz plane is defined as the main plane:

![Orientation of the circular path](images/158943292555_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | Longer positive circle segment ("PathChoice" = 2) |
| ② | Shorter positive circle segment ("PathChoice" = 0) |
| ③ | Start position |
| ④ | Target position |
| ⑤ | Shorter negative circle segment ("PathChoice" = 1) |
| ⑥ | Longer negative circle segment ("PathChoice" = 3) |

The following figure shows the positive and negative circle segments depending on the main planes:

![Orientation of the circular path](images/158943296779_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ![Orientation of the circular path](images/158943245707_DV_resource.Stream@PNG-de-DE.png) | Positive circle segments |
| ![Orientation of the circular path](images/158943249931_DV_resource.Stream@PNG-de-DE.png) | Negative circle segments |

#### Define the dynamic response of the circular motion (S7-1500T)

You can define the dynamic response of the circular path motion at the corresponding Motion Control instruction. You can only define the dynamic response of the orientation motion in the configuration of the kinematics technology object.

##### Parameter inputs

You define the dynamics of the circular motion with the following parameters of the Motion Control instruction "[MC_MoveCircularAbsolute](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_movecircularabsolute-position-kinematics-with-circular-path-motion-v8-s7-1500t)" or "[MC_MoveCircularRelative](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_movecircularrelative-relative-positioning-of-kinematics-with-circular-path-motion-v8-s7-1500t)":

- With the "Velocity" parameter, you specify the velocity of the path motion.
- With the "Acceleration" parameter, you specify the acceleration of the path motion.
- With the "Deceleration" parameter, you specify the deceleration of the path motion.
- With the "Jerk" parameter, you specify the jerk of the path motion.
- With the "DynamicAdaption" parameter, you specify the dynamic adaptation of the path motion.

With the following configuration parameters under "Technology object &gt; Configuration &gt; Extended parameters &gt; Dynamics", you define the dynamic response of the orientation motion:

- Select the entry "Orientation motion" in the "Settings for" drop-down list.
- Define the velocity of the orientation motion (&lt;TO&gt;.DynamicDefaults.Orientation.Velocity) in the field "Velocity".
- Define the acceleration of the orientation motion (&lt;TO&gt;.DynamicDefaults.Orientation.Acceleration) in the field "Acceleration".
- Define the deceleration of the orientation motion (&lt;TO&gt;.DynamicDefaults.Orientation.Deceleration) in the field "Deceleration".
- Define the jerk of the orientation motion (&lt;TO&gt;.DynamicDefaults.Orientation.Jerk) in the field "Jerk".

##### Dynamic adaptation

The dynamic adaptation limits the path dynamics to the axis dynamics. When dynamic adaptation is activated, a velocity profile for the motion of the kinematics is calculated, which takes into account not only the dynamic specifications or dynamic defaults and the dynamic limits of the kinematic motion, but also the maximum velocity, maximum acceleration and maximum deceleration of the kinematics axes. In addition, the dynamic defaults and the dynamic limits for velocity, acceleration and deceleration of the orientation motion are taken into account.

**Use the configured default**

With the "DynamicAdaption" &lt; 0 parameter, the configured default is used. You configure the default value in the field "Limit path dynamics to axis dynamics" under "Technology object &gt; Configuration &gt; Extended parameters &gt; Dynamics" of the kinematics technology object (&lt;TO&gt;.DynamicDefaults.DynamicAdaption).

**Do not limit path dynamics to axis dynamics**

With the "DynamicAdaption" = 0 parameter, no dynamic adaptation is used for the circular motion.

**Limit path dynamics to axis dynamics with segmentation of the path**

With the "DynamicAdaption" = 1 parameter, the dynamic adaptation is used for the circular motion. The path of the circular motion is divided into individual segments. For each of these segments, the velocity profile is calculated with consideration of the applicable limits. The dynamic response of the path is thus adapted for individual segments of the circular motion. As a result, a higher traversing velocity is reached section by section and the traversing time of the circular motion is reduced.

Note that dynamic adaptation with segmentation of the path requires a considerably higher computing time than dynamic adaptation without segmentation of the path.

**Limit path dynamics to axis dynamics without segmentation of the path**

With the "DynamicAdaption" = 2 parameter, the dynamic adaptation is used for the circular motion. The velocity profile is calculated for the entire circular motion. The limitations which apply to the entire motion job are taken into consideration.

#### Define the transition of circular motion (S7-1500T)

Multiple motions can be appended to one another, in which case the kinematics comes to a standstill between the individual motions. To achieve an uninterrupted Motion Control without standstill between the individual motion jobs, the individual motions can be blended with geometric transitions. You define the corresponding parameters at the new motion job (A2), into which the previous job (A1) is to be blended.

In the following examples, the various motion transitions are explained using an active linear motion (A1) and a subsequent circular motion (A2).

##### Parameter inputs

You define the transition to the active motion with the following parameters of the Motion Control instruction "[MC_MoveCircularAbsolute](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_movecircularabsolute-position-kinematics-with-circular-path-motion-v8-s7-1500t)" or "[MC_MoveCircularRelative](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_movecircularrelative-relative-positioning-of-kinematics-with-circular-path-motion-v8-s7-1500t)":

- With the "BufferMode" parameter, you define the mode of the motion transition.
- With the "TransitionParameter[1]" parameter, you define the rounding clearance.

##### Appending motion

With the "BufferMode" = 1 parameter, the circular motion is appended to the active motion. The active motion sequence (A1) is completed and the kinematics comes to a standstill. The circular motion (A2) is then executed.

![Appending motion](images/158926035339_DV_resource.Stream@PNG-de-DE.png)

In this case, the parameter "TransitionParameter[1]" is not relevant.

##### Blending motion

With the "BufferMode" = 2 parameter, the active motion is blended with the circular motion and the lower velocity of both jobs is used.

With the "BufferMode" = 5 parameter, the active motion is blended with the circular motion and the higher velocity of both jobs is used.

**Rounding clearance d &gt; 0.0**

With the "TransitionParameter[1]" &lt; 0.0 parameter, the active motion (A1) is blended with the circular motion (A2) as soon as the specified rounding clearance to the target position of the active motion is reached.

![Blending motion](images/158926181259_DV_resource.Stream@PNG-de-DE.png)

**Rounding clearance d = 0.0**

With the "TransitionParameter[1]" = 0.0 parameter the circular motion is appended to the active motion as with "BufferMode" = 1. The active motion sequence (A1) is completed and the kinematics comes to a standstill. The circular motion (A2) is then executed.

![Blending motion](images/158926186379_DV_resource.Stream@PNG-de-DE.png)

**Rounding clearance d &lt; 0.0**

With the "TransitionParameter[1]" &lt; 0.0 parameter, the active motion (A1) is blended with the circular motion (A2) as soon as the maximum rounding clearance to the target position of the active motion is reached.

You configure the factor of the maximum rounding clearance under "Technology object &gt; Configuration &gt; Extended parameters &gt; Job sequence" (&lt;TO&gt;.Transition.FactorBlendingLength). In the following example, the maximum rounding clearance is limited to 50% of the shorter distance.

![Blending motion](images/158926562699_DV_resource.Stream@PNG-de-DE.png)

#### Starting a circular motion job (S7-1500T)

After the start of the circular motion job with "Execute" = TRUE, the job is added to the [job sequence](#job-sequence-s7-1500t). The processing status is indicated in the Motion Control instruction "[MC_MoveCircularAbsolute](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_movecircularabsolute-position-kinematics-with-circular-path-motion-v8-s7-1500t)" or. "[MC_MoveCircularRelative](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_movecircularrelative-relative-positioning-of-kinematics-with-circular-path-motion-v8-s7-1500t)" with the parameter "Busy" = TRUE. If the job is active, this is indicated with the parameter "Active" = TRUE and in the "&lt;TO&gt;.StatusWord.X9 (CircularCommand)" tag of the technology object.

As soon as the target position is reached or the circular motion is blended to the next motion, the job is completed. The status is indicated with the parameter "Done" = TRUE.

You can find more information in the section "[Motion status and remaining distance](#motion-status-and-remaining-distance-s7-1500t)".

#### Tags: Circular motion (S7-1500T)

The following technology object tags are relevant for motion control:

| Tag | Description |  |
| --- | --- | --- |
| **Status values** |  |  |
| &lt;TO&gt;.StatusWord | Status indicator for an active motion |  |
| &lt;TO&gt;.StatusWord.X9 (CircularCommand) | The value "TRUE" is set if a job for circular motion is active ("MC_MoveCircularAbsolute", "MC_MoveCircularRelative"). |  |
| &lt;TO&gt;.Tcp | Target coordinates x, y, z, A, B, C of the kinematics motion in the world coordinate system |  |
| &lt;TO&gt;.StatusPath.CoordSystem | Coordinate system of the active motion job |  |
| 0 | World coordinate system |  |
| 1, 2, 3 | Object coordinate system 1, 2, 3 |  |
| 100 | Machine coordinate system |  |
| 101 | Joint coordinate system<sup>1)</sup> |  |
| &lt;TO&gt;.StatusPath.Velocity | Current path velocity (setpoint reference) |  |
| &lt;TO&gt;.StatusPath.Acceleration | Current path acceleration (setpoint reference) |  |
| &lt;TO&gt;.StatusPath.OrientationVelocity | Resulting orientation velocity |  |
| &lt;TO&gt;.StatusPath.DynamicAdaption | Dynamic adaptation |  |
| 0 | No dynamic adaptation |  |
| 1 | Dynamic adaptation with segmentation of the path |  |
| 2 | Dynamic adaptation without segmentation of the path |  |
| &lt;TO&gt;.StatusPath.TotalPathLength | Total path length of linear and circular path motions  Sum of:  - Distance of all completed motion jobs - Distance travelled of the active motion job - Remaining distance of the motion job - Calculated distance of all jobs in the job sequence |  |
| &lt;TO&gt;.StatusPath.AccumulatedPathLength | Accumulated path length of linear and circular path motions  Sum of:  - Distance of all completed motion jobs - Distance travelled of the active motion job |  |
| &lt;TO&gt;.StatusMotionQueue.NumberOfCommands | Number of jobs in the job sequence |  |
| **Override** |  |  |
| &lt;TO&gt;.Override.Velocity | Velocity override |  |
| **Dynamic limits** |  |  |
| &lt;TO&gt;.DynamicLimits.Path.Velocity | Dynamic limitation for the maximum velocity of the path |  |
| &lt;TO&gt;.DynamicLimits.Path.Acceleration | Dynamic limitation for the maximum acceleration of the path |  |
| &lt;TO&gt;.DynamicLimits.Path.Deceleration | Dynamic limitation for the maximum deceleration of the path |  |
| &lt;TO&gt;.DynamicLimits.Path.Jerk | Dynamic limitation for the maximum jerk of the path |  |
| &lt;TO&gt;.DynamicLimits.Orientation.Velocity | Dynamic limitation for the maximum velocity of the Cartesian orientation |  |
| &lt;TO&gt;.DynamicLimits.Orientation.Acceleration | Dynamic limitation for the maximum acceleration of the Cartesian orientation |  |
| &lt;TO&gt;.DynamicLimits.Orientation.Deceleration | Dynamic limitation for the maximum deceleration of the Cartesian orientation |  |
| &lt;TO&gt;.DynamicLimits.Orientation.Jerk | Dynamic limitation for the maximum jerk of the Cartesian orientation |  |
| **Dynamic defaults** |  |  |
| &lt;TO&gt;.DynamicDefaults.Path.Velocity | Default setting of the velocity of the path |  |
| &lt;TO&gt;.DynamicDefaults.Path.Acceleration | Default setting of the acceleration of the path |  |
| &lt;TO&gt;.DynamicDefaults.Path.Deceleration | Default setting of the deceleration of the path |  |
| &lt;TO&gt;.DynamicDefaults.Path.Jerk | Default setting of the jerk of the path |  |
| &lt;TO&gt;.DynamicDefaults.Orientation.Velocity | Default setting of the velocity of the Cartesian orientation |  |
| &lt;TO&gt;.DynamicDefaults.Orientation.Acceleration | Default setting of the acceleration of the Cartesian orientation |  |
| &lt;TO&gt;.DynamicDefaults.Orientation.Deceleration | Default setting of the deceleration of the Cartesian orientation |  |
| &lt;TO&gt;.DynamicDefaults.Orientation.Jerk | Default setting of the jerk of the Cartesian orientation |  |
| &lt;TO&gt;.DynamicDefaults.DynamicAdaption | Default setting of the dynamic adaptation |  |
| 0 | No dynamic adaptation |  |
| 1 | Dynamic adaptation with segmentation of the path |  |
| 2 | Dynamic adaptation without segmentation of the path |  |
| **Rounding clearance** |  |  |
| &lt;TO&gt;.Transition.FactorBlendingLength | Factor of the maximum rounding clearance in percent [%]  The configuration takes place in "Technology object &gt; Configuration &gt; Extended parameters &gt; Job sequence".  Change the factor in the user program before sending the motion jobs to the job sequence so that the change is effective. |  |
| 0.0 | No blending possible |  |
| 50.0 | Default value |  |
| 100.0 | Blending possible with complete segment length or motion length |  |
| <sup>1)</sup> With up to four interpolating kinematics axes, the joint coordinate system is identical to the machine coordinate system. |  |  |

### Moving a kinematics with a synchronous "point-to-point" motion (S7-1500T)

This section contains information on the following topics:

- [Brief description of synchronous "point-to-point" motion (S7-1500T)](#brief-description-of-synchronous-point-to-point-motion-s7-1500t)
- [Defining the target position of the sPTP motion (S7-1500T)](#defining-the-target-position-of-the-sptp-motion-s7-1500t)
- [Defining the dynamics factors of the sPTP motion (S7-1500T)](#defining-the-dynamics-factors-of-the-sptp-motion-s7-1500t)
- [Defining the transition of the sPTP motion (S7-1500T)](#defining-the-transition-of-the-sptp-motion-s7-1500t)
- [Starting the sPTP motion job (S7-1500T)](#starting-the-sptp-motion-job-s7-1500t)
- [Tags: sPTP motion (S7-1500T)](#tags-sptp-motion-s7-1500t)

#### Brief description of synchronous "point-to-point" motion (S7-1500T)

With a synchronous "point-to-point" motion (sPTP motion), you can move a kinematics time- and motion-optimized, bypass [singularities](#singularities-s7-1500t) or change joint position spaces. The kinematics does not follow a specified path. The single-axis motions, which move the kinematics axes synchronously, are calculated from the start and target positions. All kinematics axes move simultaneously and reach the corresponding target position at the same time. The kinematics axis with the longest travel time determines the travel time of the sPTP motion and therefore the travel time of all other kinematics axes. The movement path of the tool center point (TCP) results from the motions and dynamics of the individual axes.

Blending between sPTP motions and path motions results in the reduction of the travel time of a sequence of motion jobs, e.g.:

- Record product with a defined path motion
- Move product with sPTP motion as quickly as possible
- Place product with a defined path motion

With the Motion Control instruction "[MC_MoveDirectAbsolute](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_movedirectabsolute-absolute-movement-of-kinematics-with-synchronous-point-to-point-motion-v8-s7-1500t)", you move a kinematics with an sPTP motion to an absolute position. With the Motion Control instruction "[MC_MoveDirectRelative](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_movedirectrelative-relative-movement-of-kinematics-with-synchronous-point-to-point-motion-v8-s7-1500t)", you move a kinematics with an sPTP motion relative to the position which was present at the start of the job processing.

> **Note**
>
> **Traversing coupled axis with sPTP motion**
>
> For coupled axes with coupling factor ≠ 1, the traversing of joints in the JCS with an sPTP motion can result in compensation motions of the coupled axes.

You have the following options for the sPTP motion:

- Define target position:

  - [Define axis target positions](#defining-the-axis-target-position-of-the-sptp-motion-s7-1500t)
  - [Define joint target positions](#define-joint-target-positions-of-the-sptp-motion-s7-1500t)
  - [Define Cartesian coordinates](#defining-the-cartesian-target-coordinates-of-the-sptp-motion-s7-1500t)
- [Define dynamic factors](#defining-the-dynamics-factors-of-the-sptp-motion-s7-1500t)
- [Define motion transition](#defining-the-transition-of-the-sptp-motion-s7-1500t)
- [Start job and show execution progress](#starting-the-sptp-motion-job-s7-1500t)

#### Defining the target position of the sPTP motion (S7-1500T)

This section contains information on the following topics:

- [Defining the axis target position of the sPTP motion (S7-1500T)](#defining-the-axis-target-position-of-the-sptp-motion-s7-1500t)
- [Define joint target positions of the sPTP motion (S7-1500T)](#define-joint-target-positions-of-the-sptp-motion-s7-1500t)
- [Defining the Cartesian target coordinates of the sPTP motion (S7-1500T)](#defining-the-cartesian-target-coordinates-of-the-sptp-motion-s7-1500t)

##### Defining the axis target position of the sPTP motion (S7-1500T)

With the Motion Control instruction "MC_MoveDirectAbsolute", you move a kinematics with a synchronous "point-to-point" motion (sPTP motion) to an absolute position. With the Motion Control instruction "MC_MoveDirectRelative", you move a kinematics with an sPTP motion relative to the position which was present at the start of the job processing.

Enter axis-related target positions in the machine coordinate system (MCS). The single-axis motions are calculated from the start and target positions of the axes. The kinematics moves all single-axis motions synchronously. All kinematics axes move simultaneously and reach the given target positions at the same time. The kinematics axis with the longest travel time determines the travel time of the sPTP motion and therefore the travel time of all other kinematics axes.

###### Parameter inputs

**Absolute target positions**

You define the absolute target position of the axes with the following parameters of the Motion Control instruction "[MC_MoveDirectAbsolute](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_movedirectabsolute-absolute-movement-of-kinematics-with-synchronous-point-to-point-motion-v8-s7-1500t)":

- With the "CoordSystem" = 100 parameter, you define the MCS as the reference coordinate system.
- With the "Position[1..4]" parameters, you define the absolute target joint positions of the axes A1 to A4.
- With more than four interpolating kinematics axes:

  - With the "Position[5..6]" parameters, you define the absolute target joint positions of the axes A5 and A6.

**Relative target positions**

You define the relative target position of the axes with the following parameters of the Motion Control instruction "[MC_MoveDirectRelative](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_movedirectrelative-relative-movement-of-kinematics-with-synchronous-point-to-point-motion-v8-s7-1500t)":

- With the "CoordSystem" = 100 parameter, you define the MCS as the reference coordinate system.
- With the "Distance[1..4]" parameters, you define the relative target joint positions of the axes A1 to A4.
- With more than four interpolating kinematics axes:

  - With the "Distance[5..6]" parameters, you define the relative target joint positions of the axes A5 and A6.

##### Define joint target positions of the sPTP motion (S7-1500T)

With the Motion Control instruction "MC_MoveDirectAbsolute", you move a kinematics with a synchronous "point-to-point" motion (sPTP motion) to an absolute position. With the Motion Control instruction "MC_MoveDirectRelative", you move a kinematics with an sPTP motion relative to the position which was present at the start of the job processing.

Enter target positions in the joint coordinate system (JCS). The single-axis motions are calculated from the start and target positions of the joints. The kinematics moves all single-axis motions synchronously. All kinematics axes move simultaneously and reach the given target positions at the same time. The kinematics axis with the longest travel time determines the travel time of the sPTP motion and therefore the travel time of all other kinematics axes.

With up to four interpolating kinematics axes, the joint coordinate system is identical to the machine coordinate system.

###### Parameter inputs

**Absolute target positions**

You define the absolute target position of the joints with the following parameters of the Motion Control instruction "[MC_MoveDirectAbsolute](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_movedirectabsolute-absolute-movement-of-kinematics-with-synchronous-point-to-point-motion-v8-s7-1500t)":

- With the "CoordSystem" = 101 parameter, you define the JCS as the reference coordinate system.
- With the "Position[1..4]" parameters, you define the absolute target positions of joints J1 to J4.
- With more than four interpolating kinematics axes:

  - With the "Position[5..6]" parameters. you define the absolute target positions of joints J5 and J6.

**Relative target positions**

You define the relative target positions of the joints with the following parameters of the Motion Control instruction "[MC_MoveDirectRelative](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_movedirectrelative-relative-movement-of-kinematics-with-synchronous-point-to-point-motion-v8-s7-1500t)":

- With the "CoordSystem" = 101 parameter, you define the JCS as the reference coordinate system.
- With the "Distance[1..4]" parameters, you define the relative target positions of joints J1 to J4.
- With more than four interpolating kinematics axes:

  - With the "Distance[5..6]" parameters, you define the relative target positions of joints J5 and J6.

##### Defining the Cartesian target coordinates of the sPTP motion (S7-1500T)

With the Motion Control instruction "MC_MoveDirectAbsolute", you move a kinematics with a synchronous "point-to-point" motion (sPTP motion) to an absolute position. With the Motion Control instruction "MC_MoveDirectRelative", you move a kinematics with an sPTP motion relative to the position which was present at the start of the job processing.

You define the Cartesian target coordinates in the world coordinate system (WCS) or an object coordinate system (OCS). The single-axis motions are calculated from the start and target coordinates. The kinematics moves all single-axis motions synchronously. All kinematics axes move simultaneously and reach their target positions at the same time. The kinematics axis with the longest travel time determines the travel time of the sPTP motion and therefore the travel time of all other kinematics axes.

###### Parameter inputs

**Absolute Cartesian coordinates**

You define the absolute Cartesian target coordinates of the sPTP motion with the following parameters of the Motion Control instruction "[MC_MoveDirectAbsolute](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_movedirectabsolute-absolute-movement-of-kinematics-with-synchronous-point-to-point-motion-v8-s7-1500t)":

- With the "CoordSystem" = 0, 1, 2 or 3 parameter, you define the WCS, OCS1, OCS2 or OCS3 as the reference coordinate system.
- With the "Position[1..4]" parameters, you define the absolute Cartesian target coordinates x, y, z and A.
- With the "LinkConstellation" parameter, you define the target arm positioning space.
- With up to four interpolating kinematics axes:

  - With the "PositionMode" parameter, you define for the kinematics types with orientation A whether the value of the parameter "Position[4]" is to be interpreted as absolute or relative for the axis A4. This is only possible if you have enabled Modulo functionality for the axis A4.
  - If "PositionMode" = 1, you define the direction of movement of the Cartesian orientation A with the "DirectionA" parameter. This is only possible if you have enabled Modulo functionality for the axis A4.
- With more than four interpolating kinematics axes:

  - With the "Position[5..6]" parameters, you define the absolute Cartesian target coordinates B and C.
  - With the parameter "TurnJoint[1..6]", you define the target joint position ranges of the joints J1 to J6.

**Relative Cartesian coordinates**

You define the relative Cartesian target coordinates of the sPTP motion with the following parameters of the Motion Control instruction "[MC_MoveDirectRelative](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_movedirectrelative-relative-movement-of-kinematics-with-synchronous-point-to-point-motion-v8-s7-1500t)":

- With the "CoordSystem" = 0, 1, 2 or 3 parameter, you define the WCS, OCS1, OCS2 or OCS3 as the reference coordinate system.
- With the "Distance[1..4]" parameters, you define the relative Cartesian target coordinates x, y, z and A.
- With the "LinkConstellation" parameter, you define the target arm positioning space.
- With more than four interpolating kinematics axes:

  - With the "Distance[5..6]" parameters, you define the relative target coordinates B and C.
  - With the parameter "TurnJoint[1..6]", you define the target joint position ranges of the joints J1 to J6.

###### Joint position range

With more than four interpolating kinematics axes, you can define the target joint position ranges of the joints J1 to J6. You determine the joint position range of the joint J[i] at the target position with the "TurnJoint[i]" parameter. The parameter values are defined as follows:

| Value | Description |
| --- | --- |
| m (m &lt; 0) | -180° + m · 360° ≤ Position &lt; 180° + m · 360° |
| -2 | -900 ≤ position &lt; -540 |
| -1 | -540 ≤ position &lt; -180 |
| 0 | Shortest distance |
| 1 | -180 ≤ position &lt; 180 |
| 2 | 180 ≤ position &lt; 540 |
| 3 | 540 ≤ position &lt; 900 |
| n (n &gt; 0) | -180° + (n - 1) · 360° ≤ Position &lt; 180° + (n - 1) · 360° |

The parameterized values for the joint position ranges are absolute for the motion control instructions "MC_MoveDirectAbsolute" and "MC_MoveDirectRelative".

The current position setpoints of the joints J1 to J6 are indicated in the variables "&lt;TO&gt;.JointData.J[1..6].Position" of the technology object. You can derive the current joint position areas from the current position setpoints.

**Example**

The current position of a joint J[i] is 0°. The joint J[i] is therefore located in joint position range 1.

With the specification "Position[i]" = 90.0 and "TurnJoint[i]" = 2, the joint J[i] will not only rotate by 90°, but by 450° in order to reach the specified target joint position range 2.

With the specification "Position[i]" = 0.0 and "TurnJoint[i]" = 2, the joint J[i] will rotate by 360° in order to reach the center of the specified target joint position range 2.

#### Defining the dynamics factors of the sPTP motion (S7-1500T)

The dynamic response of the synchronous "point-to-point" motion (sPTP motion) is determined via dynamics factors. The factors relate to the configured maximum dynamic values of the kinematics axes. You configure the maximum dynamic values in "Technology objects &gt; Configuration &gt; Extended parameters &gt; Limits &gt; Dynamics limits" of the technology objects of the interconnected axes.

The single-axis motions, which move the kinematics axes synchronously, are calculated from the start and target positions. All kinematics axes move simultaneously and reach the corresponding target position at the same time. The kinematics axis with the longest travel time determines the travel time of the sPTP motion and therefore the travel time of all other kinematics axes. For the motion profile calculation, the dynamic values of the individual kinematics axes are adapted to the kinematics axis with the longest movement time.

##### Parameter inputs

You define the dynamics of the sPTP motion with the following parameters of the Motion Control instruction "[MC_MoveDirectAbsolute](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_movedirectabsolute-absolute-movement-of-kinematics-with-synchronous-point-to-point-motion-v8-s7-1500t)" or "[MC_MoveDirectRelative](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_movedirectrelative-relative-movement-of-kinematics-with-synchronous-point-to-point-motion-v8-s7-1500t)":

- With the "VelocityFactor" parameter, you define the velocity factor of the sPTP motion.
- With the "AccelerationFactor" parameter, you define the acceleration factor of the sPTP motion.
- With the "DecelerationFactor" parameter, you define the deceleration factor of the sPTP motion.
- With the "JerkFactor" parameter, you define the jerk factor of the sPTP motion.

##### Configure default settings

Proceed as follows to configure the defaults for the dynamics factors of the sPTP motion:

1. Open the "Technology object &gt; Configuration &gt; Extended parameters &gt; Dynamics" configuration window of the kinematics technology object.
2. Select the entry "sPTP motion" in the "Settings for" drop-down list.
3. Enter the default for the velocity factor in the field "Velocity factor" (&lt;TO&gt;.DynamicDefaults.MoveDirect.VelocityFactor).
4. Enter the default for the acceleration factor in the field "Acceleration factor" (&lt;TO&gt;.DynamicDefaults.MoveDirect.AccelerationFactor).
5. Enter the default for the deceleration factor in the field "Deceleration factor" (&lt;TO&gt;.DynamicDefaults.MoveDirect.DecelerationFactor).
6. Enter the default for the jerk factor in the field "Jerk factor" (&lt;TO&gt;.DynamicDefaults.MoveDirect.JerkFactor).

#### Defining the transition of the sPTP motion (S7-1500T)

Multiple motions can be appended to one another, in which case the kinematics comes to a standstill between the individual motions. To achieve an uninterrupted Motion Control without standstill between the individual motion jobs, the individual motions can be blended with geometric transitions. You define the corresponding parameters at the new motion job (A2), into which the previous job (A1) is to be blended.

In the following examples, the various motion transitions are explained using an active linear motion (A1) and a subsequent sPTP motion (A2). The sPTP motion is shown as an example. The motion of the kinematics results from off the joint position of the individual axes and the dynamics of the motion job.

##### Parameter inputs

You define the transition to the active motion with the following parameters of the Motion Control instruction "[MC_MoveDirectAbsolute](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_movedirectabsolute-absolute-movement-of-kinematics-with-synchronous-point-to-point-motion-v8-s7-1500t)" or "[MC_MoveDirectRelative](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_movedirectrelative-relative-movement-of-kinematics-with-synchronous-point-to-point-motion-v8-s7-1500t)":

- With the "BufferMode" parameter, you define the mode of the motion transition.
- With the "TransitionParameter[1]" parameter, you define the rounding clearance.

##### Append motion

With the "BufferMode" = 1 parameter, the sPTP motion is appended to the active motion. The active motion sequence (A1) is completed and the kinematics comes to a standstill. The sPTP motion (A2) is then executed.

![Append motion](images/158943301003_DV_resource.Stream@PNG-de-DE.png)

In this case, the parameter "TransitionParameter[1]" is not relevant.

##### Blending motion

**Blending two sPTP motions**

With parameter "BufferMode" = 2, the active sPTP motion is blended with the subsequent sPTP motion. When blending two sPTP motions, the lower velocity of the two jobs is used.

With parameter "BufferMode" = 5, the active sPTP motion is blended with the subsequent sPTP motion. When blending two sPTP motions, the higher velocity of the two jobs is used.

To enable a continuous blending between two sPTP motions, observe the following:

- Set a sufficiently large rounding clearance.
- Set the dynamic factors for the acceleration and jerk of the sPTP motion as high as possible.
- Set the dynamic response of the two sPTP motions similarly.

**Blending path motions and sPTP motions**

When blending path motions and sPTP motions, the velocity of the blending segment is independent of the parameter value "BufferMode" = 2 or 5. The dynamic limits of the axes are not exceeded in the blending area.

To enable a continuous blending between path motions and sPTP motions, observe the following:

- Set a sufficiently large rounding clearance.
- Avoid small curvature radii in the resulting contour of the TCP.
- Set the dynamic response of the path motion and the sPTP motion similarly.
- Set the dynamic adaptation for the path motion.
- Set the dynamics factors of the sPTP motion to smaller than 1.0.
- Set the acceleration and the jerk of the path motion as high as possible.

##### Define blending distance

**Rounding clearance d &gt; 0.0**

With the "TransitionParameter[1]" &lt; 0.0 parameter, the active motion (A1) is blended with the sPTP motion (A2) as soon as the specified rounding clearance to the target position of the active motion is reached.

![Define blending distance](images/158926567819_DV_resource.Stream@PNG-de-DE.png)

**Rounding clearance d = 0.0**

With the "TransitionParameter[1]" = 0.0 parameter, the sPTP motion is appended to the active motion as with "BufferMode" = 1. The active motion sequence (A1) is completed and the kinematics comes to a standstill. The sPTP motion (A2) is then executed.

![Define blending distance](images/158926572939_DV_resource.Stream@PNG-de-DE.png)

**Rounding clearance d &lt; 0.0**

With the "TransitionParameter[1]" &lt; 0.0 parameter, the active motion (A1) is blended with the sPTP motion (A2) as soon as the maximum rounding clearance to the target position of the active motion is reached.

You configure the factor of the maximum rounding clearance under "Technology object &gt; Configuration &gt; Extended parameters &gt; Job sequence" (&lt;TO&gt;.Transition.FactorBlendingLength). In the following example, the maximum rounding clearance is limited to 50% of the shorter distance.

![Define blending distance](images/158926757259_DV_resource.Stream@PNG-de-DE.png)

#### Starting the sPTP motion job (S7-1500T)

After the start of the synchronous "point-to-point" job (sPTP motion) with "Execute" = TRUE, the job is added to the [job sequence](#job-sequence-s7-1500t). The processing status is indicated in the Motion Control instruction "[MC_MoveDirectAbsolute](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_movedirectabsolute-absolute-movement-of-kinematics-with-synchronous-point-to-point-motion-v8-s7-1500t)" or. "[MC_MoveDirectRelative](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_movedirectrelative-relative-movement-of-kinematics-with-synchronous-point-to-point-motion-v8-s7-1500t)" with the parameter "Busy" = TRUE. If the job is active, this is indicated with the parameter "Active" = TRUE and in the "&lt;TO&gt;.StatusWord.X11 (DirectCommand)" tag of the technology object.

The progress of execution is displayed using the "ExecutionTimeStatus" parameter. The parameter value starts at 0.0 and increases incrementally in the course of job execution.

As soon as the target position is reached or the sPTP motion is blended to the next motion, the job is completed. The status is indicated with the parameter "Done" = TRUE and "ExecutionTimeStatus" = 1.0 .

#### Tags: sPTP motion (S7-1500T)

The following technology object tags are relevant for motion control:

| Tag | Description |  |
| --- | --- | --- |
| **Status values** |  |  |
| &lt;TO&gt;.StatusWord | Status indicator for an active motion |  |
| &lt;TO&gt;.StatusWord.X11 (DirectCommand) | The value "TRUE" is set if a job for sPTP motion is active ("MC_MoveDirectAbsolute", "MC_MoveDirectRelative"). |  |
| &lt;TO&gt;.Tcp | Target coordinates x, y, z, A, B, C of the kinematics motion in the world coordinate system |  |
| &lt;TO&gt;.AxesData.A[1..6] | Current setpoints of the kinematics motion for the kinematics axes A1 to A6 |  |
| &lt;TO&gt;.JointData.J[1..6] | Current setpoints of the kinematics motion for the joints J1 to J6 |  |
| &lt;TO&gt;.StatusPath.CoordSystem | Coordinate system of the active motion job |  |
| 0 | World coordinate system |  |
| 1, 2, 3 | Object coordinate system 1, 2, 3 |  |
| 100 | Machine coordinate system |  |
| 101 | Joint coordinate system<sup>1)</sup> |  |
| &lt;TO&gt;.StatusMotionQueue.NumberOfCommands | Number of jobs in the job sequence |  |
| **Override** |  |  |
| &lt;TO&gt;.Override.Velocity | Velocity override |  |
| **Dynamic defaults** |  |  |
| &lt;TO&gt;.DynamicDefaults.MoveDirect.VelocityFactor | Factor for the velocity of the axis motions in relation to the respective maximum velocity of the axes with sPTP motion. |  |
| &lt;TO&gt;.DynamicDefaults.MoveDirect.AccelerationFactor | Factor for the acceleration of the axis motions in relation to the respective maximum acceleration of the axes with sPTP motion. |  |
| &lt;TO&gt;.DynamicDefaults.MoveDirect.DecelerationFactor | Factor for the deceleration of the axis motions in relation to the respective maximum deceleration of the axes with sPTP motion. |  |
| &lt;TO&gt;.DynamicDefaults.MoveDirect.JerkFactor | Factor for the jerk of the axis motions in relation to the respective maximum jerk of the axes with sPTP motion. |  |
| **Rounding clearance** |  |  |
| &lt;TO&gt;.Transition.FactorBlendingLength | Factor of the maximum rounding distance in percent [%]  The configuration takes place in "Technology object &gt; Configuration &gt; Extended parameters &gt; Job sequence".  Change the factor in the user program before sending the motion jobs to the job sequence so that the change is effective. |  |
| 0.0 | No blending possible |  |
| 50.0 | Default value |  |
| 100.0 | Blending possible with complete segment length or motion length |  |
| <sup>1)</sup> With up to four interpolating kinematics axes, the joint coordinate system is identical to the machine coordinate system. |  |  |

### Conveyor Tracking (S7-1500T)

This section contains information on the following topics:

- [Brief description of conveyor tracking (S7-1500T)](#brief-description-of-conveyor-tracking-s7-1500t)
- [Configuring and starting conveyor tracking (S7-1500T)](#configuring-and-starting-conveyor-tracking-s7-1500t)
- [Phases of conveyor tracking (S7-1500T)](#phases-of-conveyor-tracking-s7-1500t)
- [Behavior of the "TrackingState" tag (S7-1500T)](#behavior-of-the-trackingstate-tag-s7-1500t)
- [Motion between two tracked OCS (S7-1500T)](#motion-between-two-tracked-ocs-s7-1500t)
- [Dynamics in the phases of the conveyor tracking (S7-1500T)](#dynamics-in-the-phases-of-the-conveyor-tracking-s7-1500t)
- [Stopping behavior with "MC_GroupStop" and "MC_GroupInterrupt" (S7-1500T)](#stopping-behavior-with-mc_groupstop-and-mc_groupinterrupt-s7-1500t)
- [Blending behavior (S7-1500T)](#blending-behavior-s7-1500t)

#### Brief description of conveyor tracking (S7-1500T)

With conveyor tracking, the kinematics can follow an object on a moving conveyor belt. The conveyor belt is represented by a leading-value-capable technology object. Leading-value-capable technology objects are:

- Positioning axis
- Synchronous axis
- External encoder
- Leading axis proxy

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Overrun of the dynamics in the vicinity of a singularity**  In the vicinity of a [singularity](#singularities-s7-1500t) a path motion without dynamic adaptation mostly results in overruns of the dynamics. This means one or more kinematics axes can move at very high speed and accelerate or decelerate with excessive force.  This can cause the following damages:  - Personal injury, for example, caused by products or machine parts coming loose - Machine damage, for example, through overload of the mechanical components   Activate the dynamic adaptation by setting the value for "DynamicAdaption" to "1" or "2" on the motion job. Also parameterize the dynamic reserve (&lt;TO&gt;.Conveyor.DynamicReserve[1..1]). |  |

A typical motion sequence runs in 5 phases.

![Figure](images/166698969227_DV_resource.Stream@PNG-de-DE.png)

**Phase 1:** Detect the object position on the conveyor belt

**Phase 2:** Assign OCS to the object position

**Phase 3:** Synchronize TCP to tracked OCS

**Phase 4:** Move TCP within the tracked OCS

**Phase 5:** Desynchronize TCP from the OCS

The current status of conveyor tracking is displayed in the tag structure "&lt;TO&gt;.StatusConveyor[1..3].TrackingState". "StatusConveyor[1]" refers to OCS1.

#### Configuring and starting conveyor tracking (S7-1500T)

Configure and start the conveyor tracking function as follows:

- In the "Conveyor tracking" configuration window, interconnect the leading values and configure the type of coupling for conveyor tracking.
- Use the "MC_TrackConveyorBelt" Motion Control instruction to start the configured conveyor tracking.

##### Configure leading values for the conveyor tracking

Configure the coupling coefficients in the "Conveyor tracking" configuration window as follows:

1. In the table column "Possible technology objects", add all leading-value-capable technology objects that you need in the instruction as leading-value-capable values for conveyor tracking.

   An object coordinate system can only be coupled with a leading-value-capable technology object whose technology object is defined in this table.
2. In the "Type of coupling" column, select how the leading value of the technology object capable of the leading value is to be coupled:

   - Via a setpoint
   - Via an actual value

     With external encoders, only the selection of the actual value is available.
   - Delayed

---

**See also**

[MC_TrackConveyorBelt: Start conveyor tracking V8 (S7-1500T)](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_trackconveyorbelt-start-conveyor-tracking-v8-s7-1500t)

#### Phases of conveyor tracking (S7-1500T)

##### Phase 1: Detect the object position on the conveyor belt

The frame "ConveyorBeltOrigin" is used to define the original position of the conveyor belt in relation to the WCS.

The x direction of the "ConveyorBeltOrigin" must be aligned in the direction of the conveyor belt. When defining frames, note the restrictions described in the "[Frames](#define-kcsocs-frame-s7-1500t)" section. The "ConveyorBeltOrigin" frame is defined in the example on the left side of the conveyor belt. However, the "ConveyorBeltOrigin" frame can be set so that it does not coincide with the zero point of the conveyor belt. The frame "ConveyorBeltOrigin" is assigned to the Motion Control instruction "MC_TrackConveyorBelt".

When an object reaches a defined position, the current position of the conveyor belt is recorded, e.g. using a measuring input function with a light barrier or with a camera. The "BeltPosition" tag shows the position of the leading-value-capable technology object. In the example, "BeltPosition" is 2000 mm at acquisition time t0. The distance between the measuring position and "ConveyorBeltOrigin" is 500 mm.

![Phase 1: Detect the object position on the conveyor belt](images/158926959499_DV_resource.Stream@PNG-de-DE.png)

After the conveyor position has been acquired, you must enter the "InitialObjectPosition" at the Motion Control instruction "MC_TrackConveyorBelt".

The "InitialObjectPosition" is calculated as follows:

"InitialObjectPosition" = Detected position of the conveyor belt at the time of object detection - Distance of the measuring position from the "ConveyorBeltOrigin" in x direction

The "InitialObjectPosition" from the example is calculated as follows:

"InitialObjectPosition" = 2000 mm - 500 mm = 1500 mm

If the frame "ConveyorBeltOrigin" is exactly at the acquisition position of the object, then the "BeltPosition" corresponds to the "InitialObjectPosition".

The relative offset of the object to the ConveyorBeltOrigin in x direction is calculated from the difference between the "BeltPosition" and the "InitialObjectPosition".

At the time of acquisition, the "BeltPosition" is 2000 mm and the "InitialObjectPosition" is 1500 mm. This results in a relative offset of 500 mm. The offset of the tracked OCS in x direction to the reference position "ConveyorBeltOrigin" is displayed in the "ObjectPosition".

The "ObjectPosition" is calculated as follows:

ObjectPosition = BeltPosition - InitialObjectPosition

No OCS is yet coupled in this phase "TrackingState" is "0". The description of the tag and an overview of the behavior of the tag can be found in section "[Behavior of the "TrackingState" tag](#behavior-of-the-trackingstate-tag-s7-1500t)".

##### Phase 2: OCS is assigned to the object position

With a Motion Control instruction "MC_TrackConveyorBelt", the OCS1 is assigned to the acquired object position ("ObjectPosition") at time t1. The OCS is then tracked with the object in x direction.

"TrackingState" changes from "0" to "1".

![Phase 2: OCS is assigned to the object position](images/158926964619_DV_resource.Stream@PNG-de-DE.png)

At time t1 the "BeltPosition" is 2400 mm. This calculates the "ObjectPosition" from the example as follows:

"ObjectPosition" = 2400 mm - 1500 mm = 900 mm.

When the conveyor belt moves, the "BeltPosition" and the "ObjectPosition" rise at the same time. The "InitialObjectPosition" is constant. The OCS is moved further in x direction.

At time t2, the conveyor belt has moved the object further in x direction of the OCS and the OCS1 continues to be tracked. The OCS frame moves with the leading value that the conveyor belt specifies.

At time t2 the "BeltPosition" is 2500 mm. This means that the "ObjectPosition" is 1000 mm.

![Phase 2: OCS is assigned to the object position](images/158926969739_DV_resource.Stream@PNG-de-DE.png)

##### Phase 3: Synchronize TCP to tracked OCS

With the first motion job in the tracked OCS, the TCP is synchronized to the motion of the OCS. Use the Motion Control instruction "MC_MoveLinearAbsolute" or "MC_MoveCircularAbsolute" for the first motion job. You specify the target position in absolute coordinates in the tracked OCS.

"TrackingState" changes with the start of the job from "1" to "2".

![Phase 3: Synchronize TCP to tracked OCS](images/158927000459_DV_resource.Stream@PNG-de-DE.png)

As soon as the target position is reached, "TrackingState" changes from "2" to "3" and the motion job is completed. The TCP now follows the object on the conveyor belt. If blended into the next motion job, the first motion job in the tracked OCS is already completed ("Done" = TRUE) before "TrackingState" changes to "3".

![Phase 3: Synchronize TCP to tracked OCS](images/158927005579_DV_resource.Stream@PNG-de-DE.png)

##### Phase 4: Move TCP within the OCS

In phase 4 you move the kinematics within the OCS, e.g. to grab or process the object. In phase 4, the TCP always follows the tracked OCS.

Select one of the following Motion Control instructions:

- "MC_MoveLinearAbsolute"
- "MC_MoveLinearRelative"
- "MC_MoveCircularAbsolute"
- "MC_MoveCircularRelative"

"TrackingState" remains at "3".

![Phase 4: Move TCP within the OCS](images/158927023499_DV_resource.Stream@PNG-de-DE.png)

The figure shows three kinematics motions at different times.

- **t1:** The TCP is moved with the instruction "MC_MoveLinearAbsolute" in the tracked OCS1 downward in z direction toward the object.
- **t2:** The object is gripped. The TCP continues to move with the tracked OCS1.
- **t3:** The TCP is moved upwards in z direction with the instruction "MC_MoveLinearAbsolute" in the tracked OCS1, in order to lift the object from the conveyor belt. The TCP continues to be tracked with the OCS1.

##### Phase 5: Desynchronize TCP from the OCS

With a Motion Control instruction "MC_MoveLinearAbsolute" or "MC_MoveCircularAbsolute" in the WCS or a non-tracked OCS, the TCP is desynchronized from the OCS and no longer follows the motion of the conveyor belt.

"TrackingState" changes with the start of the job from "3" to "4".

![Phase 5: Desynchronize TCP from the OCS](images/158927028619_DV_resource.Stream@PNG-de-DE.png)

"TrackingState" changes with the end of the job from "4" to "0". The OCS is not tracked with the object position anymore.

#### Behavior of the "TrackingState" tag (S7-1500T)

The tag "&lt;TO&gt;.StatusConveyor[1..3].TrackingState" indicates the status of conveyor tracking.

| Tag | Description |  |
| --- | --- | --- |
| &lt;TO&gt;.StatusConveyor[1..3].TrackingState | Conveyor tracking status |  |
| 0 | OCS not assigned  The OCS is not assigned to a leading-value-capable technology object. |  |
| 1 | OCS assigned  The Motion Control instruction "MC_TrackConveyorBelt" is finished and the OCS is assigned to a leading-value-capable technology object. The first path motion job in the tracked OCS can be sent. |  |
| 2 | TCP synchronizes to OCS  The OCS is assigned to a leading-value-capable technology object. The first path motion job in the tracked OCS is active. |  |
| 3 | TCP follows OCS  The OCS is assigned to a leading-value-capable technology object.   The first path motion job in the tracked OCS is completed. The kinematics has reached the position programmed in the path motion job. The kinematics follows the motion of the OCS. |  |
| 4 | TCP desynchronizes from OCS  The motion of the kinematics in the tracked OCS is ended by a motion job in the WCS or a non-tracked OCS. When the motion job is completed, the "TrackingState" changes to 0 and the OCS is not tracked with the object position anymore. |  |

The following overview shows how the value of "TrackingState" changes when a motion control instruction is issued:

| Phase | Motion control instruction | Status of the instruction | "TrackingState" |
| --- | --- | --- | --- |
| 1 | Position acquisition, for example "MC_MeasuringInput" |  | 0 |
| 2 | "MC_TrackConveyorBelt" | Done = False | 0 |
| Done = False → True | 0 → 1 |  |  |
| 3 | - "MC_MoveLinearAbsolute" - "MC_MoveCircularAbsolute"  Reference system: Currently tracked OCS | Active = False,  Done = False | 1 |
| Active = False → True,  Done = False | 1 → 2 |  |  |
| Active = True → False, Done = False → True | 2 → 3 |  |  |
| 4 | - "MC_MoveLinearAbsolute" - "MC_MoveLinearRelative" - "MC_MoveCircularAbsolute" - "MC_MoveCircularRelative"  Reference system: Currently tracked OCS | Active = False,  Done = False | 3 |
| Active = False → True,  Done = False | 3 |  |  |
| Active = True → False, Done = False → True | 3 |  |  |
| 5 | - "MC_MoveLinearAbsolute" - "MC_MoveCircularAbsolute"  Reference system: WCS or non-tracked OCS | Busy = False, Done = False | 3 |
| Busy = False → True, Done = False | 3 → 4 |  |  |
| Busy = True → False, Done = False → True | 4 → 0 |  |  |

Possible jobs to define the OCS depending on "TrackingState".

| Motion control instruction | "TrackingState" | Result with active job |
| --- | --- | --- |
| "MC_SetOcsFrame" | 0, 4 | The OCS is redefined. |
| 1, 2, 3 | - The OCS is not redefined. - The OCS is no longer tracked with the conveyor belt. - All kinematics motions are stopped. Please note the following information in this regard. |  |
| "MC_TrackConveyorBelt" | 0, 1, 4 | The OCS is tracked with the defined conveyor belt. |
| 2, 3 | - The OCS is no longer tracked with the conveyor belt. - All kinematics motions are stopped. Please note the following information in this regard. |  |

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Product and machine damage**  If the motion of the kinematics with an OCS is not yet finished and the OCS is stopped while the conveyor is running, this leads to an interruption of motion of the kinematics.   Close the coupled motion of the kinematics using the OCS or stop the conveyor belt. |  |

#### Motion between two tracked OCS (S7-1500T)

For many tasks it is necessary to place motion jobs orders in two tracked OCS.

##### Example of a pick-and-place task

A product is to be picked up by conveyor belt 1 and placed in a packaging on conveyor belt 2. The object position on conveyor belt 1 is assigned to OCS1, the object position on conveyor belt 2 is assigned to OCS2. The motion between the conveyor belts takes place via an intermediate point in the WCS.

![Example of a pick-and-place task](images/165904929547_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | Intermediate point in the WCS |

> **Note**
>
> To approach the OCS2 more quickly, smooth the intermediate point in the WCS.

Initial situation: The "TrackingState" of OCS1 is "3". The product has already been gripped and the TCP of the kinematics follows the OCS1.

Program the following Motion Control instructions to move the kinematics from the tracked OCS1 into the tracked OCS2.

1. To assign the OCS2 to the acquired object position, transmit a "MC_TrackConveyorBelt" job.
2. Transmit a "MC_MoveLinearAbsolute" job to an intermediate point in the WCS.
3. Transmit a "MC_MoveLinearAbsolute" job in the tracked OCS2 above the position for the storage.

   The kinematics follows the OCS2.
4. To store the object, transmit a motion command in the OCS2.

#### Dynamics in the phases of the conveyor tracking (S7-1500T)

This section contains information on the following topics:

- [Dynamics in the phases of the conveyor tracking (S7-1500T)](#dynamics-in-the-phases-of-the-conveyor-tracking-s7-1500t-1)
- [Dynamic adaptation during conveyor tracking (S7-1500T)](#dynamic-adaptation-during-conveyor-tracking-s7-1500t)
- [Dynamic reserve (S7-1500T)](#dynamic-reserve-s7-1500t)

##### Dynamics in the phases of the conveyor tracking (S7-1500T)

During synchronization or desynchronization, the dynamics of the kinematics results from the dynamics of the motion job and the dynamics required for synchronization or desynchronization. While traveling in the OCS, the dynamics results from the dynamics of the motion job and the dynamics of the conveyor belt.

The dynamics of the kinematics are additionally increased by a synchronization or desynchronization on conveyors with changing conveyor velocity. Execute the synchronization or desynchronization at a conveyor velocity that is as constant as possible.

The path length of the motion job for synchronization or desynchronization influences the dynamics of the kinematics. To reduce the dynamics of the kinematics during synchronization or desynchronization at a constant conveyor speed, increase the length of the path available for synchronization or desynchronization.

##### Dynamic adaptation during conveyor tracking (S7-1500T)

Use dynamic adaptation at any stage of conveyor tracking. Activate the dynamic adaptation on all motion jobs and parameterize a sufficient dynamic reserve to avoid exceeding the dynamic limits of the kinematics and the kinematics axes.

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Exceeding the dynamic limits despite active dynamic adaptation**  The following factors can cause the dynamic limits to be exceeded despite activated dynamic adaptation:  - Changing conveyor velocity - Synchronizing to the tracked OCS with short distance - Change the range of kinematics motion during conveyor tracking   Exceeding the dynamic limits can cause the following damage:  - Personal injury, for example, caused by products or machine parts coming loose - Machine damage, for example, through overload of the mechanical components   To avoid exceeding the dynamic limits, take the following measures:  - Parameterize a sufficient dynamic reserve.   Note that despite parameterized dynamic reserve, the dynamic limits can be exceeded, e.g. by changing conveyor dynamics or short distances when synchronizing or desynchronizing. - Execute the synchronization or desynchronization at the same conveyor velocity. - Increase the length of the distance available for synchronization or desynchronization. |  |

###### Mode of operation

The following overview shows which parameters influence the dynamics at the time of motion preparation and during motion execution in the tracked OCS.

![Mode of operation](images/168313487243_DV_resource.Stream@PNG-en-US.png)

The path motion of the kinematics is calculated in advance in the MC_LookAhead organization block. The following parameters are taken into account at the time of motion preparation ①:

- Dynamics specification on the motion job
- Velocity of the conveyor belt
- Dynamic limits of the Kinematics motion "&lt;TO&gt;.DynamicLimits.Path"
- Dynamic limits of the orientation motion "&lt;TO&gt;.DynamicLimits.Orientation"
- Dynamic limits of the kinematics axes "&lt;TO&gt;.DynamicLimits"

The dynamic limits take into account velocity, acceleration and deceleration. The maximum permissible jerk is not taken into account.

The following changes, which occur during motion in the tracked OCS ② and which were not taken into account at the time of motion preparation, affect the dynamics of the kinematics and the kinematics axes:

| Changes | Effect |
| --- | --- |
| Changing conveyor dynamics | If the conveyor dynamics change after the motion preparation time, the dynamics of the kinematics motion in the x direction of the tracked OCS also changes. |
| Change in the range of kinematics motion | Due to the motion of the tracked OCS, the kinematics motion takes place in a different area than for motion preparation. Due to the changed area, the dynamics of individual kinematics axes can be higher than at the time of motion preparation. |

Depending on the path length of the motion job and the conveyor dynamics, a dynamic is superimposed to or from the tracked OCS during synchronization or desynchronization.

###### Enable dynamic adaptation

Activate the [Dynamic adaptation](#dynamic-adaptation-s7-1500t) by setting the value for "DynamicAdaption" to "1" or "2" on the motion job. Alternatively, configure the default setting on the technology object by setting the "&lt;TO&gt;.DynamicDefaults.DynamicAdaption" variable to "1" or "2" and specifying the value "-1" on the motion job.

##### Dynamic reserve (S7-1500T)

To maintain the dynamic limits of the kinematics and the kinematics axes when changing the conveyor dynamics and the working range, use the dynamic reserve "&lt;TO&gt;.Conveyor.DynamicReserve[1..1]".

In order not to exceed the dynamic limits in case of dynamic changes, the motion preparation in x direction of the tracked OCS is calculated with reduced dynamic limits of the kinematics motion, the orientation motion and the kinematics axes. The dynamic limits are reduced by the dynamic reserve during motion preparation. This means that the dynamic reserve is available for dynamic changes during motion, e.g. when the speed of the conveyor is increased.

Parameterize the dynamic reserve according to the expected dynamics change. For strongly fluctuating conveyor dynamics, parameterize a higher dynamic reserve. At constant conveyor velocity, you can parameterize a low dynamic reserve.

![Figure](images/164741998347_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | Reduced dynamic limit for motion preparation |
| ② | Dynamic reserve for dynamics changes |
| ③ | Dynamic limit |

###### Example

The following example shows the dynamic behavior on a "TO_Kin_1" kinematics of the type "Cartesian Portal 3D" (without orientation) with different scenarios.

![Example](images/164707540747_DV_resource.Stream@PNG-de-DE.png)

The kinematics axis A1 is aligned along the conveyor belt and thus travels in the x direction of the tracked OCS. In the example, the velocity of axis A1 and thus the path velocity in the x direction of the tracked OCS is limited by the dynamic adaptation. The dynamic reserve is parameterized with 30% (default setting).

The conveyor travels at a constant velocity of 20.0 mm/s. The OCS1 is tracked with the already recorded product with an "MC_TrackConveyorBelt" instruction.

Before the kinematics synchronizes to the first OCS, 3 linear motion jobs are transmitted.

- B1: Synchronization of the kinematics in x direction of the tracked OCS
- B2: Motion in z direction within the tracked OCS
- B3: Motion in the x direction within the tracked OCS to the next product.

![Example](images/165574547467_DV_resource.Stream@PNG-de-DE.png)

The motions are not blended. A path velocity of 200 mm/s is specified on all 3 jobs.

The 3 motion jobs are processed together in the job sequence.

The dynamic limits of the kinematics axes A1, A2 and A3 are parameterized as follows:

- &lt;A1...A3&gt;.DynamicLimits.Velocity := 100.0
- &lt;A1...A3&gt;.DynamicsLimits.MaxVelocity := 100.0
- &lt;A1...A3&gt;.DynamicLimits.MaxAcceleration := 2000.0
- &lt;A1...A3&gt;.DynamicLimits.MaxDeceleration := 2000.0

The dynamic limits of the "TO_Kin_1" kinematics are parameterized as follows:

- &lt;TO_Kin_1&gt;.DynamicLimits.Path.Velocity := 100.0
- &lt;TO_Kin_1&gt;.DynamicLimits.Path.Acceleration := 1000.0
- &lt;TO_Kin_1&gt;.DynamicLimits.Path.Deceleration := 1000.0

**Conveyor tracking with dynamic adaptation without segmentation of the path**

![Example](images/165436528011_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ![Example](images/165475665675_DV_resource.Stream@PNG-de-DE.png) | **Scenario A** |
| ① | Due to the activated dynamic adaptation, the velocity limit of 100 mm/s and the dynamic reserve of 30 % are effective. The axis velocity of the A1 axis is limited to a maximum of 70 mm/s. The axis velocity is made up of the path velocity and the conveyor velocity. Thus, the resulting path velocity of the motion job during motion preparation is 50 mm/s. |
| ② | After the kinematics have been synchronized, the kinematics move downward at 100 mm/s in z direction. During motion preparation, the velocity is limited to 100 mm/s. The dynamic reserve is not effective because the kinematics motion is not executed in the x direction of the tracked OCS. |
| ③ | As the motion takes place while motion is coupled in the OCS, the path velocity within the tracked OCS is limited to 50 mm/s. The resulting axis velocity is 70 mm/s, as the conveyor velocity of 20 mm/s is superimposed on the path velocity. The dynamic reserve of 30 mm/s to the dynamic limit of 100 mm/s is therefore available. |
| ![Example](images/165477512843_DV_resource.Stream@PNG-de-DE.png) | **Scenario B** |
| ① | The conveyor velocity increases to 40 mm/s during synchronization. The axis velocity of axis A1 during synchronization is thus higher, but remains within the dynamic limits. |
| ② | After the kinematics have been synchronized, the kinematics move downward at 100 mm/s in z direction. During motion preparation, the velocity is limited to 100 mm/s. The dynamic reserve is not effective because the kinematics motion is not executed in the x direction of the tracked OCS. |
| ③ | As in scenario A, a resulting axis velocity of 70 mm/s was calculated in the motion preparation. As the conveyor velocity increases by 20 mm/s after motion preparation, the axis velocity of axis A1 increases to approx. 90 mm/s. |

**Conveyor tracking without dynamic adaptation**

![Example](images/164707583627_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ![Example](images/165475665675_DV_resource.Stream@PNG-de-DE.png) | **Scenario A** |
| ① | The dynamic adaptation is not used and the axis velocity of axis A1 is not reduced to the velocity limit of 100 mm/s during synchronization. |
| ② | After the kinematics have been synchronized, the kinematics move downward at 100 mm/s in z direction. During motion preparation, the axis velocity is limited to 100 mm/s. As the kinematics motion only runs in the z direction of the tracked OCS, the kinematics travels with a path velocity of 100 mm/s within the tracked OCS. |
| ③ | Without dynamic adaptation, the axis velocity is not limited within the tracked OCS. |
|  |  |
| ![Example](images/165477512843_DV_resource.Stream@PNG-de-DE.png) | **Scenario B** |
| ① | The conveyor velocity increases to 40 mm/s after motion preparation. The axis velocity exceeds the dynamic limits even more in this scenario when synchronizing. |
| ② | After the kinematics have been synchronized, the kinematics move downward at 100 mm/s in z direction. During motion preparation, the axis velocity is limited to 100 mm/s. As the kinematics motion only runs in the z direction of the tracked OCS, the kinematics travels with a path velocity of 100 mm/s within the tracked OCS. |
| ③ | The axis velocity exceeds the velocity limit higher than in scenario A, because the conveyor velocity has increased after motion preparation. |

#### Stopping behavior with "MC_GroupStop" and "MC_GroupInterrupt"  (S7-1500T)

##### "TrackingState" = "2" and "4"

An "MC_GroupStop" or "MC_GroupInterrupt" instruction completes the tracking of the OCS with "TrackingState" = "2" and "4". Alarm 811 is triggered and all kinematics motions are stopped.

##### "TrackingState" = "3"

The path motion within the coupled OCS is stopped with an "MC_GroupInterrupt" job or "MC_GroupStop" job. The status of the conveyor tracking "&lt;TO&gt;.StatusConveyor[1..3].TrackingState" = "3" is retained. The kinematics continues to follow the OCS.

An "MC_GroupContinue" job can be used to continue a motion that was interrupted with an "MC_GroupInterrupt" job.

The job sequence is emptied after an executed "MC_GroupStop" job. A new path motion is restarted with a new job in the tracked OCS.

To end all kinematics motions, follow these steps:

1. To stop the path motion within the tracked OCS, transmit an "MC_GroupStop" job.
2. If required, move the kinematics upward, e.g. with an "MC_MoveLinearRelative" job within the tracked OCS, to prevent mechanical collisions.   
   If possible, you can alternatively stop the conveyor with a "MC_Halt" job.
3. To stop moving the TCP on the conveyor belt, move the kinematics, e.g. with an "MC_MoveLinearAbsolute" job to a position in WCS or in non-tracked OCS, e.g. to a waiting position.

#### Blending behavior  (S7-1500T)

During conveyor tracking, blending between the following motions is possible:

| "TrackingState" | Description |
| --- | --- |
| 1 → 2 | In a motion job for moving into the first position in the tracked OCS |
| 3 → 3 | In a motion job for moving into the first position in the tracked OCS |
| 4 → 0 | From a motion job that desynchronizes the TCP from the tracked OCS, in the following motion job (see section "Motion between two tracked OCS") |
| **As of technology version V8.0 in addition** |  |
| 2 → 3 | From a motion job that synchronizes the TCP with the tracked OCS to the subsequent motion job in the tracked OCS |
| 3 → 4 | In a motion job that desynchronizes the TCP from the tracked OCS |

---

**See also**

[Motion between two tracked OCS (S7-1500T)](#motion-between-two-tracked-ocs-s7-1500t)

### Set kinematics to simulation mode (S7-1500T)

This section contains information on the following topics:

- [Brief description of setting kinematics to simulation mode (S7-1500T)](#brief-description-of-setting-kinematics-to-simulation-mode-s7-1500t)
- [Tags: Kinematics to simulation (S7-1500T)](#tags-kinematics-to-simulation-s7-1500t)

#### Brief description of setting kinematics to simulation mode (S7-1500T)

When disabling the kinematics axes or in case of single-axis motions, a kinematics motion is canceled, and the job sequence is cleared. By setting the kinematics to simulation mode, you will keep the motion processing at the kinematics technology object active. The jobs in the job sequence are retained.

With the ["MC_KinematicsMotionSimulation"](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_kinematicsmotionsimulation-v8-s7-1500t) Motion Control instruction, you start or end the simulation mode for a kinematics technology object. In simulation mode, the setpoints of the kinematics are still being calculated. Setpoint changes through motion jobs at the kinematics technology object are no longer taken into consideration at the kinematics axes and are no longer being forwarded to the drives.

When the simulation is started with "Execute" = TRUE and "Mode" = 1, the position setpoints of the kinematics axes are kept constant. The velocity setpoint and the setpoint acceleration of the kinematics axes are immediately set to zero.

> **Note**
>
> **Setpoint jump**
>
> When you activate the simulation during a kinematics motion, the kinematics axes will decelerate immediately with a jump of the velocity setpoint.
>
> To stop the kinematics axes in a controlled manner, interrupt the kinematics motion with a "MC_GroupInterrupt" job before you activate the simulation. Once you have ended the simulation, you can continue the kinematics motion with a "MC_GroupContinue" job.

While the kinematics technology object is in simulation, you can move, disable and enable the kinematics axes again using single-axis jobs, without the motion processing being canceled at the kinematics technology object. The same is true for technology alarms pending at the kinematics axes during the kinematics simulation.

So that the simulation mode can be exited with "Execute" = TRUE and "Mode" = 0 , each of the kinematics axes must be at position "&lt;TO&gt;.AxesData.A[1..6].Position". A modulo axis must also be in the same modulo cycle as at the start time of the simulation.

Before you exit the simulation, move each of the kinematics axes using single-axis jobs to position "&lt;TO&gt;.AxesData.A[1..6].Position".

When the simulation is exited with "Execute" = TRUE and "Mode" = 0, the kinematics motion is continued. The setpoints take effect directly on the kinematics axes.

##### Example

The following procedure shows an example of how you can disable the kinematics axes using the kinematics simulation and enable them again without canceling the motion processing at the kinematics technology object.

**Interrupting the kinematics motion and disabling the kinematics axes**

1. Interrupt the kinematics motion with a "MC_GroupInterrupt" job.

   The kinematics axes are stopped.
2. Set the kinematics to simulation with a "MC_KinematicsMotionSimulation" job with "Execute" = TRUE and "Mode" = 1.
3. If necessary, move the individual kinematics axes using single-axis jobs.
4. Disable the individual kinematics axes with a "MC_Power" job.

   The jobs in the job sequence are retained.

**Enabling the kinematics axes and continuing the kinematics motion**

1. Enable the individual kinematics axes again with a "MC_Power" job.
2. Move the individual kinematics axes using single-axis jobs to positions "&lt;TO&gt;.AxesData.A[1..6].Position". These position values match the position values after stopping the kinematics motion. With a modulo axis, additionally ensure that the axis is in the same modulo cycle as at the start time of the simulation.
3. Exit the kinematics simulation with a "MC_KinematicsMotionSimulation" job with "Execute" = TRUE and "Mode" = 0.
4. Continue the kinematics motion with a "MC_GroupContinue" job.

#### Tags: Kinematics to simulation (S7-1500T)

The following tags of the technology object are relevant for simulation:

| Status indicators |  |  |
| --- | --- | --- |
| Tag | Description |  |
| &lt;TO&gt;.StatusWord.X19 (InSimulation) | Kinematics simulation |  |
| FALSE | Not simulated |  |
| TRUE | Simulated |  |
| &lt;TO&gt;.AxesData.A[1..6].Position | Position setpoints of the kinematics motion for the kinematics axes 1 to 6 |  |
| &lt;TO&gt;.AxesData.A[1..6].Velocity | Velocity setpoints of the kinematics motion for the kinematics axes 1 to 6 |  |
| &lt;TO&gt;.AxesData.A[1..6].Acceleration | Acceleration setpoints of the kinematics motion for the kinematics axes 1 to 6 |  |

## 3D visualization (S7-1500T)

This section contains information on the following topics:

- [Brief description 3D visualization (S7-1500T)](#brief-description-3d-visualization-s7-1500t)
- [Structure of the 3D visualization (S7-1500T)](#structure-of-the-3d-visualization-s7-1500t)
- [Working with the 3D display (S7-1500T)](#working-with-the-3d-display-s7-1500t)
- [Operating the zone display (S7-1500T)](#operating-the-zone-display-s7-1500t)
- [Operating the directional pad (S7-1500T)](#operating-the-directional-pad-s7-1500t)
- [Monitoring and comparing position values (S7-1500T)](#monitoring-and-comparing-position-values-s7-1500t)

### Brief description 3D visualization (S7-1500T)

The 3D visualization supports you visually in the configuration, commissioning and diagnostics of the kinematics technology object with the following components:

- [3D display](#structure-of-the-3d-visualization-s7-1500t)
- [Diagnostics window](#structure-of-the-diagnostics-s7-1500t)
- [Toolbar](#working-with-the-3d-display-s7-1500t)
- [Directional pad](#operating-the-directional-pad-s7-1500t)
- [Kinematics control panel](#commissioning-s7-1500t)

#### Online view

In the online view, the kinematics, zones and coordinate systems are updated based on the online values. The refresh rate depends on multiple factors, for example, on the performance of the programming device and the CPU, the communication times, etc. The 3D visualization, therefore, does not show the behavior of the real machine. Note the behavior of the real machine when using calibration, diagnostics and the kinematics trace.

### Structure of the 3D visualization (S7-1500T)

The 3D visualization has a function-oriented structure. Different functions are available in the 3D visualization depending on the configuration window.

The following table gives you an overview of the configuration windows with a 3D visualization and the available functions:

| Configuration window | Structure |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| 3D display | Toolbar | Visualization of the positions | Directional pad | Kinematics control panel with "Control panel status" diagnostics window. |  |
| Zones configuration window | ✓ | ✓ | – | – | – |
| Diagnostics | ✓ | ✓ | ✓ | – | – |
| Kinematics trace | ✓ | ✓ | ✓ | – | – |
| Calibration | ✓ | ✓ | ✓ | ✓ | ✓ |
| Commissioning | ✓ | ✓ | ✓ | ✓ | ✓ |

#### 3D display

The following values and information are visualized in the 3D display:

| Configuration window | Graphically displayed values and information |
| --- | --- |
| **Zones** | - Zones - Position KCS in WCS |
| **Diagnostics** | - Kinematics and tool center point (TCP) - Zones |
| **Kinematics trace** | - Kinematics and tool center point (TCP) - Traces   - Tool center point (TCP)   - Kinematics   - OCS frames |
| **Calibration** | - Kinematics and tool center point (TCP) - Zones   - Calibrated workspace zones   - Configured kinematics zones - Calibrated object coordinate systems - Values for the calibration    - Configured points and angles   - Guide lines   - Offset of the OCS from the origin   - Current position of the TCP   - Graphically highlighted active calibration point |
| **Commissioning** | - Kinematics and tool center point (TCP) - Zones |

> **Note**
>
> You set the dimensions for the representation of the kinematics in the 3D display under "Technology object &gt; Configuration &gt; Geometry".

### Working with the 3D display (S7-1500T)

A description is provided below of how to adapt the view of the coordinate system with mapped kinematics in the 3D view using the toolbar or the mouse.

#### Customizing the appearance of the 3D display

You can adapt the display in the 3D view as follows:

1. To hide or show the coordinate system in the display, click the ![Customizing the appearance of the 3D display](images/134675215115_DV_resource.Stream@PNG-de-DE.png) symbol in the toolbar.
2. To adjust the brightness of the 3D display, select a preset brightness level via the ![Customizing the appearance of the 3D display](images/155270385675_DV_resource.Stream@PNG-de-DE.png) selection box.

   Alternatively, change the brightness using the ![Customizing the appearance of the 3D display](images/134696219147_DV_resource.Stream@PNG-de-DE.png) (darker) button or the ![Customizing the appearance of the 3D display](images/134696406027_DV_resource.Stream@PNG-de-DE.png) (brighter) button.

#### Customizing the display of the kinematics and the coordinate system

| 1. In the ![Customizing the display of the kinematics and the coordinate system](images/155269088011_DV_resource.Stream@PNG-de-DE.png) selection box, select a coordinate system that is displayed in the 3D display.     In addition, the selected coordinate system is displayed in the "Positions" window. If you select the kinematics coordinate system (KCS), the WCS is displayed in the "Positions" window.    See also [Monitoring and comparing position values](#monitoring-and-comparing-position-values-s7-1500t).    You can select the FCS or TCS in the configuration of the kinematics zones. 2. To change the display of the kinematics, click the ![Customizing the display of the kinematics and the coordinate system](images/134694181387_DV_resource.Stream@PNG-de-DE.png) button. If you click on the arrow, the other display options of the kinematics are shown and you can directly select the desired display:       | Button | Description |    | --- | --- |    | ![Customizing the display of the kinematics and the coordinate system](images/134694181387_DV_resource.Stream@PNG-de-DE.png) | Shows the kinematics. |    | ![Customizing the display of the kinematics and the coordinate system](images/134696211467_DV_resource.Stream@PNG-de-DE.png) | Shows a simplified view of the kinematics. |    | ![Customizing the display of the kinematics and the coordinate system](images/134697402507_DV_resource.Stream@PNG-de-DE.png) | Hides the view of the kinematics. | 3. To change the tool, select an already configured tool in the ![Customizing the display of the kinematics and the coordinate system](images/156425280395_DV_resource.Stream@PNG-en-US.png) selection box.    This selection box is available in the configuration of the kinematics zones and in the calibration. 4. To display the TCS, click the ![Customizing the display of the kinematics and the coordinate system](images/168648312715_DV_resource.Stream@PNG-de-DE.png) button. With more clicks on the button, or if you click the arrow, the following buttons are displayed and you can display or hide the TCS or the TCP:       | Button | Description |    | --- | --- |    | ![Customizing the display of the kinematics and the coordinate system](images/168642442891_DV_resource.Stream@PNG-de-DE.png) | Shows the TCS |    | ![Customizing the display of the kinematics and the coordinate system](images/134696754827_DV_resource.Stream@PNG-de-DE.png) | Shows the TCP |    | ![Customizing the display of the kinematics and the coordinate system](images/168646854667_DV_resource.Stream@PNG-de-DE.png) | Hides the TCS selected via the ![Customizing the display of the kinematics and the coordinate system](images/168642442891_DV_resource.Stream@PNG-de-DE.png) button or the TCP selected via the ![Customizing the display of the kinematics and the coordinate system](images/134696754827_DV_resource.Stream@PNG-de-DE.png) button. |     During calibration, the TCS is already shown in the online view and you can change the display using the ![Customizing the display of the kinematics and the coordinate system](images/168671463691_DV_resource.Stream@PNG-de-DE.png) button. 5. To switch the focus of the view to the TCS or TCP, click the ![Customizing the display of the kinematics and the coordinate system](images/134696747147_DV_resource.Stream@PNG-de-DE.png) button.    During the path motion of the kinematics, the focus is always on the TCS or the TCP. In standstill, the view can be moved or rotated using the mouse. |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

#### Change screen section

| 1. To switch the view between 2D or 3D display, use the following buttons:    - To use the 2D display, click the ![Change screen section](images/134675222795_DV_resource.Stream@PNG-de-DE.png) button.    - To use the 3D display, click the ![Change screen section](images/134675281675_DV_resource.Stream@PNG-de-DE.png) button. 2. To change the plane view of the selected coordinate system, use the following buttons:       | Button/mouse | Description |    | --- | --- |    | ![Change screen section](images/134690478091_DV_resource.Stream@PNG-de-DE.png) | Show xz plane |    | ![Change screen section](images/134690027531_DV_resource.Stream@PNG-de-DE.png) | Show the xz plane rotated around the z axis |    | ![Change screen section](images/134690293771_DV_resource.Stream@PNG-de-DE.png) | Show yz plane |    | ![Change screen section](images/134690301451_DV_resource.Stream@PNG-de-DE.png) | Show the yz plane rotated around the z axis |    | ![Change screen section](images/134689948171_DV_resource.Stream@PNG-de-DE.png) | Show xy plane |    | ![Change screen section](images/134689955851_DV_resource.Stream@PNG-de-DE.png) | Show the xy plane rotated around the x axis | 3. To rotate the view as desired, hold down the left mouse button and move the mouse in the desired direction. 4. To center the view and display the entire kinematics, click the ![Change screen section](images/134672545035_DV_resource.Stream@PNG-de-DE.png) icon in the toolbar. 5. Use the mouse wheel to zoom in and out of the display of the kinematics continuously. 6. To move the kinematics in the view, hold down the right mouse button and move the mouse in the desired direction. |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

### Operating the zone display (S7-1500T)

You show or hide all active and inactive zones with the ![Figure](images/134699079307_DV_resource.Stream@PNG-de-DE.png) button.

In addition, with the active icon ![Figure](images/134699079307_DV_resource.Stream@PNG-de-DE.png), you can show and hide all active and inactive workspace zones individually with the ![Figure](images/134699086987_DV_resource.Stream@PNG-de-DE.png) icon in the following areas:

- Diagnostics &gt; "Status zones" window
- Calibration &gt; Object coordinate systems / Workspace zones &gt; "Zone display" window

#### Zone display in calibration

When you click on the ![Zone display in calibration](images/134636636043_DV_resource.Stream@PNG-de-DE.png) icon, values of the workspace zones and the kinematics zones at the current point in time are read back from the CPU. When you click the ![Zone display in calibration](images/134692367371_DV_resource.Stream@PNG-de-DE.png) icon in the "Number" column, 2 additional rows are displayed. The additional rows contain the following values:

- ![Zone display in calibration](images/134692378763_DV_resource.Stream@PNG-de-DE.png) Start values of the CPU
- ![Zone display in calibration](images/134692757643_DV_resource.Stream@PNG-de-DE.png) Start values in project

  You can edit these values. If you want to apply the change, load the changes from the project into the device.

If you have performed an offline recalibration of a workspace zone calibrated online, both zones are displayed in the graphic view. Load the changes from the project to the device. The display is updated and the result of the last calibration is displayed.

### Operating the directional pad (S7-1500T)

The directional pad offers the following functions:

- In offline mode: Move the tool center point (TCP) in the 3D view
- In online mode: Specify target position in "Jog to target position" mode in the WCS or OCS

#### Moving the tool center point (TCP)

During calibration, you can move the tool center point (TCP) in the 3D view in offline mode using the directional pad.

> **Note**
>
> **Singularity**
>
> When you move the kinematics into a [singularity](#singularities-s7-1500t), a message is output in the graphic display and you can no longer move the kinematics using the directional pad. To be able to move the kinematics once again, click on "Reset kinematics" in the message.

1. To move the TCP to a position, click on the positive or negative x, y or z direction on the directional pad.

   ![Moving the tool center point (TCP)](images/155920687883_DV_resource.Stream@PNG-de-DE.png)

   In the 3D view, you can see the motion of the kinematics model and the TCP.

   The coordinates of the TCP are displayed in the Positions window.
2. To change the orientation of the TCP, click "ROT" or the intersection of the axes.

   Instead of the directional pad, arrows for the orientation motion are displayed.
3. Click the arrow to rotate in a positive or negative direction.

   ![Moving the tool center point (TCP)](images/155922829707_DV_resource.Stream@PNG-de-DE.png)

   The Cartesian coordinates and the Cartesian orientations in space are displayed in the "Positions" window.

   If you have shown a kinematics zone, you will see the rotation of the kinematics zone in the 3D view.
4. To move the TCP again, click "LIN".

   The directional pad is displayed.

#### Specify target position

In online mode, you can use the directional pad to specify the target position in the WCS or OCS in "Jog to target position" mode. This function is available during commissioning and calibration.

The target position in the selected coordinate system is applied and you can jog the kinematics to the target position with the kinematics control panel.

The operation of the kinematics control panel in "Jog to target position" mode is described in the section "[Jogging the kinematics](#jogging-the-kinematics-s7-1500t)".

### Monitoring and comparing position values (S7-1500T)

You monitor and compare position information with the following 3D visualization functions:

- "Positions" diagnostics window
- Position values in the graphically displayed trace

#### Operating the "Positions" diagnostics window

The "Positions" window provides the following functions:

- Monitor position values, e.g. during diagnostics
- Check approached points of the kinematics during calibration with the current position
- Compare position values in two different coordinate systems, e.g. during calibration

The values in the "Positions" window are displayed as follows:

- During commissioning, in the diagnostics and in the kinematics trace, the positions are displayed in online mode.
- The positions in offline and online mode are displayed in the calibration.

#### Selecting a reference coordinate system for recording in the kinematics trace

The selection of the coordinate systems in the toolbar and in the "Positions" window depends on the signals you have activated under "Technology object &gt; Kinematics trace &gt; Configuration &gt; Traces". The following table shows the available coordinate systems depending on the active signals:

| Active signals | Coordinate system 1 | Coordinate system 2 |
| --- | --- | --- |
| TCP and kinematics | World coordinate system (WCS), kinematics coordinate system (KCS) | Machine coordinate system (MCS), WCS, JCS |
| TCP | WCS, KCS, | WCS |
| TCP, OCS1 | WCS, KCS, OCS1 | WCS |
| TCP, OCS1, OCS2 | WCS, KCS, OCS1, OCS2 | WCS |
| TCP, OCS1, OCS2, OCS3 | WCS, KCS, OCS1, OCS2, OCS3 | WCS |

If you activate another signal or the "Monitoring on/off" ![Selecting a reference coordinate system for recording in the kinematics trace](images/163741917451_DV_resource.Stream@PNG-de-DE.png) function, the available coordinate systems are updated.

#### Comparing position values

1. Select a coordinate system in the toolbar. The selected coordinate system is displayed in the left field of the "Positions" window.

   When you select the kinematics coordinate system (KCS) in the toolbar, the WCS is displayed in the "Positions" window.
2. Select another coordinate system in the "Positions" window in the right drop-down list.
3. The actual position of the active tool in the selected reference coordinate system is displayed.

The meaning of the position information is described in the table in the section "[Positions](#positions-s7-1500t)".

#### Position values in the graphic display

If you position the mouse cursor on one of the traces in the 3D visualization in the kinematics trace, the position values are displayed directly on the trace.

The following values are displayed:

- Measuring point number
- Coordinates x, y, z and A, B, C

The values displayed show the position and rotation in the set coordinate system.

## Commissioning (S7-1500T)

This section contains information on the following topics:

- [Brief description of commissioning (S7-1500T)](#brief-description-of-commissioning-s7-1500t)
- [Control panel status (S7-1500T)](#control-panel-status-s7-1500t)
- [Taking over master control and enabling kinematics (S7-1500T)](#taking-over-master-control-and-enabling-kinematics-s7-1500t)
- [Selecting an active tool (S7-1500T)](#selecting-an-active-tool-s7-1500t)
- [Operator controls for jogging and homing (S7-1500T)](#operator-controls-for-jogging-and-homing-s7-1500t)
- [Setting the home position of a kinematics axis (S7-1500T)](#setting-the-home-position-of-a-kinematics-axis-s7-1500t)
- [Active homing of the kinematics axis (S7-1500T)](#active-homing-of-the-kinematics-axis-s7-1500t)
- [Specifying dynamics in the kinematics control panel (S7-1500T)](#specifying-dynamics-in-the-kinematics-control-panel-s7-1500t)
- [Jogging the kinematics (S7-1500T)](#jogging-the-kinematics-s7-1500t)
- [Disabling kinematics and handing over master control (S7-1500T)](#disabling-kinematics-and-handing-over-master-control-s7-1500t)

### Brief description of commissioning (S7-1500T)

You can find the kinematics control panel under "Technology object &gt; Commissioning". The kinematics control panel enables you to assume master control for a kinematics technology object and control the motions of the kinematics, the individual axes or the individual joints. You can therefore move the kinematics without affecting the user program.

You can find the [dynamics settings](#specifying-dynamics-in-the-kinematics-control-panel-s7-1500t) for commissioning in the Inspector window under "Properties".

[3D visualization](#3d-visualization-s7-1500t) provides visual support for commissioning the kinematics technology object. The status LEDs in the "[Control panel status](#control-panel-status-s7-1500t)" diagnostics window show you whether all kinematics axes are switched on and homed and whether errors are pending at the kinematics or the kinematics axes. You can also show additional [diagnostics windows](#structure-of-the-diagnostics-s7-1500t) via the toolbar.

You can also find the kinematics control panel in the project tree under "Technology object &gt; [Calibrate](#calibration-s7-1500t)". In calibration, you move the real kinematics online via the kinematics control panel in the "Jog" or "Jog to target position" operating modes.

### Control panel status (S7-1500T)

You use the "Control panel status" diagnostics window in "Technology object &gt; Commissioning" in the TIA Portal to monitor the status and error messages of the kinematics and the kinematics axes during commissioning.

The diagnostics function is available in online operation. The "Control panel status" diagnostics window is shown in the graphical display during commissioning. You can show the diagnostics window via the ![Figure](images/155910184715_DV_resource.Stream@PNG-de-DE.png) symbol of the toolbar and move the window to a desired position within the graphic display.

#### Kinematics status

The following table shows the possible statuses of the kinematics:

| Status | Description |
| --- | --- |
| Valid | The transformation values are valid. (&lt;TO&gt;.StatusKinematics.Valid) |
| Error | An error occurred at the technology object.  Error messages are displayed in the Inspector window under "Diagnostics &gt; Alarm display". |

#### Axis status

The following table shows the possible states of the kinematics axes:

| Status | Description |
| --- | --- |
| Enabled | The technology object has been enabled. The axis can be moved with motion jobs. |
| Error | An error occurred at the technology object.  Error messages are displayed in the Inspector window under "Diagnostics &gt; Alarm display". |
| Homed | The technology object is homed. |

### Taking over master control and enabling kinematics (S7-1500T)

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Unexpected axis motions**  During operation with the kinematics control panel, the kinematics can execute unexpected motions (for example, due to incorrect configuration of the drive or technology object). In addition, when a leading axis is moved with the kinematics control panel, any synchronized following axis is also moved.  Therefore, take the following protective measures before operation with the kinematics control panel:  - Ensure that the EMERGENCY OFF switch is within the reach of the operator. - Enable the hardware limit switches. - Enable the software limit switches. - Use blocked zones to prevent mechanical collisions. - Ensure that following error monitoring is enabled. - Make sure that no following axis is coupled to the axis to be moved. - Make sure that the dynamic settings in the kinematics control panel do not violate the dynamic limits of the kinematics axes or process. - Ensure that the kinematics control panel is configured correctly. |  |

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Overrun of the dynamics through singular positions**  Overruns of the dynamics in the vicinity of singular positions can result in the following damage:  - Machine damage through overload of the mechanical components - Personal injury caused by products or machine parts coming loose   To prevent dynamic overruns in the vicinity of singular positions, take the following measures:  - Move the kinematics in the MCS or the JCS. - In the WCS or OCS, avoid the "Jog" mode. The dynamic adaptation in "Jog" mode in the WCS or OCS is not active in the kinematics control panel. The dynamic limits of the kinematics axes are not taken into account during a kinematics motion with the kinematics control panel. - Up to technology version V5: In the WCS or OCS, avoid using the "Jog to target position" mode. The dynamic adaptation in "Jog to target position" mode in the WCS or OCS is not active in the kinematics control panel. The dynamic limits of the kinematics axes are not taken into account during a kinematics motion with the kinematics control panel. - As of technology version V6: Move the kinematics to the "Jog to target position" mode in the WCS or OCS using the kinematics control panel. "Dynamic adaptation without segmentation of the path" is permanently active in the "Jog to target position" mode, and the dynamic limits of the kinematics axes are taken into account. |  |

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Moving leading axes with active synchronous operation**  Any synchronized following axis is moved as well when a leading axis is moved with the kinematics control panel. |  |

#### Requirements

- The kinematics and the kinematics axes are locked in the user program.
- No axis control panel or drive control panel is active for any kinematics axis.
- The kinematics technology object is configured.
- The travel directions of the kinematics axes match the joint travel directions of the kinematics used.

  Use the axis control panel to check whether the travel directions of the kinematics axes match the joint travel directions of the kinematics used. The joint travel direction can be found in the Manufacturer descriptions. Invert the drive and encoder directions in the kinematics axis if the directions are inverse.
- The joint travel directions of the kinematics used correspond to the travel directions defined by Siemens from the kinematics type.

  Check whether the joint travel directions of the kinematics used match the travel directions defined by Siemens from the [Kinematics type](#kinematics-types-s7-1500t). If the directions are inverse, then invert the joint direction at the associated joint in the Kinematics technology object.
- The kinematics axes are homed.

  The joint zero position corresponds to the position 0.0 of the kinematics axis. For mechanical axis couplings, first home the coupling axes.
- Possible joint offsets are defined.

  Check whether the joint zero position of the kinematics deviates from the joint zero position of the kinematics type defined by Siemens. In this case, you must define a joint offset. If the offset cannot be determined from data sheets, then you can determine it practically. To do this, jog the joint in the zero position defined by Siemens and then accept the position of the joint as offset.
- All kinematics axes are ready to start.
- The CPU must be in the RUN mode.
- No alarm is active on the kinematics technology object.

#### Procedure

1. Click the "Activate" button.
2. Read the warning.
3. Set the sign-of-life monitoring time to a value between 1000 and 60 000 ms.

#### Setting the sign-of-life monitoring time

The kinematics control panel requires a direct connection from its TIA Portal to the controller, which is monitored cyclically. If there is no sign of life from the PG/PC within the monitoring time, master control is handed over for safety reasons.

| Monitoring time | Effect |
| --- | --- |
| Too low | Master control is often handed over because the monitoring time is exceeded. The kinematics stops with maximum deceleration because the communication time between TIA Portal and CPU is longer than the configured monitoring time. |
| Appropriate | The monitoring time is not exceeded. The kinematics is stopped in time if the online connection is lost or the sign-of-life monitoring is exceeded. Recommendation: 1000 ms to 2000 ms |
| Too high | The kinematics continues to move with the last setpoints of the kinematics control panel, although the connection between the TIA Portal and the CPU has been interrupted or the communication time between the TIA Portal and the CPU is too long. The kinematics is not stopped on time because the monitoring time is still running. |

#### Result

- An online connection to the CPU is established and the kinematics control panel takes master control of the technology object.
- The kinematics can now only be moved with this kinematics control panel. The user program has no influence on the functions of the technology object. Motion Control jobs from the user program to the technology object are rejected with error ("ErrorID" = 16#8012: Kinematics control panel enabled).
- Access to the kinematics and the kinematics axes is blocked by another instance of the TIA Portal.

#### Enabling the kinematics

1. Click the "Enable" button to enable interconnected axes of the selected kinematics technology object.   
   Result: The kinematics or the kinematics axes can now be moved or actively homed with the kinematics control panel.
2. Use the status LEDs in the "Control panel status" diagnostics window to check whether all kinematics axes are switched on and homed and whether errors are pending. Use the alarm display (Inspector window &gt; "Diagnostics &gt; Alarm display") in the TIA Portal to display pending causes of the error.

#### Behavior during operation of the kinematics control panel

In the following situation, the kinematics control panel retains master control and the kinematics remain in motion:

- The kinematics control panel is embedded in the TIA Portal, and you switch to another window, for example, to the kinematics trace. Use the "Split editor area" option to use the kinematics control panel and the kinematics trace at the same time.

In the following situation, the kinematics control panel retains master control but stops the kinematics with maximum deceleration and revokes the enabling of the technology objects:

- The kinematics control panel is detached in the TIA Portal, and you switch to another window within the TIA Portal, for example, to the kinematics trace.
- You switch to a window outside the TIA Portal.

In the following situations, the kinematics is stopped or the axes are stopped with maximum deceleration and the kinematics control panel returns the master control to the user program:

- The communication time between TIA Portal and CPU is longer than the configured monitoring time. In the banner above the toolbar, the message is displayed that the master control has been handed over because the monitoring time has been exceeded.   
  Adapt the time for the sign-of-life monitoring in the warning.
- The online connection to the CPU is impaired by a communication load that is too high. The following message is entered in the alarm display log: "Commissioning error. Sign-of-life failure between controller and TIA Portal". Adapt the time for the sign-of-life monitoring in the warning.
- A dialog (e.g. "Save as") or another window within the TIA Portal covers the kinematics control panel.

### Selecting an active tool (S7-1500T)

If you use kinematics with multiple tools, you can select the different tools in the kinematics control panel. This allows you to define the position of the TCP in the flange coordinate system (FCS) in relation to this tool. In the real kinematics, the tool is not changed by the changed selection.

#### Requirement

Kinematics is enabled in the kinematics control panel.

#### Procedure

1. In the "Active tool" drop-down list, select the tool that is mounted on the real kinematics.
2. If you want to use [zone monitoring](#zone-monitoring-s7-1500t), activate the tool zone associated with the active tool. If necessary, deactivate the tool zone that is not required (e.g. after a tool change). See section ["Activating zone monitoring"](#activating-zone-monitoring-s7-1500t).

> **Note**
>
> Before you return master control to the user program, the tool that the user program expects must be installed and set. The active tool is not set automatically to the active tool at the time of takeover of master control.
>
> In the user program, you can change the tool with the "MC_SetTool" Motion Control instruction after handing over master control.

### Operator controls for jogging and homing (S7-1500T)

You can use the slider to execute the following functions of the kinematics control panel:

- [Jog axes, joints, or the kinematics Cartesian in a direction or to the set target position.](#jogging-the-kinematics-s7-1500t)
- [Start active homing of a kinematics axis](#active-homing-of-the-kinematics-axis-s7-1500t)

The following sliders and buttons are displayed depending on the selected coordinate system, the kinematics type and the operating mode:

| Coordinate system | Slider/Button |
| --- | --- |
| MCS | - Axis number: A1 … A6 - ![Figure](images/159216436747_DV_resource.Stream@PNG-de-DE.png) - ![Figure](images/155918844811_DV_resource.Stream@PNG-de-DE.png) |
| JCS | Joint number: J1 … J6 |
| WCS or OCS | - Cartesian coordinates: x, y, z, A, B, C - Start ![Figure](images/155918836107_DV_resource.Stream@PNG-de-DE.png) |

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Velocity override**  The position of the slider in the "Control" area is adopted as a velocity override in the "&lt;TO&gt;.Override.Velocity" tag of the kinematics technology object.  If the velocity override is set by the user program, the user program overrides the value from the kinematics control panel. If the position of the slider is not equal to zero, then the value from the user program for the velocity override is transferred to the "&lt;TO&gt;.Override.Velocity" tag of the kinematics technology object.  Do not set the velocity override via the user program as long as the kinematics control panel is active. |  |

#### Jogging and homing velocity

The preset jogging and homing velocity is calculated as follows:

Jogging/homing velocity = configured velocity * slider position * "Adjust velocity" factor

The following shows the operation of the slider using kinematics axis A1. Operation is identical for jogging of joints and the kinematics in the Cartesian space.

#### Active homing

![Active homing](images/160094525451_DV_resource.Stream@PNG-de-DE.png)

Click the slider and drag the slider to the right. Homing is executed at the maximum preset velocity. The homing stops automatically with the set dynamics.

To home at the maximum preset velocity, click the ![Active homing](images/155899119755_DV_resource.Stream@PNG-de-DE.png) symbol.

#### Jog forward or backward

![Jog forward or backward](images/160095241227_DV_resource.Stream@PNG-de-DE.png)

**① Backward**

- Click A1 and drag the slider to the left.
- In the WCS and OCS: The further you move the slider to the left, the faster the kinematics moves backwards.
- In the JCS and MCS: As soon as you move the slider to the left, the axis/joint moves backwards at the maximum specified velocity.
- To jog backward at the maximum, specified jogging velocity, click the ![Jog forward or backward](images/155899111051_DV_resource.Stream@PNG-de-DE.png) symbol.

**② Forward**

- Click A1 and drag the slider to the right.
- In the WCS and OCS: The further you move the slider to the right, the faster the kinematics moves forward.
- In the JCS and MCS: As soon as you move the slider to the left, the axis/joint moves forward at maximum specified velocity.
- To jog forward at the maximum preset jogging velocity, click the ![Jog forward or backward](images/155899119755_DV_resource.Stream@PNG-de-DE.png) symbol.

**Stop jogging**

- Release the pressed mouse button. The slider automatically jumps to zero and the axis/joint/kinematics is stopped with the specified deceleration.

#### Jog to target position

![Jog to target position](images/160095470603_DV_resource.Stream@PNG-de-DE.png)

**In the MCS/JCS**

Click A1 and drag the slider to the right. As soon as you move the slider to the right, the axis/joint moves at the maximum specified velocity. Positioning stops automatically with the set dynamics.

To jog to the target position at the maximum preset jog velocity, click the ![Jog to target position](images/155899119755_DV_resource.Stream@PNG-de-DE.png) icon.

**In the WCS/OCS**

Click on the "Start" slider and drag it to the right. The further you move the slider to the right, the faster the kinematics moves forward.

To jog to the target position at the maximum preset jog velocity, click the ![Jog to target position](images/155899119755_DV_resource.Stream@PNG-de-DE.png) icon.

### Setting the home position of a kinematics axis (S7-1500T)

This function corresponds to direct homing (absolute) or setting the actual position or "Mode" = 0 at the "MC_Home" Motion Control instruction. The current position of the technology object is set to the value of parameter "Position".

#### Requirements

Kinematics is enabled in the kinematics control panel.

#### Procedure

1. In the drop-down list, select "Single axes: Set home position".
2. Enter the home position of the respective kinematics axis in the text box.
3. Click the "Set" button of the axis with the actual position you want to set.

   Result: The specified actual position is set. The kinematics axis is homed.
4. In the "Status and errors bits" diagnostics window, check whether the axis was homed.

### Active homing of the kinematics axis (S7-1500T)

This function corresponds to active homing with "Mode" = 3. The positioning axis/synchronous axis technology object performs a homing movement according to the configuration of the [active homing](Using%20S7-1500-S7-1500T%20Axis%20functions%20%28S7-1500%2C%20S7-1500T%29.md#active-homing-s7-1500-s7-1500t).

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Avoiding collisions**  Make sure that no unwanted positions are approached and that no collisions occur during the automatic homing movement. |  |

#### Requirements

- Kinematics is enabled in the kinematics control panel.
- The kinematics are in a position from which the homing movement of the kinematics axes is possible.

#### Procedure

1. In the drop-down list, select "Single axes: Homing".
2. Enter the home position of the respective kinematics axis in the text box.
3. To start active homing, click the slider and drag the slider to the right.
4. To cancel homing, release the pressed mouse button.  
   Result: The axis executes the homing movement configured under "Active homing". The other kinematics axes are not moved. The entered position of the kinematics control panel is used as home position.

**Note**

Up to technology version V7: Absolute encoder calibration is not possible in the kinematics control panel. The technology object is not homed when this mode is used with an absolute encoder.

As technology version V7: Absolute encoder adjustment can be performed in the kinematics control panel.

### Specifying dynamics in the kinematics control panel (S7-1500T)

In the "Jog" and "Jog to target position" modes, you can specify the dynamics for the next step of the commissioning. The dynamics settings can be found in the Inspector window under "Properties".

#### Default setting of dynamic values

The default settings of the dynamic values are as follows when the kinematics control panel is called:

| Dynamic value | Default value MCS/JCS coordinate systems | Default value WCS/OCS coordinate system |
| --- | --- | --- |
| Acceleration | 10% of the maximum acceleration of the kinematics axis | 10% of the maximum acceleration of the kinematics motion |
| Deceleration | 100% of the maximum deceleration of the kinematics axis | 100% of the maximum deceleration of the kinematics motion |
| Jerk | 100% of the maximum jerk of the kinematics axis | 100% of the maximum jerk of the kinematics motion |

#### Specifying dynamic values

In the WCS or OCS, these values apply to the motion in x, y and z direction and for the orientation.

To change these defaults temporarily, select the "User-defined dynamics" check box and enter the dynamic values.

If you have changed the values in the configuration of the technology object during operation with the kinematics control panel, these changes have no effect on the operation of the kinematics control panel. Changed values in the configuration only take effect after they have been loaded into the CPU and the control panel has been reopened.

#### Resetting dynamic values to default values

As soon as the check box "User-defined dynamics" is cleared or the commissioning is completed, the original default values are valid again. The specified dynamics values are replaced by the predefined default values in the following cases. If necessary, transfer the values to your configuration.

#### Transferring dynamic values from the kinematics control panel to the technology object

If you want to retain your specified dynamic values as default values or as dynamic limits after jogging in the WCS or OCS, transfer the dynamic values of the kinematics control panel to the configuration of the technology objects.

1. Make a note of the dynamic values of the kinematics control panel.
2. Click the "Deactivate" button.
3. Apply the noted dynamics values as the default setting of the dynamics or dynamics limit in the "Dynamics" configuration window of the kinematics.
4. Load the changed configuration into the CPU.

   The changed parameters are now effective in the user program.

#### Adjusting the velocity

Under "Adjust velocity", you correct the configured velocity using a percentage.

Example:

- Configured velocity in the kinematics control panel: 100 mm/s
- Adjust velocity: 50%
- Resulting velocity specification: 50 mm/s

You can set a value with the slider or enter a value between 1% and 200% directly in the text box below.

When master control is handed over, the last active position of the slider in the "Control" area is transferred as velocity override to the "&lt;TO&gt;.Override.Velocity" tag of the kinematics technology object. This is not influenced by the "Adjust velocity" set factor.

### Jogging the kinematics (S7-1500T)

This section contains information on the following topics:

- [Jogging the kinematics (S7-1500T)](#jogging-the-kinematics-s7-1500t-1)
- [Jogging the kinematics axes in the MCS (S7-1500T)](#jogging-the-kinematics-axes-in-the-mcs-s7-1500t)
- [Jogging joints in the JCS (S7-1500T)](#jogging-joints-in-the-jcs-s7-1500t)
- [Cartesian kinematics jogging in WCS/OCS (S7-1500T)](#cartesian-kinematics-jogging-in-wcsocs-s7-1500t)

#### Jogging the kinematics (S7-1500T)

In "Jog" mode, the following values are preset with 10% of the default value:

- Velocity of kinematics axes
- Velocity of the joints or joint angle
- Velocity in x, y and z direction
- Velocity for the orientations A, B and C

You use the slider to set the velocity override to a value between 1% and 200%.

##### Requirement

Kinematics is enabled in the kinematics control panel.

#### Jogging the kinematics axes in the MCS (S7-1500T)

In the MCS, you can jog each kinematics axis individually forwards, backwards or to a predefined target position or target angle. With mechanical couplings of the axes, select the "JCS" coordinate system to jog the [joints of the kinematics](#jogging-joints-in-the-jcs-s7-1500t).

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Limits of the joint traversing range are not taken into consideration in the MCS**   When you move the kinematics axes in the kinematics control panel in the MCS, the limits that have been set for the [joint traversing ranges](#define-joint-traversing-range-s7-1500t) are not taken into account for the joints.  In the case of kinematics without mechanically coupled axes, you can limit the joint position to the operating range by using software limit switches. The software limit switches have to be correctly set and existing offsets or the inverted traversing direction of the joints must be taken into consideration.  In the case of kinematics with mechanically coupled axes, you cannot completely limit the joint position to the operating range using the software limit switches. Therefore, you must yourself take into consideration the configured limits for the joint traversing ranges. Make sure that no unwanted positions are approached and that no collisions occur. |  |

##### Procedure for jogging forwards or backwards

1. Select the "Jog" operating mode in the drop-down list.
2. Select the "MCS" coordinate system in the drop-down list.
3. Enter the velocity for the axis.
4. Move the axis by dragging the slider forward or backward.
5. To stop the axis, release the pressed mouse button. The slider automatically jumps to the center position and the axis is stopped with the specified dynamics.

##### Procedure for jogging to a target position

1. Select the "Jog to target position" operating mode in the drop-down list.
2. Select the "MCS" coordinate system in the drop-down list.
3. Enter the target position for the kinematics axis.
4. Enter the velocity for the axis.
5. To specify the velocity, drag the slider to the right. The further you drag the slider to the right, the higher the velocity of the axis movement.
6. To stop the axis before the target position is reached, release the pressed mouse button. The slider automatically jumps to zero to the left and the axis stops with the set dynamics.
7. The axis stops automatically with the specified dynamics when the target position has been approached.

#### Jogging joints in the JCS (S7-1500T)

In the JCS, you can jog each kinematics joint individually forwards, backwards or to a set target position. In contrast to jogging in the MCS where only the axis coordinates are taken into account, the mechanical axis coupling is taken into account when jogging in the JCS.

For kinematics types with up to 4 interpolating axes, the jogging of the joints in the JCS corresponds to the jogging of the axes in the MCS.

> **Note**
>
> **Jogging joints in the JCS**
>
> For coupled axes with coupling factor ≠ 1, the jogging of joints in the JCS can result in an unwanted position change of the coupled axes.

##### Requirement

You have assumed master control in the kinematics control panel.

##### Jog forward or backward

To move a joint forward or backward in jog mode, proceed as follows:

1. In the "Operating mode" drop-down list, select the "Jog" entry.
2. In the "Coordinate system" drop-down list, select the "JCS" entry.
3. Enter the velocity for the joint.
4. To move a joint in the positive direction, drag the slider to the right.

   The joint moves in the positive direction as long as you keep the slider pressed and to the right of the zero position.
5. To move a joint in the negative direction, drag the slider to the left.

   The joint moves in the negative direction as long as you keep the slider pressed and hold it to the left of the zero position.
6. To stop the joint moving, release the pressed mouse button.

   The slider automatically jumps to the center position and the joint is stopped with the specified dynamics.

##### Jogging to a target position

To move a joint to a target position in jog mode, proceed as follows:

1. In the "Operating mode" drop-down list, select the "Jog to target position" entry.
2. In the "Coordinate system" drop-down list, select the "JCS" entry.
3. Enter the velocity for the joint.
4. Enter the target position for the joint.
5. To move the joint to the target position, move the slider to the right. The further you move the slider to the right, the higher the velocity of the joint movement.

   The kinematics stops as soon as you release the pressed mouse button or the target position is reached.

#### Cartesian kinematics jogging in WCS/OCS (S7-1500T)

In WCS or OCS, you can move each kinematic in jog mode in x, y and z direction or rotate the tool center point around the x, y and z-axis (rotation A, B, C).

When jogging to a target position, you move the kinematics to the position specified under "Target position" with a linear motion. The direction of movement of the Cartesian orientation is not limited to the positive direction here. For kinematics with up to four interpolating axes, the A4 kinematics axis is moved using the "Shortest path" mode.

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Overrun of the dynamics through singular positions**  Overruns of the dynamics in the vicinity of singular positions can result in the following damage:  - Machine damage through overload of the mechanical components - Personal injury caused by products or machine parts coming loose   To prevent dynamic overruns in the vicinity of singular positions, take the following measures:  - Move the kinematics in the MCS or the JCS. - In the WCS or OCS, avoid the "Jog" mode. The dynamic adaptation in "Jog" mode in the WCS or OCS is not active in the kinematics control panel. The dynamic limits of the kinematics axes are not taken into account during a kinematics motion with the kinematics control panel. - Up to technology version V5: In the WCS or OCS, avoid using the "Jog to target position" mode. The dynamic adaptation in "Jog to target position" mode in the WCS or OCS is not active in the kinematics control panel. The dynamic limits of the kinematics axes are not taken into account during a kinematics motion with the kinematics control panel. - As of technology version V6: Move the kinematics to the "Jog to target position" mode in the WCS or OCS using the kinematics control panel. "Dynamic adaptation without segmentation of the path" is permanently active in the "Jog to target position" mode, and the dynamic limits of the kinematics axes are taken into account. |  |

##### Jog

To move the kinematics axes in jog mode, follow these steps:

1. In the "Operating mode" drop-down list, select the "Jog" entry.
2. In the "Coordinate system" drop-down list, select the "WCS" or "OCS" entry.
3. Enter the velocity for the x, y and z directions and for the orientations A, B, and C.
4. To move a kinematics axis in the positive direction, click the slider and drag the slider to the right.

   The kinematics moves in the positive direction as long as you keep the slider pressed and to the right of the zero position. As soon as you release the pressed mouse button, the slider automatically jumps to zero and the kinematics is stopped with the specified dynamics. Depending on the kinematics type, several axes can be moved.
5. To move a kinematics axis in the negative direction, click the slider and drag the slider to the left.

   The kinematics moves in the negative direction as long as you keep the slider pressed and to the left of the zero position. As soon as you release the pressed mouse button, the slider automatically jumps to zero and the kinematics is stopped with the specified dynamics. Depending on the kinematics type, several axes can be moved.

##### Jogging to a Cartesian target position

To move the kinematics to a target position in jog mode, proceed as follows:

1. In the "Operating mode" drop-down list, select the "Jog to target position" entry.
2. In the "Coordinate system" drop-down list, select the "WCS" or "OCS" entry.

   The target position is shown in the 3D display.
3. Enter the velocity for the path and the orientation motion.
4. Enter the Cartesian target position in the selected coordinate system.

   Alternatively, you can specify the target position with the [directional pad](#operating-the-directional-pad-s7-1500t).
5. To move the kinematics to the target position, click the "Start" slider, hold down the mouse button and move the slider to the right.

   The kinematics moves to the specified target position. Movements of the kinematics axis are possible in both the positive and the negative direction. For kinematics with up to four interpolating axes, the A4 kinematics axis is moved using the "Shortest path" mode.

   The kinematics stops as soon as you release the pressed mouse button or the target position is reached.

### Disabling kinematics and handing over master control (S7-1500T)

#### Procedure

To return the master control to the user program, perform the following steps:

1. Jog the kinematics to a basic position from which the kinematics can be moved with the user program.
2. Set the currently mounted tool in the kinematics control panel and activate the tool zone associated with the active tool. If necessary, deactivate the tool zone that is no longer required (e.g. after a tool change).
3. Click the "Disable" button.

   The kinematics axes are disabled.
4. Click "Deactivate".

   The master control is returned from the kinematics control panel to the user program.
5. Set the velocity override to the value required in the user program (&lt;TO&gt;.Override.Velocity).

#### Result

You can move the kinematics via an automatic program or an HMI.

## Diagnostics (S7-1500T)

This section contains information on the following topics:

- [Introduction to diagnostics (S7-1500T)](#introduction-to-diagnostics-s7-1500t)
- [Kinematics technology object (S7-1500T)](#kinematics-technology-object-s7-1500t)

### Introduction to diagnostics (S7-1500T)

The description of Motion Control diagnostics is limited to the diagnostics view of the technology objects in TIA Portal, the technology alarms and the error IDs on Motion Control instructions.

The following descriptions can be found in the "S7-1500/S7-1500T Motion Control alarms and error IDs" documentation:

- [Diagnostics concept](S7-1500-S7-1500T%20Motion%20Control%20alarms%20and%20error%20IDs%20%28S7-1500%2C%20S7-1500T%29.md#diagnostics-concept-s7-1500-s7-1500t-1)
- [Technology alarms](S7-1500-S7-1500T%20Motion%20Control%20alarms%20and%20error%20IDs%20%28S7-1500%2C%20S7-1500T%29.md#technology-alarms-s7-1500-s7-1500t)
- [Error IDs in Motion Control instructions](S7-1500-S7-1500T%20Motion%20Control%20alarms%20and%20error%20IDs%20%28S7-1500%2C%20S7-1500T%29.md#error-ids-in-motion-control-instructions-s7-1500-s7-1500t)

A comprehensive description of the system diagnostics of the S7‑1500 CPU can be found in the ["Diagnostics" function manual](https://support.industry.siemens.com/cs/ww/en/view/59192926).

### Kinematics technology object (S7-1500T)

This section contains information on the following topics:

- [Structure of the diagnostics (S7-1500T)](#structure-of-the-diagnostics-s7-1500t)
- [Status and error bits (S7-1500T)](#status-and-error-bits-s7-1500t)
- [Zones status (S7-1500T)](#zones-status-s7-1500t)
- [Motion and tools (S7-1500T)](#motion-and-tools-s7-1500t)
- [Positions (S7-1500T)](#positions-s7-1500t)

#### Structure of the diagnostics (S7-1500T)

The diagnostics of the kinematics in "Technology object &gt; Diagnostics" is divided into the following areas:

- Graphic display
- Diagnostics window

##### Diagnostics window

The following diagnostics windows are available in the graphic display:

- [Status and error bits](#status-and-error-bits-s7-1500t)
- [Zones status](#zones-status-s7-1500t)
- [Motion and Tools](#motion-and-tools-s7-1500t)
- [Positions](#positions-s7-1500t)

With the following buttons, you can show or hide the associated diagnostics windows:

| Button | Function |
| --- | --- |
| ![Diagnostics window](images/134697410187_DV_resource.Stream@PNG-de-DE.png) | Status and error bits |
| ![Diagnostics window](images/134698672267_DV_resource.Stream@PNG-de-DE.png) | Zones status |
| ![Diagnostics window](images/134698974347_DV_resource.Stream@PNG-de-DE.png) | Motion and tools |
| ![Diagnostics window](images/134698982027_DV_resource.Stream@PNG-de-DE.png) | Positions |

You can also move the diagnostics window to a desired position within the graphic display.

#### Status and error bits (S7-1500T)

With the diagnostics window "Status and error bits" in "Technology object &gt; Diagnostics" you monitor the status and error messages of the technology object in the TIA Portal. The diagnostics function is available in online operation.

The diagnostics window "Status and error bits" is shown in the graphic display of the diagnostics. You can show the diagnostics window via the ![Figure](images/134697410187_DV_resource.Stream@PNG-de-DE.png) symbol of the toolbar and move the window to a desired position within the graphic display.

The meaning of the status and error messages is described in the following tables. The associated technology object tag is given in parentheses.

##### "Kinematics status"

The following table shows the possible statuses of the kinematics:

| Status | Description |
| --- | --- |
| Error | An error occurred at the technology object. Detailed information about the error is available in the "Error" area and in the "&lt;TO&gt;.ErrorDetail.Number" and "&lt;TO&gt;.ErrorDetail.Reaction" tags of the technology object.  (&lt;TO&gt;.StatusWord.X1 (Error)) |
| Restart active | The technology object is being reinitialized.  (&lt;TO&gt;.StatusWord.X2 (RestartActive)) |
| Kinematics control panel active | The kinematics control panel is activated. The kinematics control panel has master control over the technology object. The kinematics cannot be controlled from the user program.  (&lt;TO&gt;.StatusWord.X4 (ControlPanelActive)) |
| Restart required | Data relevant for the restart has been changed. The changes are applied only after a restart of the technology object.  (&lt;TO&gt;.StatusWord.X3 (OnlineStartValuesChanged)) |
| Valid | The transformation values are valid.  (&lt;TO&gt;.StatusKinematics.Valid) |
| Simulation active | The kinematics technology object is in simulation.  (&lt;TO&gt;.StatusWord.X19 (InSimulation)) |
| JCS enabled | The kinematics technology object uses the JCS.  (&lt;TO&gt;.StatusWord.X21 (EnabledJCS)) |

##### "Error"

The following table shows the possible errors:

| Error | Description |
| --- | --- |
| System | A system-internal error has occurred.  (&lt;TO&gt;.ErrorWord.X0 (SystemFault)) |
| Configuration | A configuration error has occurred.  One or more configuration parameters are inconsistent or invalid.  The technology object was incorrectly configured, or editable configuration data was incorrectly modified during runtime of the user program.  (&lt;TO&gt;.ErrorWord.X1 (ConfigFault)) |
| Transformation | A transformation error has occurred.  (&lt;TO&gt;.ErrorWord.X4 (TransformationFault)) |
| User program | An error has occurred in the user program at a Motion Control instruction or its use (e.g. by the kinematics control panel).  (&lt;TO&gt;.ErrorWord.X2 (UserFault)) |
| Job rejected | A job cannot be executed.  A Motion Control instruction cannot be executed because necessary requirements have not been met (e.g. technology object not homed).  (&lt;TO&gt;.ErrorWord.X3 (CommandNotAccepted)) |
| Dynamic limitation | The dynamic values are limited to the dynamic limits.  (&lt;TO&gt;.ErrorWord.X6 (DynamicError)) |

##### "Warnings"

The following table shows the possible warnings:

| Warning | Description |
| --- | --- |
| Configuration | One or more configuration parameters are being internally adapted temporarily.  (&lt;TO&gt;.WarningWord.X1 (ConfigWarning)) |
| Job rejected | A job cannot be executed.  A Motion Control instruction cannot be executed because the necessary conditions have not been met.  (&lt;TO&gt;.WarningWord.X3 (CommandNotAccepted)) |
| Dynamic limitation | The dynamic values are limited to the dynamic limits.  (&lt;TO&gt;.WarningWord.X6 (DynamicWarning)) |

##### "Motion status"

The following table shows the possible statuses of the kinematics motion:

| Status | Description |
| --- | --- |
| Done (no job running) | There is no active motion job at the technology object.  (&lt;TO&gt;.StatusWord.X6 (Done)) |
| Linear motion active | There is a linear motion job active at the technology object.  (&lt;TO&gt;.StatusWord.X8 (LinearCommand)) |
| Circular motion active | There is a circular motion job active at the technology object.  (&lt;TO&gt;.StatusWord.X9 (CircularCommand)) |
| sPTP motion active | There is a synchronous "point-to-point" motion job active at the technology object.  (&lt;TO&gt;.StatusWord.X11 (DirectCommand)) |
| Constant velocity | The kinematics is being moved at constant velocity or is at a standstill.  (&lt;TO&gt;.StatusWord.X12 (ConstantVelocity)) |
| Accelerating | The kinematics is being accelerated.  (&lt;TO&gt;.StatusWord.X13 (Accelerating)) |
| Decelerating | The kinematics is being decelerated.  (&lt;TO&gt;.StatusWord.X14 (Decelerating)) |
| Motion interrupted | The active kinematics motion is interrupted by an "MC_GroupInterrupt" command .  (&lt;TO&gt;.StatusWord.X17 (Interrupted)) |
| Orientation movement active | There is an orientation motion active at the technology object.  (&lt;TO&gt;.StatusWord.X15 (OrientationMotion)) |

---

**See also**

["StatusWord" tag (kinematics) (S7-1500T)](#statusword-tag-kinematics-s7-1500t)
  
["ErrorWord" tag (kinematics) (S7-1500T)](#errorword-tag-kinematics-s7-1500t)
  
["WarningWord" tag (kinematics) (S7-1500T)](#warningword-tag-kinematics-s7-1500t)

#### Zones status (S7-1500T)

Using the diagnostics windows "Status Zones" in "Technology object &gt; Diagnostics", you monitor the status of the workspace zones and the kinematics zones of the technology object in the TIA portal. The diagnostics function is available in online operation.

The diagnostics window "Zones Status" is displayed in the graphic display of the diagnostics. You can show the diagnostics window via the symbol ![Figure](images/134698672267_DV_resource.Stream@PNG-de-DE.png) of the toolbar and move the window to a desired position within the graphic display.

##### "Zones status"

The "Workspace zones" and "Kinematics zones" tables show the status of the individual zones. The following symbols are displayed for this purpose:

| Symbol | Description |
| --- | --- |
| !["Zones status"](images/103638857867_DV_resource.Stream@PNG-de-DE.png) | The zone is not defined. |
| !["Zones status"](images/103740605963_DV_resource.Stream@PNG-de-DE.png) | The zone is inactive. |
| !["Zones status"](images/103638891147_DV_resource.Stream@PNG-de-DE.png) | The zone is active. |
| !["Zones status"](images/104049960203_DV_resource.Stream@PNG-de-DE.png) | The zone was violated. |

You can use the toolbar icon !["Zones status"](images/134699079307_DV_resource.Stream@PNG-de-DE.png) in the graphic display of the diagnostics to show and hide all zones. In addition, when the icon !["Zones status"](images/134699079307_DV_resource.Stream@PNG-de-DE.png) is active, you can display and hide the zones using the symbol !["Zones status"](images/134699086987_DV_resource.Stream@PNG-de-DE.png).

---

**See also**

[Structure of the diagnostics (S7-1500T)](#structure-of-the-diagnostics-s7-1500t)

#### Motion and tools (S7-1500T)

You monitor the path motions and the tools of the technology object in the TIA Portal using the diagnostics window "Motion and Tools" in "Technology object &gt; Diagnostics". The diagnostics function is available in online operation.

The diagnostics window "Motion and Tools" is shown in the graphic display of the diagnostics. You can show the diagnostics window via the ![Figure](images/134698974347_DV_resource.Stream@PNG-de-DE.png) symbol of the toolbar and move the window to a desired position within the graphic display.

##### "Motion and Tools"

The following table describes the meaning of the parameters of the motion and tools:

| Status |  |  | Description |  |
| --- | --- | --- | --- | --- |
| Path dynamics values |  |  |  |  |
|  | Limit path dynamics to axis dynamics |  | Dynamic adaptation  (&lt;TO&gt;.StatusPath.DynamicAdaption) |  |
| Velocity |  | Current path velocity (setpoint reference)  (&lt;TO&gt;.StatusPath.Velocity) |  |  |
| Acceleration |  | Current path acceleration (setpoint reference)  (&lt;TO&gt;.StatusPath.Acceleration) |  |  |
| Orientation velocity |  | Resulting orientation velocity  (&lt;TO&gt;.StatusPath.OrientationVelocity) |  |  |
| Override |  | Percentage correction of the velocity specification  The setpoint velocity set in Motion Control instructions or from the kinematics control panel is superimposed with an override signal and corrected as a percentage. The following values are permitted as velocity correction:  - Path motion: from 0.0% to 200.0% - sPTP motion: from 0.0% to 100.0%   (&lt;TO&gt;.Override.Velocity) |  |  |
| Job sequence |  |  |  |  |
|  | Existing jobs |  | Current number of jobs for the kinematics technology object in the job sequence.  (&lt;TO&gt;.StatusMotionQueue.NumberOfCommands) |  |
| Prepared jobs |  | Number of prepared jobs for the kinematics technology object in the job sequence. (&lt;TO&gt;.StatusMotionQueue.NumberOfPreparedCommands) |  |  |
| Prepared jobs (distance) |  |  |  |  |
|  | Total path length |  | Total path length of linear and circular path motions  (&lt;TO&gt;.StatusPath.TotalPathLength)  Sum of:  - Distance of all completed motion jobs - Distance travelled of the active motion job - Remaining distance of the motion job - Calculated distance of all jobs in the job sequence |  |
| Accumulated path length |  | Accumulated path length of linear and circular path motions  (&lt;TO&gt;.StatusPath.AccumulatedPathLength)  Sum of:  - Distance of all completed motion jobs - Distance travelled of the active motion job |  |  |
| Active tool |  |  |  |  |
|  | Active tool |  | Currently selected tool  (&lt;TO&gt;.StatusTool.ActiveTool) |  |
| Tool center point in the FCS |  |  |  |  |
|  | x position |  | x coordinate of the current tool frame in the flange coordinate system (FCS)  (&lt;TO&gt;.StatusTool.Frame[1..3].x) |  |
| y position |  | y coordinate of the current tool frame in the FCS  (&lt;TO&gt;.StatusTool.Frame[1..3].y) |  |  |
| z position |  | z coordinate of the current tool frame in the FCS  (&lt;TO&gt;.StatusTool.Frame[1..3].z) |  |  |
| Rotation A |  | A-coordinate of the current tool frame in the FCS  (&lt;TO&gt;.StatusTool.Frame[1..3].a) |  |  |
| Rotation B |  | B-coordinate of the current tool frame in the FCS  (&lt;TO&gt;.StatusTool.Frame[1..3].b) |  |  |
| Rotation C |  | C-coordinate of the current tool frame in the FCS  (&lt;TO&gt;.StatusTool.Frame[1..3].c) |  |  |
| Joints |  |  |  |  |
|  | J1 … J6 velocity setpoint |  | Current velocity setpoint of the respective joint J1 to J6  (&lt;TO&gt;.JointData.J[1..6].Velocity) |  |
| J1 … J6 acceleration setpoint |  | Current acceleration setpoint of joint J1 to J6  (&lt;TO&gt;.JointData.J[1..6].Acceleration) |  |  |
| Conveyor tracking |  |  |  |  |
|  | OCS1 … 3 |  | Active coupled OCS 1, 2 or 3 |  |
|  | Coupled technology object | Technology object for active conveyor tracking  Leading-value-capable technology objects are:  - Positioning axis - Synchronous axis - External encoder - Leading axis proxy   (&lt;TO&gt;.StatusConveyor[1..3].ConveyorBelt) |  |  |
| Conveyor position | Conveyor position of the technology object  (&lt;TO&gt;.StatusConveyor[1..3].BeltPosition) |  |  |  |
| Position of the OCS in x direction | Position of the OCS in x direction on the conveyor  (&lt;TO&gt;.StatusConveyor[1..3].ObjectPosition) |  |  |  |
| Conveyor tracking status | Conveyor tracking status   (&lt;TO&gt;.StatusConveyor[1..3].TrackingState) |  |  |  |
| OCS not assigned | The OCS is not assigned to a leading-value-capable technology object.  (&lt;TO&gt;.StatusConveyor[1..3].TrackingState = 0) |  |  |  |
| OCS assigned | The Motion Control instruction "MC_TrackConveyorBelt" is finished and the OCS is assigned to a leading-value-capable technology object. The first path motion job in the tracked OCS can be sent.  (&lt;TO&gt;.StatusConveyor[1..3].TrackingState = 1) |  |  |  |
| TCP synchronizes to OCS | The OCS is assigned to a leading-value-capable technology object. The first path motion job in the tracked OCS is active.  (&lt;TO&gt;.StatusConveyor[1..3].TrackingState = 2) |  |  |  |
| TCP follows OCS | The OSC is assigned to a leading-value-capable technology object.   The position of the OCS is reached. The kinematics is moved with the position of the OCS.  (&lt;TO&gt;.StatusConveyor[1..3].TrackingState = 3) |  |  |  |
| TCP desynchronizes from OCS | The motion of the kinematics in the tracked OCS is ended by a motion job in the WCS or a non-tracked OCS. When the motion job is completed, the "TrackingState" changes to 0 and the OCS is not tracked with the product position anymore.  (&lt;TO&gt;.StatusConveyor[1..3].TrackingState = 4) |  |  |  |

---

**See also**

[Structure of the diagnostics (S7-1500T)](#structure-of-the-diagnostics-s7-1500t)

#### Positions (S7-1500T)

You monitor the position values of the technology object in the TIA Portal using the diagnostics window "Positions" in "Technology object &gt; Diagnostics". The diagnostics function is available in online operation.

The diagnostics window "Positions" is shown in the graphical display of the diagnostics. You can show the diagnostics window via the ![Figure](images/134698982027_DV_resource.Stream@PNG-de-DE.png) symbol of the toolbar and move the window to a desired position within the graphic display.

The available functions are described in the section "[Monitoring and comparing position values](#monitoring-and-comparing-position-values-s7-1500t)".

##### "Positions"

The following table describes the meaning of the position information:

| Status |  |  | Description |
| --- | --- | --- | --- |
| Coordinate system 1 |  |  | Reference coordinate system  - In "Diagnostics", in "Calibration" and in "Kinematics trace", this field shows the coordinate system that you have selected in the toolbar. - In "Commissioning", this field shows the coordinate system that you have selected in the kinematics control panel. - When you select the kinematics coordinate system (KCS) in the toolbar, the WCS is displayed in the "Positions" window in "Diagnostics" and in "Kinematics trace". |
|  | x position |  | x coordinate of the active tool in the set coordinate system  (&lt;TO&gt;.Tcp.x; &lt;TO&gt;.TcpInOcs[1..3].x.Position) |
| y position |  | y coordinate of the active tool in the set coordinate system  (&lt;TO&gt;.Tcp.y; &lt;TO&gt;.TcpInOcs[1..3].y.Position) |  |
| z position |  | z coordinate of the active tool in the set coordinate system  (&lt;TO&gt;.Tcp.z; &lt;TO&gt;.TcpInOcs[1..3].z.Position) |  |
| Rotation A |  | A coordinate of the active tool in the set coordinate system  (&lt;TO&gt;.Tcp.a; &lt;TO&gt;.TcpInOcs[1..3].a.Position) |  |
| Rotation B |  | B coordinate of the active tool in the set coordinate system  (&lt;TO&gt;.Tcp.b; &lt;TO&gt;.TcpInOcs[1..3].b.Position) |  |
| Rotation C |  | C coordinate of the active tool in the set coordinate system  (&lt;TO&gt;.Tcp.c; &lt;TO&gt;.TcpInOcs[1..3].c.Position) |  |
| Coordinate system 2 |  |  | Reference coordinate system  In the drop-down list, you can select an additional coordinate system in order to display the actual position of the active tool in this coordinate system. |
|  | WCS, OCS1, OCS2, OCS3 |  |  |
|  | x position | x coordinate of the active tool in the set coordinate system  (&lt;TO&gt;.Tcp.x; &lt;TO&gt;.TcpInOcs[1..3].x.Position) |  |
| y position | y coordinate of the active tool in the set coordinate system  (&lt;TO&gt;.Tcp.y; &lt;TO&gt;.TcpInOcs[1..3].y.Position) |  |  |
| z position | z coordinate of the active tool in the set coordinate system  (&lt;TO&gt;.Tcp.z; &lt;TO&gt;.TcpInOcs[1..3].z.Position) |  |  |
| Rotation A | A coordinate of the active tool in the set coordinate system  (&lt;TO&gt;.Tcp.a; &lt;TO&gt;.TcpInOcs[1..3].a.Position) |  |  |
| Rotation B | B coordinate of the active tool in the set coordinate system  (&lt;TO&gt;.Tcp.b; &lt;TO&gt;.TcpInOcs[1..3].b.Position) |  |  |
| Rotation C | C coordinate of the active tool in the set coordinate system  (&lt;TO&gt;.Tcp.c; &lt;TO&gt;.TcpInOcs[1..3].c.Position) |  |  |
| MCS |  |  |  |
|  | A[1..6] | Current position setpoint of axis A[1..6]  (&lt;TO&gt;.Position) |  |
| JCS |  |  |  |
|  | J[1..6] | Current position setpoint of joint JJ[1..6]  (&lt;TO&gt;.JointData.J[1..6].Position) |  |

---

**See also**

[Structure of the diagnostics (S7-1500T)](#structure-of-the-diagnostics-s7-1500t)

## Kinematics trace (S7-1500T)

This section contains information on the following topics:

- [Brief description of kinematics trace (S7-1500T)](#brief-description-of-kinematics-trace-s7-1500t)
- [Defining parameter values for recording (S7-1500T)](#defining-parameter-values-for-recording-s7-1500t)
- [List of recordings (S7-1500T)](#list-of-recordings-s7-1500t)
- [Recording and playing kinematics motions (S7-1500T)](#recording-and-playing-kinematics-motions-s7-1500t)
- [Saving and deleting recordings (S7-1500T)](#saving-and-deleting-recordings-s7-1500t)
- [Importing and exporting recordings (S7-1500T)](#importing-and-exporting-recordings-s7-1500t)

### Brief description of kinematics trace (S7-1500T)

The kinematics trace offers the following functions:

- 3D visualization of the current motion of the tool center point (TCP) and the object coordinate systems (OCS)
- Recording, playing and saving kinematic motions
- Exporting and importing the recordings

You can find the kinematics trace of the kinematics technology object in the project tree under "Technology object &gt; Kinematics trace".

### Defining parameter values for recording (S7-1500T)

You specify the parameter values for the recording under "Technology object &gt; Kinematics trace &gt; Configuration"

#### Setting the sampling

Configure the duration of a recording as follows:

1. In the "Time of recording" drop-down list, select the desired recording time between the following OBs:

   - MC_Servo
   - MC_Interpolator
2. In the "Record all" drop-down list, select the desired value for the recording interval:

   - Specification in cycles
   - Specification in seconds
3. The calculated value of the maximum recording duration is displayed in the "Max. recording duration" field.

   If you change the recording interval in the field "Record all", the maximum recording time changes.
4. To set the recording duration to the maximum possible, select the "Use max. recording duration" check box.
5. In the "Recording duration (a)" drop-down list, select the desired type of recording duration display for the recording:

   - In seconds
   - Number of samples

#### Setting triggers

Configure the start of a recording as follows:

1. In the "Trigger mode" drop-down list, select the desired trigger mode for your recording:

   - Record now  
     The recording starts immediately after the configuration is loaded.
   - Trigger on tag  
     The system waits for a trigger event that triggers the recording.
2. In the "Trigger tag" field, select a tag of the data type "BOOL".
3. In the "Event" drop-down list, select the desired event to be used as trigger event:

   - Positive edge
   - Falling edge
4. In the "Pretrigger (b)" drop-down list, select a suitable pretrigger for your recording:

   - In seconds
   - Number of samples

   The "pretrigger" is used to record measuring points in advance of the start of the trigger event. As soon as the trigger event occurs, the recording is displayed in the graphic view.

#### Selecting the traces to be recorded

Select the traces for the recording as follows.

1. Select whether the setpoint positions of the kinematics axes should be recorded with the coordinates of the tool center point (TCP). You have the following options:

   - Tool center point (TCP) and kinematics

     If you activate this option, the coordinates of the TCP and the set positions of the kinematics axis are recorded. The motions of the TCP and the motions of the kinematic axes are displayed when a recording is played.
   - Tool center point (TCP)

     If you activate this option, only the coordinates of the TCP will be recorded. The motions of the TCP are displayed when a recording is played, the motions of the kinematic axes are not displayed.
2. Select the object coordinate systems (OCS) to be recorded.

   - OCS 1 frame
   - OCS 2 frame
   - OCS 3 frame

#### Maximum number of signals per kinematics trace

You can record a maximum of 64 signals in a kinematics trace. The following table shows how many signals are required for the traces.

| Kinematics type | Trace | Required signals |
| --- | --- | --- |
| 2D | Tool center point (TCP) and kinematics | 4 |
| Tool center point (TCP) | 2 |  |
| per OCS | 3 |  |
| 2D with orientation | Tool center point (TCP) and kinematics | 6 |
| Tool center point (TCP) | 3 |  |
| per OCS | 2 |  |
| 3D | Tool center point (TCP) and kinematics | 6 |
| Tool center point (TCP) | 3 |  |
| per OCS | 6 |  |
| 3D with orientation | Tool center point (TCP) and kinematics | 8 |
| Tool center point (TCP) | 4 |  |
| per OCS | 4 |  |
| 3D with 2 orientations A, B | Tool center point (TCP) and kinematics | 10 |
| Tool center point (TCP) | 5 |  |
| per OCS | 4 |  |
| 3D with 3 orientations | Tool center point (TCP) and kinematics | 12 |
| Tool center point (TCP) | 6 |  |
| per OCS | 6 |  |
| 6-axis articulated arm with central hand | Tool center point (TCP) and kinematics | 12 |
| Tool center point (TCP) | 6 |  |
| per OCS | 6 |  |

The more traces you record, the lower the maximum recording duration and the number of samples per trace.

### List of recordings (S7-1500T)

The list of recordings is displayed below the graphic display as tabular editor. The list contains the following recordings:

- The current recording
- All saved recordings for the selected technology object

The recordings are displayed line by line.

#### Functions

The following functions are available in the list of recordings:

- [Saving and deleting recordings](#saving-and-deleting-recordings-s7-1500t)
- Showing traces of a recording

  You can also show all traces of a recording by expanding the line of a recording.
- Showing and hiding traces in the graphic display

  The button for showing and hiding a trace has the following functions depending on the status:

  | Button | Status and function |
  | --- | --- |
  | ![Functions](images/165350108555_DV_resource.Stream@PNG-de-DE.png) | The recording or the trace is hidden.  Shows the hidden recording or trace. |
  | ![Functions](images/134705312395_DV_resource.Stream@PNG-de-DE.png) | The traces of the recording are partially shown and hidden. |
  | ![Functions](images/134699086987_DV_resource.Stream@PNG-de-DE.png) | The recording or the trace is shown.  Hides the recording or trace |

### Recording and playing kinematics motions (S7-1500T)

For the recording, use the values set under "Technology object &gt; Kinematics trace &gt; Configuration".

**Switch to live display**

You can show the current motion or position of the kinematics with the ![Figure](images/134702074763_DV_resource.Stream@PNG-de-DE.png) icon in online mode. The button for the live display is active when a saved recording is selected or while a recording is played. In offline mode and when no recording is available, the live display button is inactive.

#### Requirement

- The kinematics trace was configured under "Technology object &gt; Kinematics trace &gt; Configuration".

#### Record kinematics motion

To record a kinematics motion, proceed as follows:

1. Click the ![Record kinematics motion](images/163741917451_DV_resource.Stream@PNG-de-DE.png) icon in the toolbar to establish an online connection to the device.

   The kinematics trace establishes an online connection to the device. If the online and offline trace configurations differ, the trace configuration is loaded into the device.
2. To start a recording, click on the symbol ![Record kinematics motion](images/134699901323_DV_resource.Stream@PNG-de-DE.png) in the toolbar.

   If you start a recording directly without previously establishing the online connection (step 1), an online connection is established automatically.
3. Move the kinematics.
4. To end the recording, click on the symbol ![Record kinematics motion](images/134701944203_DV_resource.Stream@PNG-de-DE.png) on the toolbar.

   The current recording and the configuration are kept until the "kinematics trace" has been closed. When you start a new recording, the current recording is overwritten.

#### Play kinematics motion

To play a kinematics motion, proceed as follows:

| 1. If the live display is activated, switch off the live display by clicking the symbol ![Play kinematics motion](images/134702074763_DV_resource.Stream@PNG-de-DE.png). 2. In the list of recordings, select the recording you want to play. 3. To show the trace in the graphic display, click on the ![Play kinematics motion](images/134699086987_DV_resource.Stream@PNG-de-DE.png) symbol in the line of the selected recording.    The complete trace of the selected recording is displayed graphically in the display. 4. To play the recording, click on the ![Play kinematics motion](images/134702792843_DV_resource.Stream@PNG-de-DE.png) symbol at the bottom of the graphic display.    The recording that is selected as a line in the list is played. 5. To adjust the playback speed, change the position of the speed slider in the toolbar for playing a recording.       ![Play kinematics motion](images/134704971403_DV_resource.Stream@PNG-de-DE.png) . 6. Use the following buttons to control the playback of a recording:       | Button | Function |    | --- | --- |    | ![Play kinematics motion](images/134703084683_DV_resource.Stream@PNG-de-DE.png) | Jumps back to the start of the selected recording. |    | ![Play kinematics motion](images/134703092363_DV_resource.Stream@PNG-de-DE.png) | Jumps back step-by-step in the selected recording. |    | ![Play kinematics motion](images/134704866443_DV_resource.Stream@PNG-de-DE.png) | Jumps forward step-by-step in the selected recording. |    | ![Play kinematics motion](images/134704963723_DV_resource.Stream@PNG-de-DE.png) | Jumps to the end of the selected recording. | 7. To pause a recording, click on the symbol ![Play kinematics motion](images/134702979723_DV_resource.Stream@PNG-de-DE.png) in the toolbar for playing a recording. 8. To stop a recording, click on the symbol ![Play kinematics motion](images/134702987403_DV_resource.Stream@PNG-de-DE.png) in the toolbar for playing a recording. |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

#### Show TCP orientation

Use the ![Show TCP orientation](images/154941693451_DV_resource.Stream@PNG-de-DE.png) button to show or hide the TCP orientation as a trace in the kinematics trace.

#### Displaying and comparing position values

In the kinematics trace, you can monitor position values of the technology object or compare the position values in two different reference coordinate systems with the "Positions" window.

In addition, you can view position values directly on the trace.

The available functions are described in the section "[Monitoring and comparing position values](#monitoring-and-comparing-position-values-s7-1500t)".

### Saving and deleting recordings (S7-1500T)

#### Saving a recording

You can save a current recording. A saved recording contains the following data:

- Kinematics type
- Coordinates of:

  - Kinematics
  - Tool center point (TCP)
  - Object coordinate systems (OCS)
- Valid online geometry at the time of the recording

To adjust and save a recording, proceed as follows:

1. In the "Current recording" area, enter the name of the recording in the "Name" column.
2. In the "Color" column, select the desired colors for the traces.
3. If necessary, enter comments in the "Comment" column.
4. To save the current recording, click on the symbol ![Saving a recording](images/134705776011_DV_resource.Stream@PNG-de-DE.png) in the "Current recording" area.

   The recording is inserted in the "Saved recordings" area in the tabular editor.

**Note**

**Up to 20 recordings which can be saved**

The tabular editor can save a maximum of 20 recordings.

To save additional recordings, delete the recording you no longer need.

#### Deleting saved recordings

To delete a recording, follow these steps:

1. To delete a recording, click on the symbol ![Deleting saved recordings](images/165350104587_DV_resource.Stream@PNG-de-DE.png) in the corresponding line in the "Saved recordings" area.

   The record is deleted.

**Note**

**Traces cannot be deleted individually**

You cannot delete traces individually. When you delete a recording, all included traces are deleted.

### Importing and exporting recordings (S7-1500T)

You have the option to export a recording as measurement, as *.ltr or *.csv file. The exported file contains the TCP position values, the OCS position values and the configuration of the kinematics technology object. Optionally, the following values can be exported:

- Up to technology version V6.0: Axis position values
- As of technology version V7.0: Joint position values

You can re-import an exported *.ltr file into the kinematics trace. The recordings saved under measurements cannot be imported into the kinematics trace again.

#### Export record as file

To export a record, proceed as follows:

1. From the list of recordings, select the record to be exported.
2. Click on the symbol ![Export record as file](images/165344870155_DV_resource.Stream@PNG-de-DE.png) in the toolbar.

   The "Export recording" dialog opens.
3. Select "*.csv" or "*.ltr" as file format.
4. Select the storage location.
5. Click "Save".

   The file is exported and saved.

#### Import recording as file

To import a recording, proceed as follows:

1. Click on the symbol ![Import recording as file](images/165344866187_DV_resource.Stream@PNG-de-DE.png) in the toolbar.

   The "Import recording" dialog opens.
2. In the corresponding folder, select the file of the "*.ltr" file format to be imported.
3. Click the "Open" button.

   The file is imported. The recording is displayed in the tabular editor under saved recordings.

#### Save recording as measurement

With the trace you have extended evaluation options to analyze kinematics motion in detail.

To save the recording as a measurement, proceed as follows:

1. Select the current recording or a saved recording.
2. Click on the symbol ![Save recording as measurement](images/134701951883_DV_resource.Stream@PNG-de-DE.png) in the toolbar.

   The recording is saved under "Traces &gt; Measurements".
3. Open the recording stored under "Traces &gt; Measurements" in the trace.

   The recorded parameters are displayed in the trace.

## Calibration (S7-1500T)

This section contains information on the following topics:

- [Brief description of calibration (S7-1500T)](#brief-description-of-calibration-s7-1500t)
- [Using 3D display for the calibration (S7-1500T)](#using-3d-display-for-the-calibration-s7-1500t)
- [Configuring the calibration (S7-1500T)](#configuring-the-calibration-s7-1500t)
- [Moving the kinematics for calibration (S7-1500T)](#moving-the-kinematics-for-calibration-s7-1500t)
- [Display progress and status (S7-1500T)](#display-progress-and-status-s7-1500t)
- [Setting points (S7-1500T)](#setting-points-s7-1500t)
- [Apply or reset values (S7-1500T)](#apply-or-reset-values-s7-1500t)
- [Calibrate object coordinate systems (S7-1500T)](#calibrate-object-coordinate-systems-s7-1500t)
- [Calibrate workspace zones (S7-1500T)](#calibrate-workspace-zones-s7-1500t)

### Brief description of calibration (S7-1500T)

During calibration, you move a kinematics to relevant points and use the position values to determine the exact position of an object coordinate system (OCS) in the world coordinate system (WCS), to check a predefined OCS in the WCS or to define a workspace zone.

Open calibration under "Technology object &gt; Calibration".

Alternatively, you can open the calibration to the following type:

- To calibrate an object coordinate system, select an object coordinate system in the selection box under "Technology object &gt; Configuration &gt; Extended parameters &gt; Object coordinate systems" and click the ![Figure](images/158889361803_DV_resource.Stream@PNG-de-DE.png) symbol.
- To calibrate a workspace zone, go to "Technology object &gt; Configuration &gt; Extended parameters &gt; Zones &gt; Workspace zones" and click the ![Figure](images/158889361803_DV_resource.Stream@PNG-de-DE.png) symbol in the line for the respective workspace zone.

#### Requirement

The kinematics technology object is correctly configured and connected.

#### Structure

Calibration is divided into two views:

- Object coordinate systems
- Workspace zones

Each view is divided into the following areas:

- [Configuration section](#configuring-the-calibration-s7-1500t)
- [3D visualization](#using-3d-display-for-the-calibration-s7-1500t) and [control pad](#operating-the-directional-pad-s7-1500t)
- [Kinematics control panel](#commissioning-s7-1500t)

### Using 3D display for the calibration (S7-1500T)

The 3D display provides you with visual support during calibration. The following values are displayed graphically depending on the configured calibration method:

- Configured points and angles
- Guide lines
- Offset of the OCS from the origin
- Current position of the TCP
- Graphically highlighted active calibration point
- Active and inactive workspace zones

In addition, you can also use the following functions of the 3D visualization for the calibration:

- [Operating the zone display](#operating-the-zone-display-s7-1500t)
- [Selecting values for the calibration](#working-with-the-3d-display-s7-1500t)
- [Monitoring and comparing position values](#monitoring-and-comparing-position-values-s7-1500t)

### Configuring the calibration (S7-1500T)

In the configuration area, select a calibration method and set all the required parameters for the calibration.

The configuration area is structured differently for the calibration of object coordinate systems, the calibration of workspace zones and depending on the selected calibration method.

- [Configuring calibration of an object coordinate system](#calibrate-object-coordinate-systems-s7-1500t)
- [Configuring calibration of a workspace zone](#calibrate-workspace-zones-s7-1500t)

### Moving the kinematics for calibration (S7-1500T)

For the calibration, you can move the kinematics as follows:

- **Offline, move the tool center point in the 3D view using the control pad**

  See also section "[Operating the directional pad](#operating-the-directional-pad-s7-1500t)".
- **Moving real kinematics online**

  You move the real kinematics online via the control panel in the "Jog" or "Jog to target position" mode. In the 3D view, you can see the motion of the kinematics model.

  To specify the target position in the "Jog to target position" mode, you can determine the coordinates with the control pad or enter them directly on the control panel.

  The functionality of the kinematics control panel is described in section "[Commissioning](#commissioning-s7-1500t)".

### Display progress and status (S7-1500T)

The progress and notes on the input of the values are displayed in the configuration area of the calibration method.

The entered values of the calibration are checked for the "Three-point" and "Two-point" methods. The distances between the points in the OCS are compared with the distances between the points in the WCS. Comparison of the points is not required with the "One-point" method.

If the entries are still incomplete, the status indicator is displayed in red. Depending on your inputs, the status indicator shows the following:

- In the case of the ["Three-point"](#move-ocs-and-rotate-around-one-axis-or-two-axes-s7-1500t) calibration method

  - Angle of triangles in the WCS and the OCS, less than 20°
  - Deviation of the points in WCS and OCS to each other greater than 5%
- In the case of the ["Two-point"](#move-ocs-with-the-two-point-calibration-method-s7-1500t) calibration method

  - Deviation of the points in WCS and OCS to each other greater than 5%

Each correctly set point is shown in green in the progress display.

![Figure](images/158889365771_DV_resource.Stream@PNG-de-DE.png)

If your entries are complete and correct, the status indicator "Finished" appears green. You can accept the values in the configuration.

### Setting points (S7-1500T)

To set points, use the following input options:

- Enter the position manually
- Apply TCP position
- Couple coordinates to TCP position

Each of the values displayed in the fields is a position value in the following coordinate system:

- Calibrate object coordinate system: WCS or selected object coordinate system (marking in adjustment range of the individual points)
- Calibrate workspace zone: Coordinate system of the workspace zone (selection in the zone properties)

#### Enter the position manually

1. Enter the position of the workspace zone in the x, y and z directions in the respective field.

#### Apply TCP position

To adopt the current position value of the TCP, proceed as follows:

1. Move the kinematics to a position.

   You can monitor the current position values in the "Positions" window.
2. To adopt the current position value of the TCP, click the ![Apply TCP position](images/158889370891_DV_resource.Stream@PNG-de-DE.png) symbol.

   - To apply all coordinates of a position, click the uppermost and higher-level symbol in the area for a point.
   - To apply the coordinates individually or an angle of a position, click the symbol next to the field for the coordinates or the angle.

   The position value of the TCP is displayed in the selected fields. An angle for a rotation defined by the position value is displayed in the graphical view.

#### Couple coordinates to TCP position

1. To link the coordinates to the TCP, click the ![Couple coordinates to TCP position](images/158889413259_DV_resource.Stream@PNG-de-DE.png) symbol.

   - To couple all coordinates of a position, click the uppermost and higher-level symbol in the area for a point.
   - To couple a single coordinate or angle, click the symbol next to the respective field for the coordinate or angle.

   The symbol changes to ![Couple coordinates to TCP position](images/158889417227_DV_resource.Stream@PNG-de-DE.png) and the position value is coupled to the TCP. The corresponding fields of the coordinates are inactive.
2. Move the kinematics to a position.

   In the corresponding fields of the coupled coordinates, the current value of the TCP is displayed while moving the kinematics. An angle for a rotation defined by the position value is displayed in the graphical view.
3. To decouple the coordinates from the TCP, click the symbol ![Couple coordinates to TCP position](images/158889417227_DV_resource.Stream@PNG-de-DE.png).

   - To decouple all coordinates of a position, click the uppermost and higher-level symbol in the area for a point.
   - To uncouple a single coordinate or angle, click the symbol next to the respective field for the coordinate or angle.

   The corresponding fields of the coordinates can be edited again.
4. To adopt the current position value or the angle of the TCP, click the ![Couple coordinates to TCP position](images/158889370891_DV_resource.Stream@PNG-de-DE.png) symbol.

   The position value of the TCP is displayed in the selected fields. An applied angle is shown in the graphic view .

---

**See also**

[Apply or reset values (S7-1500T)](#apply-or-reset-values-s7-1500t)

### Apply or reset values (S7-1500T)

#### Apply values

If you have entered new values for the calibration and the "status indicator" is green, you can click on the button "Apply values". The values from the calibration are applied to the configuration. If you calibrate an already defined zone and adopt the calibrated values, the previously defined values are overwritten.

The "Apply values" button becomes inactive as soon as the values from the calibration have been successfully applied in the configuration.

#### Reset values

With the "Reset values" button, you reset the entered values of the calibration.

### Calibrate object coordinate systems (S7-1500T)

This section contains information on the following topics:

- [Configuring calibration of an object coordinate system (S7-1500T)](#configuring-calibration-of-an-object-coordinate-system-s7-1500t)
- [Move OCS with the "Two-point" calibration method (S7-1500T)](#move-ocs-with-the-two-point-calibration-method-s7-1500t)
- [Move OCS and rotate around the y axis (S7-1500T)](#move-ocs-and-rotate-around-the-y-axis-s7-1500t)
- [Move OCS with the "One-point" calibration method (S7-1500T)](#move-ocs-with-the-one-point-calibration-method-s7-1500t)
- [Move OCS and rotate around one axis or two axes (S7-1500T)](#move-ocs-and-rotate-around-one-axis-or-two-axes-s7-1500t)
- [Move OCS and rotate around the z axis (S7-1500T)](#move-ocs-and-rotate-around-the-z-axis-s7-1500t)
- [Examples (S7-1500T)](#examples-s7-1500t)

#### Configuring calibration of an object coordinate system (S7-1500T)

##### Requirement

The kinematics technology object is correctly configured and connected.

##### Selecting the object coordinate system

1. Select an OCS from the drop-down list.

##### Selecting the calibration method

Select a calibration method In the drop-down list.

Depending on the type of kinematics, you can use the calibration methods as follows:

| Kinematics type | Definition OCS / Checking the OCS position | Calibration methods |
| --- | --- | --- |
| **2D** | Move OCS | [Two-point](#move-ocs-with-the-two-point-calibration-method-s7-1500t) |
| Move OCS and rotate around the y axis | [Move and rotate around y](#move-ocs-and-rotate-around-the-y-axis-s7-1500t) |  |
| **2D with orientation** | Move OCS | [One-point](#move-ocs-with-the-one-point-calibration-method-s7-1500t) |
| **3D, 3D with 3 orientations and  6-axis articulated arm with central hand** | Move OCS | [Three-point](#move-ocs-and-rotate-around-one-axis-or-two-axes-s7-1500t) |
| Move OCS and rotate around an axis | - [Three-point](#move-ocs-and-rotate-around-one-axis-or-two-axes-s7-1500t) - [Move and rotate](#move-ocs-and-rotate-around-one-axis-or-two-axes-s7-1500t) |  |
| Move OCS and rotate around two axes | - [Three-point](#move-ocs-and-rotate-around-one-axis-or-two-axes-s7-1500t) - [Plane](#move-ocs-and-rotate-around-one-axis-or-two-axes-s7-1500t) |  |
| **3D with orientation and  3D with 2 orientations A, B** | Move OCS | [Two-point](#move-ocs-with-the-two-point-calibration-method-s7-1500t) |
| Move OCS and rotate around the z axis | [Move and rotate around z](#move-ocs-and-rotate-around-the-z-axis-s7-1500t) |  |

#### Move OCS with the "Two-point" calibration method (S7-1500T)

To move the origin of the object coordinate system (OCS) and define the location of the OCS, use the "Two-point" calibration method.

##### "Two-point" calibration method

Using this method, you can move the OCS origin or check the position of an already defined OCS in the WCS.

The calibration method assumes that the defined points for the tool center point (TCP) of the kinematics can be reached.

With this method, you calibrate the OCS based on 2 points. You define the OCS origin using the first item in the menu "1. Set point 1" .

You define the second point in the "2. Set point 2" menu as follows:

- With 2D kinematics: Define a point on the xz plane
- With 3D kinematics with orientation or with 2 orientations: Define a point on the xy plane. The z coordinate is automatically applied from the first point and cannot be changed for the second point.

The points entered in the WCS and in the OCS each form a route. The method compares the length and location of the two distances in the WCS and the OCS. If the deviation between the two distances is greater than 5%, this is shown in red in the status display. If the entries are incomplete, this is also shown in red in the status display.

To compare the actual position of an OCS in the WCS with your configured OCS frames, move the kinematics to the corresponding points.

#### Move OCS and rotate around the y axis (S7-1500T)

To move the origin of the object coordinate system (OCS) and define the position of the OCS, use the "Move and rotate around y" calibration method.

##### "Move and rotate around y" calibration method

With this method, you can move the OCS origin to a point and rotate the OCS with an angle of rotation around the y axis.

In the menu "1. Move origin of OCS", you define the new position of the OCS origin.

In the second step, you define the rotation of the OCS in the menu "2. Rotate OCS around one coordinate axis". First select the x axis or z axis from the "Rotate around" drop-down list. This determines which axis should be rotated around the y axis. Then move the kinematics to a point through which the selected coordinate axis should run after rotation. In the "Angle" field, you accept the value of the TCP and thus define the angle of rotation for the selected coordinate axis and the OCS.

#### Move OCS with the "One-point" calibration method (S7-1500T)

To move the origin of the object coordinate system (OCS) and define the position of the OCS, use the "One-point" calibration method.

##### "One-point" calibration method

Using this method, you can move the OCS origin or check the position of an already defined OCS in the WCS.

The calibration method assumes that the defined points for the tool center point (TCP) of the kinematics can be reached.

With this method, you calibrate the OCS based on one point. In the menu "1. Set point 1" you define the x and z coordinates of the point in the WCS. Then enter the corresponding coordinates in the OCS.

The method checks whether all coordinates for the point have been entered. If the entries are still incomplete, the status indicator is displayed in red.

To compare the actual position of an OCS in the WCS with your configured OCS frames, move the kinematics to the corresponding point.

#### Move OCS and rotate around one axis or two axes (S7-1500T)

Use one of the following calibration methods to move the origin of the object coordinate system (OCS) and define the position of the OCS:

- Move and rotate
- Three-point
- Plane

With the "Move and rotate" calibration method, you can rotate the OCS around 1 axis. If you want to rotate the OCS around a second axis, use the "Three-point" or "Plane" calibration method.

##### "Three-point" calibration method

With this method, you can:

- Move the OCS origin and rotate the OCS around 2 axes
- Check the position of an already defined OCS in the WCS

The calibration method assumes that the defined points for the tool center point (TCP) of the kinematics can be reached.

With this method, you calibrate the OCS based on 3 points. You define the coordinates of the points in the WCS. Then enter the corresponding coordinates in the OCS.

The points entered in the WCS and the OCS each form a triangle. The method compares the angles and side lengths of the two triangles.

The status of the check gives you feedback on the accuracy of your information. Depending on your inputs, the status indicator shows the following:

- Angle of triangles in the WCS and the OCS, less than 20°
- Deviation of the points in WCS and OCS to each other greater than 5%
- Conformity error of the side lengths of the triangle greater than 5%

If the entries are incomplete, this is also shown in red in the status display.

If the two triangles are within the tolerances, the position of the OCS is defined via the 3 points.

To compare the actual position of an OCS in the WCS with your configured OCS frames, move the kinematics to the corresponding points.

##### "Move and rotate" calibration method

With this method, you can move the OCS origin to a point and rotate the OCS with an angle of rotation around one of the three coordinate axes.

In the menu "1. Move origin of OCS", you define the new position of the OCS origin.

In the second step, you define the rotation of the OCS in the menu "2. Rotate OCS around one coordinate axis". First, select a coordinate axis (x, y or zaxis) in the drop-down list "Rotate around" around which the OCS is to be rotated. Then select a coordinate axis in the "Axis to rotate" drop-down list that is to be rotated around the previously selected coordinate axis. To conclude, move the kinematics to a point through which the coordinate axis selected in the second step should pass after the rotation. In the "Angle" field, you accept the value of the TCP and thus define the angle of rotation for the selected coordinate axis and the OCS.

##### "Plane" calibration method

With this method, you can move the OCS origin to a point and rotate the OCS with 2 angles of rotation around 2 coordinate axes.

In the menu "1. Move origin of OCS", you define the new position of the OCS origin.

In the second step, you define the first rotation of the OCS in the menu "2. Rotate coordinate axis to TCP". In the "Axis" drop-down list, first select the coordinate axis (x, y or z-axis) to be rotated to the TCP. Then move the kinematics to a point through which the selected coordinate axis should run after rotation. Adopt the value of the TCP to define the angle of rotation for the selected coordinate axis and the OCS.

In the last step, you define the second rotation of the OCS in the menu "Span plane over two coordinate axes". First select a plane from the "Plane" drop-down list, which is spanned between the previously rotated and a second coordinate axis. Then move the kinematics to a point through which the spanned plane should run. Adopt the value of the TCP to define the angle of rotation for the selected coordinate axes and the OCS.

#### Move OCS and rotate around the z axis (S7-1500T)

To move the origin of the object coordinate system (OCS) and define the position of the OCS, use the "Move and rotate around z" calibration method.

##### "Move and rotate around z" calibration method

With this method, you can move the OCS origin to a point and rotate the OCS with an angle of rotation around the z axis.

In the menu "1. Move origin of OCS", you define the new position of the OCS origin.

In the second step, you define the rotation of the OCS in the menu "2. Rotate OCS around one coordinate axis". First select the x or y axis in the "Rotate around" drop-down list. This determines which axis should be rotated around the z axis. Then move the kinematics to a point through which the selected coordinate axis should run after rotation. In the "Angle" field, you accept the value of the TCP and thus define the angle of rotation for the selected coordinate axis and the OCS.

#### Examples (S7-1500T)

This section contains information on the following topics:

- [Introduction (S7-1500T)](#introduction-s7-1500t)
- [Move OCS 1 (S7-1500T)](#move-ocs-1-s7-1500t)
- [Move OCS 1 and rotate around the y axis (S7-1500T)](#move-ocs-1-and-rotate-around-the-y-axis-s7-1500t)
- [Move OCS 1 and rotate around z axis (S7-1500T)](#move-ocs-1-and-rotate-around-z-axis-s7-1500t)
- [Move OCS 1 and rotate it around the z axis and y axis (S7-1500T)](#move-ocs-1-and-rotate-it-around-the-z-axis-and-y-axis-s7-1500t)

##### Introduction (S7-1500T)

The following examples show you how to calibrate an object coordinate system using the different calibration methods.

The example looks at the following application. A kinematics stacks products on pallets. The products have four different shapes, for which the pallet is repositioned in each case depending on the surrounding area. The position of the pallet is described by the OCS 1 frame. Based on a few details relating to position, the calibration determines the position of the OCS 1 frame after a change of position.

To illustrate all calibration methods, the following examples are carried out with the different types of Cartesian Portal kinematics.

| Kinematics | New position of the pallet | Calibration method used | Example |
| --- | --- | --- | --- |
| Cartesian portal 2D | Position 1 | Two-point | [Move OCS 1](#move-ocs-1-s7-1500t) |
| Cartesian portal 2D with orientation | One-point |  |  |
| Cartesian portal 2D | Position 2 | Move and rotate around y | [Move OCS 1 and rotate around the y axis](#move-ocs-1-and-rotate-around-the-y-axis-s7-1500t) |
| Cartesian portal 3D | Move and rotate |  |  |
| Cartesian portal 3D | Position 3 | Move and rotate | [Move OCS 1 and rotate around z axis](#move-ocs-1-and-rotate-around-z-axis-s7-1500t) |
| Cartesian portal 3D with orientation | Move and rotate around z |  |  |
| Cartesian portal 3D | Position 4 | - Three-point - Plane | [Move OCS 1 and rotate it around the z axis and y axis](#move-ocs-1-and-rotate-it-around-the-z-axis-and-y-axis-s7-1500t) |

###### Pallet

The pallet has the following dimensions:

- Width: 800.0 mm
- Height: 144.0 mm
- Depth: 1200.0 mm

The origin of the pallet is the same for all four positions and has the following position in the WCS:

|  | Position in the WCS (mm) |  |
| --- | --- | --- |
| 2D | 3D |  |
| x | 600.0 | 600.0 |
| y | 0.0 | 600.0 |
| z | 0.0 | 0.0 |

The pallet is rotated differently in each position. The following angles are used for the new positioning:

- **Position 1**

  2D kinematics

  ![Pallet](images/158889444235_DV_resource.Stream@PNG-de-DE.png)

  | Symbol | Meaning |
  | --- | --- |
  | ① | Origin of the pallet |

  3D kinematics

  ![Pallet](images/158889538955_DV_resource.Stream@PNG-de-DE.png)

  | Symbol | Meaning |
  | --- | --- |
  | ① | Origin of the pallet |
- **Position 2**

  2D kinematics

  ![Pallet](images/158889544075_DV_resource.Stream@PNG-de-DE.png)

  | Symbol | Meaning |
  | --- | --- |
  | ① | Origin of the pallet |
  | ② | Rotation with angle B |

  3D kinematics

  ![Pallet](images/158889549195_DV_resource.Stream@PNG-de-DE.png)

  | Symbol | Meaning |
  | --- | --- |
  | ① | Origin of the pallet |
  | ② | Rotation with angle B |
- **Position 3**

  ![Pallet](images/158889421195_DV_resource.Stream@PNG-de-DE.png)

  | Symbol | Meaning |
  | --- | --- |
  | ① | Origin of the pallet |
  | ② | Rotation with angle A |
- **Position 4**

  ![Pallet](images/158889439115_DV_resource.Stream@PNG-de-DE.png)

  | Symbol | Meaning |
  | --- | --- |
  | ① | Origin of the pallet |
  | ② | First rotation with angle A |
  | ③ | Second rotation with angle B |

| Position | Angle |  |  |
| --- | --- | --- | --- |
| A | B | C |  |
| 1 | 0° | 0° | 0° |
| 2 | 0° | -45° | 0° |
| 3 | 45° | 0° | 0° |
| 4 | 45° | 30° | 0° |

###### Kinematics

Execute the examples for each of the kinematics types mentioned in the overview and enter the following values for the geometry:

| Parameters | 2D kinematics / 2D kinematics with orientation | 3D kinematics / 3D kinematics with orientation |
| --- | --- | --- |
| Length L1 | 500.0 mm |  |
| Length L2 | 500.0 mm |  |
| Length L3 | - | 500.0 mm |
| Flange length FL | 100.0 mm |  |
| x minimum | -500.0 mm |  |
| x maximum | 2500.0 mm |  |
| y minimum | - | 0.0 mm |
| y maximum | - | 2000.0 mm |
| z minimum | 0.0 mm |  |
| z maximum | 1000.0 mm |  |

If you want to use a different kinematics, consider the position and dimensions of the pallet when defining the geometric parameters of the kinematics. Make sure that all points are accessible for the kinematics.

##### Move OCS 1 (S7-1500T)

###### Introduction

The pallet was moved in the direction of the x axis in the WCS. Two corner points at the pallet edge are used to determine the new position of the OCS 1 frame.

The position of the first pallet corner defines the origin of the OCS 1. Using the position of the second pallet corner, an additional point for the OCS 1 in the WCS can be determined using the "Two-point" calibration method.

The following methods are used for calibration:

- 2D kinematics: "Two-point" calibration method
- 2D kinematics with orientation: "One-point" calibration method

**Coordinates of the points used in the example**

![Introduction](images/158889771915_DV_resource.Stream@PNG-de-DE.png)

|  |  | Position in the WCS (mm) |  | Position in the OCS (mm) |  |
| --- | --- | --- | --- | --- | --- |
| x | z | x | z |  |  |
| ① | Point P1 on pallet corner | 600.0 | 144.0 | 0.0 | 0.0 |
| ② | Point P2 on pallet corner | 1800.0 | 144.0 | 1200.0 | 0.0 |

###### 2D kinematics: "Two-point" calibration method

Two corner points at the pallet edge are used to determine the new position of the OCS 1 frame.

The position of the first pallet corner defines the origin of the OCS 1. The position of the second pallet corner can be used to determine the position in the WCS for another point.

1. Select the object coordinate system "OCS 1".
2. Select the "Two-point" calibration method in the drop-down list.

Define the origin for the OCS 1 as follows:

1. Move the kinematics to the point P1 ① on the pallet.
2. Accept the position coordinates of the TCP in WCS by clicking on the symbol ![2D kinematics: "Two-point" calibration method](images/158889370891_DV_resource.Stream@PNG-de-DE.png) next to the field "Position in WCS".
3. Enter the values for the position in OCS for the point P1 ①.

   You have defined the origin of OCS 1.

Define the point P2 ② as follows:

1. Move the kinematics to the point P2 ② on the pallet.
2. Define the coordinates for point P2 ② in the WCS by adopting the current position values of the TCP. Click the symbol ![2D kinematics: "Two-point" calibration method](images/158889370891_DV_resource.Stream@PNG-de-DE.png) next to the "Position in WCS" field.
3. For the point P2 ②, enter the values for the position in the OCS.

The position of the OCS is thus unambiguously determined and the "Apply values" button is active.

1. Accept the values from the calibration into the configuration.

###### 2D kinematics with orientation: "One-point" calibration method

A corner point of the pallet is used to determine the new position of the OCS 1 frame.

The position of the pallet corner defines the origin of the OCS 1.

1. Select the object coordinate system "OCS 1".
2. Select the "One-point" calibration method in the drop-down list.

Define the origin for the OCS 1 as follows:

1. Move the kinematics to the point P1 ① on the pallet.
2. Accept the position coordinates of the TCP in WCS by clicking on the symbol ![2D kinematics with orientation: "One-point" calibration method](images/158889370891_DV_resource.Stream@PNG-de-DE.png) next to the field "Position in WCS".
3. Enter the values for the position in OCS for the point P1 ①.

   You have defined the origin of OCS 1.

The position of the OCS is thus unambiguously determined and the "Apply values" button is active.

1. Accept the values from the calibration into the configuration.

##### Move OCS 1 and rotate around the y axis (S7-1500T)

###### Introduction

The pallet has been tilted. Two points at the pallet edge are used to determine the new position of the OCS 1 frame.

The position of the pallet corner defines the origin of the OCS 1. The angle of rotation for the OCS 1 is determined via a point on the pallet edge.

The following methods are used for calibration:

- 3D kinematics: "Move and rotate" calibration method
- 2D kinematics: "Move and rotate around y" calibration method

**Coordinates of the points used in the example**

![Introduction](images/158889777035_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | Point P1 pallet corner |
| ② | Point at pallet edge  The rotated x axis now runs through this point |
| ③ | Angle of rotation OCS 1 |

|  |  | Position in the WCS (mm) |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| 3D kinematics |  |  | 2D kinematics |  |  |  |
| x | y | z | x | z |  |  |
| ① | Point pallet corner | 498.5 | 600.0 | 102.0 | 498.5 | 102.0 |
| ② | Point at pallet edge | 900.0 | 600.0 | 504.0 | 900.0 | 504.0 |

###### 3D kinematics: "Move and rotate" calibration method

1. Select the object coordinate system "OCS 1".
2. Select the "Move and rotate" calibration method in the drop-down list.

Define the origin for the OCS 1 as follows:

1. Move the kinematics to the point P1 ① on the pallet.
2. Accept the position coordinates of the TCP in WCS by clicking the button ![3D kinematics: "Move and rotate" calibration method](images/158889370891_DV_resource.Stream@PNG-de-DE.png) next to the field "Position in WCS".

   You have defined the origin of the OCS 1 with point P1 ①.

Define the angle of rotation ③ for the OCS 1 as follows:

1. Select the y axis as the coordinate axis around which the OCS 1 is rotated.
2. Select the x axis as the coordinate axis that is rotated around the y axis to the TCP or point ②.
3. Move the kinematics to the point ② at the pallet edge.
4. Rotate OCS 1 by clicking on the symbol ![3D kinematics: "Move and rotate" calibration method](images/158889370891_DV_resource.Stream@PNG-de-DE.png) next to the field for the angle.

   The set angle of rotation ③ is shown in the field and in the graphic display . The rotated x axis now runs through the point ②.

The position of the OCS 1 is thus unambiguously determined and the "Apply values" button is active.

1. Accept the values from the calibration into the configuration.

###### 2D kinematics: "Move and rotate around y" calibration method

1. Select the object coordinate system "OCS 1".
2. Select the "Move and rotate around y" calibration method in the drop-down list.

Define the origin for the OCS 1 as follows:

1. Move the kinematics to the point P1 ① on the pallet.
2. Accept the position coordinates of the TCP in WCS by clicking on the symbol ![2D kinematics: "Move and rotate around y" calibration method](images/158889370891_DV_resource.Stream@PNG-de-DE.png) next to the field "Position in WCS".

   You have defined the origin of the OCS 1 with point P1 ①.

Define the angle of rotation ③ for the OCS 1 as follows:

1. Select the rotation of the x axis around the y axis.

   In this way, you specify that the x axis is rotated around the y axis to the TCP or point ②.
2. Move the kinematics to the point ② at the pallet edge.
3. Rotate OCS 1 by clicking on the symbol ![2D kinematics: "Move and rotate around y" calibration method](images/158889370891_DV_resource.Stream@PNG-de-DE.png) next to the field for the angle.

   The set angle of rotation ③ is shown in the field and in the graphic display . The rotated x axis now runs through the point ②.

The position of the OCS 1 is thus unambiguously determined and the "Apply values" button is active.

1. Accept the values from the calibration into the configuration.

##### Move OCS 1 and rotate around z axis (S7-1500T)

###### Introduction

The pallet was rotated horizontally. Two points at the pallet edge are used to determine the new position of the OCS 1 frame.

The position of the pallet corner defines the origin of the OCS 1. The angle of rotation for the OCS 1 is determined via a point on the pallet edge.

The following methods are used for calibration:

- 3D kinematics: "Move and rotate" calibration method
- 3D kinematics with orientation: "Move and rotate around z" calibration method

**Coordinates of the points used in the example**

![Introduction](images/158889986955_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | Point P1 on pallet corner |
| ② | Point at pallet edge  The rotated x axis now runs through this point |
| ③ | Angle of rotation OCS 1 |

|  |  | Position in the WCS (mm) |  |  |
| --- | --- | --- | --- | --- |
| x | y | z |  |  |
| ① | Point P1 on pallet corner | 600.0 | 600.0 | 144.0 |
| ② | Point at pallet edge | 1000.0 | 1000.0 | 144.0 |

###### 3D kinematics: "Move and rotate" calibration method

1. Select the object coordinate system "OCS 1".
2. Select the "Move and rotate" calibration method in the drop-down list.

Define the origin for the OCS 1 as follows:

1. Move the kinematics to the point P1 ① on the pallet.
2. Accept the position coordinates of the TCP in WCS by clicking on the symbol ![3D kinematics: "Move and rotate" calibration method](images/158889370891_DV_resource.Stream@PNG-de-DE.png) next to the field "Position in WCS".

   You have defined the origin of the OCS 1 with point P1.

Define the angle of rotation ③ for the OCS 1 as follows:

1. Select the z axis as the coordinate axis around which the OCS 1 is rotated.
2. Select the x axis as the coordinate axis that is rotated around the z axis to the TCP or point ②.
3. Move the kinematics to the point ② at the pallet edge.
4. Rotate OCS 1 by clicking on the symbol ![3D kinematics: "Move and rotate" calibration method](images/158889370891_DV_resource.Stream@PNG-de-DE.png) next to the field for the angle.

   The set angle of rotation ③ is shown in the field and in the graphic display . The rotated x axis now runs through the point ②.

The position of the OCS 1 is thus unambiguously determined and the "Apply values" button is active.

1. Accept the values from the calibration into the configuration.

###### 3D kinematics with orientation: "Move and rotate around z" calibration method

1. Select the object coordinate system "OCS 1".
2. Select the "Move and rotate around z" calibration method in the drop-down list.

Define the origin for the OCS 1 as follows:

1. Move the kinematics to the point P1 ① on the pallet.
2. Accept the position coordinates of the TCP in WCS by clicking on the symbol ![3D kinematics with orientation: "Move and rotate around z" calibration method](images/158889370891_DV_resource.Stream@PNG-de-DE.png) next to the field "Position in WCS".

   You have defined the origin of the OCS 1 with point P1 ①.

Define the angle of rotation ③ for the OCS 1 as follows:

1. Select the rotation of the x axis around the z axis.

   In this way, you specify that the x axis is rotated around the z axis to the TCP or point ②.
2. Move the kinematics to the point ② at the pallet edge.
3. Rotate OCS 1 by clicking on the symbol ![3D kinematics with orientation: "Move and rotate around z" calibration method](images/158889370891_DV_resource.Stream@PNG-de-DE.png) next to the field for the angle.

   The set angle of rotation ③ is shown in the field and in the graphic display . The rotated x axis now runs through the point ②.

The position of the OCS 1 is thus unambiguously determined and the "Apply values" button is active.

1. Accept the values from the calibration into the configuration.

##### Move OCS 1 and rotate it around the z axis and y axis (S7-1500T)

###### Introduction

The pallet was tilted and also rotated horizontally.

###### 3D kinematics: "Plane" calibration method

Three points on the pallet surface are used to determine the new position of the OCS 1 frame.

The origin of the OCS 1 is determined via the position of a pallet corner. The positions of the other two points are used to determine the angles of rotation for the OCS 1.

The "Plane" calibration method is used for calibration with 3D kinematics.

**Coordinates of the points used in the example**

![3D kinematics: "Plane" calibration method](images/158889992075_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | Point pallet corner as origin of the OCS 1 |
| ② | Point at pallet edge  The set point through which the rotated x axis passes defines the angle of rotation for the x axis. |
| ③ | Angle of rotation for the x axis |
| ④ | Point on pallet surface  The set point, together with the first two points, defines the selected xy plane. |
| ⑤ | xy plane which passes through the three set points |

|  |  | Position in the WCS (mm) |  |  |
| --- | --- | --- | --- | --- |
| x | y | z |  |  |
| ① | Point pallet corner | 549.1 | 549.1 | 124.7 |
| ② | Point pallet edge | 916.5 | 916.5 | 424.7 |
| ④ | Point pallet surface | 633.7 | 1199.3 | 424.7 |

1. Select the object coordinate system "OCS 1".
2. Select the "Plane" calibration method in the drop-down list.

Define the origin for the OCS 1 as follows:

1. Move the kinematics to point P1 on the pallet.
2. Accept the position coordinates of the TCP in WCS by clicking on the symbol ![3D kinematics: "Plane" calibration method](images/158889370891_DV_resource.Stream@PNG-de-DE.png) next to the field "Position in WCS".

   You have defined the origin for OCS 1.

Define the angle of rotation for the OCS 1 as follows:

1. Select the x axis as the coordinate axis to be rotated to the TCP or point ②.
2. Move the kinematics to the point ② at the pallet edge.
3. Rotate OCS 1 by clicking on the symbol ![3D kinematics: "Plane" calibration method](images/158889370891_DV_resource.Stream@PNG-de-DE.png) next to the field for the coordinate axis.

   The set angles of rotation are shown in the graphic display.
4. Select the xy plane to be spanned between the three set points.
5. Move the kinematics to the point ④ on the pallet surface.
6. To align the OCS 1, click the symbol ![3D kinematics: "Plane" calibration method](images/158889370891_DV_resource.Stream@PNG-de-DE.png) next to the field for the plane.

   The spanned plane is shown in the graphic display.

The position of the OCS 1 is thus unambiguously determined and the "Apply values" button is active.

1. Accept the values from the calibration into the configuration.

###### 3D kinematics: "Three-point" calibration method

Three corner points of the pallet are used to determine the new position of the OCS 1 frame.

The positions of the corner points in OCS 1 can be derived from the dimensions of the pallet. The position of the corner points in the WCS is determined using the "three-point" method.

The origin of the OCS 1 is determined via the position of a pallet corner. The positions of the other two corner points are used to determine the angles of rotation for OCS 1.

**Coordinates of the points used in the example**

![3D kinematics: "Three-point" calibration method](images/158889997195_DV_resource.Stream@PNG-de-DE.png)

|  | Position in the WCS (mm) |  |  | Position in the OCS (mm) |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| x | y | z | x | y | z |  |
| Point P1 pallet corner | 549.1 | 549.1 | 124.7 | 0.0 | 0.0 | 0.0 |
| Point P2 pallet corner | 1283.9 | 1283.9 | 724.7 | 1200.0 | 0.0 | 0.0 |
| Point P3 pallet corner | -16.6 | 1114.8 | 124.7 | 0.0 | 800.0 | 0.0 |

1. Select the object coordinate system "OCS 1".
2. Select the "Plane" calibration method in the drop-down list.

Define the origin for the OCS 1 as follows:

1. Move the kinematics to the pallet corner (point P1).
2. Accept the position coordinates of the TCP in WCS by clicking on the symbol ![3D kinematics: "Three-point" calibration method](images/158889370891_DV_resource.Stream@PNG-de-DE.png) next to the field "Position in WCS".
3. For the point P1, enter the values for the position in OCS 1.

   You have defined the origin of OCS 1.

Define the angle of rotation for the OCS 1 as follows:

1. Move the kinematics to the second pallet corner (point P2).
2. Define the coordinates for point P2 in the WCS by adopting the current position values of TCP. Click the symbol ![3D kinematics: "Three-point" calibration method](images/158889370891_DV_resource.Stream@PNG-de-DE.png) next to the "Position in WCS" box.
3. For the point P2, enter the values for the position in the OCS.
4. Move the kinematics to point P3 on the pallet.
5. Define the coordinates for point P3 in the WCS by adopting the current position values of the TCP. Click the symbol ![3D kinematics: "Three-point" calibration method](images/158889370891_DV_resource.Stream@PNG-de-DE.png) next to the "Position in WCS" box.
6. For the point P3, enter the values for the position in the OCS.

The position of the OCS is thus unambiguously determined and the "Apply values" button is active.

1. Accept the values from the calibration into the configuration.

### Calibrate workspace zones (S7-1500T)

This section contains information on the following topics:

- [Configuring calibration of a workspace zone (S7-1500T)](#configuring-calibration-of-a-workspace-zone-s7-1500t)
- [Calibrate cuboid zone with corner points (S7-1500T)](#calibrate-cuboid-zone-with-corner-points-s7-1500t)
- [Calibrate cylindrical zone with surface line (S7-1500T)](#calibrate-cylindrical-zone-with-surface-line-s7-1500t)
- [Calibrate cylindrical zone with circular plane (S7-1500T)](#calibrate-cylindrical-zone-with-circular-plane-s7-1500t)
- [Calibrate spherical zone with diameter (S7-1500T)](#calibrate-spherical-zone-with-diameter-s7-1500t)
- [Calibrate spherical zone with radius (S7-1500T)](#calibrate-spherical-zone-with-radius-s7-1500t)

#### Configuring calibration of a workspace zone (S7-1500T)

##### Requirement

The kinematics technology object is correctly configured and connected.

##### Configuring zone properties

1. In the "Workspace zone" drop-down list, select the zone you want to calibrate.

   If you have opened the calibration for a zone via the symbol ![Configuring zone properties](images/158889361803_DV_resource.Stream@PNG-de-DE.png) in the configuration window "Configuration &gt; Extended parameters &gt; Zones", the corresponding zone is already preselected. If you open the calibration via the project tree, workspace zone 1 is preselected.
2. In the "Status" drop-down list, select the activation status "Active" or "Inactive".

   If you select status "Not defined", all other settings in the configuration mask for the calibration are deactivated.
3. In the "Zone type" drop-down list, select the Blocked zone or Signal zone work zone type.
4. In the "Geometry" drop-down list, select the shape Cuboid, Cylinder or Sphere.
5. In the "Coordinate system" drop-down list, select the "WCS" or an "OCS".

You can find more information on the zone parameters in the section "[Configuring zones](#configuring-zones-s7-1500t-1)".

##### Selecting the suitable calibration method

The selectable calibration methods are dependent on the selected geometry of the zone. The calibration methods "circular plane" and "radius" are not suitable for calibrating zones containing obstacles as the zones are traversed during calibration. As a result, these two calibration methods for calibrating blocked and signal zones which usually contain obstacles are not suitable.

The following table shows an overview of the calibration methods that are suitable for the selected type of zone:

| Selected zone type | Suitable calibration methods |  |  |
| --- | --- | --- | --- |
| ![Selecting the suitable calibration method](images/158890040715_DV_resource.Stream@PNG-de-DE.png) Cuboid | ![Selecting the suitable calibration method](images/158890044811_DV_resource.Stream@PNG-de-DE.png) Cylinder | ![Selecting the suitable calibration method](images/158890048907_DV_resource.Stream@PNG-de-DE.png) Sphere |  |
| **Work zone** | [Corner points](#calibrate-cuboid-zone-with-corner-points-s7-1500t) | [Circular plane](#calibrate-cylindrical-zone-with-circular-plane-s7-1500t) | [Radius](#calibrate-spherical-zone-with-radius-s7-1500t) |
| **Signal zones** | [Surface line](#calibrate-cylindrical-zone-with-surface-line-s7-1500t) | [Diameter](#calibrate-spherical-zone-with-diameter-s7-1500t) |  |
| **Blocked zones** |  |  |  |

The individual points are fixed for each calibration method. However, you can calibrate the individual points in any order.

#### Calibrate cuboid zone with corner points (S7-1500T)

You calibrate a cuboid workspace zone using the "Corner points" calibration method.

##### Definition

With this calibration method, the cuboid zone is defined by the position values of three or four corner points.

![Definition](images/158890206603_DV_resource.Stream@PNG-de-DE.png)

A cuboid workspace zone for 2D kinematics is defined by three points.

![Definition](images/158890211723_DV_resource.Stream@PNG-de-DE.png)

##### Requirements

- The kinematics technology object is correctly configured and connected.
- You have selected a cuboid workspace zone for the calibration.

##### Procedure

1. Enter the origin of the cuboid as point P1.
2. Starting from the origin, use the other points to determine the edge lengths in x, y and z direction.

#### Calibrate cylindrical zone with surface line (S7-1500T)

A cylindrical signal or blocked zone is calibrated using the "Surface line" calibration method.

##### Definition

With this calibration method, the cylindrical zone is defined by the points of the surface line and the diameter.

![Definition](images/158890216843_DV_resource.Stream@PNG-de-DE.png)

##### Requirements

- The kinematics technology object is correctly configured and connected.
- You have selected a cylindrical signal or blocked zone for the calibration.

##### Procedure

1. Set the point P1 as the start of the surface line.
2. Set point P2 as the end of the surface line.

   With the points P1 and P2 you have defined the surface line of the cylinder. The surface line defines the height and orientation of the cylinder.
3. To define the diameter of the cylinder, set point P3 diametrically to the surface line P1 ↔ P2.

   The surface opposite the P1 ↔ P2 surface line runs through the point P3. As the height of the cylinder is defined by surface line P1 ↔ P2, you can also set point P3 outside the cylinder height.

#### Calibrate cylindrical zone with circular plane (S7-1500T)

You calibrate a cylindrical workspace zone using the "Circular plane" calibration method.

##### Definition

With this calibration method, the cylindrical zone is defined by the points of the circular plane and the height.

![Definition](images/158890311563_DV_resource.Stream@PNG-de-DE.png)

##### Requirements

- The kinematics technology object is correctly configured and connected.
- You have selected a cylindrical work zone for the calibration.

##### Procedure

1. Set the point P1 on the circumference of the cylinder.
2. Set point P2 diametrically to point P1 and on the circumference of the cylinder.

   With points P1 and P2, you have defined the diameter and orientation of the cylinder.
3. To define the height of the cylinder, set point P3 at distance h from the circular plane.

   Since point P3 only determines the height of the cylinder, you can also set point P3 outside the previously set cylinder width.

#### Calibrate spherical zone with diameter (S7-1500T)

You calibrate a spherical signal or blocked zone using the "Diameter" calibration method.

##### Definition

With this calibration method, the spherical zone is defined by two points for the diameter.

![Definition](images/158890316683_DV_resource.Stream@PNG-de-DE.png)

##### Requirements

- The kinematics technology object is correctly configured and connected.
- You have selected a spherical signal or blocked zone for the calibration.

##### Procedure

1. Enter the first point on the surface of the sphere as point P1.
2. To form the diameter, enter the point P2 on the surface of the sphere and diametrical to the point P1.

#### Calibrate spherical zone with radius (S7-1500T)

You calibrate a spherical workspace zone using the "Radius" calibration method.

##### Definition

With this calibration method, the spherical zone is defined by two points for the radius.

![Definition](images/158890321803_DV_resource.Stream@PNG-de-DE.png)

##### Requirements

- The kinematics technology object is correctly configured and connected.
- You have selected a spherical work zone for the calibration.

##### Procedure

1. Enter the origin of the sphere as point P1.
2. To determine the radius, set the second point P2 on the surface.

## Tags of the technology object data blocks (S7-1500T)

This section contains information on the following topics:

- [Tags of the kinematics technology object (S7-1500T)](#tags-of-the-kinematics-technology-object-s7-1500t)

### Tags of the kinematics technology object (S7-1500T)

This section contains information on the following topics:

- [Legend (S7-1500T)](#legend-s7-1500t)
- ["Tcp" tag (kinematics) (S7-1500T)](#tcp-tag-kinematics-s7-1500t)
- ["Kinematics" tag (kinematics) (S7-1500T)](#kinematics-tag-kinematics-s7-1500t)
- ["KcsFrame" tag (kinematics) (S7-1500T)](#kcsframe-tag-kinematics-s7-1500t)
- ["OcsFrame[1..3]" tag (kinematics) (S7-1500T)](#ocsframe13-tag-kinematics-s7-1500t)
- ["Tool[1..3]" tag (kinematics) (S7-1500T)](#tool13-tag-kinematics-s7-1500t)
- ["DynamicDefaults" tag (kinematics) (S7-1500T)](#dynamicdefaults-tag-kinematics-s7-1500t)
- ["DynamicLimits" tag (kinematics) (S7-1500T)](#dynamiclimits-tag-kinematics-s7-1500t)
- ["Joint" tag (kinematics) (S7-1500T)](#joint-tag-kinematics-s7-1500t)
- ["AxisCoupling" tag (kinematics) (S7-1500T)](#axiscoupling-tag-kinematics-s7-1500t)
- ["MotionQueue" tag (kinematics) (S7-1500T)](#motionqueue-tag-kinematics-s7-1500t)
- ["Transition" tag (kinematics) (S7-1500T)](#transition-tag-kinematics-s7-1500t)
- ["Override" tag (kinematics) (S7-1500T)](#override-tag-kinematics-s7-1500t)
- ["Conveyor" variable (kinematics) (S7-1500T)](#conveyor-variable-kinematics-s7-1500t)
- ["WorkspaceZone[1..10]" tag (kinematics) (S7-1500T)](#workspacezone110-tag-kinematics-s7-1500t)
- ["KinematicsZone[2..10]" tag (kinematics) (S7-1500T)](#kinematicszone210-tag-kinematics-s7-1500t)
- ["StatusPath" tag (kinematics) (S7-1500T)](#statuspath-tag-kinematics-s7-1500t)
- ["TcpInWcs" tag (kinematics) (S7-1500T)](#tcpinwcs-tag-kinematics-s7-1500t)
- ["TcpInOcs[1..3]" tag (kinematics) (S7-1500T)](#tcpinocs13-tag-kinematics-s7-1500t)
- ["StatusOcsFrame[1..3]" tag (kinematics) (S7-1500T)](#statusocsframe13-tag-kinematics-s7-1500t)
- ["StatusKinematics" tag (kinematics) (S7-1500T)](#statuskinematics-tag-kinematics-s7-1500t)
- ["AxesData" tag (kinematics) (S7-1500T)](#axesdata-tag-kinematics-s7-1500t)
- ["JointData" tag (kinematics) (S7-1500T)](#jointdata-tag-kinematics-s7-1500t)
- ["FlangeInKcs" tag (kinematics) (S7-1500T)](#flangeinkcs-tag-kinematics-s7-1500t)
- ["StatusTool" tag (kinematics) (S7-1500T)](#statustool-tag-kinematics-s7-1500t)
- ["StatusConveyor[1..3]" tag (kinematics) (S7-1500T)](#statusconveyor13-tag-kinematics-s7-1500t)
- ["StatusWorkspaceZone[1..10]" tag (kinematics) (S7-1500T)](#statusworkspacezone110-tag-kinematics-s7-1500t)
- ["StatusKinematicsZone[2..10]" tag (kinematics) (S7-1500T)](#statuskinematicszone210-tag-kinematics-s7-1500t)
- ["StatusZoneMonitoring" tag (kinematics) (S7-1500T)](#statuszonemonitoring-tag-kinematics-s7-1500t)
- ["StatusMotionQueue" tag (kinematics) (S7-1500T)](#statusmotionqueue-tag-kinematics-s7-1500t)
- ["KinematicsAxis" tag (kinematics) (S7-1500T)](#kinematicsaxis-tag-kinematics-s7-1500t)
- ["Units" tag (kinematics) (S7-1500T)](#units-tag-kinematics-s7-1500t)
- ["StatusInterpreterMotion" tag (kinematics) (S7-1500T)](#statusinterpretermotion-tag-kinematics-s7-1500t)
- ["StatusWord" tag (kinematics) (S7-1500T)](#statusword-tag-kinematics-s7-1500t)
- ["ErrorWord" tag (kinematics) (S7-1500T)](#errorword-tag-kinematics-s7-1500t)
- ["ErrorDetail" tag (kinematics) (S7-1500T)](#errordetail-tag-kinematics-s7-1500t)
- ["WarningWord" tag (kinematics) (S7-1500T)](#warningword-tag-kinematics-s7-1500t)
- ["ControlPanel" tag (kinematics) (S7-1500T)](#controlpanel-tag-kinematics-s7-1500t)

#### Legend (S7-1500T)

|  |  |  |
| --- | --- | --- |
| Tag | Name of the tag |  |
| Data type | Data type of the tag |  |
| Values | Value range of the tag - minimum value to maximum value  (L - linear specification R - rotary specification)  If no specific value is shown, the value range limits of the relevant data type apply or the information under "Description". |  |
| W | Effectiveness of changes in the technology data block |  |
| DIR | Direct:  Values are changed via direct assignment and take effect at the start of the next MC_Servo. |  |
| CAL | At call of Motion Control instruction:  Values are changed directly and take effect at the start of the next MC_Servo after the call of the corresponding Motion Control instruction in the user program. |  |
| RES | Restart:  Changes to the start value in the load memory are made using the extended instruction "WRIT_DBL" (write to DB in load memory). Changes will not take effect until after restart of the technology object. |  |
| RON | Read only:  The tag cannot and must not be changed during runtime of the user program. |  |
| Description | Description of the tag |  |

Access to the tags is with "&lt;TO&gt;.&lt;tag name&gt;". The placeholder &lt;TO&gt; represents the name of the technology object.

#### "Tcp" tag (kinematics) (S7-1500T)

The tag structure "&lt;TO&gt;.Tcp.&lt;Tag name&gt;" contains the position of the tool center point (TCP), the TCP frame in the World Coordinate System (WCS).

##### Tags

[Legend](#legend-s7-1500t)

| Tag |  | Data type | Values | W | Description |
| --- | --- | --- | --- | --- | --- |
| Tcp. |  | TO_Struct_Kinematics_StatusKinematicsFrameTcp |  |  |  |
|  | x | LREAL | -1.0E12 … 1.0E12 | RON | x coordinate |
| y | LREAL | -1.0E12 … 1.0E12 | RON | y coordinate |  |
| z | LREAL | -1.0E12 … 1.0E12 | RON | z coordinate |  |
| a | LREAL | -180.0 to 179.999 | RON | A coordinate |  |
| b | LREAL | -90.0 to 90.0 | RON | B coordinate |  |
| c | LREAL | -180.0 to 179.999 | RON | C coordinate |  |

---

**See also**

[Tags: Coordinate systems and frames (S7-1500T)](#tags-coordinate-systems-and-frames-s7-1500t)

#### "Kinematics" tag (kinematics) (S7-1500T)

The tag structure "&lt;TO&gt;.Kinematics.&lt;Tag name&gt;" contains the defined kinematics type.

##### Tags

[Legend](#legend-s7-1500t)

| Tag |  | Data type | Values | W | Description |  |
| --- | --- | --- | --- | --- | --- | --- |
| Kinematics. |  | TO_Struct_Kinematics_Kinematics |  |  |  |  |
|  | TypeOfKinematics | DINT | 1 to 36 | RON | Kinematics type  The configuration is performed using the function view. |  |
| 1 | Cartesian portal 2D |  |  |  |  |  |
| 2 | Cartesian portal 2D with orientation |  |  |  |  |  |
| 3 | Cartesian portal 3D |  |  |  |  |  |
| 4 | Cartesian portal 3D with orientation |  |  |  |  |  |
| 5 | Roller picker 2D |  |  |  |  |  |
| 6 | Roller picker 2D with orientation |  |  |  |  |  |
| 7 | Roller picker 3D (vertical) |  |  |  |  |  |
| 8 | Roller picker 3D with orientation (vertical) |  |  |  |  |  |
| 9 | Roller picker 3D with orientation (horizontal) |  |  |  |  |  |
| 10 | SCARA 3D with orientation |  |  |  |  |  |
| 11 | Articulated arm 2D |  |  |  |  |  |
| 12 | Articulated arm 2D with orientation |  |  |  |  |  |
| 13 | Articulated arm 3D |  |  |  |  |  |
| 14 | Articulated arm 3D with orientation |  |  |  |  |  |
| 15 | Delta picker 2D |  |  |  |  |  |
| 16 | Delta picker 2D with orientation |  |  |  |  |  |
| 17 | Delta picker 3D |  |  |  |  |  |
| 18 | Delta picker 3D with orientation |  |  |  |  |  |
| 19 | Reserved |  |  |  |  |  |
| 20 | SCARA 2D with orientation |  |  |  |  |  |
| 21 | Cylindrical robot 3D |  |  |  |  |  |
| 22 | Cylindrical robot 3D with orientation |  |  |  |  |  |
| 23 | Tripod 3D |  |  |  |  |  |
| 24 | Tripod 3D with orientation |  |  |  |  |  |
| 25 | 6-axis articulated arm with central hand |  |  |  |  |  |
| 26 | Cartesian portal 3D with 2 orientations A, B |  |  |  |  |  |
| 27 | Delta picker 3D with 2 orientations A, B |  |  |  |  |  |
| 28 to 30 | Reserved |  |  |  |  |  |
| 31 | User-defined 2D |  |  |  |  |  |
| 32 | User-defined 2D with orientation A |  |  |  |  |  |
| 33 | User-defined 3D |  |  |  |  |  |
| 34 | User-defined 3D with orientation A |  |  |  |  |  |
| 36 | User-defined 3D with 3 orientations |  |  |  |  |  |
| Parameter[1..32] | ARRAY [1..32] OF LREAL | -1.0E12 … 1.0E12 | RES | Kinematics-specific parameters |  |  |

---

**See also**

[Tags: Cartesian portal (S7-1500T)](#tags-cartesian-portal-s7-1500t)
  
[Tags: Delta picker (S7-1500T)](#tags-delta-picker-s7-1500t)
  
[Tags: Roller picker (S7-1500T)](#tags-roller-picker-s7-1500t)
  
[Tags: Articulated arm (S7-1500T)](#tags-articulated-arm-s7-1500t)
  
[Tags: Cylindrical robot (S7-1500T)](#tags-cylindrical-robot-s7-1500t)
  
[Tags: Tripod (S7-1500T)](#tags-tripod-s7-1500t)
  
[Tags: SCARA (S7-1500T)](#tags-scara-s7-1500t)
  
[Tags: User-defined kinematics systems (S7-1500T)](#tags-user-defined-kinematics-systems-s7-1500t)

#### "KcsFrame" tag (kinematics) (S7-1500T)

The tag structure "&lt;TO&gt;.KcsFrame.&lt;Tag name&gt;" contains the frame of the Kinematic Coordinate System (KCS) in the World Coordinate System (WCS).

##### Tags

[Legend](#legend-s7-1500t)

| Tag |  | Data type | Value range | W | Description |
| --- | --- | --- | --- | --- | --- |
| KcsFrame. |  | TO_Struct_Kinematics_Frame |  |  |  |
|  | x | LREAL | -1.0E12 … 1.0E12 | RES | x coordinate |
| y | LREAL | -1.0E12 … 1.0E12 | RES | y coordinate |  |
| z | LREAL | -1.0E12 … 1.0E12 | RES | z coordinate |  |
| a | LREAL |  | RES | A coordinate |  |
| 0.0 | With kinematics type:  - "2D" - "2D with orientation" |  |  |  |  |
| -180.0 to 179.999 | With kinematics type:  - "3D" - "3D with orientation" - "3D with 2 orientations" - "3D with 3 orientations" - "with central hand" |  |  |  |  |
| b | LREAL |  | RES | B coordinates |  |
| 0.0 | With kinematics type:  - "2D with orientation" - "3D with orientation" - "3D with 2 orientations" |  |  |  |  |
| -90.0 to 90.0 | With kinematics type:  - "3D" - "with central hand" |  |  |  |  |
| -180.0 to 179.999 | With kinematics type:   - "2D" |  |  |  |  |
| c | LREAL |  | RES | C coordinates |  |
| 0.0 | With kinematics type:  - "2D" - "2D with orientation" - "3D with orientation" - "3D with 2 orientations" |  |  |  |  |
| -180.0 to 179.999 | With kinematics type:  - "3D" - "3D with 3 orientations" - "with central hand" |  |  |  |  |

---

**See also**

[Tags: Coordinate systems and frames (S7-1500T)](#tags-coordinate-systems-and-frames-s7-1500t)

#### "OcsFrame[1..3]" tag (kinematics) (S7-1500T)

The tag structure "&lt;TO&gt;.OcsFrame[1..3].&lt;Tag name&gt;" contains the frames of the Object Coordinate Systems 1 to 3 (OCS) in the World Coordinate System (WCS).

##### Tags

| Tag |  | Data type | Value range | W | Description |
| --- | --- | --- | --- | --- | --- |
| OcsFrame[1..3]. |  | ARRAY [1..3] OF TO_Struct_Kinematics_Frame |  |  |  |
|  | x | LREAL | -1.0E12 … 1.0E12 | RES | x coordinate |
| y | LREAL | -1.0E12 … 1.0E12 | RES | y coordinate |  |
| z | LREAL | -1.0E12 … 1.0E12 | RES | z coordinate |  |
| a | LREAL |  | RES | A coordinate |  |
| 0.0 | With kinematics type:  - "2D" - "2D with orientation" |  |  |  |  |
| -180.0 to 179.999 | With kinematics type:  - "3D" - "3D with orientation" - "3D with 2 orientations" - "3D with 3 orientations" - "with central hand" |  |  |  |  |
| b | LREAL |  | RES | B coordinates |  |
| 0.0 | With kinematics type:  - "2D with orientation" - "3D with orientation" - "3D with 2 orientations" |  |  |  |  |
| -90.0 to 90.0 | With kinematics type:  - "3D" - "with central hand" |  |  |  |  |
| -180.0 to 179.999 | With kinematics type "2D" |  |  |  |  |
| c | LREAL |  | RES | C coordinates |  |
| 0.0 | With kinematics type:  - "2D" - "2D with orientation" - "3D with orientation" - "3D with 2 orientations" |  |  |  |  |
| -180.0 to 179.999 | With kinematics type:  - "3D" - "3D with 3 orientations" - "with central hand" |  |  |  |  |

---

**See also**

[Tags: Coordinate systems and frames (S7-1500T)](#tags-coordinate-systems-and-frames-s7-1500t)
  
[Legend (S7-1500T)](#legend-s7-1500t)

#### "Tool[1..3]" tag (kinematics) (S7-1500T)

The tag structure "&lt;TO&gt;.Tool[1..3].&lt;Tag name&gt;" contains the tool frame in the Flange Coordinate System (FCS).

##### Tags

[Legend](#legend-s7-1500t)

| Tag |  |  | Data type | Value range | W | Description |
| --- | --- | --- | --- | --- | --- | --- |
| Tool[1..3]. |  |  | ARRAY [1..3] OF TO_Struct_Kinematics_Tool |  |  |  |
|  | Frame. |  | TO_Struct_Kinematics_KinematicsFrame |  |  |  |
|  | x | LREAL | -1.0E12 … 1.0E12 | RES | x coordinate in the FCS |  |
| y | LREAL | -1.0E12 … 1.0E12 | RES | y coordinate in the FCS |  |  |
| z | LREAL | -1.0E12 … 1.0E12 | RES | z coordinate in the FCS |  |  |
| a | LREAL |  | RES | A coordinate |  |  |
| 0.0 | With kinematics type:  - "2D" - "3D" - "3D with 2 orientations A, B" |  |  |  |  |  |
| -180.0 to 179.999 | With kinematics type:  - "2D with orientation" - "3D with orientation" - "3D with 3 orientations" - "with central hand" |  |  |  |  |  |
| b | LREAL |  | RES | B coordinates |  |  |
| 0.0 | With kinematics type:  - "2D" - "2D with orientation" - "3D" - "3D with orientation" |  |  |  |  |  |
| -180.0 to 179.999 | With kinematics type:  - "3D with 2 orientations A, B" |  |  |  |  |  |
| -90.0 to 90.0 | With kinematics type:  - "3D with 3 orientations" - "with central hand" |  |  |  |  |  |
| c | LREAL |  | RES | C coordinates |  |  |
| 0.0 | With kinematics type:  - "2D" - "2D with orientation" - "3D" - "3D with orientation" - "3D with 2 orientations A, B" |  |  |  |  |  |
| -180.0 to 179.999 | With kinematics type:  - "3D with 3 orientations" - "with central hand" |  |  |  |  |  |

---

**See also**

[Tags: Coordinate systems and frames (S7-1500T)](#tags-coordinate-systems-and-frames-s7-1500t)

#### "DynamicDefaults" tag (kinematics) (S7-1500T)

The tag structure "&lt;TO&gt;.DynamicDefaults.&lt;Tag name&gt;" contains the configuration of the dynamic presets. These settings will be used when you specify a dynamic value less than 0.0 for a Motion Control instruction. Changes to the default dynamics will be applied at the next positive edge at the "Execute" parameter of a Motion Control instruction.

##### Tags

[Legend](#legend-s7-1500t)

| Tag |  |  | Data type | Values | W | Description |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| DynamicDefaults. |  |  | TO_Struct_Kinematics_DynamicDefaults |  |  |  |  |
|  | Path. |  | TO_Struct_Kinematics_Dynamics |  |  |  |  |
|  | Velocity | LREAL | 0.0 to 1.0E12 | DIR | Default setting of the velocity of the path |  |  |
| Acceleration | LREAL | 0.0 to 1.0E12 | DIR | Default setting of the acceleration of the path |  |  |  |
| Deceleration | LREAL | 0.0 to 1.0E12 | DIR | Default setting of the deceleration of the path |  |  |  |
| Jerk | LREAL | 0.0 to 1.0E12 | DIR | Default setting of the jerk of the path |  |  |  |
| Orientation. |  | TO_Struct_Kinematics_OrientationDynamics |  |  |  |  |  |
|  | Velocity | LREAL | 0.0 to 1.0E12 | DIR | Default setting of the velocity of the Cartesian orientation |  |  |
| Acceleration | LREAL | 0.0 to 1.0E12 | DIR | Default setting of the acceleration of the Cartesian orientation |  |  |  |
| Deceleration | LREAL | 0.0 to 1.0E12 | DIR | Default setting of the deceleration of the Cartesian orientation |  |  |  |
| Jerk | LREAL | 0.0 to 1.0E12 | DIR | Default setting of the jerk of the Cartesian orientation |  |  |  |
| DynamicAdaption |  | DINT | 0 to 2 | CAL | Default setting of the dynamic adaptation |  |  |
| 0 | No dynamic adaptation |  |  |  |  |  |  |
| 1 | Dynamic adaptation with segmentation of the path |  |  |  |  |  |  |
| 2 | Dynamic adaptation without segmentation of the path |  |  |  |  |  |  |
| MoveDirect |  | TO_Struct_Kinematics_MoveDirectDynamics |  |  |  |  |  |
|  | VelocityFactor | LREAL | 0.0 to 1.0E12 | CAL | Factor for the velocity of the axis motions in relation to the respective maximum velocity of the axes with sPTP motion. |  |  |
| AccelerationFactor | LREAL | 0.0 to 1.0E12 | CAL | Factor for the acceleration of the axis motions in relation to the respective maximum acceleration of the axes with sPTP motion. |  |  |  |
| DecelerationFactor | LREAL | 0.0 to 1.0E12 | CAL | Factor for the deceleration of the axis motions in relation to the respective maximum deceleration of the axes with sPTP motion. |  |  |  |
| JerkFactor | LREAL | 0.0 to 1.0E12 | CAL | Factor for the jerk of the axis motions in relation to the respective maximum jerk of the axes with sPTP motion. |  |  |  |

---

**See also**

[Tags: Kinematics motions (S7-1500T)](#tags-kinematics-motions-s7-1500t)

#### "DynamicLimits" tag (kinematics) (S7-1500T)

The tag structure "&lt;TO&gt;.DynamicLimits.&lt;Tag name&gt;" contains the configuration of the dynamic limits. During Motion Control, no dynamic values greater than the dynamic limits are permitted. If you have specified greater values in a Motion Control instruction, then motion is performed using the dynamic limits, and a warning is indicated (alarm 501 to 503 - Dynamic values are limited).

##### Tags

[Legend](#legend-s7-1500t)

| Tag |  |  | Data type | Values | W | Description |
| --- | --- | --- | --- | --- | --- | --- |
| DynamicLimits. |  |  | TO_Struct_Kinematics_DynamicLimits |  |  |  |
|  | Path. |  | TO_Struct_Kinematics_Dynamics |  |  |  |
|  | Velocity | LREAL | 0.0 to 1.0E12 | DIR | Dynamic limitation for the maximum velocity of the path |  |
| Acceleration | LREAL | 0.0 to 1.0E12 | DIR | Dynamic limitation for the maximum acceleration of the path |  |  |
| Deceleration | LREAL | 0.0 to 1.0E12 | DIR | Dynamic limitation for the maximum deceleration of the path |  |  |
| Jerk | LREAL | 0.0 to 1.0E12 | DIR | Dynamic limitation for the maximum jerk of the path |  |  |
| Orientation. |  | TO_Struct_Kinematics_OrientationDynamics |  |  |  |  |
|  | Velocity | LREAL | 0.0 to 1.0E12 | DIR | Dynamic limitation for the maximum velocity of the Cartesian orientation |  |
| Acceleration | LREAL | 0.0 to 1.0E12 | DIR | Dynamic limitation for the maximum acceleration of the Cartesian orientation |  |  |
| Deceleration | LREAL | 0.0 to 1.0E12 | DIR | Dynamic limitation for the maximum deceleration of the Cartesian orientation |  |  |
| Jerk | LREAL | 0.0 to 1.0E12 | DIR | Dynamic limitation for the maximum jerk of the Cartesian orientation |  |  |

---

**See also**

[Tags: Kinematics motions (S7-1500T)](#tags-kinematics-motions-s7-1500t)

#### "Joint" tag (kinematics) (S7-1500T)

The tag structure "&lt;TO&gt;.Joint.&lt;Tag name&gt;" contains the configuration of the joints for kinematics types with more than four interpolating kinematics axes.

##### Tags

[Legend](#legend-s7-1500t)

| Tag |  |  | Data type | Value range | W | Description |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Joint. |  |  | TO_Struct_Kinematics_Joint |  |  |  |  |
|  | J[1..6]. |  | ARRAY [1..6] OF TO_Struct_Kinematics_JointParameters |  |  |  |  |
|  | InverseDirection | BOOL | - | RES | FALSE | Direction of movement of the joint corresponds to the defined direction of movement of the [kinematics type](#kinematics-types-s7-1500t) |  |
| TRUE | Direction of movement of the joint is inverse to the defined direction of movement of the [kinematics type](#kinematics-types-s7-1500t) |  |  |  |  |  |  |
| Offset | LREAL | -1.0E12 … 1.0E12 | RES | Difference between the defined zero position of the joint of the [kinematics type](#kinematics-types-s7-1500t) and the mechanical zero position of the joint at the kinematics used |  |  |  |
| LowerLimit | LREAL | -5.0E11 … 5.0E11,  -5.0E8 … 5.0E8 <sup>1)</sup> | RES | Lower limit of the joint traversing range |  |  |  |
| UpperLimit | LREAL | -5.0E11 … 5.0E11,  -5.0E8 … 5.0E8 <sup>1)</sup> | RES | Upper limit of the joint traversing range |  |  |  |
| <sup>1)</sup> If position values with higher resolution are used |  |  |  |  |  |  |  |

#### "AxisCoupling" tag (kinematics) (S7-1500T)

The tag structure "&lt;TO&gt;.AxisCoupling.&lt;Tag name&gt;" contains the configuration of the mechanical axis coupling for kinematics types with more than four interpolating kinematics axes.

##### Tags

[Legend](#legend-s7-1500t)

| Tag |  |  | Data type | Value range | W | Description |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| AxisCoupling. |  |  | TO_Struct_Kinematics_AxisCoupling |  |  |  |  |
|  | N[1..5]. |  | ARRAY [1..5] OF TO_Struct_Kinematics_AxisCouplingParameters |  |  |  |  |
|  | Enable | BOOL | - | RES | FALSE | Mechanical axis coupling is disabled |  |
| TRUE | Mechanical axis coupling is enabled |  |  |  |  |  |  |
| CausingAxis | DINT | 1 to 6 | RES | Mechanically coupled axis that is moved |  |  |  |
| AffectedAxis | DINT | 1 to 6 | RES | Mechanically coupled axis that is also moved |  |  |  |
| Factor | LREAL | -1.0E12 … 1.0E12 | RES | Coupling factor |  |  |  |

#### "MotionQueue" tag (kinematics) (S7-1500T)

The tag structure "&lt;TO&gt;.MotionQueue.&lt;Tag name&gt;" contains the configuration of parameters of the job sequence.

##### Tags

[Legend](#legend-s7-1500t)

| Tag |  | Data type | Values | W | Description |
| --- | --- | --- | --- | --- | --- |
| MotionQueue. |  | TO_Struct_Kinematics_MotionQueue |  |  |  |
|  | MaxNumberOfCommands | DINT | 1 to 10 | RON | Maximum number of commands in job sequence  The configuration takes place in "Technology object &gt; Configuration &gt; Extended parameters &gt; Job sequence". |

---

**See also**

[Tags: Kinematics motions (S7-1500T)](#tags-kinematics-motions-s7-1500t)

#### "Transition" tag (kinematics) (S7-1500T)

The tag structure "&lt;TO&gt;.Transition.&lt;tag name&gt;" contains the configuration of motion jobs.

##### Tags

[Legend](#legend-s7-1500t)

| Tag |  | Data type | Values | W | Description |  |
| --- | --- | --- | --- | --- | --- | --- |
| Transition. |  | TO_Struct_Kinematics_Transition |  |  |  |  |
|  | FactorBlendingLength | LREAL | 0 to 100.0 | DIR | Factor of the maximum rounding distance in percent [%]  The configuration takes place in "Technology object &gt; Configuration &gt; Extended parameters &gt; Job sequence".  Change the factor in the user program before sending the motion jobs to the job sequence so that the change is effective. |  |
| = 0.0 | No blending possible |  |  |  |  |  |
| = 50.0 | Default  This configuration ensures compatibility with projects that are compatible with Motion Control versions &lt; V6.0. |  |  |  |  |  |
| = 100.0 | Blending possible with complete segment length or motion length |  |  |  |  |  |

#### "Override" tag (kinematics) (S7-1500T)

The tag structure "&lt;TO&gt;.Override.&lt;Tag name&gt;" contains the configuration of override parameters.

##### Tags

[Legend](#legend-s7-1500t)

| Tag |  | Data type | Values | W | Description |
| --- | --- | --- | --- | --- | --- |
| Override. |  | TO_Struct_Kinematics_Override |  |  |  |
|  | Velocity | LREAL | 0.0 to 200.0 | DIR | Velocity override  The following values are permitted as velocity correction:  - Path motion: from 0.0% to 200.0% - sPTP motion: from 0.0% to 100.0% |

---

**See also**

[Tags: Kinematics motions (S7-1500T)](#tags-kinematics-motions-s7-1500t)

#### "Conveyor" variable (kinematics) (S7-1500T)

The tag structure "&lt;TO&gt;.Conveyor.&lt;tag name&gt;" contains the configuration of the [Dynamic reserve](#dynamic-adaptation-during-conveyor-tracking-s7-1500t) for the conveyor tracking.

##### Tags

[Legend](#legend-s7-1500t)

| Tag |  | Data type | Value range | W | Description |  |
| --- | --- | --- | --- | --- | --- | --- |
| Conveyor. |  | TO_Struct_Kinematics_Conveyor |  |  |  |  |
|  | DynamicReserve[1..1] | ARRAY [1..1] OF LREAL | 0 to 50 | RES | Dynamic reserve for dynamics changes during conveyor tracking in percent [%]. |  |
| 30% | Default setting (default) |  |  |  |  |  |

#### "WorkspaceZone[1..10]" tag (kinematics) (S7-1500T)

The tag structure "&lt;TO&gt;.WorkspaceZone[1..10].&lt;Tag name&gt;" contains the parameter for the workspace zones.

##### Tags

[Legend](#legend-s7-1500t)

| Tag |  |  | Data type | Values | W | Description |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| WorkspaceZone[1..10]. |  |  | ARRAY [1..10] OF TO_Struct_Kinematics_WorkSpaceZone |  |  |  |  |
|  | Active |  | BOOL | - | RES | FALSE | Workspace zone deactivated |
| TRUE | Workspace zone activated |  |  |  |  |  |  |
| Valid |  | BOOL | - | RES | FALSE | Zone is not defined |  |
| TRUE | Zone is defined |  |  |  |  |  |  |
| Type |  | DINT | 0 to 2 | RES | Type of the workspace zone |  |  |
| 0 | Blocked zone |  |  |  |  |  |  |
| 1 | Work zone |  |  |  |  |  |  |
| 2 | Signal zone |  |  |  |  |  |  |
| ReferenceSystem |  | DINT | 0 … 3 | RES | Reference coordinate system for the workspace zone |  |  |
| 0 | WCS |  |  |  |  |  |  |
| 1 | OCS1 |  |  |  |  |  |  |
| 2 | OCS2 |  |  |  |  |  |  |
| 3 | OCS3 |  |  |  |  |  |  |
| Frame. |  | TO_Struct_Kinematics_Frame |  |  |  |  |  |
|  | x | LREAL | -1.0E12 to 1.0E12 | RES | x coordinate |  |  |
| y | LREAL | -1.0E12 to 1.0E12 | RES | y coordinate |  |  |  |
| z | LREAL | -1.0E12 to 1.0E12 | RES | z coordinate |  |  |  |
| a | LREAL | -180.0 to 179.999 | RES | A coordinate |  |  |  |
| b | LREAL | -90.0 to 90.0 | RES | B coordinate |  |  |  |
| c | LREAL | -180.0 to 179.999 | RES | C coordinate |  |  |  |
| Geometry. |  | TO_Struct_Kinematics_ZoneGeometry |  |  |  |  |  |
|  | Type | DINT | 0 to 2 | RES | Zone geometry |  |  |
| 0 | Cuboid |  |  |  |  |  |  |
| 1 | Sphere |  |  |  |  |  |  |
| 2 | Cylinder |  |  |  |  |  |  |
| Parameter[1..3] | ARRAY [1..3] OF LREAL | 0.0 to 1.0E12 | RES | 1 | Length x (cuboid) or radius (sphere, cylinder) |  |  |
| 2 | Length y (cuboid) or height (cylinder) |  |  |  |  |  |  |
| 3 | Length z (cuboid) |  |  |  |  |  |  |

---

**See also**

[Tags: Zone monitoring (S7-1500T)](#tags-zone-monitoring-s7-1500t)

#### "KinematicsZone[2..10]" tag (kinematics) (S7-1500T)

The tag structure "&lt;TO&gt;.KinematicsZone[2..10].&lt;Tag name&gt;" contains the parameters for kinematic zones.

##### Tags

[Legend](#legend-s7-1500t)

| Tag |  |  | Data type | Values | W | Description |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| KinematicsZone[2..10]. |  |  | ARRAY [2..10] OF TO_Struct_Kinematics_KinematicsZone |  |  |  |  |
|  | Active |  | BOOL | - | RES | FALSE | Kinematics zone deactivated |
| TRUE | Kinematics zone activated |  |  |  |  |  |  |
| Valid |  | BOOL | - | RES | FALSE | Zone is not defined |  |
| TRUE | Zone is defined |  |  |  |  |  |  |
| ReferenceSystem |  | DINT | 0 to 1 | RES | Reference coordinate system for the kinematics zone |  |  |
| 0 | FCS |  |  |  |  |  |  |
| 1 | TCS |  |  |  |  |  |  |
| Frame. |  | TO_Struct_Kinematics_Frame |  |  |  |  |  |
|  | x | LREAL | -1.0E12 to 1.0E12 | RES | x coordinate |  |  |
| y | LREAL | -1.0E12 to 1.0E12 | RES | y coordinate |  |  |  |
| z | LREAL | -1.0E12 to 1.0E12 | RES | z coordinate |  |  |  |
| a | LREAL | -180.0 to 179.999 | RES | A coordinate |  |  |  |
| b | LREAL | -90.0 to 90.0 | RES | B coordinate |  |  |  |
| c | LREAL | -180.0 to 179.999 | RES | C coordinate |  |  |  |
| Geometry. |  | TO_Struct_Kinematics_ZoneGeometry |  |  |  |  |  |
|  | Type | DINT | 0 to 2 | RES | Zone geometry |  |  |
| 0 | Cuboid |  |  |  |  |  |  |
| 1 | Sphere |  |  |  |  |  |  |
| 2 | Cylinder |  |  |  |  |  |  |
| Parameter[1..3] | ARRAY [1..3] OF LREAL | 0.0 to 1.0E12 | RES | 1 | Length x (cuboid) or radius (sphere, cylinder) |  |  |
| 2 | Length y (cuboid) or height (cylinder) |  |  |  |  |  |  |
| 3 | Length z (cuboid) |  |  |  |  |  |  |

---

**See also**

[Tags: Zone monitoring (S7-1500T)](#tags-zone-monitoring-s7-1500t)

#### "StatusPath" tag (kinematics) (S7-1500T)

The tag structure "&lt;TO&gt;.StatusPath.&lt;Tag name&gt;" contains the parameters of the current kinematics movement. With a synchronous "point-to-point" motion (sPTP motion) the parameters "&lt;TO&gt;.StatusPath.Velocity" and "&lt;TO&gt;.StatusPath.Acceleration" = 0.0.

##### Tags

[Legend](#legend-s7-1500t)

| Tag |  | Data type | Values | W | Description |  |
| --- | --- | --- | --- | --- | --- | --- |
| StatusPath. |  | TO_Struct_Kinematics_StatusPath |  |  |  |  |
|  | CoordSystem | DINT | 0 … 100 | RON | Coordinate system of the active motion job |  |
| 0 | World coordinate system |  |  |  |  |  |
| 1, 2, 3 | Object coordinate system 1, 2, 3 |  |  |  |  |  |
| 100 | Machine coordinate system |  |  |  |  |  |
| 101 | Joint coordinate system<sup>1)</sup> |  |  |  |  |  |
| Velocity | LREAL | -1.0E12 … 1.0E12 | RON | Current path velocity (setpoint reference) |  |  |
| Acceleration | LREAL | -1.0E12 … 1.0E12 | RON | Current path acceleration (setpoint reference) |  |  |
| OrientationVelocity | LREAL | 0 to 1.0E12 | RON | Resulting orientation velocity |  |  |
| DynamicAdaption | DINT | 0 ... 2 | RON | Dynamic adaptation |  |  |
| 0 | No dynamic adaptation |  |  |  |  |  |
| 1 | Dynamic adaptation with segmentation of the path |  |  |  |  |  |
| 2 | Dynamic adaptation without segmentation of the path |  |  |  |  |  |
| TotalPathLength | LREAL | 0 to 1.0E12 | RON | Total path length of linear and circular path motions  Sum of:  - Distance of all completed motion jobs - Distance travelled of the active motion job - Remaining distance of the motion job - Calculated distance of all jobs in the job sequence |  |  |
| AccumulatedPathLength | LREAL | 0 to 1.0E12 | RON | Accumulated path length of linear and circular path motions  Sum of:  - Distance of all completed motion jobs - Distance travelled of the active motion job |  |  |
| <sup>1)</sup> Only relevant with more than four kinematics axes. |  |  |  |  |  |  |

---

**See also**

[Tags: Kinematics motions (S7-1500T)](#tags-kinematics-motions-s7-1500t)

#### "TcpInWcs" tag (kinematics) (S7-1500T)

The tag structure "&lt;TO&gt;.TcpInWcs.&lt;Tag name&gt;" contains the parameters for the tool center point (TCP) in the World Coordinate System (WCS).

##### Tags

[Legend](#legend-s7-1500t)

| Tag |  |  | Data type | Values | W | Description |
| --- | --- | --- | --- | --- | --- | --- |
| TcpInWcs. |  |  | TO_Struct_Kinematics_StatusKinematicsFrameWithDynamics |  |  |  |
|  | x. |  | TO_Struct_Kinematics_StatusMotionVector |  |  |  |
|  | Acceleration | LREAL | -1.0E12 … 1.0E12 | RON | Acceleration of path coordinate x |  |
| Position | LREAL | -1.0E12 … 1.0E12 | RON | Position of path coordinate x |  |  |
| Velocity | LREAL | -1.0E12 … 1.0E12 | RON | Velocity of path coordinate x |  |  |
| y. |  | TO_Struct_Kinematics_StatusMotionVector |  |  |  |  |
|  | Acceleration | LREAL | -1.0E12 … 1.0E12 | RON | Acceleration of path coordinate y |  |
| Position | LREAL | -1.0E12 … 1.0E12 | RON | Position of path coordinate y |  |  |
| Velocity | LREAL | -1.0E12 … 1.0E12 | RON | Velocity of path coordinate y |  |  |
| z. |  | TO_Struct_Kinematics_StatusMotionVector |  |  |  |  |
|  | Acceleration | LREAL | -1.0E12 … 1.0E12 | RON | Acceleration of path coordinate z |  |
| Position | LREAL | -1.0E12 … 1.0E12 | RON | Position of path coordinate z |  |  |
| Velocity | LREAL | -1.0E12 … 1.0E12 | RON | Velocity of path coordinate z |  |  |
| a. |  | TO_Struct_Kinematics_StatusMotionVector |  |  |  |  |
|  | Acceleration | LREAL | -1.0E12 … 1.0E12 | RON | Acceleration of rotation A |  |
| Position | LREAL | -1.0E12 … 1.0E12 | RON | Position of rotation A |  |  |
| Velocity | LREAL | -1.0E12 … 1.0E12 | RON | Velocity of rotation A |  |  |
| b. |  | TO_Struct_Kinematics_StatusMotionVector |  |  |  |  |
|  | Acceleration | LREAL | -1.0E12 … 1.0E12 | RON | Acceleration of rotation B |  |
| Position | LREAL | -1.0E12 … 1.0E12 | RON | Position of rotation B |  |  |
| Velocity | LREAL | -1.0E12 … 1.0E12 | RON | Velocity of the rotation B |  |  |
| c. |  | TO_Struct_Kinematics_StatusMotionVector |  |  |  |  |
|  | Acceleration | LREAL | -1.0E12 … 1.0E12 | RON | Acceleration of rotation C |  |
| Position | LREAL | -1.0E12 … 1.0E12 | RON | Position of rotation C |  |  |
| Velocity | LREAL | -1.0E12 … 1.0E12 | RON | Velocity the rotation C |  |  |

---

**See also**

[Tags: Coordinate systems and frames (S7-1500T)](#tags-coordinate-systems-and-frames-s7-1500t)

#### "TcpInOcs[1..3]" tag (kinematics) (S7-1500T)

The tag structure "&lt;TO&gt;.TcpInOcs[1..3].&lt;Tag name&gt;" contains the parameters for the tool center point (TCP) in the Object Coordinate Systems 1 to 3 (OCS).

##### Tags

[Legend](#legend-s7-1500t)

| Tag |  |  | Data type | Values | W | Description |
| --- | --- | --- | --- | --- | --- | --- |
| TcpInOcs[1..3]. |  |  | ARRAY [1..3] OF TO_Struct_Kinematics_StatusKinematicsFrameWithDynamicsOcs |  |  |  |
|  | x. |  | TO_Struct_Kinematics_StatusMotionVectorOcs |  |  |  |
|  | Acceleration | LREAL | -1.0E12 … 1.0E12 | RON | Acceleration of the x coordinate of the tool center point in the object coordinate system 1 to 3 |  |
| Position | LREAL | -1.0E12 … 1.0E12 | RON | x coordinate of the tool center point in the object coordinate system 1 to 3 |  |  |
| Velocity | LREAL | -1.0E12 … 1.0E12 | RON | Velocity of the x coordinate of the tool center point in the object coordinate system 1 to 3 |  |  |
| y. |  | TO_Struct_Kinematics_StatusMotionVectorOcs |  |  |  |  |
|  | Acceleration | LREAL | -1.0E12 … 1.0E12 | RON | Acceleration of the y coordinate of the tool center point in the object coordinate system 1 to 3 |  |
| Position | LREAL | -1.0E12 … 1.0E12 | RON | y coordinate of the tool center point in the object coordinate system 1 to 3 |  |  |
| Velocity | LREAL | -1.0E12 … 1.0E12 | RON | Velocity of the y coordinate of the tool center point in the object coordinate system 1 to 3 |  |  |
| z. |  | TO_Struct_Kinematics_StatusMotionVectorOcs |  |  |  |  |
|  | Acceleration | LREAL | -1.0E12 … 1.0E12 | RON | Acceleration of the z coordinate of the tool center point in the object coordinate system 1 to 3 |  |
| Position | LREAL | -1.0E12 … 1.0E12 | RON | z coordinate of the tool center point in the object coordinate system 1 to 3 |  |  |
| Velocity | LREAL | -1.0E12 … 1.0E12 | RON | Velocity of the z coordinate of the tool center point in the object coordinate system 1 to 3 |  |  |
| a. |  | TO_Struct_Kinematics_StatusMotionVectorOcs |  |  |  |  |
|  | Acceleration | LREAL | -1.0E12 … 1.0E12 | RON | Acceleration of the A coordinate of the tool center point in the object coordinate system 1 to 3 |  |
| Position | LREAL | -1.0E12 … 1.0E12 | RON | A coordinate of the tool center point in the object coordinate system 1 to 3 |  |  |
| Velocity | LREAL | -1.0E12 … 1.0E12 | RON | Velocity of the A coordinate of the tool center point in the object coordinate system 1 to 3 |  |  |
| b. |  | TO_Struct_Kinematics_StatusMotionVectorOcs |  |  |  |  |
|  | Acceleration | LREAL | -1.0E12 … 1.0E12 | RON | Acceleration of the B coordinate of the tool center point in the object coordinate system 1 to 3 |  |
| Position | LREAL | -1.0E12 … 1.0E12 | RON | B coordinate of the tool center point in the object coordinate system 1 to 3 |  |  |
| Velocity | LREAL | -1.0E12 … 1.0E12 | RON | Velocity of the B coordinate of the tool center point in the object coordinate system 1 to 3 |  |  |
| c. |  | TO_Struct_Kinematics_StatusMotionVectorOcs |  |  |  |  |
|  | Acceleration | LREAL | -1.0E12 … 1.0E12 | RON | Acceleration of the C coordinate of the tool center point in the object coordinate system 1 to 3 |  |
| Position | LREAL | -1.0E12 … 1.0E12 | RON | C coordinate of the tool center point in the object coordinate system 1 to 3 |  |  |
| Velocity | LREAL | -1.0E12 … 1.0E12 | RON | Velocity the C coordinate of the tool center point in the object coordinate system 1 to 3 |  |  |

---

**See also**

[Tags: Coordinate systems and frames (S7-1500T)](#tags-coordinate-systems-and-frames-s7-1500t)

#### "StatusOcsFrame[1..3]" tag (kinematics) (S7-1500T)

The tag structure "&lt;TO&gt;.StatusOcsFrame[1..3].&lt;Tag name&gt;" contains the frames of the Object Coordinate Systems 1 to 3 (OCS) in the World Coordinate System (WCS).

##### Tags

[Legend](#legend-s7-1500t)

| Tag |  | Data type | Value range | W | Description |
| --- | --- | --- | --- | --- | --- |
| StatusOcsFrame[1..3]. |  | ARRAY [1..3] OF TO_Struct_Kinematics_StatusFrame |  |  |  |
|  | x | LREAL | -1.0E12 … 1.0E12 | RON | x coordinate in the WCS |
| y | LREAL | -1.0E12 … 1.0E12 | RON | y coordinate in the WCS |  |
| z | LREAL | -1.0E12 … 1.0E12 | RON | z coordinate in the WCS |  |
| a | LREAL |  | RON | A coordinate in the WCS |  |
| 0.0 | With kinematics type:  - "2D" - "2D with orientation" |  |  |  |  |
| -180.0 to 179.999 | With kinematics type:  - "3D" - "3D with orientation" - "3D with 2 orientations" - "3D with 3 orientations" - "with central hand" |  |  |  |  |
| b | LREAL |  | RON | B coordinate in the WCS |  |
| 0.0 | With kinematics type:  - "2D with orientation" - "3D with orientation" - "3D with 2 orientations" |  |  |  |  |
| -90.0 to 90.0 | With kinematics type:  - "3D" - "with central hand" |  |  |  |  |
| -180.0 to 179.999 | With kinematics type "2D" |  |  |  |  |
| c | LREAL |  | RON | C coordinate in the WCS |  |
| 0.0 | With kinematics type:  - "2D" - "2D with orientation" - "3D with orientation" - "3D with 2 orientations" |  |  |  |  |
| -180.0 to 179.999 | With kinematics type:  - "3D" - "3D with 3 orientations" - "with central hand" |  |  |  |  |

---

**See also**

[Tags: Coordinate systems and frames (S7-1500T)](#tags-coordinate-systems-and-frames-s7-1500t)

#### "StatusKinematics" tag (kinematics) (S7-1500T)

The tag structure "&lt;TO&gt;.StatusKinematics.&lt;Tag name&gt;" contains the status of the kinematics.

##### Tags

[Legend](#legend-s7-1500t)

| Tag |  |  | Data type | Values | W | Description |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| StatusKinematics. |  |  | TO_Struct_Kinematics_StatusKinematics |  |  |  |  |
|  | Type5D6D |  | BOOL | - | RON | FALSE | The kinematics type can be operated without "S7-1500T Motion Control KinPlus". |
| TRUE | The kinematics type can only be operated with "S7-1500T Motion Control KinPlus". |  |  |  |  |  |  |
| Valid |  | BOOL | - | RON | Validity of the transformation values |  |  |
| FALSE | Invalid |  |  |  |  |  |  |
| TRUE | Valid |  |  |  |  |  |  |
| LinkConstellation |  | DWORD | 0 … n | RON | Joint position space |  |  |
|  | Bit 0 | - | - | - | Angle α1 of axis A1 in the front/rear area (standard area/overhead area) |  |  |
| 0 | The zero point of the FCS is located in the front area (standard area) of the joint position lines for the axis A1.  α1 = arctan(y<sub>FCS</sub>/x<sub>FCS</sub>) |  |  |  |  |  |  |
| With 6-axis articulated arm with central hand (KinPlus):  The manual root point is located in the front area (standard area) of the joint position lines for joint J1. |  |  |  |  |  |  |  |
| 1 | The zero point of the FCS is located in the rear area (overhead area) of the joint position lines for the axis A1.  α1 = -arctan(y<sub>FCS</sub>/x<sub>FCS</sub>) |  |  |  |  |  |  |
| With 6-axis articulated arm with central hand (KinPlus):  The manual root point is located in the rear area (overhead area) of the joint position lines for joint J1. |  |  |  |  |  |  |  |
| Bit 1 | - | - | - | Angle α2 of axis A2 positive/negative taking into consideration the mechanical axis coupling |  |  |  |
| 0 | α2 positive |  |  |  |  |  |  |
| 1 | α2 negative |  |  |  |  |  |  |
| Bit 2 | - | - | - | Angle α3 of axis A3 positive/negative taking into consideration the mechanical axis coupling |  |  |  |
| 0 | α3 positive |  |  |  |  |  |  |
| With 6-axis articulated arm with central hand (KinPlus):  The manual root point is located on, in the standard area above or in the overhead area below the joint position lines for joint J3. |  |  |  |  |  |  |  |
| 1 | α3 negative |  |  |  |  |  |  |
| With 6-axis articulated arm with central hand (KinPlus):  The manual root point is located in the standard area below or in the overhead above the joint position lines for joint J3. |  |  |  |  |  |  |  |
| Bit 3 | - | - | - | Angle α4 of axis A4 positive/negative taking into consideration the mechanical axis coupling |  |  |  |
| 0 | α4 positive |  |  |  |  |  |  |
| 1 | α4 negative |  |  |  |  |  |  |
| Bit 4 | - | - | - | Geometric joint position joint J5 (KinPlus) |  |  |  |
| 0 | α5 positive |  |  |  |  |  |  |
| 1 | α5 negative or α5 = 0° |  |  |  |  |  |  |
| Bit 5 | - | - | - | Geometric joint position joint J6 (KinPlus) |  |  |  |
| 0 | α6 positive |  |  |  |  |  |  |
| 1 | α6 negative |  |  |  |  |  |  |
| Bit 6 … 31 | - | - | - | Not relevant |  |  |  |

---

**See also**

[Tags: Kinematics transformation (S7-1500T)](#tags-kinematics-transformation-s7-1500t)

#### "AxesData" tag (kinematics) (S7-1500T)

The tag structure "&lt;TO&gt;.AxesData.&lt;Tag name&gt;" contains the setpoints of the kinematics motion for the kinematics axes.

##### Tags

[Legend](#legend-s7-1500t)

| Tag |  |  | Data type | Values | W | Description |
| --- | --- | --- | --- | --- | --- | --- |
| AxesData. |  |  | TO_Struct_Kinematics_AxesData |  |  |  |
|  | A[1..6]. |  | ARRAY [1..6] OF TO_Struct_Kinematics_AxisMotionVector |  |  | Setpoints of the kinematics motion for the kinematics axes A1 to A6 |
|  | Position | LREAL | -1.0E12 … 1.0E12 | RON | Current position setpoint |  |
| Velocity | LREAL | -1.0E12 … 1.0E12 | RON | Current velocity setpoint |  |  |
| Acceleration | LREAL | -1.0E12 … 1.0E12 | RON | Current acceleration setpoint |  |  |

#### "JointData" tag (kinematics) (S7-1500T)

The tag structure "&lt;TO&gt;.JointData.&lt;Tag name&gt;" contains the setpoints of the kinematics motion for the joints.

##### Tags

[Legend](#legend-s7-1500t)

| Tag |  |  | Data type | Values | W | Description |
| --- | --- | --- | --- | --- | --- | --- |
| JointData. |  |  | TO_Struct_Kinematics_StatusJointData |  |  |  |
|  | J[1..6]. |  | ARRAY [1..6] OF TO_Struct_Kinematics_StatusJointMotionVector |  |  | Setpoints of the kinematics motion for the joints J1 to J6 |
|  | Acceleration | LREAL | -1.0E12 … 1.0E12 | RON | Current acceleration setpoint |  |
| Position | LREAL | -1.0E12 … 1.0E12 | RON | Current position setpoint |  |  |
| Velocity | LREAL | -1.0E12 … 1.0E12 | RON | Current velocity setpoint |  |  |

#### "FlangeInKcs" tag (kinematics) (S7-1500T)

The tag structure "&lt;TO&gt;.FlangeInKcs.&lt;Tag name&gt;" contains the parameters for the Flange Coordinate System (FCS) in the Kinematics Coordinate System (KCS).

##### Tags

[Legend](#legend-s7-1500t)

| Tag |  |  | Data type | Values | W | Description |
| --- | --- | --- | --- | --- | --- | --- |
| FlangeInKcs. |  |  | TO_Struct_Kinematics_StatusFlangeInKcs |  |  |  |
|  | x. |  | TO_Struct_Kinematics_StatusMotionVectorKcs |  |  |  |
|  | Acceleration | LREAL | -1.0E12 … 1.0E12 | RON | Acceleration of the x coordinate of the flange coordinate system (FCS) in the kinematics coordinate system (KCS) |  |
| Position | LREAL | -1.0E12 … 1.0E12 | RON | x coordinate of the flange coordinate system in the kinematics coordinate system |  |  |
| Velocity | LREAL | -1.0E12 … 1.0E12 | RON | Velocity of the x coordinate of the flange coordinate system in the kinematics coordinate system |  |  |
| y. |  | TO_Struct_Kinematics_StatusMotionVectorKcs |  |  |  |  |
|  | Acceleration | LREAL | -1.0E12 … 1.0E12 | RON | Acceleration of the y coordinate of the flange coordinate system in the kinematics coordinate system |  |
| Position | LREAL | -1.0E12 … 1.0E12 | RON | y coordinate of the flange coordinate system in the kinematics coordinate system |  |  |
| Velocity | LREAL | -1.0E12 … 1.0E12 | RON | Velocity of the y coordinate of the flange coordinate system in the kinematics coordinate system |  |  |
| z. |  | TO_Struct_Kinematics_StatusMotionVectorKcs |  |  |  |  |
|  | Acceleration | LREAL | -1.0E12 … 1.0E12 | RON | Acceleration of the z coordinate of the flange coordinate system in the kinematics coordinate system |  |
| Position | LREAL | -1.0E12 … 1.0E12 | RON | z coordinate of the flange coordinate system in the kinematics coordinate system |  |  |
| Velocity | LREAL | -1.0E12 … 1.0E12 | RON | Velocity of the z coordinate of the flange coordinate system in the kinematics coordinate system |  |  |
| a. |  | TO_Struct_Kinematics_StatusMotionVectorKcs |  |  |  |  |
|  | Acceleration | LREAL | -1.0E12 … 1.0E12 | RON | Acceleration of the rotation A of the flange coordinate system in the kinematics coordinate system |  |
| Position | LREAL | -1.0E12 … 1.0E12 | RON | Position of the rotation A of the flange coordinate system in the kinematics coordinate system |  |  |
| Velocity | LREAL | -1.0E12 … 1.0E12 | RON | Velocity of the rotation A of the flange coordinate system in the kinematics coordinate system |  |  |
| b. |  | TO_Struct_Kinematics_StatusMotionVectorKcs |  |  |  |  |
|  | Acceleration | LREAL | -1.0E12 … 1.0E12 | RON | Acceleration of the rotation B of the flange coordinate system in the kinematics coordinate system. |  |
| Position | LREAL | -1.0E12 … 1.0E12 | RON | Position of rotation B of the flange coordinate system in the kinematics coordinate system. |  |  |
| Velocity | LREAL | -1.0E12 … 1.0E12 | RON | Velocity of the rotation B of the flange coordinate system in the kinematics coordinate system. |  |  |
| c. |  | TO_Struct_Kinematics_StatusMotionVectorKcs |  |  |  |  |
|  | Acceleration | LREAL | -1.0E12 … 1.0E12 | RON | Acceleration of the rotation C of the flange coordinate system in the kinematics coordinate system. |  |
| Position | LREAL | -1.0E12 … 1.0E12 | RON | Position of the rotation C of the flange coordinate system in the kinematics coordinate system. |  |  |
| Velocity | LREAL | -1.0E12 … 1.0E12 | RON | Velocity of the rotation C of the flange coordinate system in the kinematics coordinate system. |  |  |

---

**See also**

[Tags: Coordinate systems and frames (S7-1500T)](#tags-coordinate-systems-and-frames-s7-1500t)

#### "StatusTool" tag (kinematics) (S7-1500T)

The tag structure "&lt;TO&gt;.StatusTool.&lt;Tag name&gt;" contains the parameters for the tools.

##### Tags

[Legend](#legend-s7-1500t)

| Tag |  |  | Data type | Values | W | Description |
| --- | --- | --- | --- | --- | --- | --- |
| StatusTool. |  |  | TO_Struct_Kinematics_StatusTool |  |  |  |
|  | ActiveTool |  | DINT | 1 to 3 | RON | Currently effective tool |
| Frame[1..3]. |  | ARRAY [1..3] OF TO_Struct_Kinematics_StatusKinematicsFrame |  |  | Current coordinates of tools 1 to 3 |  |
|  | x | LREAL | -1.0E12 … 1.0E12 | RON | x coordinate |  |
| y | LREAL | -1.0E12 … 1.0E12 | RON | y coordinate |  |  |
| z | LREAL | -1.0E12 … 1.0E12 | RON | z coordinate |  |  |
| a | LREAL | -1.0E12 … 1.0E12 | RON | A coordinate |  |  |
| b | LREAL | -1.0E12 … 1.0E12 | RON | B coordinate |  |  |
| c | LREAL | -1.0E12 … 1.0E12 | RON | C coordinate |  |  |

---

**See also**

[Tags: Coordinate systems and frames (S7-1500T)](#tags-coordinate-systems-and-frames-s7-1500t)

#### "StatusConveyor[1..3]" tag (kinematics) (S7-1500T)

The tag structure "&lt;TO&gt;.StatusConveyor[1..3].&lt;Tag name&gt;" contains the conveyor tracking status.

##### Tags

[Legend](#legend-s7-1500t)

| Tag |  |  | Data type | Values | W | Description |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| StatusConveyor[1..3]. |  |  | ARRAY [1..3] OF TO_Struct_Kinematics_StatusConveyor |  |  |  |  |
|  | ConveyorBelt |  | DB_ANY | - | RON | Active leading-value-capable technology object to which the object coordinate system (OCS) is coupled:  Leading-value-capable technology objects are:  - Positioning axis - Synchronous axis - External encoder - Leading axis proxy |  |
| BeltPosition |  | LREAL | - | RON | Position of the leading-value-capable technology object. |  |  |
| ObjectPosition |  | TO_Struct_Kinematics_StatusFrame | - | RON | Object position  Relative offset of the OCS in x direction to the reference position "ConveyorBeltOrigin"  "ObjectPosition.x" = "BeltPosition" - "InitialObjectPosition.x" |  |  |
|  | x | LREAL | -1.0E12 … 1.0E12 | RON | x coordinate |  |  |
| y | LREAL | -1.0E12 … 1.0E12 | RON | y coordinate |  |  |  |
| z | LREAL | -1.0E12 … 1.0E12 | RON | z coordinate |  |  |  |
| a | LREAL | -180.0 to 179.999 | RON | A coordinate |  |  |  |
| b | LREAL | -180.0 to 179.999 | RON | B coordinate |  |  |  |
| c | LREAL | -180.0 to 179.999 | RON | C coordinate |  |  |  |
| TrackingState |  | DINT | 0 to 4 | RON | Conveyor tracking status |  |  |
| 0 | OCS not assigned  The OCS is not assigned to a leading-value-capable technology object. |  |  |  |  |  |  |
| 1 | OCS assigned  The Motion Control instruction "MC_TrackConveyorBelt" is finished and the OCS is assigned to a leading-value-capable technology object. The first path motion job in the tracked OCS can be sent. |  |  |  |  |  |  |
| 2 | TCP synchronizes to OCS  The OCS is assigned to a leading-value-capable technology object. The first path motion job in the tracked OCS is active. |  |  |  |  |  |  |
| 3 | TCP follows OCS  The OCS is assigned to a leading-value-capable technology object.   The first path motion job in the tracked OCS is completed. The kinematics has reached the position programmed in the path motion job. The kinematics follows the motion of the OCS. |  |  |  |  |  |  |
| 4 | TCP desynchronizes from OCS  The motion of the kinematics in the tracked OCS is ended by a motion job in the WCS or a non-tracked OCS. When the motion job is completed, the "TrackingState" changes to 0 and the OCS is not tracked with the object position anymore. |  |  |  |  |  |  |

#### "StatusWorkspaceZone[1..10]" tag (kinematics) (S7-1500T)

The tag structure "&lt;TO&gt;.StatusWorkspaceZone[1..10].&lt;Tag name&gt;" contains the status of the workspace zones.

##### Tags

[Legend](#legend-s7-1500t)

| Tag |  |  | Data type | Values | W | Description |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| StatusWorkspaceZone[1..10]. |  |  | ARRAY [1..10] OF TO_Struct_Kinematics_StatusWorkSpaceZone |  |  |  |  |
|  | Active |  | BOOL | - | RON | FALSE | Workspace zone deactivated |
| TRUE | Workspace zone activated |  |  |  |  |  |  |
| Valid |  | BOOL | - | RON | FALSE | Zone is not defined |  |
| TRUE | Zone is defined |  |  |  |  |  |  |
| Type |  | DINT | 0 ... 2 | RON | Type of the workspace zone |  |  |
| 0 | Blocked zone |  |  |  |  |  |  |
| 1 | Work zone |  |  |  |  |  |  |
| 2 | Signal zone |  |  |  |  |  |  |
| ReferenceSystem |  | DINT | 0 … 3 | RON | Reference coordinate system for the workspace zone |  |  |
| 0 | WCS |  |  |  |  |  |  |
| 1 | OCS1 |  |  |  |  |  |  |
| 2 | OCS2 |  |  |  |  |  |  |
| 3 | OCS3 |  |  |  |  |  |  |
| Frame. |  | TO_Struct_Kinematics_StatusFrame |  |  |  |  |  |
|  | x | LREAL | -1.0E12 … 1.0E12 | RON | x coordinate |  |  |
| y | LREAL | -1.0E12 … 1.0E12 | RON | y coordinate |  |  |  |
| z | LREAL | -1.0E12 … 1.0E12 | RON | z coordinate |  |  |  |
| a | LREAL | -180.0 to 179.999 | RON | A coordinate |  |  |  |
| b | LREAL | -90.0 to 90.0 | RON | B coordinate |  |  |  |
| c | LREAL | -180.0 to 179.999 | RON | C coordinate |  |  |  |
| Geometry. |  | TO_Struct_Kinematics_StatusZoneGeometry |  |  |  |  |  |
|  | Type | DINT | 0 ... 2 | RON | Zone geometry |  |  |
| 0 | Cuboid |  |  |  |  |  |  |
| 1 | Sphere |  |  |  |  |  |  |
| 2 | Cylinder |  |  |  |  |  |  |
| Parameter[1..3] | ARRAY [1..3] OF LREAL | 0.0 to 1.0E12 | RON | 1 | Length x (cuboid) or radius (sphere, cylinder) |  |  |
| 2 | Length y (cuboid) or height (cylinder) |  |  |  |  |  |  |
| 3 | Length z (cuboid) |  |  |  |  |  |  |

---

**See also**

[Tags: Zone monitoring (S7-1500T)](#tags-zone-monitoring-s7-1500t)

#### "StatusKinematicsZone[2..10]" tag (kinematics) (S7-1500T)

The tag structure "&lt;TO&gt;.StatusKinematicsZone[2..10].&lt;Tag name&gt;" contains the status of the kinematics zones.

##### Tags

[Legend](#legend-s7-1500t)

| Tag |  |  | Data type | Values | W | Description |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| StatusKinematicsZone[2..10]. |  |  | ARRAY [2..10] OF TO_Struct_Kinematics_StatusKinematicsZone |  |  |  |  |
|  | Active |  | BOOL | - | RON | FALSE | Kinematics zone deactivated |
| TRUE | Kinematics zone activated |  |  |  |  |  |  |
| Valid |  | BOOL | - | RON | FALSE | Zone is not present |  |
| TRUE | Zone is present |  |  |  |  |  |  |
| ReferenceSystem |  | DINT | 0 to 1 | RON | Reference coordinate system for the kinematics zone |  |  |
| 0 | FCS |  |  |  |  |  |  |
| 1 | TCS |  |  |  |  |  |  |
| Frame. |  | TO_Struct_Kinematics_StatusFrame |  |  |  |  |  |
|  | x | LREAL | -1.0E12 … 1.0E12 | RON | x coordinate |  |  |
| y | LREAL | -1.0E12 … 1.0E12 | RON | y coordinate |  |  |  |
| z | LREAL | -1.0E12 … 1.0E12 | RON | z coordinate |  |  |  |
| a | LREAL | -180.0 to 179.999 | RON | A coordinate |  |  |  |
| b | LREAL | -90.0 to 90.0 | RON | B coordinate |  |  |  |
| c | LREAL | -180.0 to 179.999 | RON | C coordinate |  |  |  |
| Geometry. |  | TO_Struct_Kinematics_StatusZoneGeometry |  |  |  |  |  |
|  | Type | DINT | 0 to 2 | RON | Zone geometry |  |  |
| 0 | Cuboid |  |  |  |  |  |  |
| 1 | Sphere |  |  |  |  |  |  |
| 2 | Cylinder |  |  |  |  |  |  |
| Parameter[1..3] | ARRAY [1..3] OF LREAL | 0.0 to 1.0E12 | RON | 1 | Length x (cuboid) or radius (sphere, cylinder) |  |  |
| 2 | Length y (cuboid) or height (cylinder) |  |  |  |  |  |  |
| 3 | Length z (cuboid) |  |  |  |  |  |  |

---

**See also**

[Tags: Zone monitoring (S7-1500T)](#tags-zone-monitoring-s7-1500t)

#### "StatusZoneMonitoring" tag (kinematics) (S7-1500T)

The tag structure "&lt;TO&gt;.StatusZoneMonitoring.&lt;Tag name&gt;" contains the status of the violated zones.

##### Tags

[Legend](#legend-s7-1500t)

| Tag |  | Data type | Values | W | Description |
| --- | --- | --- | --- | --- | --- |
| StatusZoneMonitoring. |  | TO_Struct_Kinematics_StatusZoneMonitoring |  |  |  |
|  | WorkingZones | DWORD | - | RON | Display of violated work zones  Bit numbers 0 to 9 correspond to the configured zone numbers. |
| BlockedZones | DWORD | - | RON | Display of violated blocked zones  Bit numbers 0 to 9 correspond to the configured zone numbers. |  |
| SignalizingZones | DWORD | - | RON | Display of approached signal zones  Bit numbers 0 to 9 correspond to the configured zone numbers. |  |
| KinematicsZones | DWORD | - | RON | Display of kinematics zones that violate workspace zones  Bit number 0 indicates the monitoring status of the tool center point (TCP). Bit numbers 1 to 9 correspond to the configured zone numbers. |  |

---

**See also**

[Tags: Zone monitoring (S7-1500T)](#tags-zone-monitoring-s7-1500t)

#### "StatusMotionQueue" tag (kinematics) (S7-1500T)

The tag structure "&lt;TO&gt;.StatusMotionQueue.&lt;Tag name&gt;" contains the status of the job sequence.

##### Tags

[Legend](#legend-s7-1500t)

| Tag |  | Data type | Values | W | Description |
| --- | --- | --- | --- | --- | --- |
| StatusMotionQueue. |  | TO_Struct_Kinematics_StatusMotionQueue |  |  |  |
|  | NumberOfCommands | DINT | - | RON | Number of queued jobs in the job sequence |
| NumberOfPreparedCommands | DINT | - | RON | Number of prepared commands in the job sequence |  |

---

**See also**

[Tags: Kinematics motions (S7-1500T)](#tags-kinematics-motions-s7-1500t)

#### "KinematicsAxis" tag (kinematics) (S7-1500T)

The tag structure "&lt;TO&gt;.KinematicsAxis.&lt;Tag name&gt;" contains the defined kinematics axes.

##### Tags

[Legend](#legend-s7-1500t)

| Tag |  | Data type | Values | W | Description |
| --- | --- | --- | --- | --- | --- |
| KinematicsAxis. |  | TO_Struct_Kinematics_KinematicsAxis |  |  |  |
|  | A1 | DB_ANY | - | RON | Technology object data block of the kinematics axis A1 |
| A2 | DB_ANY | - | RON | Technology object data block of the kinematics axis A2 |  |
| A3 | DB_ANY | - | RON | Technology object data block of the kinematics axis A3 |  |
| A4 | DB_ANY | - | RON | Technology object data block of the kinematics axis A4 |  |
| A5 | DB_ANY | - | RON | Technology object data block of the kinematics axis A5 |  |
| A6 | DB_ANY | - | RON | Technology object data block of the kinematics axis A6 |  |

#### "Units" tag (kinematics) (S7-1500T)

The tag structure "&lt;TO&gt;.Units.&lt;Tag name&gt;" contains the configured technological units of measure.

##### Tags

[Legend](#legend-s7-1500t)

| Tag |  | Data type | Values | W | Description |  |
| --- | --- | --- | --- | --- | --- | --- |
| Units. |  | TO_Struct_Kinematics_Units |  |  |  |  |
|  | LengthUnit | UDINT | - | RON | Unit of measure for the position |  |
| 1010 | m |  |  |  |  |  |
| 1013 | mm |  |  |  |  |  |
| 1536 | mm<sup>1)</sup> |  |  |  |  |  |
| 1011 | km |  |  |  |  |  |
| 1014 | µm |  |  |  |  |  |
| 1015 | nm |  |  |  |  |  |
| 1019 | in |  |  |  |  |  |
| 1018 | ft |  |  |  |  |  |
| 1021 | mi |  |  |  |  |  |
| LengthVelocityUnit | UDINT | - | RON | Unit of measure for the velocity |  |  |
| 1062 | mm/s |  |  |  |  |  |
| 1538 | mm/s<sup>1)</sup> |  |  |  |  |  |
| 1061 | m/s |  |  |  |  |  |
| 1524 | mm/min |  |  |  |  |  |
| 1525 | m/min |  |  |  |  |  |
| 1526 | mm/h |  |  |  |  |  |
| 1063 | m/h |  |  |  |  |  |
| 1527 | km/min |  |  |  |  |  |
| 1064 | km/h |  |  |  |  |  |
| 1066 | in/s |  |  |  |  |  |
| 1069 | in/min |  |  |  |  |  |
| 1067 | ft/s |  |  |  |  |  |
| 1070 | ft/min |  |  |  |  |  |
| 1075 | mi/h |  |  |  |  |  |
| AngleUnit | UDINT | - | RON | Unit of measure for the position of the rotary axes |  |  |
| 1004 | rad |  |  |  |  |  |
| 1005 | ° |  |  |  |  |  |
| 1537 | °<sup>1)</sup> |  |  |  |  |  |
| AngleVelocityUnit | UDINT | - | RON | Unit of measure for the velocity of the rotary axes |  |  |
| 1521 | °/s |  |  |  |  |  |
| 1522 | °/min |  |  |  |  |  |
| 1539 | °/s<sup>1)</sup> |  |  |  |  |  |
| 1086 | rad/s |  |  |  |  |  |
| 1523 | rad/min |  |  |  |  |  |
| <sup>1)</sup> Position values with higher resolution or six decimal places |  |  |  |  |  |  |

---

**See also**

[Units of measure (S7-1500T)](#units-of-measure-s7-1500t)

#### "StatusInterpreterMotion" tag (kinematics) (S7-1500T)

The tag structure "&lt;TO&gt;.StatusInterpreterMotion.&lt;tag name&gt;" contains status information on motion jobs controlled by a technology object Interpreter.

##### Tags

[Legend](#legend-s7-1500t)

| Tag |  |  | Data type | Values | W | Description |
| --- | --- | --- | --- | --- | --- | --- |
| StatusInterpreterMotion. |  |  | TO_Struct_Kinematics_StatusInterpreterMotion |  |  |  |
|  | StatusWord. |  | DWORD | - | RON | Status information |
|  | Bit 0 | - | - | - | "ControlledByInterpreter"  An MCL job is processed or active or the bit is set via the MCL instruction "[setControlledByInterpreter()](Using%20S7-1500T%20Interpreter%20functions%20%28S7-1500T%29.md#setcontrolledbyinterpreter-set-controlledbyinterpreter-bit-for-a-technology-object-s7-1500t)". |  |
| Bit 1 | - | - | - | "MotionByInterpreter"  An MCL motion job is in effect. |  |  |
| Bit 2 …   Bit 31 | - | - | - | Reserved |  |  |

#### "StatusWord" tag (kinematics) (S7-1500T)

The "&lt;TO&gt;.StatusWord" tag contains the status information of the technology object.

Information on the evaluation of the individual bits (e.g. bit 2 "RestartActive") can be found in the "[Evaluating StatusWord, ErrorWord and WarningWord](S7-1500-S7-1500T%20Motion%20Control%20Overview%20%28S7-1500%2C%20S7-1500T%29.md#evaluate-statusword-errorword-and-warningword-s7-1500-s7-1500t)" section of the "S7-1500/S7-1500T Motion Control Overview" documentation.

##### Tags

[Legend](#legend-s7-1500t)

| Tag |  | Data type | Values | W | Description |
| --- | --- | --- | --- | --- | --- |
| StatusWord |  | DWORD | - | RON | Status information of the technology object |
|  | Bit 0 | - | - | - | Reserved |
| Bit 1 | - | - | - | "Error"  An error is present. |  |
| Bit 2 | - | - | - | "RestartActive"  A restart is active. The technology object is being reinitialized. |  |
| Bit 3 | - | - | - | "OnlineStartValuesChanged"  The restart tags have been changed. For the changes to be applied, the technology object must be reinitialized. |  |
| Bit 4 | - | - | - | "ControlPanelActive"  The kinematics control panel is activated. |  |
| Bit 5 | - | - | - | Reserved |  |
| Bit 6 | - | - | - | "Done"  No motion job is in progress and the kinematics control panel is deactivated. |  |
| Bit 7 | - | - | - | Reserved |  |
| Bit 8 | - | - | - | "LinearCommand"  A linear motion is active. |  |
| Bit 9 | - | - | - | "CircularCommand"  A circular motion is active. |  |
| Bit 10 | - | - | - | Reserved |  |
| Bit 11 | - | - | - | "DirectCommand"  A synchronous point-to-point motion is active. |  |
| Bit 12 | - | - | - | "ConstantVelocity"  The velocity setpoint is reached. The path motion of the kinematics is moving at this constant velocity or is at a standstill. |  |
| Bit 13 | - | - | - | "Accelerating"  An acceleration operation of a path motion is active. |  |
| Bit 14 | - | - | - | "Decelerating"  A deceleration operation of a path motion is active. |  |
| Bit 15 | - | - | - | "OrientationMotion"  An orientation motion is active. |  |
| Bit 16 | - | - | - | "Stopping"  An "MC_GroupStop" job is running. The motion of the kinematics technology object is aborted |  |
| Bit 17 | - | - | - | "Interrupted"  The motion of the kinematics technology object is interrupted with an "MC_GroupInterrupt" job. The motion can be continued with a "MC_GroupContinue" command. |  |
| Bit 18 | - | - | - | "Blending"  A blending segment is active. |  |
| Bit 19 | - | - | - | "InSimulation"  The technology object is in simulation. |  |
| Bit 20 | - | - | - | Reserved |  |
| Bit 21 | - | - | - | "EnabledJCS"  The kinematics technology object uses the JCS. |  |
| Bit 22 | - | - | - | Reserved |  |
| Bit 23 | - | - | - | Reserved |  |
| Bit 24 | - | - | - | "StandardOrientationMode5D"  A linear or circular motion of a 3D kinematics with 2 orientations is active. |  |
| Bit 25 | - | - | - | "StandardOrientationMode6D"  A linear or circular motion of a 3D kinematics with 3 orientations is active. |  |
| Bit 26 …  Bit 31 | - | - | - | Reserved |  |

#### "ErrorWord" tag (kinematics) (S7-1500T)

The "&lt;TO&gt;.ErrorWord" tag indicates technology object errors (technology alarms).

Information on the evaluation of the individual bits (e.g. bit 3 "CommandNotAccepted") can be found in the "[Evaluating StatusWord, ErrorWord and WarningWord](S7-1500-S7-1500T%20Motion%20Control%20Overview%20%28S7-1500%2C%20S7-1500T%29.md#evaluate-statusword-errorword-and-warningword-s7-1500-s7-1500t)" section of the "S7-1500/S7-1500T Motion Control Overview" documentation.

##### Tags

[Legend](#legend-s7-1500t)

| Tag |  | Data type | Values | W | Description |
| --- | --- | --- | --- | --- | --- |
| ErrorWord |  | DWORD | - | RON |  |
|  | Bit 0 | - | - | - | "SystemFault"  A system-internal error has occurred. |
| Bit 1 | - | - | - | "ConfigFault"  Configuration error  One or more configuration parameters are inconsistent or invalid. |  |
| Bit 2 | - | - | - | "UserFault"  Error in the user program at a Motion Control instruction or its use (e.g. by the kinematics control panel). |  |
| Bit 3 | - | - | - | "CommandNotAccepted"  Job cannot be executed  A Motion Control instruction cannot be executed because the necessary conditions have not been met. |  |
| Bit 4 | - | - | - | "TransformationFault"  Error in the kinematics transformation |  |
| Bit 5 | - | - | - | Reserved |  |
| Bit 6 | - | - | - | "DynamicError"  Specified dynamic values are limited to permissible values. |  |
| Bit 7 | - | - | - | "ConveyorFault"  Error in the conveyor tracking |  |
| Bit 8 | - | - | - | "JointLimit"   Joint traversing range limit approached or overtraveled. |  |
| Bit 9 …  Bit 31 | - | - | - | Reserved |  |

#### "ErrorDetail" tag (kinematics) (S7-1500T)

The tag structure "&lt;TO&gt;.ErrorDetail.&lt;Tag name&gt;" contains the alarm number and the effective local alarm response for the technology alarm that is currently pending on the technology object.

You can find a list of the technology alarms and alarm responses in the "[Overview of the technology alarms](S7-1500-S7-1500T%20Motion%20Control%20alarms%20and%20error%20IDs%20%28S7-1500%2C%20S7-1500T%29.md#overview-of-the-technology-alarms-s7-1500-s7-1500t)" section of the "S7-1500/S7-1500T Motion Control alarms and error IDs" documentation.

##### Tags

[Legend](#legend-s7-1500t)

| Tag |  | Data type | Values | W | Description |  |
| --- | --- | --- | --- | --- | --- | --- |
| ErrorDetail. |  | TO_Struct_Kinematics_ErrorDetail |  |  |  |  |
|  | Number | UDINT | - | RON | Alarm number |  |
| Reaction | DINT | 0, 11, 12 | RON | Effective alarm response |  |  |
| 0 | No reaction (warnings only) |  |  |  |  |  |
| 11 | Stop without leaving the path |  |  |  |  |  |
| 12 | Stop with maximum dynamic values of the axes |  |  |  |  |  |

#### "WarningWord" tag (kinematics) (S7-1500T)

The "&lt;TO&gt;.WarningWord" tag indicates pending warnings at the technology object.

Information on the evaluation of the individual bits (e.g. bit 2 "UserFault") can be found in the "[Evaluating StatusWord, ErrorWord and WarningWord](S7-1500-S7-1500T%20Motion%20Control%20Overview%20%28S7-1500%2C%20S7-1500T%29.md#evaluate-statusword-errorword-and-warningword-s7-1500-s7-1500t)" section of the "S7-1500/S7-1500T Motion Control overview" documentation.

##### Tags

[Legend](#legend-s7-1500t)

| Tag |  | Data type | Values | W | Description |
| --- | --- | --- | --- | --- | --- |
| WarningWord |  | DWORD | - | RON |  |
|  | Bit 0 | - | - | - | "SystemFault"  A system-internal error has occurred. |
| Bit 1 | - | - | - | "ConfigFault"  Configuration error  One or more configuration parameters will be adjusted internally. |  |
| Bit 2 | - | - | - | "UserFault"  Error in user program at a Motion Control instruction or its use |  |
| Bit 3 | - | - | - | "CommandNotAccepted"  Job cannot be executed  A Motion Control instruction cannot be executed because the necessary conditions have not been met. |  |
| Bit 4 | - | - | - | Reserved |  |
| Bit 5 | - | - | - | Reserved |  |
| Bit 6 | - | - | - | "DynamicWarning"  Specified dynamic values are limited to permissible values. |  |
| Bit 7 …  Bit 31 | - | - | - | Reserved |  |

#### "ControlPanel" tag (kinematics) (S7-1500T)

The tag structure "&lt;TO&gt;.ControlPanel.&lt;tag name&gt;" contains no relevant data for you. This tag structure is internally used.

##### Tags

[Legend](#legend-s7-1500t)

| Tag |  |  |  | Data type | Values | W | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ControlPanel. |  |  |  | TO_Struct_Kinematics_ControlPanel |  |  |  |
|  | Input. |  |  | TO_Struct_Kinematics_ControlPanelInput |  |  |  |
|  | TimeOut |  | LREAL | 100 to 60000 | DIR | - |  |
| EsLifeSign |  | UDINT | - | DIR | - |  |  |
| Command[1..3]. |  | ARRAY [1..3] OF TO_Struct_Kinematics_ControlPanelInput |  |  |  |  |  |
|  | ReqCounter | UDINT | - | DIR | - |  |  |
| Type | UDINT | - | DIR | - |  |  |  |
| Position[1..6] | ARRAY [1..6] OF LREAL | - | DIR | - |  |  |  |
| Velocity[1..2] | ARRAY [1..2] OF LREAL | - | DIR | - |  |  |  |
| Acceleration[1..2] | ARRAY [1..2] OF LREAL | - | DIR | - |  |  |  |
| Deceleration[1..2] | ARRAY [1..2] OF LREAL | - | DIR | - |  |  |  |
| Jerk[1..2] | ARRAY [1..2] OF LREAL | - | DIR | - |  |  |  |
| Param[1..9] | ARRAY [1..9] OF LREAL | - | DIR | - |  |  |  |
| CoordinateSystem | UDINT | - | DIR | - |  |  |  |
| ToolNumber | UDINT | - | DIR | - |  |  |  |
| Output. |  |  | TO_Struct_Kinematics_ControlPanelOutput |  |  |  |  |
|  | RtLifeSign |  | UDINT | - | RON | - |  |
| Command[1..3]. |  | ARRAY [1..3] OF TO_Struct_Kinematics_ControlPanelOutputCmd |  |  |  |  |  |
|  | AckCounter | UDINT | - | RON | - |  |  |
| Error | BOOL | - | RON | - |  |  |  |
| ErrorID | WORD | - | RON | - |  |  |  |
| Done | BOOL | - | RON | - |  |  |  |
| Aborted | BOOL | - | RON | - |  |  |  |

---
title: "SINAMICS MV drives"
package: Stdr013000UIenUS
topics: 112
source: Siemens TIA Portal Information System (offline help, en-US)
---


# SINAMICS MV drives

This section contains information on the following topics:

- [Overview](#overview)
- [Drive objects of the SINAMICS MV](#drive-objects-of-the-sinamics-mv)
- [Parameterization](#parameterization)
- [Diagnostics](#diagnostics)

## Overview

The motor connected to a vector control is simulated in a vector model based on data from the equivalent circuit diagram. The motor model is emulated as precisely as possible to obtain the best results regarding control precision and control quality.

There are two variants of vector control:

- Sensorless vector control (SLVC) as frequency control
- Vector control with sensor as speed-torque control with speed feedback

Properties of the vector control:

- Normal computing speed
- Best speed accuracy
- Best speed ripple
- Best torque accuracy
- Best torque ripple

Vector control can be used with or without an actual speed value sensor.

**Using an actual speed value sensor**

An actual speed value sensor is required if the following criteria apply:

- High speed accuracy is required
- High dynamic response is required

  - Better control behavior
  - Better response to disturbances
- Torque control is required in a control range greater than 1:10
- Allows a defined and/or variable torque for speeds below approx. 10% of the rated motor frequency (p0310) to be maintained.

With regard to setpoint specification, vector control is divided into:

- Speed control
- Torque/current control (in short: torque control)

**Differences with respect to vector V/f control**

Compared with vector V/f control, vector control offers the following benefits:

- Stability for load and setpoint changes
- Short rise times for setpoint changes (→ better control behavior)
- Short settling times for load changes (→ better response to disturbances)
- Acceleration and braking are possible with maximum settable torque
- Motor protection due to variable torque limitation in motorized and regenerative mode
- Drive and braking torque controlled independently of the speed
- Maximum breakaway torque possible at speed 0

## Drive objects of the SINAMICS MV

The drive objects of SINAMICS MV map the following devices:

| Drive object | Devices |
| --- | --- |
| Vectorgl | GL150 |
| Vectormv | GM150/SM150 |
| Vectorsl | SL150 |
| Vector3p | SM120 |
| Vectorm2c | SM120/GH150 |

## Parameterization

This section contains information on the following topics:

- [Basic parameterization](#basic-parameterization)
- [Setpoint channel](#setpoint-channel)
- [Open-loop/closed-loop control](#open-loopclosed-loop-control)
- [Drive functions](#drive-functions)
- [Technology functions](#technology-functions)
- [Control logic](#control-logic)

### Basic parameterization

This section contains information on the following topics:

- [MV function modules](#mv-function-modules)
- [MV control type](#mv-control-type)
- [Limitations MV](#limitations-mv)
- [MV enable logic](#mv-enable-logic)
- [Data sets](#data-sets)

#### MV function modules

You can connect various function modules for the associated deployed drive axis or for the deployed infeed. The function modules that can be activated are listed in the "Function modules" screen form.

> **Note**
>
> You can only activate or deactivate function modules offline.

These are the function modules that can be used:

| Function module | Explanation |
| --- | --- |
| **Frequently used function modules** |  |
| [Technology controller](#technology-controller) (r0108.16) | Activates the "Technology controller" subarea with four configuration screen forms in the "Technology functions" area. The activated function module is also the basic requirement for the "Bypass mode" screen form. |
| [Extended messages/monitoring](#mv-load-torque-monitoring) (r0108.17) | The "Messages and monitoring" function is complemented in the "Drive functions" area by the "Load torque monitoring" function. |
| Speed/torque control ([r0108](SINAMICS%20Parameter%20VECTORMV.md#r0108-drive-objects-function-module).2) | Extends the "Friction characteristic" function with two configuration screen forms in the "Drive functions" area.   Extends the "Open-loop/closed-loop control" area with the configuration screen forms of the following functions:  - [Speed setpoint filter](#speed-setpoint-filter) - [Speed controller](#speed-controller) - [Torque setpoints](#torque-setpoints) - [Current setpoint filter](#current-setpoint-filter) - [Current controller](#current-controller) - [Motor encoder](#motor-encoder)   The function module is activated in the default setting. |
| Free function blocks | In the parameter view, activates the parameters for the F blocks (p20030 … p20288). The free function blocks can only be parameterized in the parameter view. |

##### Requirement

- The drive axis is OFFLINE.

  The entire basic parameter assignment can only be performed offline for the selected drive axis.

##### Activating a function module

1. Activate the required function module by clicking the option.

   Repeat this for all other function modules that you want to activate.
2. Save the project to save the settings.

##### Additional parameters

---

#### MV control type

##### Control types

The following control types are available for vector-controlled drives:

- V/f control with linear characteristic
- V/f control with parabolic characteristic
- I/f control with fixed current
- Speed control (encoderless)
- Speed control (with encoder)
- Torque control (encoderless)
- Torque control (with encoder)

In addition, a maximum of 6 vector drives of the control types mentioned can also be operated with speed control/torque control. Instead of a vector drive with additional speed control/torque control, 2 drives can be operated without speed control/torque control.

##### Requirement

- The motor used in the device configuration of the drive axis has been completely specified and configured.

  This basic parameterization cannot be performed without complete configuration.

##### Selecting the control type

1. Select one of the control types listed above ([p1300](SINAMICS%20Parameter%20VECTORMV.md#p13000n-open-loopclosed-loop-control-operating-mode)).

   The screen form is structured according to the selected control type.
2. If you want to additionally operate the drive with speed control/torque control, enable the option "Speed/torque control".

   Note that only 6 vector drives can be operated at the same time with this speed/torque control.

**Note**

If a "V/f control..." is selected as the control type, other setting screen forms in the secondary navigation of the drive axis, such as current controller or current setpoint filter, are automatically hidden.

##### Terminology for the use of linear motors

When linear motors are used, a linear motion is executed instead of a rotary motion. The terms change accordingly:

- Speed corresponds to velocity
- Torque corresponds to force

##### Additional parameters

- [r0108](SINAMICS%20Parameter%20VECTORMV.md#r0108-drive-objects-function-module)
- p1300

---

#### Limitations MV

##### Description

The basic properties of the drive control are defined with the "Operating parameters".

| Number | Name | Description |
| --- | --- | --- |
| [p0640](SINAMICS%20Parameter%20VECTORMV.md#p06400n-current-limit) | Current limit | Determines the limit value of the motor overload current. |
| [p1080](SINAMICS%20Parameter%20VECTORMV.md#p10800n-minimum-speed) | Minimum speed | Setting of the lowest possible speed/velocity. This value is not fallen below in operation. |
| [p1082](SINAMICS%20Parameter%20VECTORMV.md#p10820n-maximum-speed) | Maximum rotational speed | Setting of the highest possible speed/velocity. The value is calculated during the commissioning phase in accordance with the motor and drive unit and can only be equal to or less than the value in [p0322](SINAMICS%20Parameter%20VECTORMV.md#p03220n-maximum-motor-speed) (maximum motor speed). |
| [p1120](SINAMICS%20Parameter%20VECTORMV.md#p11200n-ramp-function-generator-ramp-up-time) | Ramp-up time | Ramp-up/ramp-down time always refers to the time interval from motor standstill to the set maximum speed (without using roundings). |
| [p1121](SINAMICS%20Parameter%20VECTORMV.md#p11210n-ramp-function-generator-ramp-down-time) | Ramp-down time |  |
| [p1135](SINAMICS%20Parameter%20VECTORMV.md#p11350n-off3-ramp-down-time) | OFF3 ramp-down time | The OFF3 ramp-down time is effective from the maximum speed down to the motor standstill. |

##### Requirement

- The motor used in the device configuration of the drive axis has been completely specified and configured.

  This basic parameterization cannot be performed without complete configuration.

##### Additional parameters

- p0640

---

#### MV enable logic

If telegrams were interconnected during commissioning, these interconnections are displayed here and an additional specification is not required.

If no telegrams were specified previously, then you must interconnect the required signal sources via the enable logic.

The enable logic can be carried out ONLINE as well as OFFLINE.

##### Interconnecting signal sources

1. Interconnect the signal source for the "OFF1 (low-active)" command ([p0840](SINAMICS%20Parameter%20VECTORMV.md#p08400n-bi-on-off-off1)).

   This command corresponds to control word 1 bit 0 (STW1.0) in the PROFIdrive profile.
2. Interconnect the 1st signal source for the "OFF2 (low-active) signal source 1" command ([p0844](SINAMICS%20Parameter%20VECTORMV.md#p08440n-bi-no-coast-down-coast-down-off2-signal-source-1)).

   This command corresponds to control word 1 bit 1 (STW1.1) in the PROFIdrive profile.
3. Interconnect the 2nd signal source for the "OFF2 (low-active) signal source 2" command ([p0845](SINAMICS%20Parameter%20VECTORMV.md#p08450n-bi-no-coast-down-coast-down-off2-signal-source-2)).
4. Interconnect the 1st signal source for the "OFF2 (low-active) signal source 1" command ([p0848](SINAMICS%20Parameter%20VECTORMV.md#p08480n-bi-no-quick-stop-quick-stop-off3-signal-source-1)).

   This command corresponds to control word 1 bit 2 (STW1.2) in the PROFIdrive profile.
5. Interconnect the 2nd signal source for the "OFF2 (low-active) signal source 2" command ([p0849](SINAMICS%20Parameter%20VECTORMV.md#p08490n-bi-no-quick-stop-quick-stop-off3-signal-source-2)).

   This command corresponds to control word 1 bit 2 (STW1.2) in the PROFIdrive profile.
6. Interconnect the signal source for the "Release operation" command ([p0852](SINAMICS%20Parameter%20VECTORMV.md#p08520n-bi-enable-operationinhibit-operation)).

   This command corresponds to control word 1 bit 3 (STW1.3) in the PROFIdrive profile.
7. Interconnect the signal source for the "Enable speed controller" command ([p0856](SINAMICS%20Parameter%20VECTORMV.md#p08560n-bi-enable-speed-controller)).

##### Additional parameters

---

#### Data sets

This section contains information on the following topics:

- [Fundamentals](#fundamentals)
- [Structure of the data set screen form](#structure-of-the-data-set-screen-form)
- [Managing a command data set (CDS)](#managing-a-command-data-set-cds)
- [Managing a drive data set (DDS)](#managing-a-drive-data-set-dds)
- [Activating or editing data sets](#activating-or-editing-data-sets)
- [Switching data sets](#switching-data-sets)

##### Fundamentals

###### Overview

For many applications it is beneficial if multiple parameters can be changed simultaneously by means of an external signal during operation or when the system is ready for operation. This can be carried out with the aid of indexed parameters. For the purpose of this function, the parameters have been combined in such a way that they form groups or data sets and are indexed. By using the indexing, several different settings can be stored for each parameter and activated by changing the data set (i.e. switching back and forth between the data sets).

Those parameters (connector and binector inputs) that are used to control the converter and enter a setpoint are assigned to the command data set (CDS).

The drive data set (DDS) contains various adjustable parameters that are relevant for the open-loop and closed-loop motor control.

You can configure the data sets for each drive within a project:

- You create the corresponding components in the device configuration.
- You configure the available data sets in Startdrive while creating new data sets or deleting existing data sets.

###### Function diagrams (FD)

- FD-8560 (54)
- FD-8565 (54)
- Data sets - encoder data sets (EDS) - 8570 -
- Data sets - motor data sets (MDS) - 8575 -

###### Parameters

- [p0120](SINAMICS%20Parameter%20VECTORMV.md#p0120-number-of-power-unit-data-sets-pds)
- [p0130](SINAMICS%20Parameter%20VECTORMV.md#p0130-number-of-motor-data-sets-mds)
- [p0139](SINAMICS%20Parameter%20VECTORMV.md#p013902-copy-motor-data-set-mds)
- [p0140](SINAMICS%20Parameter%20VECTORMV.md#p0140-number-of-encoder-data-sets-eds)
- [p0170](SINAMICS%20Parameter%20VECTORMV.md#p0170-number-of-command-data-sets-cds)
- [p0180](SINAMICS%20Parameter%20VECTORMV.md#p0180-number-of-drive-data-sets-dds)
- [p0809](SINAMICS%20Parameter%20VECTORMV.md#p080902-copy-command-data-set-cds)
- [p0819](SINAMICS%20Parameter%20VECTORMV.md#p081902-copy-drive-data-set-dds)

---

---

**See also**

[Activating or editing data sets](#activating-or-editing-data-sets)
  
[Data set definitions](Configuring%20SINAMICS%20S-G-MV%20drives.md#data-set-definitions)
  
[Rules for using data sets](Configuring%20SINAMICS%20S-G-MV%20drives.md#rules-for-using-data-sets)

##### Structure of the data set screen form

###### Structure of the data set screen forms

![Example: Screen form for drive data sets](images/147854769291_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Icons for editing/activating DDS drive data sets in online mode. Not relevant for CDS. |
| ② | Two buttons in the active data set screen form enable the insertion and deletion of individual data sets of the list. |
| ③ | List of created drive data sets. The created data sets are numbered chronologically. In the list of drive data sets, different (MDS or EDS) data sets are assigned to the drive data sets. |
| ④ | Working area for activating a selected data set via BICO interconnections. |

Example: Screen form for drive data sets

###### Icons for editing data sets in the online mode

The editing mode must be activated first in order to edit data sets in the online mode. The editing mode is not required in the offline mode.

| Icon | Description |
| --- | --- |
| ![Icons for editing data sets in the online mode](images/147854075915_DV_resource.Stream@PNG-en-US.png) | Startdrive is not online.   You can only edit the data sets offline. |
| ![Icons for editing data sets in the online mode](images/147854079883_DV_resource.Stream@PNG-en-US.png) | Startdrive is online.   The editing mode is not activated yet. |
| ![Icons for editing data sets in the online mode](images/147854083851_DV_resource.Stream@PNG-en-US.png) | Startdrive is online.   The editing mode is active. |

##### Managing a command data set (CDS)

###### Overview

You can edit the command data sets of the drive via the "Command data sets (CDS)" screen form. The following CDS can be edited at most:

- 2 CDS for infeeds
- 2 CDS for SERVO drives
- 4 CDS for VECTOR drives

###### Requirements

- At least 1 CDS exists (for Line Module, Power Module, or Motor Module).
- The basic parameterization of an infeed or a drive axis has been opened in the secondary navigation.
- Creating and deleting CDSs: There is no online connection to the drive.

  CDSs can only be created or deleted offline. However, CDSs can be activated online.

###### Creating a new command data set (CDS)

1. Click "Add".

   The "Add new command data set" dialog box opens.

   ![Adding a CDS](images/147854110859_DV_resource.Stream@PNG-en-US.PNG)

   ![Adding a CDS](images/147854110859_DV_resource.Stream@PNG-en-US.PNG)

   Adding a CDS
2. Make sure that the "Create as copy" option is deactivated.
3. Click "OK" in the dialog box.

**Result**

A new command data set is created in the list.

###### Creating a new CDS with contents from other CDSs

1. Click "Add".

   The "Add new command data set" dialog box opens.

   ![Adding a CDS](images/147854110859_DV_resource.Stream@PNG-en-US.PNG)

   ![Adding a CDS](images/147854110859_DV_resource.Stream@PNG-en-US.PNG)

   Adding a CDS
2. Activate the "Create as copy" option.
3. Click "OK" in the dialog box to confirm your selection.

**Note**

**Special case for VECTOR drives**

If more than 2 CDS are available for VECTOR drives, you can select at this point which available CDS should be copied.

**Result**

The new command data set is created from the selected template and also inserted in the last position of the list of command data sets.

###### Deleting a command data set (CDS)

In order for command data sets to be deleted, at least 2 CDS (for servo drives or infeed) or 3 CDS (for vector drives) must be available in the list.

1. Select the CDSs to be deleted in the list of command data sets.

   The CDS is displayed again in detail in a worklist located below the collective list.
2. Click "Delete".

   A confirmation prompt is displayed.

   ![Deleting a CDS](images/147854114827_DV_resource.Stream@PNG-en-US.PNG)

   ![Deleting a CDS](images/147854114827_DV_resource.Stream@PNG-en-US.PNG)

   Deleting a CDS
3. Click "OK" to delete the data set.

**Result**

The CDS is deleted from the list of command data sets. The subsequent CDSs in the list will be renumbered if necessary. The numbering of the CDSs is always chronological. The last available CDS remains and cannot be deleted.

##### Managing a drive data set (DDS)

###### Overview

You can edit the drive data sets of the drive via the "Drive data sets (DDS)" screen form.

###### Requirements

- The drive has at least one drive axis.
- The basic parameterization of a drive axis has been opened in the secondary navigation.

###### Creating a new DDS as a copy of an existing DDS

New drive data sets always can be created via the "Drive data sets (DDS)" screen form only as a copy of an existing data set.

1. Click "Add".

   The "Add new drive data set" dialog box opens.

   ![Adding a DDS](images/147854795531_DV_resource.Stream@PNG-en-US.PNG)

   ![Adding a DDS](images/147854795531_DV_resource.Stream@PNG-en-US.PNG)

   Adding a DDS

   The list shows the existing drive data sets which can be used as master copies.
2. Activate the "Copy" option for the existing data set which you want to use as a master copy.
3. Click "OK" in the dialog box to confirm your selection.

**Result**

The new drive data set is created from the selected template and also inserted in the last position of the list of drive data sets.

###### Deleting a drive data set (DDS)

Drive data sets can be deleted only if there are at least two DDSs in the list.

1. Select the DDSs to be deleted in the list of drive data sets.

   The DDS is displayed again in detail in a worklist located below the collective list.
2. Click "Delete".

   A confirmation prompt is displayed.

   ![Example: Deleting a DDS](images/147854799499_DV_resource.Stream@PNG-en-US.PNG)

   ![Example: Deleting a DDS](images/147854799499_DV_resource.Stream@PNG-en-US.PNG)

   Example: Deleting a DDS
3. Click "OK" to delete the DDS.

**Result**

The DDS is deleted from the list of drive data sets. The subsequent DDSs in the list will be renumbered if necessary. The numbering of the DDSs is always chronological. The last available DDS remains and cannot be deleted.

###### Online mode: Assign encoder data sets (EDS)

The editing mode must be active in order to edit data sets in the online mode.

1. Click the ![Online mode: Assign encoder data sets (EDS)](images/147854138763_DV_resource.Stream@PNG-en-US.png) icon to start the editing mode.
2. Select a DDS in the list of drive data sets.
3. Click in the EDS cell of the data set row and select the required EDS from the "Motor encoder" drop-down list.

   If you want to assign 2 additional EDSs, repeat this step using the "External encoder 1" and "External encoder 2" drop-down lists.
4. Click the ![Online mode: Assign encoder data sets (EDS)](images/147854142731_DV_resource.Stream@PNG-en-US.png) icon to quit the editing mode on completing the settings.

**Result**

The assigned data sets are displayed for the selected DDS in the list of drive data sets.

###### Offline mode: Assign encoder data sets (EDS)

In the offline mode, the data sets can be configured without an editing mode.

1. Select a DDS in the list of drive data sets.
2. Click in the EDS cell of the data set row and select the required EDS from the "Motor encoder" drop-down list.

   If you want to assign 2 additional EDSs, repeat this step using the "External encoder 1" and "External encoder 2" drop-down lists.

**Result**

The assigned data sets are displayed for the selected DDS in the list of drive data sets. The drive data then has to be downloaded to the drive for use in the drive.

##### Activating or editing data sets

###### Overview

Several data sets of a data set type must be created for a data set switchover.

###### Editing offline

To assign the settings of a drive to a data set, proceed as follows:

1. Open the configuration screen form for the desired data set type (e.g. the screen form for the drive data set).
2. Select the required data set from the list of data sets.
3. Change the signal sources of the BICO interconnections at the bottom of the working area.
4. Save your settings [permanently](Configuring%20SINAMICS%20S-G-MV%20drives.md#permanently-save-the-settings).

**Result:**

Specific parameterizations are available for each of the various data sets.

###### Editing online

The editing mode must be active in order to edit data sets in the online mode.   
To assign the settings of a drive to a data set, proceed as follows:

1. Click the ![Editing online](images/147854138763_DV_resource.Stream@PNG-en-US.png) icon to start the editing mode.
2. Open the configuration screen form for the desired data set type (e.g. the screen form for the drive data set).
3. Select the required data set from the list of data sets.
4. Change the signal sources of the BICO interconnections at the bottom of the working area.
5. Save your settings [permanently](Configuring%20SINAMICS%20S-G-MV%20drives.md#permanently-save-the-settings).
6. Click the ![Editing online](images/147854142731_DV_resource.Stream@PNG-en-US.png) icon to quit the editing mode on completing the settings.

**Result:**

Specific parameterizations are available for each of the various data sets.

##### Switching data sets

###### Overview

You can switch between different data sets in the configuration screen form. The switchover is performed via drop-down lists in the toolbar.

![Data set switchover](images/147854824715_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Shows the active drive data set (DDS). Enables switchover to a different data set. |
| ② | Shows the active command data set (CDS). Enables switchover to a different data set. |

Data set switchover

###### Requirement

- Multiple drive data sets or command data sets have been created.

  If only one data set of one data set type has been created, the drop-down list for switchover is deactivated.

###### Procedure

1. Open the required configuration screen form.

   The drop-down lists for the data set switchover show the active data set in each case. The settings and parameter values of this data set are displayed in the screen form below them.
2. Select another data set from the drop-down lists for the data set switchover.
3. Change the signal sources of the BICO interconnections at the bottom of the working area.

###### Result

In the screen form, all data-set-dependent settings are changed to the values of the selected data set (if these values are configured differently). The differences in the drive data sets also may result solely from the MDSs or EDSs used in the selected DDS.

### Setpoint channel

This section contains information on the following topics:

- [MV setpoint sources and setpoint preparation](#mv-setpoint-sources-and-setpoint-preparation)
- [Motorized potentiometer](#motorized-potentiometer)
- [Fixed setpoints](#fixed-setpoints)
- [Speed setpoint](#speed-setpoint)
- [Speed limiting](#speed-limiting)
- [Ramp-function generator](#ramp-function-generator)

#### MV setpoint sources and setpoint preparation

For drive objects of the type "VECTORMV", the setpoint channel is automatically active and configurable.

##### Overview of the setpoint sources and the setpoint processing

The setpoint channel forms the connecting element between the external interfaces and the actual motor control. Whereby the input signals are influenced from the point of view of the driven machine, e.g. disabling a direction, hiding certain frequencies, forming acceleration and deceleration ramps through to switchover between different setpoint and command sources.

Generally, different command sources result from the requirements to operate a drive from different locations (local/remote access), in different situations (normal/emergency operation) and/or in different operating modes.

The setpoint source is therefore the interface via which the converter receives its setpoint. The following options are available:

- Motorized potentiometer emulated in the converter
- Analog input of the converter
- Fixed setpoints stored in the converter
- Fieldbus interface of the converter

Depending on the parameter assignment, the setpoint in the converter has one of the following meanings:

- Speed setpoint for the motor
- Torque setpoint for the motor
- Setpoint for a process variable

  The converter receives a setpoint for a process variable, e.g. the level of a liquid container. The converter calculates the speed setpoint internally in the technology controller from this process variable.

##### Overview of the setpoint processing

The setpoint processing modifies the speed setpoint. For example, it limits the setpoint to a maximum and a minimum value and prevents speed jumps of the motor via the ramp-function generator.

- Minimum speed and maximum speed
- Ramp-function generator

##### Function diagrams (FD)

- Setpoint channel - overview - 3001 -

#### Motorized potentiometer

This section contains information on the following topics:

- [Overview](#overview-1)
- [MV motorized potentiometer](#mv-motorized-potentiometer)
- [Ramp-function Generator (motorized potentiometer) MV](#ramp-function-generator-motorized-potentiometer-mv)

##### Overview

###### Description

The drive emulates an electromechanical motorized potentiometer. It is possible to switch over between manual and automatic operation for the setpoint specification. The specified setpoint is supplied to an internal ramp-function generator. Setting values and initial values, as well as braking with OFF1 do not require the ramp-function generator of the motorized potentiometer.

They change the motorized potentiometer (MOP) smoothly via the "Higher" and "Lower" control signals. The control signal can be switched via the digital inputs of the drive or via status words of telegrams. The longer the commands are present, the quicker the setpoint change.

###### Application cases

- Specification of the speed setpoint during the commissioning phase.
- Manual operation of the motor if the higher-level controller fails.
- Specification of the speed setpoint after switchover from automatic to manual mode.
- Applications with mainly constant setpoint without a higher-level controller.
- Interconnection as main or additional setpoint via r1050.

##### MV motorized potentiometer

###### Description

The "Motorized potentiometer" function emulates an electromechanical potentiometer for the input of setpoints. The value of the motorized potentiometer is set via the "Setpoint higher" and "Setpoint lower" commands. This value is saved and can be interconnected as main setpoint or as additional setpoint. The "Motorized potentiometer" function can be selected when digital inputs of the operator panel or fieldbusses are used. The behavior of the motorized potentiometer depends on the duration of the "Setpoint higher" and "Setpoint lower" commands: The longer the commands are present, the quicker the setpoint change.

The function is intended for manual control of the drive or for automatic speed specification. The ramp-function generator of the motorized potentiometer can be switched off in automatic operation.

- With manual control, you manually specify the setpoint via a digital input, for example.
- In automatic operation, a higher-level controller specifies the setpoint, for example. You then interconnect the signal source via BICO.

###### Setting automatic operation or manual operation

1. Interconnect the "Manual/automatic" signal source ([p1041](SINAMICS%20Parameter%20VECTORMV.md#p10410n-bi-motorized-potentiometer-manualautomatic)) for switching from manual to automatic at the motorized potentiometer.

   In manual operation, the setpoint is set higher and lower via two signals.

   In automatic operation, the setpoint must be interconnected via a connector input.

###### Parameterizing the motorized potentiometer for manual operation

1. To specify limit values for the speed setpoint in manual operation, enter a maximum value ([p1037](SINAMICS%20Parameter%20VECTORMV.md#p10370n-motorized-potentiometer-maximum-speed)) or minimum value ([p1038](SINAMICS%20Parameter%20VECTORMV.md#p10380n-motorized-potentiometer-minimum-speed)).

   The "Maximum speed" or "Minimum speed" is not overshot or undershot when using the motorized potentiometer.
2. Interconnect the "Setpoint higher" signal source ([p1035](SINAMICS%20Parameter%20VECTORMV.md#p10350n-bi-motorized-potentiometer-setpoint-raise)) for a continuous increase of the setpoint at the motorized potentiometer.
3. Interconnect the "Setpoint lower" signal source ([p1036](SINAMICS%20Parameter%20VECTORMV.md#p10360n-bi-motorized-potentiometer-lower-setpoint)) for a continuous decrease of the setpoint at the motorized potentiometer.
4. Interconnect the "Inversion" signal source ([p1039](SINAMICS%20Parameter%20VECTORMV.md#p10390n-bi-motorized-potentiometer-inversion)) to invert the minimum speed/velocity or the maximum speed/velocity at the motorized potentiometer.
5. To parameterize the ramp-function generator, click the "Ramp-function generator" button.

   Specify the values for the ramp-function generator in the dialog of the same name (see [Ramp-function Generator (motorized potentiometer) MV](#ramp-function-generator-motorized-potentiometer-mv)).

###### Parameterizing the motorized potentiometer for automatic operation

1. Interconnect the "Automatic setpoint" signal source ([p1042](SINAMICS%20Parameter%20VECTORMV.md#p10420n-ci-motorized-potentiometer-automatic-setpoint)) for the setpoint of the motorized potentiometer during automatic operation.
2. In the "Automatic operation active" drop-down list ([p1030](SINAMICS%20Parameter%20VECTORMV.md#p10300n-motorized-potentiometer-configuration).1), select whether the ramp-function generator is to be active during Automatic operation.

   - [0] No = In this case, the "Ramp-function generator" button is deactivated.
   - [1] Yes = In this case, the ramp-function generator can be subsequently parameterized.
3. To parameterize the activated ramp-function generator, click the "Ramp-function generator" button.

   Specify the values for the ramp-function generator in the dialog of the same name. (See [Ramp-function Generator (motorized potentiometer) MV](#ramp-function-generator-motorized-potentiometer-mv)).

###### Saving the setpoint

The output of the motorized potentiometer [r1050](SINAMICS%20Parameter%20VECTORMV.md#r1050-co-motor-potentiometer-setpoint-after-the-ramp-function-generator) is saved after OFF and the motorized potentiometer is set to the saved value after ON if p1030.0 = 1. The ramp-function generator of the motorized potentiometer moves from this start value in the direction of the new setpoint. With p1030.0 a decision is made as to whether the ramp-function generator of the motorized potentiometer is based on the motorized potentiometer output that was valid before the OFF command or on a start value specified by [p1040](SINAMICS%20Parameter%20VECTORMV.md#p10400n-motorized-potentiometer-starting-value). Parameter p1030.3 decides whether or not the setpoint is stored in a non-volatile memory.

For saving important data, the converter has an NVRAM (Non-Volatile Random Access Memory). The setpoint of the motorized potentiometer is stored in the non-volatile memory there. The value is re-loaded after POWER ON and specified as the start value after OFF1 enable.

1. Select the "[1] Yes" option in the "Save active" (p1030.0) drop-down list to save the setpoint in the volatile memory (not in the non-volatile memory).
2. Select the "[1] Yes" option in the "Non-volatile saving active" (p1030.3) drop-down list to save the setpoint in the non-volatile memory.

> **Note**
>
> Non-volatile saving is only performed when p1030.0 = 1 and p1030.3 = 1, that is, if the "[1] Yes" option is selected in both drop-down lists.

###### Function diagrams (FD)

Setpoint channel - motorized potentiometer - 3020 -

Internal control/status words - control word, sequence control - 2501 -

###### Additional parameters

- [p0115](SINAMICS%20Parameter%20VECTORMV.md#p011506-sampling-times-for-internal-control-loops)
- [r1045](SINAMICS%20Parameter%20VECTORMV.md#r1045-co-mot-potentiometer-speed-setpoint-in-front-of-ramp-function-gen)

---

---

**See also**

[Overview](#overview-1)

##### Ramp-function Generator (motorized potentiometer) MV

###### Description

The ramp-function generator (RFG) limits the acceleration at sudden setpoint changes and helps to avoid load surges in the entire drive train. An acceleration ramp and a deceleration ramp can be set independently with the ramp-up time and ramp-down time. This enables a controlled transition at setpoint changes.

In addition to the acceleration limitation, the "Ramp-function generator" screen form also displays the maximum motor speed, and in which speed range the motor operates.

> **Note**
>
> If the ramp-function generator of the motorized potentiometer is used, the actual [Ramp-function generator of the setpoint channel](#mv-ramp-function-generator) is generally not used in addition.

###### Activating the initial rounding ([p1030](SINAMICS%20Parameter%20VECTORMV.md#p10300n-motorized-potentiometer-configuration))

An initial rounding results in an S-shaped ramp which provides smooth transitions for acceleration and deceleration.

1. To connect a fixed specified rounding, select the "[1] Yes" entry in the "Initial rounding active" (p1030.2) drop-down list.

   The set ramp-up or ramp-down time can be exceeded with the initial rounding.

###### Setting the ramp-up time and ramp-down time

The ramp-function generator is parameterized via the ramp-up and ramp-down time parameters, whereby these refer to the speed limit n_max.

1. Correct the value specified for the "Ramp-up time" ([p1047](SINAMICS%20Parameter%20VECTORMV.md#p10470n-motorized-potentiometer-ramp-up-time)). The lower the value, the faster the drive accelerates.

   The ramp-up time is extended accordingly with activated initial rounding (p1030.2).
2. Correct the value specified for the "Ramp-down time" ([p1048](SINAMICS%20Parameter%20VECTORMV.md#p10480n-motorized-potentiometer-ramp-down-time)). The lower the value, the faster the drive decelerates.

   The ramp-down time is extended accordingly with activated initial rounding (p1030.2).

> **Note**
>
> **Direction reversal**
>
> With direction reversal, the two times are added: With direction reversal, the ramp-down time is effective first and then the ramp-up time in the opposite direction.

###### Parameterizing the start value and the setting value

Setting values are the values to which the ramp-function generator jumps automatically. You set the ramp-function generator output to the motorized potentiometer setting value.

1. Interconnect the "Accept setting value" signal source ([p1043](SINAMICS%20Parameter%20VECTORMV.md#p10430n-bi-motorized-potentiometer-accept-setting-value)) to accept the setting value at the motorized potentiometer.
2. Interconnect the "Setting value" ([p1044](SINAMICS%20Parameter%20VECTORMV.md#p10440n-ci-motorized-potentiometer-setting-value)) signal source for the setting value at the motorized potentiometer.

   The setting value influences [r1050](SINAMICS%20Parameter%20VECTORMV.md#r1050-co-motor-potentiometer-setpoint-after-the-ramp-function-generator) (motorized potentiometer setpoint after ramp-function generator).
3. Enter a start value for the motorized potentiometer in the "Start value" ([p1040](SINAMICS%20Parameter%20VECTORMV.md#p10400n-motorized-potentiometer-starting-value)) field.

   The ramp-function generator of the motorized potentiometer moves from this start value in the direction of the new setpoint.

###### Display parameters

The following information is displayed via display parameters:

- Maximum speed ([p1082](SINAMICS%20Parameter%20VECTORMV.md#p10820n-maximum-speed))

  Display of the highest possible speed.

###### Function diagrams (FD)

Internal control/status words - control word, sequence control - 2501 -

Setpoint channel - basic ramp-function generator - 3060 -

Setpoint channel - extended ramp-function generator - 3070 -

Setpoint channel - ramp-function generator selection, status word, tracking - 3080 -

###### Additional parameters

- [r1045](SINAMICS%20Parameter%20VECTORMV.md#r1045-co-mot-potentiometer-speed-setpoint-in-front-of-ramp-function-gen)
- r1050

---

#### Fixed setpoints

This section contains information on the following topics:

- [MV fixed setpoints](#mv-fixed-setpoints)
- [MV fixed setpoint interconnection](#mv-fixed-setpoint-interconnection)
- [Application example: Operating a drive with constant speed](#application-example-operating-a-drive-with-constant-speed)

##### MV fixed setpoints

###### Description

This function allows you to specify preset speed/frequency setpoints. The fixed setpoints are defined in parameters and selected via binector inputs. For example, the digital inputs or the appropriate bits in the PROFINET telegrams can be used for the external control. The individual fixed setpoints and the effective fixed setpoint are each available via a connector output for further interconnection. Simple applications in which switchover is only to be between a few dedicated speeds, can be implemented with this function.

###### Procedure

These fixed setpoints are up to 15 freely stored speed setpoints which you can select via a bit pattern. If all the selected bits have low status, then the value 0 is specified as fixed setpoint.

1. Enter fixed speed setpoints 1...15 in the "Fixed value 1...15" ([p1001](SINAMICS%20Parameter%20VECTORMV.md#p10010n-co-fixed-speed-setpoint-1)...[p1015](SINAMICS%20Parameter%20VECTORMV.md#p10150n-co-fixed-speed-setpoint-15)) fields.
2. Then interconnect the signal sources for selecting the fixed velocity setpoint for the following bit fields

   - "Bit 0" ([p1020](SINAMICS%20Parameter%20VECTORMV.md#p10200n-bi-fixed-speed-setpoint-selection-bit-0))
   - "Bit 1" ([p1021](SINAMICS%20Parameter%20VECTORMV.md#p10210n-bi-fixed-speed-setpoint-selection-bit-1))
   - "Bit 2" ([p1022](SINAMICS%20Parameter%20VECTORMV.md#p10220n-bi-fixed-speed-setpoint-selection-bit-2))
   - "Bit 3" ([p1023](SINAMICS%20Parameter%20VECTORMV.md#p10230n-bi-fixed-speed-setpoint-selection-bit-3))

###### Additional parameters

- [p0115](SINAMICS%20Parameter%20VECTORMV.md#p011506-sampling-times-for-internal-control-loops)
- [r1024](SINAMICS%20Parameter%20VECTORMV.md#r1024-co-fixed-speed-setpoint-effective)

---

##### MV fixed setpoint interconnection

###### Description

The fixed setpoints are interconnected via BICO technology. Several interconnections can be created for each fixed setpoint.

###### Procedure

1. Click the "Interconnections" button in the "Fixed setpoints" screen form.

   The "Fixed setpoint interconnection" dialog opens.
2. Enter fixed speed setpoints in the "Fixed value 1...15" ([p1001](SINAMICS%20Parameter%20VECTORMV.md#p10010n-co-fixed-speed-setpoint-1)...[p1015](SINAMICS%20Parameter%20VECTORMV.md#p10150n-co-fixed-speed-setpoint-15)) fields.
3. To set percentage values for the "Fixed value 1" or "2" ([p2900](SINAMICS%20Parameter%20VECTORMV.md#p29000n-co-fixed-value-1)...[p2901](SINAMICS%20Parameter%20VECTORMV.md#p29010n-co-fixed-value-2)), enter a value at "Fixed value 1" or "Fixed value 2". You can use the percentage fixed values, for example, as signal source for the scaling of the main or additional setpoint in the "Speed setpoint" screen form.
4. To enter a fixed torque value, enter a value at "Fixed value M" ([p2930](SINAMICS%20Parameter%20VECTORMV.md#p29300n-co-fixed-value-m-nm)).

   These values are used as signal source to interconnect the fixed speed to another BICO signal.
5. Interconnect the appropriate connector output to each recorded fixed setpoint (on the right of the associated fixed setpoint field).

   Several connections are also possible for each fixed setpoint.
6. Once you have made all the necessary settings, click the "Close" button.

   The dialog closes.

###### Function diagrams (FD)

Setpoint channel - overview - 3001 -

Setpoint channel - fixed speed setpoints - 3010 -

###### Additional parameters

- [p0115](SINAMICS%20Parameter%20VECTORMV.md#p011506-sampling-times-for-internal-control-loops)
- [r1024](SINAMICS%20Parameter%20VECTORMV.md#r1024-co-fixed-speed-setpoint-effective)

---

##### Application example: Operating a drive with constant speed

###### Using constant speed (fixed speeds)

Use fixed speeds for simple applications in which the drive only has to turn at constant speed. The drive allows you to predefine up to 15 fixed speeds.

The defined fixed speeds are selected via binector inputs. The various speeds are controlled via digital inputs or via appropriate bits in PROFIdrive telegrams.

If you switch between different fixed speeds, the resulting speed setpoint is accelerated or decelerated via the acceleration ramp of deceleration ramp of the ramp-function generator. Therefore, check the ramp-up times and ramp-down times set in the ramp-function generator. The ramps are set to 10 seconds in the factory setting and can be changed. The OFF3 ramp is set to 0 seconds.

###### Sample applications

Simple applications in which switchover is between a few specified speeds, can be implemented with fixed speeds:

- Mixer with stepped mixing speed
- Conveyor belt with several speed stages
- Fixed setpoint as main or additional setpoint, see also [MV speed setpoint](#mv-speed-setpoint).

###### Procedure

You want to select fixed setpoint 6 and connect it to a BICO parameter in order to use it as a speed setpoint:

1. Enter a "1" for bit 1.
2. Enter a "2" for bit 1.

   This results in bit pattern "0110" with which you can select fixed value 6.
3. Enter a value for fixed value 6 ([p1006](SINAMICS%20Parameter%20VECTORMV.md#p10060n-co-fixed-speed-setpoint-6)[6]).
4. Connect the output signal ([r1024](SINAMICS%20Parameter%20VECTORMV.md#r1024-co-fixed-speed-setpoint-effective)). As default, r1024 is connected to the main setpoint at "Speed setpoint".

![Connecting fixed setpoints](images/148105265675_DV_resource.Stream@PNG-en-US.png)

Connecting fixed setpoints

###### Additional parameters

- [p1020](SINAMICS%20Parameter%20VECTORMV.md#p10200n-bi-fixed-speed-setpoint-selection-bit-0)
- [p1021](SINAMICS%20Parameter%20VECTORMV.md#p10210n-bi-fixed-speed-setpoint-selection-bit-1)
- [p1022](SINAMICS%20Parameter%20VECTORMV.md#p10220n-bi-fixed-speed-setpoint-selection-bit-2)
- [p1023](SINAMICS%20Parameter%20VECTORMV.md#p10230n-bi-fixed-speed-setpoint-selection-bit-3)
- ---

---

**See also**

[MV fixed setpoint interconnection](#mv-fixed-setpoint-interconnection)

#### Speed setpoint

This section contains information on the following topics:

- [MV speed setpoint](#mv-speed-setpoint)
- [Application example: Using the main and additional setpoint](#application-example-using-the-main-and-additional-setpoint)

##### MV speed setpoint

###### Description

The speed setpoint is the reference variable of the drive to be controlled. You also specify the speed of the drive via the size of the speed setpoint. There are numerous ways to influence the speed setpoint:

- Main setpoint (+ scaling)
- Additional setpoint (+ scaling)
- Jog
- Direction of rotation limitation and direction reversal
- Speed limit in the setpoint channel

###### Setting the main/additional setpoint and setpoint modification

The additional setpoint can be used to incorporate correction values from lower-level controllers. This can be easily carried out using the addition point of the main/additional setpoint in the setpoint channel. Both variables are imported via two separate sources and added in the setpoint channel. In contrast to the setpoint addition, the main and additional setpoints are added before the ramp-function generator. The added speed setpoint is then routed over the acceleration ramp of the ramp-function generator.

1. Connect the "Main setpoint" signal source ([p1070](SINAMICS%20Parameter%20VECTORMV.md#p10700n-ci-main-setpoint)) of the main setpoint.
2. Connect the "Scaling" signal source ([p1071](SINAMICS%20Parameter%20VECTORMV.md#p10710n-ci-main-setpoint-scaling)) for scaling the main setpoint.

   Example: Connect "Fixed value 1" at "Fixed setpoint interconnection" as signal source.
3. Connect the "Additional setpoint" signal source ([p1075](SINAMICS%20Parameter%20VECTORMV.md#p10750n-ci-supplementary-setpoint)) of the additional setpoint.
4. Connect the "Additional setpoint scaling" signal source ([p1076](SINAMICS%20Parameter%20VECTORMV.md#p10760n-ci-supplementary-setpoint-scaling)) for scaling the additional setpoint.

   Example: Connect "Fixed value 2" at "Fixed setpoint interconnection" as signal source.

###### Setting jog

"Jog" is oriented towards typical "finger tapping" with which you can traverse a motor through short taps.

When a jog signal is connected, the motor accelerates with the acceleration ramp of the ramp-function generator (in relation to the maximum speed [p1082](SINAMICS%20Parameter%20VECTORMV.md#p10820n-maximum-speed); see figure) up to the jog setpoint. When the jog signal is deselected, shutdown is performed on the set ramp of the ramp-function generator.

![Jog 1 and Jog 2 flow diagram](images/148105343755_DV_resource.Stream@PNG-en-US.png)

Jog 1 and Jog 2 flow diagram

To traverse a motor via "Jog", e.g. a motor after a program interruption, enter speed setpoints in the following fields:

1. Enter a value for "Jog 1" ([p1058](SINAMICS%20Parameter%20VECTORMV.md#p10580n-jog-1-speed-setpoint)).

   - and/or -
2. Enter a value for "Jog 2" ([p1059](SINAMICS%20Parameter%20VECTORMV.md#p10590n-jog-2-speed-setpoint)).
3. Connect the signal sources for Jog 1 or Jog 2, and therefore enable the drive for "Jog":

   - "Jog bit 0" ([p1055](SINAMICS%20Parameter%20VECTORMV.md#p10550n-bi-jog-bit-0)); signal source for Jog 1
   - "Jog bit 1" ([p1056](SINAMICS%20Parameter%20VECTORMV.md#p10560n-bi-jog-bit-1)); signal source for Jog 2

   If you have connected both signal sources, the setpoint is maintained.

**Jog properties**

- If both Jog signals are set simultaneously, the momentary speed is maintained (constant speed phase).
- Jog setpoints are approached and left via the ramp-function generator.
- Jog is possible from the "Ready to start" state.
- If ON/OFF1 = "1" and Jog have been selected simultaneously, ON/OFF1 takes priority.  
  For this reason, ON/OFF1 = "1" must not be active for Jog to be activated.
- OFF2 and OFF3 take priority over Jog.
- The ON command is issued via p1055 and p1056.
- The Jog speed is defined via p1058 and p1059.
- The following applies during "Jog mode":

  - The main speed setpoints ([r1078](SINAMICS%20Parameter%20VECTORMV.md#r1078-co-total-setpoint-effective)) are disabled.
  - Additional setpoint 1 ([p1155](SINAMICS%20Parameter%20VECTORMV.md#p11550n-ci-speed-controller-speed-setpoint-1)) is disabled.
  - Additional setpoint 2 ([p1160](SINAMICS%20Parameter%20VECTORMV.md#p11600n-ci-speed-controller-speed-setpoint-2)) is passed on and added to the current speed.
- The skip frequency bands ([p1091](SINAMICS%20Parameter%20VECTORMV.md#p10910n-skip-speed-1) ... [p1094](SINAMICS%20Parameter%20VECTORMV.md#p10940n-skip-speed-4)) and the minimum limit ([p1080](SINAMICS%20Parameter%20VECTORMV.md#p10800n-minimum-speed)) in the setpoint channel are also effective in Jog mode.
- The freezing of the ramp-function generator via [p1141](SINAMICS%20Parameter%20VECTORMV.md#p11410n-bi-continue-ramp-function-generatorfreeze-ramp-function-generator) is deactivated ([r0046](SINAMICS%20Parameter%20VECTORMV.md#r0046029-cobo-missing-enable-sig).31 = 1) during Jog mode.

###### Setting the direction of rotation limitation and direction reversal

A direction reversal can be achieved in the setpoint channel by selecting the setpoint inversion ([p1113](SINAMICS%20Parameter%20VECTORMV.md#p11130n-bi-setpoint-inversion)). However, if the specification of a negative or positive setpoint via the setpoint channel is to be prevented, this can be disabled.

1. Connect the "Setpoint inversion" signal source (p1113) to set the reversal of the direction of rotation.
2. Connect the "Disable negative direction" signal source ([p1110](SINAMICS%20Parameter%20VECTORMV.md#p11100n-bi-inhibit-negative-direction)) to disable the negative direction of rotation.
3. Connect the "Disable positive direction" signal source ([p1111](SINAMICS%20Parameter%20VECTORMV.md#p11110n-bi-inhibit-positive-direction)) to disable the positive direction of rotation.

###### Setting the speed limit in the setpoint channel

To limit the speed in the setpoint channel, enter a value for the "Speed limit setpoint channel" ([p1063](SINAMICS%20Parameter%20VECTORMV.md#p10630n-setpoint-channel-speed-limit)).

###### Signal processing

| Symbol | Meaning |
| --- | --- |
| ![Signal processing](images/148105339531_DV_resource.Stream@PNG-en-US.png) | [Speed limiting](#speed-limiting) |

###### Function diagrams (FD)

Setpoint channel - overview - 3001 -

Setpoint channel - main setpoint/additional setpoint, setpoint scaling, jog - 3030 -

Setpoint channel - direction limitation and direction reversal - 3040 -

###### Additional parameters

- [p0115](SINAMICS%20Parameter%20VECTORMV.md#p011506-sampling-times-for-internal-control-loops)
- [r0899](SINAMICS%20Parameter%20VECTORMV.md#r0899015-cobo-status-word-sequence-control)
- [r1114](SINAMICS%20Parameter%20VECTORMV.md#r1114-co-setpoint-after-the-direction-limiting)
- [r1073](SINAMICS%20Parameter%20VECTORMV.md#r1073-co-main-setpoint-effective)
- [r1077](SINAMICS%20Parameter%20VECTORMV.md#r1077-co-supplementary-setpoint-effective)

---

---

**See also**

[Application example: Using the main and additional setpoint](#application-example-using-the-main-and-additional-setpoint)

##### Application example: Using the main and additional setpoint

###### Description

The additional setpoint can be used to incorporate correction values from lower-level controllers. This can be easily carried out using the addition point of the main/additional setpoint in the setpoint channel. Both variables are imported via two separate sources and added in the setpoint channel.

![Main and additional setpoint](images/148105387403_DV_resource.Stream@PNG-en-US.png)

Main and additional setpoint

In contrast to the [setpoint addition](#mv-droop-feedback), the main and additional setpoints are added before the ramp-function generator. The sum of the main and additional setpoints is then routed through the setpoint channel over the acceleration ramp of the ramp-function generator. The update is performed in the sampling time of the setpoint channel ([p0115](SINAMICS%20Parameter%20VECTORMV.md#p011506-sampling-times-for-internal-control-loops)[3]) and not in the faster sampling time of the speed controller cycle.

###### Procedure

The resulting fixed speed setpoint [r1024](SINAMICS%20Parameter%20VECTORMV.md#r1024-co-fixed-speed-setpoint-effective) is connected as default setting:

1. If required, check and reconnect [p1070](SINAMICS%20Parameter%20VECTORMV.md#p10700n-ci-main-setpoint) to the signal source for the main setpoint.

   Connect [p1071](SINAMICS%20Parameter%20VECTORMV.md#p10710n-ci-main-setpoint-scaling) to the signal source for the scaling factor of the main setpoint.
2. Connect [p1075](SINAMICS%20Parameter%20VECTORMV.md#p10750n-ci-supplementary-setpoint) to the signal source for the additional setpoint.

   Connect [p1076](SINAMICS%20Parameter%20VECTORMV.md#p10760n-ci-supplementary-setpoint-scaling) to the signal source for the scaling factor of the additional setpoint.

###### Function diagrams (FD)

Setpoint channel - overview - 3001 -

Setpoint channel - ramp-function generator selection, status word, tracking - 3080 -

###### Additional parameters

- p1070
- p1071
- [r1073](SINAMICS%20Parameter%20VECTORMV.md#r1073-co-main-setpoint-effective)
- p1075
- p1076
- [r1077](SINAMICS%20Parameter%20VECTORMV.md#r1077-co-supplementary-setpoint-effective)
- [r1078](SINAMICS%20Parameter%20VECTORMV.md#r1078-co-total-setpoint-effective)

---

#### Speed limiting

This section contains information on the following topics:

- [MV speed limitation](#mv-speed-limitation)
- [Application example: Parameterizing skip frequency bands and minimum limitation](#application-example-parameterizing-skip-frequency-bands-and-minimum-limitation)

##### MV speed limitation

###### Description

The speed limitation is used to avoid damage to the connected machine. For example, reversing is not always possible and must be avoided. The speed setpoint limitation can disable the specification of a negative or positive setpoint via the setpoint channel. The maximum speed can also be limited for the connected machine.

In torque control, the sum of the two torque setpoints is limited in the same way as the torque setpoint of the speed control. Above the maximum speed, a speed limitation reduces the torque limits in order to prevent a further acceleration of the drive.

###### Signal source

| Symbol | Meaning |
| --- | --- |
| ![Signal source](images/148105438091_DV_resource.Stream@PNG-en-US.PNG) | [Speed setpoint](#speed-setpoint) |

###### Defining skip frequency bands

If a drive train has interfering points of resonance in the range from 0 rpm to the setpoint speed, you can define skip frequency bands for these points. Skip frequency bands are used, e.g. to prevent mechanical resonance effects. Resonances can cause unwanted mechanical vibrations. The skip frequency bands prevent continuous operation of the drive at these points of resonance. During ramp-up, the speed remains at the lower limit of a skip frequency band, and during ramp-down, the speed remains at the upper limit.

1. To define skip frequency bands, click the "Skip frequency bands" button.

   The "Skip frequency bands" dialog opens.
2. Enter values in the "Skip value 1 to 4" fields ([p1091](SINAMICS%20Parameter%20VECTORMV.md#p10910n-skip-speed-1) to [p1094](SINAMICS%20Parameter%20VECTORMV.md#p10940n-skip-speed-4)) in order to define up to four skip frequency bands.
3. Enter a value for the skip frequency band ([p1101](SINAMICS%20Parameter%20VECTORMV.md#p11010n-skip-speed-bandwidth)) in the "Bandwidth" field. You can only define one identical bandwidth for all four skip frequency bands.

   If you enter "0" as value, no skip frequency bands are taken into account - irrespective of which values you have defined for the "Skip values 1 to 4" (p1091 to p1094).
4. Once you have made all the necessary settings, click the "Close" button.

   The dialog closes.

   You have defined valid skip frequency bands when the "Skip frequency bands" button appears as follows:

   ![Defining skip frequency bands](images/148105430155_DV_resource.Stream@PNG-en-US.png)

   ![Defining skip frequency bands](images/148105430155_DV_resource.Stream@PNG-en-US.png)

###### Defining the minimum limitation

A minimum limitation is approached after the pulse enable.

1. To enter a minimum value for the speed setpoint, click the "Minimum limitation" button.

   The "Minimum limitation" dialog opens.
2. Enter a value for the lower limit of the speed setpoint at "Minimum speed" ([p1080](SINAMICS%20Parameter%20VECTORMV.md#p10800n-minimum-speed)).

   - Or -

   Interconnect the "Minimum speed signal source" signal source ([p1106](SINAMICS%20Parameter%20VECTORMV.md#p11060n-ci-minimum-speed-signal-source)) for the lowest possible speed of the motor.
3. Once you have made all the necessary settings, click the "Close" button.

   The dialog closes.

   You have defined a valid minimum limitation when the "Minimum limitation" button appears as follows:

   ![Defining the minimum limitation](images/148105434123_DV_resource.Stream@PNG-en-US.png)

   ![Defining the minimum limitation](images/148105434123_DV_resource.Stream@PNG-en-US.png)

###### Defining the maximum limitation

1. To enter a maximum value for the speed setpoint, click the "Maximum limitation" button.

   The "Maximum limitation" dialog opens.
2. Make the following settings for the speed limit of the RFG here:

   - "Speed limit, positive direction of rotation" ([p1051](SINAMICS%20Parameter%20VECTORMV.md#p10510n-ci-speed-limit-rfg-positive-direction-of-rotation))

     Interconnect the signal source of the speed limitation in the positive direction of rotation: This speed limitation goes directly into the ramp-function generator.
   - "Speed limit negative direction of rotation" ([p1052](SINAMICS%20Parameter%20VECTORMV.md#p10520n-ci-speed-limit-rfg-negative-direction-of-rotation))

     Interconnect the signal source of the speed limitation in the negative direction of rotation: This speed limitation goes directly into the ramp-function generator.
3. Make the following settings for the "Speed limit positive effective" ([r1084](SINAMICS%20Parameter%20VECTORMV.md#r1084-co-speed-limit-positive-effective)) here:

   - "pos. variable speed limit" ([p1085](SINAMICS%20Parameter%20VECTORMV.md#p10850n-ci-speed-limit-in-positive-direction-of-rotation))

     Interconnect the signal source of a variable speed limitation in the positive direction of rotation.
   - "Positive speed limit" ([p1083](SINAMICS%20Parameter%20VECTORMV.md#p10830n-co-speed-limit-in-positive-direction-of-rotation))

     Enter the maximum speed for the positive direction.
   - "Maximum speed" ([p1082](SINAMICS%20Parameter%20VECTORMV.md#p10820n-maximum-speed))

     Enter a value for the highest possible positive speed. The inverted value is used as the lowest possible value.

   The lowest of the three values in p1082, p1083 and p1085 is used as the "Speed limit positive effective" (r1084).
4. Make the following settings for the "Speed limit negative effective" ([p1086](SINAMICS%20Parameter%20VECTORMV.md#p10860n-co-speed-limit-in-negative-direction-of-rotation)) here:

   - "negative speed limit" (p1086)

     Enter the maximum speed for the positive direction.
   - "neg. variable speed limit" (p1052)

     Interconnect the signal source of a variable speed limitation in the negative direction of rotation.

   The lowest of the three values in p1082, p1086 and [p1088](SINAMICS%20Parameter%20VECTORMV.md#p10880n-ci-speed-limit-in-negative-direction-of-rotation) is used as the "Speed limit positive effective" ([r1087](SINAMICS%20Parameter%20VECTORMV.md#r1087-co-speed-limit-negative-effective)).

   The setpoint of the ramp-function generator for diagnostic and control purposes is displayed in "CO: ramp-function generator setpoint at the input" ([r1119](SINAMICS%20Parameter%20VECTORMV.md#r1119-co-ramp-function-generator-setpoint-at-the-input)).
5. Once you have made all the necessary settings, click the "Close" button.

   The dialog closes.

###### Signal processing

| Symbol | Meaning |
| --- | --- |
| ![Signal processing](images/148105455115_DV_resource.Stream@PNG-en-US.png) | [Ramp-function generator](#ramp-function-generator) |

###### Function diagrams (FD)

Setpoint channel - overview - 3001 -

Setpoint channel - skip frequency bands and speed limits - 3050 -

###### Additional parameters

- [p0115](SINAMICS%20Parameter%20VECTORMV.md#p011506-sampling-times-for-internal-control-loops)
- [r1112](SINAMICS%20Parameter%20VECTORMV.md#r1112-co-speed-setpoint-after-minimum-limiting)
- [r1114](SINAMICS%20Parameter%20VECTORMV.md#r1114-co-setpoint-after-the-direction-limiting)

---

##### Application example: Parameterizing skip frequency bands and minimum limitation

###### Setting up skip frequency bands and minimum limitation

If a drive train has interfering points of resonance in the range from 0 rpm to the setpoint speed, you can define skip frequency bands for these points. The drive crosses the set skip frequency bands on the acceleration/deceleration ramp, but continuous operation in the set skip frequency bands is not possible.

- Reduction of resonant frequencies in mechanical systems, e.g. in pipes and ventilation ducts.

  - Reduced material fatigue
  - Reduced noise levels

###### Determining the points of resonance

You can use the trace technology of the TIA Portal to determine the points of resonance. You may also have noticed a speed range during commissioning in which resonance occurred.

1. Open the trace and select "Configuration > Signals".
2. Select the actual speed value ([r0062](SINAMICS%20Parameter%20VECTORMV.md#r0062-co-speed-setpoint-after-the-filter)) as the signal to be recorded.

   ![Trace with signal r62](images/148105478923_DV_resource.Stream@PNG-en-US.png)

   Trace with signal r62
3. Go online and load the trace configuration to the drive.
4. Specify the speed via the drive control panel.
5. If you find a speed range with resonance, increase or decrease the speed until you have located the resonance point. In this way, you also obtain the speed range in which the resonance occurs.

###### Parameterizing skip frequency bands

To parameterize the skip frequency bands, proceed as follows:

1. Open the "Speed limitation" screen form in the secondary navigation and click the "Skip frequency bands" button.

   ![Skip frequency bands](images/148105495819_DV_resource.Stream@PNG-en-US.png)

   Skip frequency bands
2. Enter the determined value for the skip frequency band ([p1091](SINAMICS%20Parameter%20VECTORMV.md#p10910n-skip-speed-1)).
3. Enter a value for the bandwidth ([p1101](SINAMICS%20Parameter%20VECTORMV.md#p11010n-skip-speed-bandwidth)), e.g. +/- 15 rpm.
4. In this way, define all the skip frequency bands.
5. Once you have made all the necessary settings, click the "Close" button.

   The dialog closes.

###### Minimum limitation

The minimum limitation depends on the requirements of your application or your process. An example of this is a conventional pump application in which a specific delivery rate must be maintained. Accordingly, the motor speed must not fall below the minimum speed.

In addition to the fixed set limit, it is also possible to dynamically influence these limits during operation with the connectors, in order, for example, to be able to adapt the machine for different processing materials.

1. Open the "Speed limitation" screen form in the secondary navigation and click the "Minimum limitation" button.

   ![Minimum limitation](images/148105499915_DV_resource.Stream@PNG-en-US.png)

   Minimum limitation
2. Enter a value for the minimum motor speed ([p1080](SINAMICS%20Parameter%20VECTORMV.md#p10800n-minimum-speed)).

   or
3. Connect a signal for the minimum motor speed ([p1006](SINAMICS%20Parameter%20VECTORMV.md#p10060n-co-fixed-speed-setpoint-6)).
4. Once you have made all the necessary settings, click the "Close" button.

   The dialog closes.

###### Additional parameters

---

#### Ramp-function generator

This section contains information on the following topics:

- [MV ramp-function generator](#mv-ramp-function-generator)
- [MV simple ramp-function generator](#mv-simple-ramp-function-generator)
- [MV extended ramp-function generator](#mv-extended-ramp-function-generator)
- [Application example: Parameterizing the ramp-function generator](#application-example-parameterizing-the-ramp-function-generator)

##### MV ramp-function generator

###### Description

The ramp-function generator is used to limit the acceleration at sudden setpoint changes and helps to avoid load surges in the entire drive train.

- [Basic ramp-function generator](#mv-simple-ramp-function-generator)

  The basic ramp-function generator passes on the input values to the output via linear ramps. The speed setpoint is accelerated or decelerated linearly.
- [Extended ramp-function generator](#mv-extended-ramp-function-generator)

  With the extended ramp-function generator, acceleration and deceleration are not linear. Rounding can be parameterized at the start and end of the range via a selected rounding type.

An acceleration ramp and a deceleration ramp can be set independently with the ramp-up time and ramp-down time. This enables a controlled transition at setpoint changes.

If the drive is in the range of the torque limits or the drive is temporarily not controlled via the ramp-function generator, then the actual speed value moves away from the speed setpoint.

With ramp-function generator tracking, the speed setpoint follows the actual speed value and therefore flattens the ramp. The ramp-function generator tracking can be activated for the basic and the extended ramp-function generator.

> **Note**
>
> If a [Motorized potentiometer with ramp-function generator](#mv-motorized-potentiometer) is used in the setpoint channel, then the ramp-function generator described in the following is usually superfluous.

###### Signal source

| Symbol | Meaning |
| --- | --- |
| ![Signal source](images/148105339531_DV_resource.Stream@PNG-en-US.png) | [Speed limitation](#mv-speed-limitation) |

###### Making the basic settings for the ramp-function generator

1. Select in the "Ramp-function generator selection" drop-down list whether a basic ramp-function generator or an extended ramp-function generator is to be used.

   The ramp-function generator type is shown as subentry in the secondary navigation:
2. Interconnect the signal source for enabling the frequency setpoint in the "Enable setpoint" ([p1142](SINAMICS%20Parameter%20VECTORMV.md#p11420n-bi-enable-setpointinhibit-setpoint)) field.
3. Interconnect the signal source to start the ramp-function generator in the "Start ramp-function generator" ([p1141](SINAMICS%20Parameter%20VECTORMV.md#p11410n-bi-continue-ramp-function-generatorfreeze-ramp-function-generator)) field.
4. Click the "Ramp-function generator" button or select the appropriate screen form via the secondary navigation.
5. Make the additional settings for the selected ramp-function generator type.

   - [Basic ramp-function generator](#mv-simple-ramp-function-generator)
   - [Extended ramp-function generator](#mv-extended-ramp-function-generator)
6. Interconnect the signal source in the "Enable ramp-function generator" ([p1140](SINAMICS%20Parameter%20VECTORMV.md#p11400n-bi-enable-ramp-function-generatorinhibit-ramp-function-generator)) field to enable the ramp-function generator.
7. Save the settings.

###### Required enables

Various enables are required to operate the ramp-function generator.

- "OFF1 enable" and "OFF3 enable" are set via the control word "Sequential control system". Check the individual bits of the control word at "Diagnostics > Control/status words". Check the interconnection at "Diagnostics > Interconnections".

  The control inputs of the ramp-function generator take effect as follows:

  - 1st priority: OFF3
  - 2nd priority: Ramp-function generator enable
  - 3rd priority: Ramp-function generator start
  - 4th priority: Setpoint enable

The following internal enables are required ([r0046](SINAMICS%20Parameter%20VECTORMV.md#r0046029-cobo-missing-enable-sig)):

- "OFF1 enable internal missing" (r0046[16])

  Shows whether a fault response is present at OFF1. The enable is made only when the fault has been corrected and acknowledged, and the switching on disabled removed with OFF1 = 0.
- "OFF3 enable internal missing" (r0046[18])

  Shows whether an OFF3 has not yet been completed or an OFF3 fault response is present.
- "STOP2 enable internal missing" (r0046[18])

  Shows whether a STOP2 fault response is present.
- "Operation enable missing" (r0046[3])

  Shows that the signal source in [p0852](SINAMICS%20Parameter%20VECTORMV.md#p08520n-bi-enable-operationinhibit-operation) is a 0 signal.

###### Bypassing the ramp-function generator

If you do not want to use the ramp-function generator for a certain time, you can bypass it.

1. In this case, interconnect the signal source in the "Bypass ramp-function generator" ([p1122](SINAMICS%20Parameter%20VECTORMV.md#p11220n-bi-bypass-ramp-function-generator)) field.

###### Enabling the ramp-function generator

To enable the ramp-function generator, proceed as follows:

1. Interconnect the signal source in the "Enable ramp-function generator" (p1140) field to enable the ramp-function generator.

###### Ramp-function generator active

The ramp-function generator only becomes active when the settings described above have been made and the enables according to the logical operations are present.

###### Signal processing

| Symbol | Meaning |
| --- | --- |
| ![Signal processing](images/148105527691_DV_resource.Stream@PNG-en-US.png) | [Setpoint addition](#setpoint-addition) |

###### Function diagrams (FD)

Setpoint channel - basic ramp-function generator - 3060 -

Setpoint channel - extended ramp-function generator - 3070 -

Setpoint channel - ramp-function generator selection, status word, tracking - 3080 -

###### Additional parameters

- [p0115](SINAMICS%20Parameter%20VECTORMV.md#p011506-sampling-times-for-internal-control-loops)
- [r1119](SINAMICS%20Parameter%20VECTORMV.md#r1119-co-ramp-function-generator-setpoint-at-the-input)
- [r1150](SINAMICS%20Parameter%20VECTORMV.md#r1150-co-ramp-function-generator-speed-setpoint-at-the-output)
- [r1198](SINAMICS%20Parameter%20VECTORMV.md#r1198015-cobo-control-word-setpoint-channel)

---

##### MV simple ramp-function generator

###### Description

With the basic ramp-function generator, the input values are passed on to the output via linear ramps, i.e. there is no rounding at the start and end of the range; the drive is accelerated or decelerated linearly.

![Basic ramp-function generator](images/147855220363_DV_resource.Stream@PNG-en-US.png)

Basic ramp-function generator

###### Signal source

| Symbol | Meaning |
| --- | --- |
| ![Signal source](images/148105455115_DV_resource.Stream@PNG-en-US.png) | [Ramp-function generator](#mv-ramp-function-generator) |

###### Setting the ramp-up time and ramp-down time

The ramp-function generator is parameterized via the ramp-up and ramp-down times, whereby these refer to the speed limit n<sub>max</sub>.

1. Correct the specified ramp-up time ([p1047](SINAMICS%20Parameter%20VECTORMV.md#p10470n-motorized-potentiometer-ramp-up-time)) from standstill to maximum speed.
2. Interconnect the signal source for scaling the ramp-up time of the ramp-function generator in the "Scaling factor" ([p1138](SINAMICS%20Parameter%20VECTORMV.md#p11380n-ci-ramp-function-generator-ramp-up-time-scaling)) field.
3. Correct the specified ramp-down time ([p1048](SINAMICS%20Parameter%20VECTORMV.md#p10480n-motorized-potentiometer-ramp-down-time)) from maximum speed to standstill.
4. Interconnect the signal source for scaling the ramp-down time of the ramp-function generator in the "Scaling factor" ([p1139](SINAMICS%20Parameter%20VECTORMV.md#p11390n-ci-ramp-function-generator-ramp-down-time-scaling)) field.
5. Correct the specified value for the OFF3 ramp-down time ([p1135](SINAMICS%20Parameter%20VECTORMV.md#p11350n-off3-ramp-down-time)).

   The OFF3 ramp-down time is the ramp-down time that may elapse from maximum speed down to standstill for the OFF3 command.

###### Setting the setting value

Setting values are the values to which the ramp-function generator jumps automatically.

| Symbol | Meaning |
| --- | --- |
| 1. Interconnect the signal source to accept the setting value in the "Accept setting value" ([p1143](SINAMICS%20Parameter%20VECTORMV.md#p11430n-bi-ramp-function-generator-accept-setting-value)) field.     The ramp-function generator behaves as follows depending on the values of parameter p1143:       | Symbol | Meaning |    | --- | --- |    | 0/1 signal | The output of the ramp-function generator is set to the setting value of the ramp-function generator without delay. |    | 1 signal | The setting value of the ramp-function generator takes effect. |    | 1/0 signal | The input value of the ramp-function generator takes effect. The output of the ramp-function generator is adapted to the input value via the ramp-up time or the ramp-down time. |    | 0 signal | The input value of the ramp-function generator takes effect. | 2. Interconnect the signal source for the setting value on the ramp-function generator in the "Setting value" ([p1144](SINAMICS%20Parameter%20VECTORMV.md#p11440n-ci-ramp-function-generator-setting-value)) field. |  |

###### Display parameters

The following information is displayed via display parameters:

- Maximum speed ([p1082](SINAMICS%20Parameter%20VECTORMV.md#p10820n-maximum-speed))

  Display of the highest possible speed. The value for the maximum speed comes from the speed limitation.

###### Signal processing

| Symbol | Meaning |
| --- | --- |
| ![Signal processing](images/148105455115_DV_resource.Stream@PNG-en-US.png) | [Ramp-function generator](#mv-ramp-function-generator) |

###### Function diagrams (FD)

Setpoint channel - basic ramp-function generator - 3060 -

###### Additional parameters

---

##### MV extended ramp-function generator

###### Description

The acceleration (deceleration) is linear. The acceleration can be described by a ramp for a set rounding (without rounding, the acceleration jumps to the value specified by the ramp-up or ramp-down time).

![Extended ramp-function generator](images/147855258379_DV_resource.Stream@PNG-en-US.png)

Extended ramp-function generator

The "Effective ramp-up/ramp-down time" is calculated according to the following formula:

- Effective ramp-up time = ramp-up time + initial rounding/2 + final rounding/2
- Effective ramp-down time = ramp-down time + initial rounding/2 + final rounding/2

###### Signal source

| Symbol | Meaning |
| --- | --- |
| ![Signal source](images/148105455115_DV_resource.Stream@PNG-en-US.png) | [Ramp-function generator](#mv-ramp-function-generator) |

###### Entering rounding parameters

1. Enter a value for the "initial rounding time" ([p1130](SINAMICS%20Parameter%20VECTORMV.md#p11300n-ramp-function-generator-initial-rounding-off-time)).

   The value applies for ramp-up and ramp-down.
2. Enter a value for the "final rounding time" ([p1131](SINAMICS%20Parameter%20VECTORMV.md#p11310n-ramp-function-generator-final-rounding-off-time)).

   The value applies for ramp-up and ramp-down.

###### Setting the ramp-up time and ramp-down time

The ramp-function generator is parameterized via the ramp-up and ramp-down times, whereby these refer to the speed limit n<sub>max</sub>.

1. Correct the specified ramp-up time ([p1047](SINAMICS%20Parameter%20VECTORMV.md#p10470n-motorized-potentiometer-ramp-up-time)) from standstill to maximum speed.
2. Interconnect the signal source for scaling the ramp-up time of the ramp-function generator in the "Scaling factor" ([p1138](SINAMICS%20Parameter%20VECTORMV.md#p11380n-ci-ramp-function-generator-ramp-up-time-scaling)) field.
3. Correct the specified ramp-down time ([p1048](SINAMICS%20Parameter%20VECTORMV.md#p10480n-motorized-potentiometer-ramp-down-time)) from maximum speed to standstill.
4. Interconnect the signal source for scaling the ramp-down time of the ramp-function generator in the "Scaling factor" ([p1139](SINAMICS%20Parameter%20VECTORMV.md#p11390n-ci-ramp-function-generator-ramp-down-time-scaling)) field.
5. Select the "[1] Yes" setting in the "Enable rounding at the zero crossover" drop-down list to enable the rounding at the zero crossover.

###### Setting the setting value

Setting values are the values to which the ramp-function generator jumps automatically. You set the ramp-function generator output to the ramp-function generator setting value.

| Symbol | Meaning |
| --- | --- |
| 1. Interconnect the signal source to accept the setting value in the "Accept setting value" ([p1143](SINAMICS%20Parameter%20VECTORMV.md#p11430n-bi-ramp-function-generator-accept-setting-value)) field.     The ramp-function generator behaves as follows depending on the values of parameter p1143:       | Symbol | Meaning |    | --- | --- |    | 0/1 signal | The output of the ramp-function generator is set to the setting value of the ramp-function generator without delay. |    | 1 signal | The setting value of the ramp-function generator takes effect. |    | 1/0 signal | The input value of the ramp-function generator takes effect. The output of the ramp-function generator is adapted to the input value via the ramp-up time or the ramp-down time. |    | 0 signal | The input value of the ramp-function generator takes effect. | 2. Interconnect the signal source for the setting value on the ramp-function generator in the "Setting value" ([p1144](SINAMICS%20Parameter%20VECTORMV.md#p11440n-ci-ramp-function-generator-setting-value)) field. |  |

###### Setting OFF3-relevant parameters

When an OFF3 occurs, the drive is braked along the OFF3 deceleration ramp.

1. To specify a rounding type, select one of the following options from the drop-down list:

   - "Continuous smoothing" ([p1134](SINAMICS%20Parameter%20VECTORMV.md#p11340n-ramp-function-generator-rounding-off-type) = 0)

     With this setting the rounding is always active, i.e. when setpoint changes occur, they only take effect after the final rounding has been completed. This can result in overshoot.
   - "Discontinuous smoothing" (p1134 = 1)

     A change in the setpoint causes a final rounding to be aborted. This prevents an overshoot. However, this can result in abrupt changes of the velocity/acceleration (jerk).
2. Enter a value for the "OFF3 ramp-down time" ([p1135](SINAMICS%20Parameter%20VECTORMV.md#p11350n-off3-ramp-down-time)).

   The value describes the ramp-down time from maximum speed to standstill with OFF3.
3. Enter a value for the "OFF3 initial rounding time" ([p1136](SINAMICS%20Parameter%20VECTORMV.md#p11360n-off3-initial-rounding-off-time)).
4. Enter a value for the "OFF3 final rounding time" ([p1137](SINAMICS%20Parameter%20VECTORMV.md#p11370n-off3-final-rounding-off-time)).

###### Display parameters

The following information is displayed via display parameters:

- Maximum speed ([p1082](SINAMICS%20Parameter%20VECTORMV.md#p10820n-maximum-speed))

  Display of the highest possible speed. The value for the maximum speed comes from the speed limitation.

###### Signal processing

| Symbol | Meaning |
| --- | --- |
| ![Signal processing](images/148105455115_DV_resource.Stream@PNG-en-US.png) | [Ramp-function generator](#mv-ramp-function-generator) |

###### Function diagrams (FD)

Setpoint channel - extended ramp-function generator - 3070 -

###### Additional parameters

---

##### Application example: Parameterizing the ramp-function generator

###### Basic ramp-function generator or extended ramp-function generator

The ramp-function generator is used to limit the acceleration at sudden setpoint changes. The setting of the ramp-function generator parameters depends on your application and the construction of your machine.

- [Extended ramp-function generator](#mv-extended-ramp-function-generator)

  The extended ramp-function generator limits the acceleration and jerk. This prevents torque jerks at the transitions (constant velocity phase ←→ acceleration/deceleration phase). This is of particular importance for applications (e.g. transport of liquids or lifting gear) that require very "smooth", jerk-free acceleration or deceleration operations.
- [Basic ramp-function generator](#mv-simple-ramp-function-generator)

  The basic ramp-function generator limits the acceleration, but not the change in acceleration (jerk).

If the ramp-up time of the machine is specified via a higher-level controller, the ramp-up time in the drive should be set significantly shorter or maximum the same, in order to avoid delays or overtravel.

If the drive has been dimensioned too small for dynamic ramp-ups, then the ramp-up time should be set so that the drive does not come into overcurrent during acceleration.

###### Parameterizing the ramp-up time and ramp-down time for the extended ramp-function generator

Parameterizing the roundings for the ramp-up time and ramp-down time lengthens the ramp-up time and the ramp-down time; see also [Ramp-function Generator (motorized potentiometer) MV](#ramp-function-generator-motorized-potentiometer-mv). The default setting for the ramp-up time and ramp-down time is 10 s.

![Parameterizing the extended ramp-function generator](images/148105593355_DV_resource.Stream@PNG-en-US.png)

Parameterizing the extended ramp-function generator

1. Enter a value for the ramp-up time ([p1120](SINAMICS%20Parameter%20VECTORMV.md#p11200n-ramp-function-generator-ramp-up-time)).
2. Enter a value for the initial rounding ([p1130](SINAMICS%20Parameter%20VECTORMV.md#p11300n-ramp-function-generator-initial-rounding-off-time)). The value is also taken for the deceleration ramp.
3. Enter a value for the final rounding ([p1131](SINAMICS%20Parameter%20VECTORMV.md#p11310n-ramp-function-generator-final-rounding-off-time)). The value is also taken for the deceleration ramp.
4. Enter a value for the ramp-down time ([p1121](SINAMICS%20Parameter%20VECTORMV.md#p11210n-ramp-function-generator-ramp-down-time)). The factory setting of 10 s is more suitable for larger drives. If you use highly dynamic servo drives, you should adapt this value, i.e. set a shorter time.

The effective ramp-up and ramp-down times are calculated from the entered values.

###### Setting the zero point rounding

The zero point rounding is used for a soft change of direction of rotation, whereby the change also takes longer however. If the change of direction of rotation is to be performed as fast as possible, disable the zero point rounding. Note however that this can result in shocks in the mechanical system if the ramp-up time is set greater than the ramp-down time.

![Zero point rounding](images/148105597707_DV_resource.Stream@PNG-en-US.png)

Zero point rounding

- Select "Yes" in the "Disable rounding at the zero crossover" ([p1151](SINAMICS%20Parameter%20VECTORMV.md#p11510n-ramp-function-generator-configuration)) drop-down list:

###### Parameterizing behavior on OFF3

There is a special ramp which can be set via [p1135](SINAMICS%20Parameter%20VECTORMV.md#p11350n-off3-ramp-down-time) for a quick stop (OFF3) (e.g. for a quick controlled shutdown after pressing the emergency stop pushbutton). The OFF3 ramp-down time sets the ramp time from maximum speed down to standstill for the OFF3 command.

1. Select the required type of smoothing from the "Rounding type" ([p1134](SINAMICS%20Parameter%20VECTORMV.md#p11340n-ramp-function-generator-rounding-off-type)) drop-down list.
2. Enter a value for the OFF3 ramp-down time (p1135). If you do not parameterize a time here, maximum braking is applied on the drive.
3. Enter a value for the "OFF3 initial rounding time" ([p1136](SINAMICS%20Parameter%20VECTORMV.md#p11360n-off3-initial-rounding-off-time)).
4. Enter a value for the "OFF3 final rounding time" ([p1137](SINAMICS%20Parameter%20VECTORMV.md#p11370n-off3-final-rounding-off-time)).

###### Setting the rounding type for setpoint reduction and OFF3

You can set how the setpoint change is to be performed for a setpoint change or for an OFF3 command:

- ② p1134 = "0": Continuous smoothing; rounding is always active. Overshoot can occur. At a setpoint change, the final rounding is performed first and then travel in the direction of the new setpoint.
- ① p1134 = "1": Discontinuous smoothing; at a setpoint change, travel is immediately in the direction of the new setpoint.

  ![Smoothing type](images/148105601803_DV_resource.Stream@PNG-en-US.png)

  Smoothing type

###### Function diagrams (FD)

Setpoint channel - extended ramp-function generator - 3070 -

###### Additional parameters

- [p1143](SINAMICS%20Parameter%20VECTORMV.md#p11430n-bi-ramp-function-generator-accept-setting-value)

---

---

**See also**

[MV ramp-function generator](#mv-ramp-function-generator)

### Open-loop/closed-loop control

This section contains information on the following topics:

- [Vector control features](#vector-control-features)
- [Setpoint addition](#setpoint-addition)
- [Speed setpoint filter](#speed-setpoint-filter)
- [Speed controller](#speed-controller)
- [U/f control](#uf-control)
- [Torque setpoints](#torque-setpoints)
- [Torque limitation](#torque-limitation)
- [Current setpoint filter](#current-setpoint-filter)
- [Current controller](#current-controller)
- [Power unit](#power-unit)
- [Motor](#motor)
- [Motor encoder](#motor-encoder)

#### Vector control features

##### Vector control - Overview

Compared with vector V/f control, vector control offers the following benefits:

- Stability for load and setpoint changes
- Short rise times for setpoint changes (→ better control behavior)
- Short settling times for load changes (→ better response to disturbances)
- Acceleration and braking are possible with maximum settable torque
- Motor protection due to variable torque limitation in motor and regenerative mode
- Drive and braking torque-controlled independently of the speed
- Maximum breakaway torque possible at speed 0

Vector control can be used with or without an encoder.

The following criteria indicate when an encoder is required:

- High speed accuracy is required
- High dynamic response is required

  - Better command behavior
  - Better disturbance characteristic
- Torque control is required in a control range greater than 1:10
- Allows a defined and/or variable torque for speeds below approx. 10% of the rated motor frequency (p0310) to be maintained.

With regard to setpoint input, vector control is divided into:

- Speed control
- Torque/current control (in short: torque control)

##### Sensorless vector control

During operation via the "Sensorless vector control" (SLVC) function, the position of the flux or the actual speed must be determined via the electric motor model. Whereby the motor model is supported by the accessible currents or voltages. At low frequencies (around approx. 0 Hz), the motor model cannot determine the speed accurately enough. For this reason, the vector control can be switched from closed-loop controlled operation to open-loop controlled operation in this range. When using passive loads, additional supplementary conditions must be taken into account (see Supplementary conditions for the operation of third-party motors).

##### Function diagrams (FD)

Vector control - speed controller with/without encoder - 6040 -

#### Setpoint addition

This section contains information on the following topics:

- [MV setpoint addition](#mv-setpoint-addition)
- [MV droop feedback](#mv-droop-feedback)

##### MV setpoint addition

###### Description

The setpoint addition optionally adds two additional speed setpoints to the main setpoint, which is specified by the ramp-function generator.

An interpolator causes a finer grading of the speed setpoints from the ramp-function generator by calculating intermediate steps (interpolation). An interpolator can be used for the respective speed setpoints 1 and 2, and for the speed setpoint at the output of the ramp-function generator.

###### Signal source

| Symbol | Meaning |
| --- | --- |
| ![Signal source](images/148105704459_DV_resource.Stream@PNG-en-US.png) | [MV ramp-function generator](#mv-ramp-function-generator) |
| ![Signal source](images/148105708683_DV_resource.Stream@PNG-en-US.PNG) | [Torque limiting](#mv-torque-limiting)   For source for droop feedback: "[1] Droop from the torque setpoint" |
| ![Signal source](images/148105712907_DV_resource.Stream@PNG-en-US.PNG) | [Torque setpoints](#mv-torque-setpoint)   For source for droop feedback: "[2] Droop from the speed controller output" |
| ![Signal source](images/148105717131_DV_resource.Stream@PNG-en-US.PNG) | [Speed controller](#mv-speed-controller)   For source for droop feedback: "[3] Droop from the integral output speed controller" |

###### Parameterizing setpoint addition

1. In the "Droop source" ([p1488](SINAMICS%20Parameter%20VECTORMV.md#p14880n-droop-input-source)) drop-down list, select from where the value is to be taken for the droop feedback:

   - "[0] Droop feedback not connected"
   - "[1] Droop from the torque setpoint"
   - "[2] Droop from the torque control output"
   - "[3] Droop from the integral output, speed controller"
2. Interconnect the signal source for speed setpoint 1 of the speed controller in the "Speed setpoint 1" ([p1155](SINAMICS%20Parameter%20VECTORMV.md#p11550n-ci-speed-controller-speed-setpoint-1)) field.
3. Interconnect the signal source for speed setpoint 2 of the speed controller in the "Speed setpoint 2" ([p1160](SINAMICS%20Parameter%20VECTORMV.md#p11600n-ci-speed-controller-speed-setpoint-2)) field.

   "Speed setpoint 1" and "Speed setpoint 2" are added to the speed setpoint after the ramp-function generator.
4. Select the interpolators if required:

   - In the drop-down list below the top button "Interpolation", select the option "[1] Yes" ([p1189](SINAMICS%20Parameter%20VECTORMV.md#p11890n-speed-setpoint-configuration).1) to activate the interpolator for speed setpoints 1 and 2.
   - In the drop-down list below the lower button "Interpolation", select the option "[1] Yes" (p1189.0) to activate the interpolator for the speed setpoint from the ramp-function generator.
5. If you have activated a droop feedback (droop source [1] ... [3]), you now parameterize the droop feedback (see [Droop feedback](#mv-droop-feedback)).

###### Signal processing

| Symbol | Meaning |
| --- | --- |
| ![Signal processing](images/148105700235_DV_resource.Stream@PNG-en-US.png) | [Speed setpoint filter](#speed-setpoint-filter) |

###### Function diagrams (FD)

Vector control - speed setpoint, droop - 6030 -

###### Additional parameters

- [p0115](SINAMICS%20Parameter%20VECTORMV.md#p011506-sampling-times-for-internal-control-loops)
- [r0898](SINAMICS%20Parameter%20VECTORMV.md#r0898012-cobo-control-word-sequence-control)
- [r1150](SINAMICS%20Parameter%20VECTORMV.md#r1150-co-ramp-function-generator-speed-setpoint-at-the-output)
- [r1169](SINAMICS%20Parameter%20VECTORMV.md#r1169-co-speed-controller-speed-setpoints-1-and-2)
- [r1170](SINAMICS%20Parameter%20VECTORMV.md#r1170-co-speed-controller-setpoint-sum)

---

##### MV droop feedback

Droop (enabled via [p1492](SINAMICS%20Parameter%20VECTORMV.md#p14920n-bi-droop-feedback-enable)) ensures that the speed setpoint is reduced proportionally as the load torque increases.

![Speed controller with droop](images/148105742987_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Active only when the precontrol has been activated ([p1496](SINAMICS%20Parameter%20VECTORMV.md#p14960n-acceleration-precontrol-scaling) > 0) |
| ② | Active only for SLVC |

Speed controller with droop

The droop has a torque limiting effect on a drive that is mechanically coupled to a different speed (e.g. roller for a web guidance). In connection with the torque setpoint of a leading speed-controlled drive, a very effective load distribution can also be implemented. With the appropriate setting (in contrast to torque control or load distribution with overload and limitation), this load distribution controls even a smooth mechanical coupling or the case of slipping.

This method is only suitable to a limited extent for drives that are accelerated and braked with significant changes in speed.

The droop feedback is used, for example, in applications in which two or more motors are connected mechanically or operate with a common shaft and fulfill the above requirements. It limits the torque differences that can occur as a result of the mechanical coupling by appropriately modifying the speeds of the individual motors. The drive is relieved when the torque is too large.

**Requirements**

- All coupled drives must be operated in vector control and closed-loop speed control, with or without an encoder.
- Only a single common ramp-function generator may be used for mechanically coupled drives.

###### Parameterizing the droop feedback

1. Click the "Droop feedback" button.

   A dialog with the same name opens.
2. Interconnect the signal source for the compensation torque within the droop calculation in the "Droop torque 2" ([p1486](SINAMICS%20Parameter%20VECTORMV.md#p14860n-ci-droop-compensation-torque)) field.
3. Correct the specified value for scaling the compensation torque within the droop calculation in the "Droop scaling torque 2" ([p1487](SINAMICS%20Parameter%20VECTORMV.md#p14870n-droop-compensation-torque-scaling)) field.
4. Interconnect the signal source to enable the droop to be applied to the speed/velocity setpoint in the "Droop enable" (p1492) field.
5. Correct the specified value for scaling the droop feedback in the "Droop scaling" ([p1489](SINAMICS%20Parameter%20VECTORMV.md#p14890n-droop-feedback-scaling)) field.
6. Once you have made all the necessary settings, click the "Close" button.

   The dialog closes.

###### Function diagrams (FD)

Vector control - speed setpoint, droop - 6030 -

###### Additional parameters

- [r0079](SINAMICS%20Parameter%20VECTORMV.md#r0079-co-torque-setpoint)
- [r1482](SINAMICS%20Parameter%20VECTORMV.md#r1482-co-speed-controller-i-torque-output)
- [p1488](SINAMICS%20Parameter%20VECTORMV.md#p14880n-droop-input-source)
- [r1490](SINAMICS%20Parameter%20VECTORMV.md#r1490-co-droop-feedback-speed-reduction)
- [r1508](SINAMICS%20Parameter%20VECTORMV.md#r1508-co-torque-setpoint-before-supplementary-torque)

---

#### Speed setpoint filter

This section contains information on the following topics:

- [MV speed setpoint filter](#mv-speed-setpoint-filter)
- [MV maximum limit](#mv-maximum-limit)
- [MV acceleration precontrol](#mv-acceleration-precontrol)
- [MV precontrol balancing](#mv-precontrol-balancing)

##### MV speed setpoint filter

###### Description

The speed setpoint filter contains the acceleration precontrol, the speed setpoint limiting, and the precontrol balancing.

The speed precontrol and the acceleration precontrol are processed via an acceleration model. The acceleration is calculated from the speed difference over the time "dn/dt". You can parameterize settings for the acceleration precontrol torque in the "[Precontrol](#mv-acceleration-precontrol)" dialog. A limiter ensures that the acceleration torque cannot become too great. Over the further course, an integration element ensures that the acceleration is converted back to a speed and is applied to the speed setpoint as a value for the speed precontrol.

The signal paths depend on the following settings:

- Acceleration precontrol signal source ([p1400](SINAMICS%20Parameter%20VECTORMV.md#p14000n-speed-control-configuration).2):

  - "Internal"

    The main signal comes from the setpoint addition and is modified via the acceleration model (precontrol).
  - "External"

    An external signal is interconnected for the acceleration precontrol. The value comes from a higher-level control, for example.
- Reference model (p1400.3):

  - "On"

    The signal runs through the reference model.
  - "Off"

    The signal runs directly from the setpoint addition into the speed controller. The reference model plays no role in this scenario.

###### Signal source

| Symbol | Meaning |
| --- | --- |
| ![Signal source](images/148105806091_DV_resource.Stream@PNG-en-US.png) | [Setpoint addition](#mv-setpoint-addition) |

###### Set speed setpoint with acceleration precontrol from external signal source

1. Select the "[1] External ([p1495](SINAMICS%20Parameter%20VECTORMV.md#p14950n-ci-acceleration-precontrol))" signal source in the "Acceleration precontrol signal source" (p1400.2) drop-down list.

   The circuit diagram is updated according to this setting.
2. Interconnect the signal source for the acceleration precontrol in the "Acceleration precontrol" field (p1495).
3. Click the "Precontrol acceleration" button and record the values for the precontrol in the "[Precontrol](#mv-acceleration-precontrol)" dialog.
4. Enter a value for the scaling of the acceleration precontrol ([p1496](SINAMICS%20Parameter%20VECTORMV.md#p14960n-acceleration-precontrol-scaling)) in the field below the "Precontrol acceleration" button.

   Via this evaluation factor, you can adapt the acceleration precontrol depending on the application.
5. Then make the settings for the precontrol balancing as needed via the [Precontrol balancing](#mv-precontrol-balancing) dialog.

###### Set speed setpoint from "Setpoint addition" without acceleration model

1. Select the "[0] Internal (n_set)" or "[1] External (p1495)" signal source in the "Acceleration precontrol signal source" (p1400.2) drop-down list.

   The circuit diagram is updated according to this setting. With the "External" setting, you can also parameterize the precontrol balancing.
2. Because you do not want to use an acceleration model, deactivate the option "Reference model" (p1400).

   In this way, you define that the input value of the "Precontrol balancing" comes from the "setpoint addition".
3. Click the "Speed setpoint limited" button and record the values for the maximum limit of the speed setpoint in the "[Maximum limitation](#mv-maximum-limit)" dialog.
4. Enter a value for the time constant in the "Smoothing" field ([p1416](SINAMICS%20Parameter%20VECTORMV.md#p14160n-speed-setpoint-filter-1-time-constant)).

   The speed setpoint is given to the "Precontrol balancing" delayed by the time constant (PT1 behavior).
5. If you set an external signal source (see 1.), you can make the settings for [precontrol balancing](#mv-precontrol-balancing).

###### Set speed setpoint from "Setpoint addition" with acceleration model

1. Select the "[0] Internal (n_set)" signal source in the "Acceleration precontrol signal source" (p1400.2) drop-down list.

   The circuit diagram is updated according to this setting.
2. Click the "Speed setpoint limited" button and record the values for the maximum limit of the speed setpoint in the "[Maximum limitation](#mv-maximum-limit)" dialog.
3. Enter a value for the time constant in the "Smoothing" field (p1416).

   The speed setpoint is given at the output, delayed by the time constant (PT1 behavior).
4. Click the "Precontrol acceleration" button and record the values for the Dn/Dt precontrol in the "[Precontrol](#mv-acceleration-precontrol)" dialog.
5. Enter a value for the scaling of the acceleration precontrol (p1496) in the field below the "Precontrol acceleration" button.

   Via this evaluation factor, you can adapt the acceleration precontrol depending on the application.

###### Signal processing

| Symbol | Meaning |
| --- | --- |
| ![Signal processing](images/148105810315_DV_resource.Stream@PNG-en-US.png) | [Torque setpoints](#torque-setpoints) |
| ![Signal processing](images/148105865739_DV_resource.Stream@PNG-en-US.png) | [Speed controller](#speed-controller) |

###### Function diagrams (FD)

Vector control - speed setpoint, droop - 6030 -

Vector control - pre-control balancing reference/acceleration model - 6031 -

###### Additional parameters

- [r0062](SINAMICS%20Parameter%20VECTORMV.md#r0062-co-speed-setpoint-after-the-filter)
- [r0115](SINAMICS%20Parameter%20VECTORMV.md#p011506-sampling-times-for-internal-control-loops)
- [r1438](SINAMICS%20Parameter%20VECTORMV.md#r1438-co-speed-controller-speed-setpoint)

---

##### MV maximum limit

###### Description

You limit the speed setpoint via a maximum speed. This is the maximum speed value the motor should have. A change of this value has an effect on the controller and ramp-function generator settings. There are other limitation variants, i.e. an individual fixed limit can be specified for the negative and the positive direction of rotation.

The value "n max" (maximum speed) always has priority.

> **Note**
>
> **Changing the maximum speed**
>
> Changing the maximum speed [p1082](SINAMICS%20Parameter%20VECTORMV.md#p10820n-maximum-speed) has an effect on the following functions:
>
> - OFF3 deceleration ramp
> - Ramp-function generator
> - Motorized potentiometer

###### Defining the maximum limitation of the speed

1. Click the "Speed setpoint limited" button.

   The "Maximum limitation" dialog opens.
2. Interconnect the signal source for speed limitation in the positive direction of rotation in the "Pos. variable speed limit" ([p1085](SINAMICS%20Parameter%20VECTORMV.md#p10850n-ci-speed-limit-in-positive-direction-of-rotation)) field.
3. Correct the value specified for limitation of the positive speed setpoint in the "Positive speed limit" ([p1083](SINAMICS%20Parameter%20VECTORMV.md#p10830n-co-speed-limit-in-positive-direction-of-rotation)) field.
4. Correct the value specified for the maximum speed in the "Maximum speed" (p1082) field.
5. Correct the value specified for limitation of the negative speed setpoint in the "Negative speed limit" ([p1086](SINAMICS%20Parameter%20VECTORMV.md#p10860n-co-speed-limit-in-negative-direction-of-rotation)) field.
6. Interconnect the signal source for speed limitation in the negative direction of rotation in the "Neg. variable speed limit" ([p1088](SINAMICS%20Parameter%20VECTORMV.md#p10880n-ci-speed-limit-in-negative-direction-of-rotation)) field.
7. Once you have made all the necessary settings, click the "Close" button.

   The dialog closes.

###### Function diagrams (FD)

Vector control - speed setpoint, droop - 6030 -

###### Additional parameters

- [r1084](SINAMICS%20Parameter%20VECTORMV.md#r1084-co-speed-limit-positive-effective)
- [r1087](SINAMICS%20Parameter%20VECTORMV.md#r1087-co-speed-limit-negative-effective)

---

##### MV acceleration precontrol

###### Description

The command behavior of the speed control loop is improved when the acceleration torque is calculated from the speed setpoint and the speed controller is series-connected.

###### Parameterizing the motor moment of inertia and scaling

The motor moment of inertia [p0341](SINAMICS%20Parameter%20VECTORMV.md#p03410n-motor-moment-of-inertia) is calculated directly during commissioning or when the entire set of parameters is calculated ([p0340](SINAMICS%20Parameter%20VECTORMV.md#p03400n-automatic-calculation-motorcontrol-parameters) = 1). You determine the factor [p0342](SINAMICS%20Parameter%20VECTORMV.md#p03420n-ratio-between-the-total-and-motor-moment-of-inertia) between the total moment of inertia J and the motor moment of inertia manually or via the speed controller optimization. The acceleration is calculated from the speed difference over time dn/dt.

1. Click the "Acceleration precontrol" button.

   The "Precontrol" dialog opens.
2. Interconnect the signal source for scaling the moment of inertia in the "Scaling of moment of inertia" field ([p1497](SINAMICS%20Parameter%20VECTORMV.md#p14970n-ci-moment-of-inertia-scaling-signal-source)).
3. Enter a value for the scaling of the acceleration precontrol in [%] in the "Precontrol acceleration" field ([p1496](SINAMICS%20Parameter%20VECTORMV.md#p14960n-acceleration-precontrol-scaling)).
4. Enter a value for the motor moment of inertia in the "Motor moment of inertia" field (p0341).
5. Correct the value specified for the ratio between the total moment of inertia/mass (load + motor) and the solitary motor moment of inertia/mass (without load) in the "Ratio moment of inertia/motor" (p0342) field.

   The rated startup time of the motor for a vector drive is calculated from p0342 and p0341.
6. Once you have made all the necessary settings, click the "Close" button.

   The dialog closes.

###### Function diagrams (FD)

Vector control - pre-control balancing reference/acceleration model - 6031 -

Vector control - speed controller with/without encoder - 6040 -

###### Additional parameters

- [r0056](SINAMICS%20Parameter%20VECTORMV.md#r0056215-cobo-status-word-closed-loop-control)
- [r1493](SINAMICS%20Parameter%20VECTORMV.md#r1493-co-moment-of-inertia-total)

---

##### MV precontrol balancing

###### Description

In order that the speed controller does not counteract the applied torque setpoint, you must parameterize the precontrol balancing. The precontrol balancing serves to prevent unwanted controller motions until the precontrol is activated. The precontrol balancing is implemented as a PT1 element.

###### Requirement

- The precontrol balancing becomes active only when P gain [p1460](SINAMICS%20Parameter%20VECTORMV.md#p14600n-speed-controller-p-gain-adaptation-speed-lower) > 0% is set and the reference model is deactivated.

###### Setting precontrol balancing

1. Click the "Precontrol balancing" button in the "Speed setpoint filter" screen form.

   An input dialog with the same name opens.
2. In the "Dead time factor" field ([p1428](SINAMICS%20Parameter%20VECTORMV.md#p14280n-speed-precontrol-balancing-dead-time)), enter the dead time for the balancing of the speed setpoint with active torque precontrol.

   With active torque precontrol, the speed precontrol must be delayed until the torque precontrol has acted, and the new actual speed value is available. The "new" setpoint should not arrive until the current actual value of the speed controller is known. If torque precontrol is not possible (e.g. the moment of inertia J of the drive is not known), the speed precontrol value does not need to be delayed.
3. In the "Smoothing" field ([p1429](SINAMICS%20Parameter%20VECTORMV.md#p14290n-speed-precontrol-balancing-time-constant)), enter the time constant (PT1) for the balancing of the speed setpoint with active torque precontrol.

   The time constant specifies the course of the signal rise. You specify the rate of increase of the speed setpoint with this time constant.

p1428 and p1429 together emulate the runtime behavior of the torque development (dynamics of the closed current control loop).

###### Function diagrams (FD)

Vector control - pre-control balancing reference/acceleration model - 6031 -

Vector control - speed controller with/without encoder - 6040 -

###### Additional parameters

---

#### Speed controller

This section contains information on the following topics:

- [MV speed controller](#mv-speed-controller)
- [MV Kp/Tn adaptation](#mv-kptn-adaptation)
- [MV integrator control](#mv-integrator-control)
- [Application example: Parameterizing the reference model](#application-example-parameterizing-the-reference-model)

##### MV speed controller

###### Description

Define the parameters of the speed controller without encoder here.

- The P gain K<sub>p</sub> and the integral time T<sub>n</sub> of the lower adaptation speed of the speed controller will be displayed.
- The smoothing for the actual speed value can be entered.

Reference model On/Off can be used to activate/deactivate the reference model. The corresponding buttons for the reference model will be displayed or hidden.

Using the adaptation, enables a switchable parameterization of the K<sub>p</sub> (P gain) value for two different speeds (upper and lower adaptation speed). It is hence easier to overcome friction forces, for example, if during startup a higher K<sub>p</sub> is selected and then switched over.

Use the PI controller to amplify the controller difference between the setpoint (from the speed setpoint filter) and the actual speed value.

###### Signal source

| Symbol | Meaning |
| --- | --- |
| ![Signal source](images/148105700235_DV_resource.Stream@PNG-en-US.png) | [Speed setpoint filter](#mv-speed-setpoint-filter) |
| ![Signal source](images/148105978251_DV_resource.Stream@PNG-en-US.png) | [Motor encoder](#mv-motor-encoder) |

###### Parameterizing the speed controller

1. Select the control type in the "Control type" ([p1300](SINAMICS%20Parameter%20VECTORMV.md#p13000n-open-loopclosed-loop-control-operating-mode)) drop-down list:

   - Speed control (encoderless)  
     For this type of control, an automatic Kp/Tn adaptation can also be optionally activated.
   - Speed control (with encoder)
   - Speed control (encoderless)  
     For this type of control, an automatic Kp/Tn adaptation can also be optionally activated.
   - Torque control (with encoder)
2. Select in the "Reference model" drop-down list ([p1400](SINAMICS%20Parameter%20VECTORMV.md#p14000n-speed-control-configuration).3) whether a "Velocity setpoint I-component" reference model is to be used:

   - "[0] Off"
   - "[1] On"

   For an activated reference model, additional configuration parameters are displayed (see "Parameterizing a reference model").
3. Correct the P gain before the adaptation speed range specified in the "P gain" ([p1470](SINAMICS%20Parameter%20VECTORMV.md#p14700n-speed-controller-encoderless-operation-p-gain)) field.
4. Correct the integral time before the adaptation speed range specified in the "Integral time" ([p1472](SINAMICS%20Parameter%20VECTORMV.md#p14720n-speed-controller-encoderless-operation-integral-time)) field.
5. Click the "Smoothing" button and interconnect the signal source for the actual speed value of the speed controller ([p1440](SINAMICS%20Parameter%20VECTORMV.md#p14400n-ci-speed-controller-speed-actual-value-input)) in the "Actual speed value filter" dialog.
6. In the "Smoothing" field ([p1452](SINAMICS%20Parameter%20VECTORMV.md#p14520n-speed-controller-speed-actual-value-smoothing-time-sensorless)), enter the smoothing time for the actual speed value of the speed controller for speed control with encoder.
7. Specify the values for the Kp/Tn adaptation (see [MV Kp/Tn adaptation](#mv-kptn-adaptation)).
8. Specify the controller parameters for the I component of the PI controller via the "Integrator control" (see [MV integrator control](#mv-integrator-control)).

###### Parameterizing the reference model

The following configuration parameters are only displayed in the screen form when the "Reference model" option is activated.

Then make the following settings:

1. Click the "Reference model" button.

   A dialog with the same name opens.
2. Enter the "Natural frequency" ([p1433](SINAMICS%20Parameter%20VECTORMV.md#p14330n-speed-controller-reference-model-natural-frequency)), the natural frequency of a PT2 element, for the reference model of the speed controller.
3. Enter the "Damping" ([p1434](SINAMICS%20Parameter%20VECTORMV.md#p14340n-speed-controller-reference-model-damping)), the damping of a PT2 element, for the reference model of the speed controller.
4. Enter the "Dead time factor" ([p1435](SINAMICS%20Parameter%20VECTORMV.md#p14350n-speed-controller-reference-model-dead-time)), the broken dead time for the reference model of the speed controller.
5. If applicable, in the "Interconnections..." drop-down list, select one of the following signal sources or inputs and interconnect them:

   - Speed controller reference model I component input ([p1436](SINAMICS%20Parameter%20VECTORMV.md#r1436-co-speed-controller-reference-model-speed-setpoint-output)[0])
   - Speed controller reference model I component input (p1436[1])
6. In the "Reference model I component input" field ([p1437](SINAMICS%20Parameter%20VECTORMV.md#p14370n-ci-speed-controller-reference-model-i-component-input)), interconnect the signal source for the speed setpoint for the integral component of the speed controller.
7. Once you have made all the necessary settings, click the "Close" button.

   The dialog closes. You have defined a valid reference model when the button shows a curve:

   ![Parameterizing the reference model](images/148105974283_DV_resource.Stream@PNG-en-US.png)

   ![Parameterizing the reference model](images/148105974283_DV_resource.Stream@PNG-en-US.png)

###### Signal processing

| Symbol | Meaning |
| --- | --- |
| ![Signal processing](images/148105810315_DV_resource.Stream@PNG-en-US.png) | [Torque setpoints](#mv-torque-setpoint) |
| ![Signal processing](images/148106020875_DV_resource.Stream@PNG-en-US.png) | [Setpoint addition](#mv-setpoint-addition) |

###### Function diagrams (FD)

Vector control - speed control and generation of the torque limits, overview - 6020 -

Vector control - speed controller adaptation (Kp_n/Tn_n adaptation) - 6050 -

###### Additional parameters

- [r0062](SINAMICS%20Parameter%20VECTORMV.md#r0062-co-speed-setpoint-after-the-filter)
- [r0063](SINAMICS%20Parameter%20VECTORMV.md#r006302-co-speed-actual-value)
- [r0064](SINAMICS%20Parameter%20VECTORMV.md#r0064-co-speed-controller-system-deviation)
- [p0115](SINAMICS%20Parameter%20VECTORMV.md#p011506-sampling-times-for-internal-control-loops)
- [r1436](SINAMICS%20Parameter%20VECTORMV.md#r1436-co-speed-controller-reference-model-speed-setpoint-output)
- [r1438](SINAMICS%20Parameter%20VECTORMV.md#r1438-co-speed-controller-speed-setpoint)
- [r1443](SINAMICS%20Parameter%20VECTORMV.md#r1443-co-speed-controller-speed-actual-value-at-actual-value-input)
- [r1445](SINAMICS%20Parameter%20VECTORMV.md#r1445-co-actual-speed-smoothed)
- [r1454](SINAMICS%20Parameter%20VECTORMV.md#r1454-co-speed-controller-system-deviation-i-component)
- [r1468](SINAMICS%20Parameter%20VECTORMV.md#r1468-co-speed-controller-p-gain-effective)
- [r1469](SINAMICS%20Parameter%20VECTORMV.md#r1469-speed-controller-integral-time-effective)
- [r1480](SINAMICS%20Parameter%20VECTORMV.md#r1480-co-speed-controller-pi-torque-output)
- [r1481](SINAMICS%20Parameter%20VECTORMV.md#r1481-co-speed-controller-p-torque-output)
- [r1482](SINAMICS%20Parameter%20VECTORMV.md#r1482-co-speed-controller-i-torque-output)

---

##### MV Kp/Tn adaptation

###### Description

The K<sub>p</sub>/T<sub>n</sub> adaptation permits a completely variable proportional gain K<sub>p</sub>. To do this, the adaptation factor can be scalably interconnected via BICO technology. A linear adaptation characteristic can be defined by specifying two characteristic interpolation points.

###### Defining adaptation parameters

1. In the "K<sub>p</sub>/T<sub>n</sub> adaptation active" drop-down list, select the option "[1] Yes" ([p1400](SINAMICS%20Parameter%20VECTORMV.md#p14000n-speed-control-configuration).5).

   The K<sub>p</sub>/T<sub>n</sub> adaptation is activated and can be parameterized. No adaptation parameters can be specified without this activation.
2. Click the "Adaptation" button next to the input field of the p gain.

   The input screen form "K<sub>p</sub>/T<sub>n</sub> adaptation" is displayed.
3. Interconnect the signal source for scaling the P gain of the velocity controller in the "Scaling" ([p1466](SINAMICS%20Parameter%20VECTORMV.md#p14660n-ci-speed-controller-p-gain-scaling)) field.
4. Interconnect the signal source for the adaptation signal for the additional adaptation of the P gain of the speed controller in the "Adaptation signal" ([p1455](SINAMICS%20Parameter%20VECTORMV.md#p14550n-ci-speed-controller-p-gain-adaptation-signal)) field.
5. Click the "Adaptation" button.

   A dialog with the same name opens.
6. Enter the percentage values for the following adaptation parameters:

   - "Adaptation factor upper" ([p1459](SINAMICS%20Parameter%20VECTORMV.md#p14590n-adaptation-factor-upper))

     Set the adaptation factor after the adaptation range (> [p1457](SINAMICS%20Parameter%20VECTORMV.md#p14570n-speed-controller-p-gain-adaptation-upper-starting-point)) to additionally adapt the P gain of the speed/velocity controller.
   - "Adaptation factor lower" ([p1458](SINAMICS%20Parameter%20VECTORMV.md#p14580n-adaptation-factor-lower))

     Set the adaptation factor before the adaptation range (0% ... [p1456](SINAMICS%20Parameter%20VECTORMV.md#p14560n-speed-controller-p-gain-adaptation-lower-starting-point)) to additionally adapt the P gain of the speed/velocity controller.
   - "Lower application point" (p1456)

     Set the lower application point of the adaptation range for the additional adaptation of the P gain of the speed controller.
   - "Upper application point" (p1457)

     Set the upper application point of the adaptation range for the additional adaptation of the P gain of the speed controller.
7. Once you have made all the necessary settings, click the "Close" button.

   The dialog closes.
8. Enter the percentage values for the following parameters:

   - "Scaling" ([p1461](SINAMICS%20Parameter%20VECTORMV.md#p14610n-speed-controller-kp-adaptation-speed-upper-scaling))

     Enter the P gain of the speed controller for the upper adaptation speed range (> [p1465](SINAMICS%20Parameter%20VECTORMV.md#p14650n-speed-controller-adaptation-speed-upper)).
   - "Scaling" ([p1463](SINAMICS%20Parameter%20VECTORMV.md#p14630n-speed-controller-tn-adaptation-speed-upper-scaling))

     Set the integral time of the speed controller after the adaptation speed range (> p1465).
9. Enter the desired speed in the "Upper adaptation speed" (p1465) field.
10. Enter the desired speed in the "Lower adaptation speed" ([p1464](SINAMICS%20Parameter%20VECTORMV.md#p14640n-speed-controller-adaptation-speed-lower)) field.
11. In the "Free T<sub>n</sub> adaptation active" drop-down list (p1400.6) select the option "[1] Yes" if you want to optimize the T<sub>n</sub> component of the speed-dependent adaptation. The T<sub>n</sub> value of the speed-dependent adaptation is divided by the factor of the free adaptation.

**Note**

For the control type "V/f controller with linear characteristics", you can activate an automatic adaptation in parallel to the manual adaptation.

In this case, select the entry "[1] Yes" in the "Auto K<sub>p</sub>/T<sub>n</sub> adaptation" drop-down list (p1400.0).

###### Display parameters

The following information is displayed via display parameters:

- "P gain" ([p1470](SINAMICS%20Parameter%20VECTORMV.md#p14700n-speed-controller-encoderless-operation-p-gain))

  Display of the p gain value
- "Actual speed value" ([r0063](SINAMICS%20Parameter%20VECTORMV.md#r006302-co-speed-actual-value))

  Display and connector output for the currently smoothed actual speed value.
- "Integral time" ([p1472](SINAMICS%20Parameter%20VECTORMV.md#p14720n-speed-controller-encoderless-operation-integral-time))

  Display of the integral time

###### Signal processing

| Symbol | Meaning |
| --- | --- |
| ![Signal processing](images/148105865739_DV_resource.Stream@PNG-en-US.png) | [Speed controller](#mv-speed-controller) |

###### Function diagrams (FD)

Vector control - speed controller with/without encoder - 6040 -

Vector control - speed controller adaptation (Kp_n/Tn_n adaptation) - 6050 -

###### Additional parameters

- [r1468](SINAMICS%20Parameter%20VECTORMV.md#r1468-co-speed-controller-p-gain-effective)
- [r1469](SINAMICS%20Parameter%20VECTORMV.md#r1469-speed-controller-integral-time-effective)

---

##### MV integrator control

###### Description

You specify the parameters used to control the I-component of the PI controller in the "Integrator control" dialog.

If you set a value in "Integrator feedback", the integrator of the speed/velocity controller is reparameterized to become a PT1 filter through a feedback element (1st order low-pass filter characteristic).

For cases in which the control becomes saturated because, for example, a limit is exceeded (e.g. hanging load), the I-component grows rapidly. If the fault disappears, the actual exceedingly high I-component must first be slowly reduced (windup).

With "Hold integrator", you shut down the integrator when the limitation is exceeded (saturation) and specify a setting value when switching on the final controlling element for the I component, e.g. via "Set integrator value".

###### Specifying the parameters of the I component

1. Click the "Integrator control" button in the "Speed controller" screen form.

   The dialog with the same name opens.
2. Interconnect the signal source for the "Enable speed controller" command ([r0898](SINAMICS%20Parameter%20VECTORMV.md#r0898012-cobo-control-word-sequence-control).12) in the "Enable speed controller" field ([p0856](SINAMICS%20Parameter%20VECTORMV.md#p08560n-bi-enable-speed-controller)).
3. Interconnect the signal source to hold the integrator (speed control with encoder, torque control with encoder) in the "Hold integrator" ([p1476](SINAMICS%20Parameter%20VECTORMV.md#p14760n-bi-speed-controller-hold-integrator)) field.
4. Interconnect the signal source to set the integrator value in the "Set integrator value" ([p1477](SINAMICS%20Parameter%20VECTORMV.md#p14770n-bi-speed-controller-set-integrator-value)) field.
5. Interconnect the signal source from which the integrator setting value is to be read in the "Integrator setting value" ([p1478](SINAMICS%20Parameter%20VECTORMV.md#p14780n-ci-speed-controller-integrator-setting-value)) field.
6. Interconnect the signal source for scaling the integrator setting value (p1478) of the speed controller in the "Scaling setting value" ([p1479](SINAMICS%20Parameter%20VECTORMV.md#p14790n-ci-speed-controller-integrator-setting-value-scaling)) field.
7. Once you have made all the necessary settings, click the "Close" button.

   The dialog closes.

###### Display parameters

The following information is displayed via display parameters:

- "P gain" ([r1468](SINAMICS%20Parameter%20VECTORMV.md#r1468-co-speed-controller-p-gain-effective))

  Displays the effective P gain of the speed controller.
- "Integral time" ([r1469](SINAMICS%20Parameter%20VECTORMV.md#r1469-speed-controller-integral-time-effective))

  Displays the effective integral time of the speed controller.
- "PI torque output" ([r1480](SINAMICS%20Parameter%20VECTORMV.md#r1480-co-speed-controller-pi-torque-output))

  Display and connector output for the torque setpoint at the output of the PI speed controller.
- "P torque output" ([r1481](SINAMICS%20Parameter%20VECTORMV.md#r1481-co-speed-controller-p-torque-output))

  Display and connector output for the torque setpoint at the output of the P speed controller.
- "I torque output" ([r1482](SINAMICS%20Parameter%20VECTORMV.md#r1482-co-speed-controller-i-torque-output))

  Display and connector output for the torque setpoint at the output of the I speed controller.

###### Terminology for the use of linear motors

When linear motors are used, a linear motion is executed instead of a rotary motion. The terms change accordingly:

- Speed corresponds to velocity
- Torque corresponds to force

###### Function diagrams (FD)

Vector control - speed controller with/without encoder - 6040 -

###### Additional parameters

- p1476
- p1477

---

##### Application example: Parameterizing the reference model

###### Reference model

The reference model serves for simulating the path of the speed control loop with a P speed controller. The reference model delays the setpoint / actual value deviation for the integral component of the speed controller so that the transient elements can be suppressed. The integral component in the controller is mainly responsible for excessive oscillations that are further integrated during the limitation phase, and thus generate an actuating signal that is too large.

![Reference model](images/148106107403_DV_resource.Stream@PNG-en-US.png)

Reference model

The reference model is activated with [p1400](SINAMICS%20Parameter%20VECTORMV.md#p14000n-speed-control-configuration).3 = 1.

**Parameters**

- "Dead time factor ([p1435](SINAMICS%20Parameter%20VECTORMV.md#p14350n-speed-controller-reference-model-dead-time))", with active torque precontrol, the speed precontrol must be delayed until the torque precontrol has acted, and the new actual speed value is available.
- "Natural frequency ([p1433](SINAMICS%20Parameter%20VECTORMV.md#p14330n-speed-controller-reference-model-natural-frequency))"; the natural frequency is the frequency of the system at which it can oscillate after one excitation. You must determine the natural frequency of your system or adapt it empirically.
- "Damping ([p1434](SINAMICS%20Parameter%20VECTORMV.md#p14340n-speed-controller-reference-model-damping))"; value for the damping in the PT2 element

The reference model can also be emulated externally and its output signal injected via [p1437](SINAMICS%20Parameter%20VECTORMV.md#p14370n-ci-speed-controller-reference-model-i-component-input).

###### Function diagrams (FD)

Vector control - pre-control balancing reference/acceleration model - 6031 -

Vector control - speed controller with/without encoder - 6040 -

###### Additional parameters

- p1435

---

#### U/f control

This section contains information on the following topics:

- [MV V/f control](#mv-vf-control)
- [MV V/f characteristic](#mv-vf-characteristic)

##### MV V/f control

###### Description

The simplest solution for a control procedure is the V/f characteristic. Whereby the stator voltage for the induction motor or synchronous motor is controlled proportionately to the stator frequency. This method has proved successful in a wide range of applications with low dynamic requirements, such as:

- Pumps and fans,
- Belt drives
- and other similar processes.

See also [MV V/f characteristic](#mv-vf-characteristic)

###### Signal sources

| Symbol | Meaning |
| --- | --- |
| ![Signal sources](images/148106142475_DV_resource.Stream@PNG-en-US.png) | [MV setpoint addition](#mv-setpoint-addition) |

###### Requirement

- A "V/f control ..." is set as control type in the basic parameter assignment of the drive axis (see [MV control type](#mv-control-type)).

###### Parameterizing V/f control

1. Select one of the entries for the "V/f control" from the "Control type" drop-down list ([p1300](SINAMICS%20Parameter%20VECTORMV.md#p13000n-open-loopclosed-loop-control-operating-mode)).
2. Enter a start value for the setpoint encoder at frequency zero in the "Setpoint encoder start value" ([p6890](SINAMICS%20Parameter%20VECTORMV.md#p68900n-setpoint-transmitter-starting-value)) field.
3. Interconnect the signal source for a variable additional start value of the setpoint encoder in the "Setpoint encoder start value signal source" ([p6896](SINAMICS%20Parameter%20VECTORMV.md#p68960n-ci-setpoint-transmitter-start-value-signal-source)) field.
4. Interconnect the signal sink for the total of the start value of the setpoint encoder in the "Setpoint encoder start value total" ([p6897](SINAMICS%20Parameter%20VECTORMV.md#r6897-co-setpoint-transmitter-starting-value-sum)) field.
5. Enter a value for the maximum possible amplitude of the setpoint output in the "Setpoint encoder maximum amplitude" ([p6891](SINAMICS%20Parameter%20VECTORMV.md#p68910n-setpoint-transmitter-maximum-amplitude)) field.
6. Enter a value for the rated motor voltage in the "Rated motor voltage" ([p0304](SINAMICS%20Parameter%20VECTORMV.md#p03040n-rated-motor-voltage)) field.
7. Enter a value for the scaling factor of the frequency in the "Setpoint encoder frequency scaling factor" ([p6892](SINAMICS%20Parameter%20VECTORMV.md#p68920n-setpoint-transmitter-frequency-scaling-factor)) field.

###### Signal processing

| Symbol | Meaning |
| --- | --- |
| ![Signal processing](images/148106171659_DV_resource.Stream@PNG-en-US.png) | [MV power unit](#mv-power-unit) |

###### Function diagrams (FD)

- Vector control - U/f and I/f setpoint generator - 6301 -

###### Additional parameters

- ---

##### MV V/f characteristic

###### Description

At low output frequencies, the V/f characteristics supply only a low output voltage. Along with the influence of the ohmic resistance at low frequencies, this can result in a too low output voltage. To counteract this, a voltage boost can be set to achieve the following:

- Implement the magnetization of the induction motor
- Maintain the load
- Compensate for the losses (ohmic losses in the winding resistors) in the system
- Generate a breakaway/acceleration/braking torque

###### V/f characteristic

| V/f control type | Application/property |  |
| --- | --- | --- |
| [0] V/f control with linear characteristic | Standard case (without voltage boost) | ![V/f characteristic](images/147860942475_DV_resource.Stream@PNG-en-US.png) |
| [2] V/f control with parabolic characteristic | Characteristic that takes into account the motor torque curve (e.g. fan/pump):  - Quadratic characteristic (f<sup>2</sup> characteristic) - Energy saving because the low voltage also results in low currents and losses | ![V/f characteristic](images/147860962699_DV_resource.Stream@PNG-en-US.png) |

###### Function diagrams (FD)

- Vector control - U/f and I/f setpoint generator - 6301 -

###### Additional parameters

---

#### Torque setpoints

This section contains information on the following topics:

- [MV torque setpoint](#mv-torque-setpoint)

##### MV torque setpoint

###### Description

You edit the torque setpoint by scaling or by applying an additional setpoint. The supplementary torque acts for the torque control as well as for the speed control.

This feature with the additional torque setpoint enables a precontrol torque to be implemented for speed control.

###### Signal source

| Symbol | Meaning |
| --- | --- |
| ![Signal source](images/148105700235_DV_resource.Stream@PNG-en-US.png) | [Speed setpoint filter](#mv-speed-setpoint-filter) |
| ![Signal source](images/148105865739_DV_resource.Stream@PNG-en-US.png) | [Speed controller](#mv-speed-controller) |

###### Switchover between speed/torque control

1. In the "Speed/torque-control" field ([p1501](SINAMICS%20Parameter%20VECTORMV.md#p15010n-bi-change-over-between-closed-loop-speedtorque-control)), interconnect the signal source for the switchover between speed control and torque control.

   - 0 signal: Speed control
   - 1 signal: Torque control
2. Depending on the set signal source, now make the settings for speed control or torque control.

###### Setting torque setpoints for speed control

1. Interconnect the signal source "Torque setpoint" ([p1503](SINAMICS%20Parameter%20VECTORMV.md#p15030n-ci-torque-setpoint))" for the torque setpoint of the torque control.
2. Specify the torque limiting (see "Specifying the torque limiting").
3. Set up to two additional torques (see "Setting additional torques").

###### Setting torque setpoints for torque control

1. Enter a smoothing constant of the acceleration torque in the "Smoothing" field ([p1517](SINAMICS%20Parameter%20VECTORMV.md#p15170n-accelerating-torque-smoothing-time-constant)).
2. Specify the torque limiting (see "Specifying the torque limiting").

###### Defining torque limiting

1. Click the "Torque limiting" button.

   The "Torque limiting speed controller" dialog opens.
2. Interconnect the signal source for scaling the upper torque limit to limit the speed controller output in the "Scaling upper torque limit" ([p1540](SINAMICS%20Parameter%20VECTORMV.md#p15400n-ci-torque-limit-speed-controller-upper-scaling)[0]) field.
3. Interconnect the scaling signal source for scaling the upper torque limit to limit the speed controller output without considering current and power limits in the "Scaling" ([p1552](SINAMICS%20Parameter%20VECTORMV.md#p15520n-ci-torque-limit-upper-scaling-without-offset)[0]) field.
4. Interconnect the scaling signal source of the lower torque limit to limit the speed controller output without considering current and power limits in the "Scaling" ([p1554](SINAMICS%20Parameter%20VECTORMV.md#p15540n-ci-torque-limit-lower-scaling-without-offset)[0]) field.
5. Interconnect the scaling signal source of the lower torque limit to limit the speed controller output in the "Scaling lower torque limit" ([p1541](SINAMICS%20Parameter%20VECTORMV.md#p15410n-ci-torque-limit-speed-controller-lower-scaling)[0]) field.
6. Interconnect the signal source to switch the torque limits between variable ([p1551](SINAMICS%20Parameter%20VECTORMV.md#p15510n-bi-torque-limit-variablefixed-signal-source)[0] = 1) and fixed torque limit (p1551[0] = 0) in the "Variable torque limit" (p1551[0]) field.
7. Once you have made all the necessary settings, click the "Close" button.

   The dialog closes.

###### Setting supplementary torques

For an activated speed control, you can set up to two additional torques.

1. Interconnect the signal source of supplementary torque 1 in the "Supplementary torque 1" ([p1511](SINAMICS%20Parameter%20VECTORMV.md#p15110n-ci-supplementary-torque-1)) field.
2. Interconnect the signal source of the scaling factor of supplementary torque 1 in the "Scaling" ([p1512](SINAMICS%20Parameter%20VECTORMV.md#p15120n-ci-supplementary-torque-1-scaling)) field.
3. Interconnect the signal source of supplementary torque 2 in the "Supplementary torque 2" ([p1513](SINAMICS%20Parameter%20VECTORMV.md#p15130n-ci-supplementary-torque-2)) field.
4. Enter the scaling of supplementary torque 2 in the "Supplementary torque 2 scaling" field ([p1514](SINAMICS%20Parameter%20VECTORMV.md#p15140n-supplementary-torque-2-scaling)).

###### Signal processing

| Symbol | Meaning |
| --- | --- |
| ![Signal processing](images/148106233867_DV_resource.Stream@PNG-en-US.png) | [Torque limiting](#mv-torque-limiting) |

###### Function diagrams (FD)

Vector control - torque setpoint - 6060 -

###### Additional parameters

- [p0115](SINAMICS%20Parameter%20VECTORMV.md#p011506-sampling-times-for-internal-control-loops)
- [r1480](SINAMICS%20Parameter%20VECTORMV.md#r1480-co-speed-controller-pi-torque-output)
- [r1508](SINAMICS%20Parameter%20VECTORMV.md#r1508-co-torque-setpoint-before-supplementary-torque)
- [r1516](SINAMICS%20Parameter%20VECTORMV.md#r1516-co-supplementary-torque-and-acceleration-torque)
- [r1515](SINAMICS%20Parameter%20VECTORMV.md#r1515-supplementary-torque-total)
- [r1518](SINAMICS%20Parameter%20VECTORMV.md#r151801-co-accelerating-torque)

---

#### Torque limitation

This section contains information on the following topics:

- [MV torque limiting](#mv-torque-limiting)

##### MV torque limiting

###### Description

A machine sets a counter-torque or load torque against the torque of the drive.

In order to avoid overloads of the machine particularly during acceleration and deceleration phases, the torque of the drive must be limited according to the connected machine.

The following limits can be set for the torque limiting:

- Upper torque limit

  Permits the upper torque value to be specified and, if necessary, be scaled.
- Current limit

  Permits the actual current limit to be viewed. Because the current limiting also limits the maximum torque that the motor can provide, if the torque limit is increased, more torque will only be available if a higher current can also flow. It may be necessary to also adapt the current limit.
- Power limit

  Permits the current motorized and regenerative power limit to be viewed. The value specifies the maximum permissible power, whereby different limits can be viewed for motorized and regenerative mode.
- Lower torque limit

  Permits the lower torque value to be specified and, if necessary, be scaled.

###### Signal source

| Symbol | Meaning |
| --- | --- |
| ![Signal source](images/148105810315_DV_resource.Stream@PNG-en-US.png) | [Torque setpoints](#mv-torque-setpoint) |

###### Configuring the torque limiting

1. Click the "Upper torque limit" button.

   A dialog with the same name opens.
2. Enter the fixed upper torque limit in the "Upper torque limit" ([p1520](SINAMICS%20Parameter%20VECTORMV.md#p15200n-co-torque-limit-uppermotoring)[0]) field.
3. Interconnect the signal source for the upper torque limit in the Feld "Variable upper torque limit" ([p1522](SINAMICS%20Parameter%20VECTORMV.md#p15220n-ci-torque-limit-uppermotoring)[0]) field.
4. Correct the scaling for the upper torque limit in the "Scaling" ([p1524](SINAMICS%20Parameter%20VECTORMV.md#p15240n-co-torque-limit-uppermotoring-scaling)[0]) field.
5. Interconnect the scaling signal source of the upper torque limit with p1524[0] in the field [p1528](SINAMICS%20Parameter%20VECTORMV.md#p15280n-ci-torque-limit-upper-scaling).
6. Interconnect the signal source to switch the torque limits between variable ([p1551](SINAMICS%20Parameter%20VECTORMV.md#p15510n-bi-torque-limit-variablefixed-signal-source)[0] = 1) and fixed torque limit (p1551[0] = 0) in the "Variable torque limit" (p1551[0]) field.

   If you select the setting "Fixed torque limit", the value "Upper torque limit" (p1520[0]) is used. For a "variable torque limit", the minimum of "Upper torque limit" (p1520[0]) and the scaled "Variable upper torque limit" (p1528[0]) is used.
7. Enter a value for the fixed lower torque limit in the "Lower torque limit" ([p1521](SINAMICS%20Parameter%20VECTORMV.md#p15210n-co-torque-limit-lowerregenerative)[0]) field.
8. Once you have made all the necessary settings, click the "Close" button.

   The dialog closes.
9. Click the "Lower torque limit" button.

   A dialog with the same name opens.
10. Enter a value for the fixed lower torque limit in the "Lower torque limit" (p1521[0]) field.
11. Interconnect the signal source for the lower torque limit in the "Lower torque limit" ([p1523](SINAMICS%20Parameter%20VECTORMV.md#p15230n-ci-torque-limit-lowerregenerative)[0]) field.
12. Correct the specified scaling for the lower torque limit in the "Scaling" ([p1525](SINAMICS%20Parameter%20VECTORMV.md#p15250n-co-torque-limit-lowerregenerative-scaling)[0]) field.
13. Interconnect the scaling signal source of the lower or generator torque limit in p1523 in the field "[p1529](SINAMICS%20Parameter%20VECTORMV.md#p15290n-ci-torque-limit-lower-scaling)[0]".
14. Interconnect the signal source to switch the torque limits between variable (p1551[0] = 1) and fixed torque limit (p1551[0] = 0) in the "Variable torque limit" (p1551[0]) field.

    If you select the setting "Fixed torque limit", the value "Lower torque limit" (p1521[0]) is used. For a "variable torque limit", the maximum of "Lower torque limit" (p1521[0]) and the scaled "Variable lower torque limit" (p1529[0]) is used.
15. Once you have made all the necessary settings, click the "Close" button.

    The dialog closes.

###### Configuring the current limit

The current limit can be configured alternatively or in addition to the torque limiting. If only the current limit is configured (without the torque limit), the drive ramps up quickly. However, as only the ramp-function generator is stopped when the current limit is reached, the current can continue to rise. This must be taken into account during the parameter assignment (if required, through a safety clearance) so that the drive is not switched off with an overcurrent error.

1. Click the "Current limit" button.

   A dialog with the same name opens.
2. Enter the "Current limit" ([p0640](SINAMICS%20Parameter%20VECTORMV.md#p06400n-current-limit)[0]) here.
3. Once you have made all the necessary settings, click the "Close" button.

   The dialog closes.

###### Configuring the power limit

The power limit can be configured alternatively or in addition to the torque limiting.

1. Click the "Power limit" button.

   A dialog with the same name opens.
2. In the "Power limit motorized" field ([p1530](SINAMICS%20Parameter%20VECTORMV.md#p15300n-power-limit-motoring)[0]), enter the motorized power limit.
3. In the "Power limit scaling" field ([p1556](SINAMICS%20Parameter%20VECTORMV.md#p15560n-power-limit-scaling)[0]), enter the scaling of the signal source for the motorized and negative generator power limit.
4. In the "Power limit" field ([p1555](SINAMICS%20Parameter%20VECTORMV.md#p15550n-ci-power-limit)[0]), interconnect the signal source for the motorized and negative generator power limit.
5. In the "Power limit generator" field ([p1531](SINAMICS%20Parameter%20VECTORMV.md#p15310n-power-limit-regenerative)[0]), enter the generator power limit.
6. Once you have made all the necessary settings, click the "Close" button.

   The dialog closes.

###### Display of the set torque limiting

The set torque limiting is displayed via the following parameters:

- Torque limit reached ([r1407](SINAMICS%20Parameter%20VECTORMV.md#r1407027-cobo-status-word-speed-controller).7)
- Upper torque limit reached (r1407.8)
- Lower torque limit reached (1407.9)
- Speed limitation controller active (r1407.17)

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Uncontrolled movement of the drive as a result of incorrect parameter assignment**   Incorrect parameterization of the torque limits can result in uncontrolled movement of the drives if there is no counter-torque, and can cause death or serious injury to persons in the danger zone.  - Make sure that the parameter assignment is correct. |  |

###### Signal processing

| Symbol | Meaning |
| --- | --- |
| ![Signal processing](images/148106269451_DV_resource.Stream@PNG-en-US.png) | [Current setpoint filter](#mv-current-setpoint-filter) |

###### Function diagrams (FD)

Vector control - torque setpoint - 6060 -

Vector control - upper/lower torque limit - 6630 -

Vector control - current/power/torque limits - 6640 -

###### Additional parameters

- [r0079](SINAMICS%20Parameter%20VECTORMV.md#r0079-co-torque-setpoint)
- [p0115](SINAMICS%20Parameter%20VECTORMV.md#p011506-sampling-times-for-internal-control-loops)
- [r1526](SINAMICS%20Parameter%20VECTORMV.md#r1526-co-torque-limit-uppermotoring-without-offset)
- [r1527](SINAMICS%20Parameter%20VECTORMV.md#r1527-co-torque-limit-lowerregenerative-without-offset)
- [r1536](SINAMICS%20Parameter%20VECTORMV.md#r153601-torque-generating-current-maximum-limit)
- [r1537](SINAMICS%20Parameter%20VECTORMV.md#r153701-torque-generating-current-minimum-limit)
- [r1538](SINAMICS%20Parameter%20VECTORMV.md#r1538-co-upper-effective-torque-limit)
- [r1539](SINAMICS%20Parameter%20VECTORMV.md#r1539-co-lower-effective-torque-limit)
- [r1548](SINAMICS%20Parameter%20VECTORMV.md#r154801-co-stall-current-limit-torque-generating-maximum)

---

#### Current setpoint filter

This section contains information on the following topics:

- [MV current setpoint filter](#mv-current-setpoint-filter)
- [Application example: Setting the current setpoint filters (vector)](#application-example-setting-the-current-setpoint-filters-vector)

##### MV current setpoint filter

###### Description

The current setpoint filters are used to skip or weaken certain frequency ranges in order to suppress resonance effects. Bandstop filters and low-pass filters are available to suppress specific interference frequency ranges.

By default, up to two current setpoint filters and a supplementary torque can be set for a vector drive.

You can parameterize the two current setpoint filters 1 and 2 connected in series as follows:

- PT2 low pass (PT2: -40 dB/decade)
- General 2nd order filter

###### Signal source

| Symbol | Meaning |
| --- | --- |
| ![Signal source](images/148106233867_DV_resource.Stream@PNG-en-US.png) | [Torque limiting](#mv-torque-limiting) |

###### Set supplementary torque 3

1. Interconnect the signal source in the "Supplementary torque 3" field ([p1569](SINAMICS%20Parameter%20VECTORMV.md#p15690n-ci-supplementary-torque-3)[0]) for supplementary torque 3.

   The signal input is preferably used for injecting the friction characteristic. The compensation of the friction is also effective if the velocity controller output reaches its force limits, but the current limits have not yet been reached.

###### Activating and setting current setpoint filters

1. To activate current setpoint filter 1, activate the "Filter 1" ([p1656](SINAMICS%20Parameter%20VECTORMV.md#p16560n-current-setpointspeed-actual-value-filter-activation)[0].0) option.

   To activate further available current setpoint filters, activate further filter options in the same way.

   The screen form now displays a curve for all filters not activated previously rather than a straight line.
2. Click the button for filter 1.

   The "Current setpoint filter" dialog opens.
3. Select the required filter type for current setpoint filter 1 in the "Filter type" ([p1657](SINAMICS%20Parameter%20VECTORMV.md#p16570n-current-setpoint-filter-1-type)) drop-down list:

   - [1] PT2 low pass
   - [2] General 2nd order filter
4. Correct the following default values for current setpoint filter 1:

   - Numerator frequency
   - Numerator damping
   - Denominator frequency
   - Denominator damping
5. If you have activated further current setpoint filters, repeat steps 3 and 4 for these filters.
6. Once you have made all the necessary settings, click the "Close" button.

   The dialog closes.
7. Interconnect the signal source in the "Natural frequency tuning" ([p1655](SINAMICS%20Parameter%20VECTORMV.md#p165504-ci-current-setpointspeed-actual-value-filter-nat-frequency-tuning)[0]) field for the tuning of the natural frequency of current setpoint filter 1.

   If a 2nd current setpoint filter is configured, interconnect the signal source in the "Natural frequency tuning" (p1655[1]) field for tuning the natural frequency of current setpoint filter 2.

###### Signal processing

| Symbol | Meaning |
| --- | --- |
| ![Signal processing](images/148106318219_DV_resource.Stream@PNG-en-US.png) | [Current controller](#mv-current-controller) |

###### Function diagrams (FD)

Vector control - current setpoint filter - 6710 -

###### Additional parameters

- [r0079](SINAMICS%20Parameter%20VECTORMV.md#r0079-co-torque-setpoint)
- [p0115](SINAMICS%20Parameter%20VECTORMV.md#p011506-sampling-times-for-internal-control-loops)
- [r1536](SINAMICS%20Parameter%20VECTORMV.md#r153601-torque-generating-current-maximum-limit)
- [r1537](SINAMICS%20Parameter%20VECTORMV.md#r153701-torque-generating-current-minimum-limit)
- [p0108](SINAMICS%20Parameter%20SINAMICS%20MV.md#p01080n-drive-objects-function-module)
- [p1400](SINAMICS%20Parameter%20VECTORMV.md#p14000n-speed-control-configuration)
- [p1658](SINAMICS%20Parameter%20VECTORMV.md#p16580n-current-setpoint-filter-1-denominator-natural-frequency)
- [p1659](SINAMICS%20Parameter%20VECTORMV.md#p16590n-current-setpoint-filter-1-denominator-damping)
- [p1660](SINAMICS%20Parameter%20VECTORMV.md#p16600n-current-setpoint-filter-1-numerator-natural-frequency)
- [p1661](SINAMICS%20Parameter%20VECTORMV.md#p16610n-current-setpoint-filter-1-numerator-damping)
- [p1662](SINAMICS%20Parameter%20VECTORMV.md#p16620n-current-setpoint-filter-2-type)
- [p1663](SINAMICS%20Parameter%20VECTORMV.md#p16630n-current-setpoint-filter-2-denominator-natural-frequency)
- [p1664](SINAMICS%20Parameter%20VECTORMV.md#p16640n-current-setpoint-filter-2-denominator-damping)
- [p1665](SINAMICS%20Parameter%20VECTORMV.md#p16650n-current-setpoint-filter-2-numerator-natural-frequency)

---

##### Application example: Setting the current setpoint filters (vector)

You can parameterize the two current setpoint filters 1 and 2 connected in series as follows:

- 2nd order lowpass (PT2: -40 dB/decade)
- Bandstop
- Low-pass with reduction
- General 2nd order filter

Bandstop and lowpass with reduction are converted into the parameters of the general 2nd order filter using Startdrive. The phase frequency curve is shown alongside the amplitude-log frequency curve. A phase shift results in a control system delay and should be kept to a minimum.

###### Activating and parameterizing the current setpoint filters

1. Select the group parameter [p1656](SINAMICS%20Parameter%20VECTORMV.md#p16560n-current-setpointspeed-actual-value-filter-activation)[0].0 and open the substructure.
2. Select the first current setpoint filter (e.g. [p1656](SINAMICS%20Parameter%20VECTORMV.md#p16560n-current-setpointspeed-actual-value-filter-activation)[0].0) - and in the drop-down list of the parameter line, select setting "[1] Active".
3. If you also want to activate the second current setpoint filter, select it as well (e.g. p1656[0].1) and select the setting "[1] Active" in the drop-down list of the parameter line.
4. For each activated current setpoint filter, parameterize the following values in the parameter range [p1657](SINAMICS%20Parameter%20VECTORMV.md#p16570n-current-setpoint-filter-1-type) ... [p1666](SINAMICS%20Parameter%20VECTORMV.md#p16660n-current-setpoint-filter-2-numerator-damping):

   - Type
   - Denominator natural frequency
   - Denominator damping
   - Numerator damping

   As long as the parameter setting [p1699](SINAMICS%20Parameter%20VECTORMV.md#p1699-filter-data-acceptance) = 1 is active, the background calculation of the filter data is not performed, even when filter parameters are changed.
5. Make the setting p1699 = 0 to start calculating the filter data.
6. Then save the modified project settings.

###### Function diagrams (FD)

Vector control - current setpoint filter - 6710 -

###### Additional parameters

- [p0108](SINAMICS%20Parameter%20SINAMICS%20MV.md#p01080n-drive-objects-function-module)
- [p1400](SINAMICS%20Parameter%20VECTORMV.md#p14000n-speed-control-configuration)
- [p1658](SINAMICS%20Parameter%20VECTORMV.md#p16580n-current-setpoint-filter-1-denominator-natural-frequency)
- [p1659](SINAMICS%20Parameter%20VECTORMV.md#p16590n-current-setpoint-filter-1-denominator-damping)
- [p1660](SINAMICS%20Parameter%20VECTORMV.md#p16600n-current-setpoint-filter-1-numerator-natural-frequency)
- [p1661](SINAMICS%20Parameter%20VECTORMV.md#p16610n-current-setpoint-filter-1-numerator-damping)
- [p1662](SINAMICS%20Parameter%20VECTORMV.md#p16620n-current-setpoint-filter-2-type)
- [p1663](SINAMICS%20Parameter%20VECTORMV.md#p16630n-current-setpoint-filter-2-denominator-natural-frequency)
- [p1664](SINAMICS%20Parameter%20VECTORMV.md#p16640n-current-setpoint-filter-2-denominator-damping)
- [p1665](SINAMICS%20Parameter%20VECTORMV.md#p16650n-current-setpoint-filter-2-numerator-natural-frequency)

---

#### Current controller

This section contains information on the following topics:

- [MV current controller](#mv-current-controller)

##### MV current controller

###### Description

The current controller is generally only required for the first commissioning. No further settings are required in normal operation. The settings of the controller can be further optimized for special application cases.

The following settings can be made for the current controller:

- P gain
- Adaptation of the current controller
- Integral time

###### Signal source

| Symbol | Meaning |
| --- | --- |
| ![Signal source](images/148106269451_DV_resource.Stream@PNG-en-US.png) | [Current setpoint filter](#mv-current-setpoint-filter) |
| ![Signal source](images/148106387595_DV_resource.Stream@PNG-en-US.png) | [Power unit (torque-generating actual current value)](#mv-power-unit) |
| ![Signal source](images/148106387595_DV_resource.Stream@PNG-en-US.png) | [Power unit (field-generating actual current value)](#mv-power-unit) |

###### Setting P gain and integral time

1. Enter the desired value for the proportional gain of the lower adaptation current range in the "P gain" ([p1715](SINAMICS%20Parameter%20VECTORMV.md#p17150n-current-controller-p-gain)[0]) field.
2. Correct the specified value for the integral time of the current controller in the "Integral time" ([p1717](SINAMICS%20Parameter%20VECTORMV.md#p17170n-current-controller-integral-action-time)[0]) field.

###### Checking the current limit

If required, check the values determined for the current limit.

1. Click the "Current limit" button.

   A dialog with the same name opens. The following current limit values are displayed:

   - [r0067](SINAMICS%20Parameter%20VECTORMV.md#r0067-co-output-current-maximum) Maximum output current (output current of the power unit)
   - [r0331](SINAMICS%20Parameter%20VECTORMV.md#r03310n-actual-motor-magnetizing-current) Motor magnetizing current (normally display of the motor rated magnetizing current from [p0320](SINAMICS%20Parameter%20VECTORMV.md#p03200n-motor-rated-magnetizing-currentshort-circuit-current))
2. Click "Close" to close the dialog.

###### Setting the adaptation of the current controller

The P gain of the current controller can be reduced via an adaptation depending on the current. The adaptation function must be activated first for the configuration of the adaptation.

1. Select the "[1] Yes" option ([p1402](SINAMICS%20Parameter%20VECTORMV.md#p14020n-closed-loop-current-control-and-motor-model-configuration).2) in the drop-down list below the "Adaptation" button in the "Current controller" screen form.

   The "Adaptation" button now shows a curve and can be used.
2. Click the "Adaptation" button.

   A dialog with the same name opens.
3. Correct the factor for the P gain of the current controller in the adaptation range (current > [p0392](SINAMICS%20Parameter%20VECTORMV.md#p03920n-current-controller-adaptation-starting-point-kp-adapted)) in the "Scaling" ([p0393](SINAMICS%20Parameter%20VECTORMV.md#p03930n-current-controller-adaptation-p-gain-adaptation)) field.
4. Enter the application point of the current-dependent current controller adaptation at which the adapted current controller gain takes effect p1715 x p0393 in the "Application point Kp adapted" (p0392) field.
5. Enter the application point of the current-dependent current controller adaptation at which the current controller gain takes effect p1715 in the "Application point Kp" ([p0391](SINAMICS%20Parameter%20VECTORMV.md#p03910n-current-controller-adaptation-starting-point-kp)) field.
6. Once you have made all the necessary settings, click the "Close" button.

   The dialog closes.

###### Display parameters

The following information is displayed via display parameters:

- "Current setpoint torque-producing ([r0077](SINAMICS%20Parameter%20VECTORMV.md#r0077-co-current-setpoint-torque-generating))

  Display and connector output for the torque/force-generating current setpoint.
- "Field-generating current setpoint" ([r0075](SINAMICS%20Parameter%20VECTORMV.md#r0075-co-current-setpoint-field-generating))

  Display and connector output for the field-generating current setpoint (Id_setpoint).
- "Current setpoint torque-generating smoothed" ([r0030](SINAMICS%20Parameter%20VECTORMV.md#r0030-co-current-actual-value-torque-generating-smoothed))

  Displays the smoothed torque-generating actual current value.
- "Current setpoint field-generating smoothed" ([r0029](SINAMICS%20Parameter%20VECTORMV.md#r0029-co-current-actual-value-field-generating-smoothed))

  Displays the smoothed field-generating actual current value.

###### Signal processing

| Symbol | Meaning |
| --- | --- |
| ![Signal processing](images/148106387595_DV_resource.Stream@PNG-en-US.png) | [Power unit](#mv-power-unit) |
| ![Signal processing](images/148106387595_DV_resource.Stream@PNG-en-US.png) | [Power unit](#mv-power-unit) |

###### Function diagrams (FD)

FD-6714 (58)

###### Additional parameters

- [r0072](SINAMICS%20Parameter%20VECTORMV.md#r0072-co-output-voltage)
- [p0115](SINAMICS%20Parameter%20VECTORMV.md#p011506-sampling-times-for-internal-control-loops)

---

#### Power unit

This section contains information on the following topics:

- [MV power unit](#mv-power-unit)

##### MV power unit

###### Description

The operating values of the power unit are displayed in the "Power unit" screen form.

###### Signal source

| Symbol | Meaning |
| --- | --- |
| ![Signal source](images/148106318219_DV_resource.Stream@PNG-en-US.png) | [Current controller](#mv-current-controller) |
| ![Signal source](images/148106318219_DV_resource.Stream@PNG-en-US.png) | [Current controller](#mv-current-controller) |
| ![Signal source](images/147861394955_DV_resource.Stream@PNG-en-US.PNG) | [V/f control](#uf-control)   Only for activated V/f control |
| ![Signal source](images/147861394955_DV_resource.Stream@PNG-en-US.PNG) | [V/f control](#uf-control)   Only for activated V/f control |

###### Display parameters

The following information is displayed via display parameters:

- DC link voltage ([r0070](SINAMICS%20Parameter%20VECTORMV.md#r007002-co-actual-dc-link-voltage))

  Display and connector output for the measured actual value of the DC link voltage.
- Power unit overload l2t ([r0036](SINAMICS%20Parameter%20VECTORMV.md#r0036-co-power-unit-overload-i2t))

  Display of the overload of the power unit determined with the aid of the I2t calculation.
- Actual pulse frequency ([r1801](SINAMICS%20Parameter%20VECTORMV.md#r1801-co-actual-pulse-frequency))

  Display and connector output for the current converter switching frequency.
- Power unit temperatures, inverter maximum value ([r0037](SINAMICS%20Parameter%20VECTORMV.md#r0037019-co-power-unit-temperatures))

  Display and connector output for temperatures in the power unit.
- Output frequency smoothed ([r0024](SINAMICS%20Parameter%20VECTORMV.md#r0024-co-output-frequency-smoothed))

  Displays the smoothed output frequency.
- Actual phase current value, phase U ([r0069](SINAMICS%20Parameter%20VECTORMV.md#r006904-co-phase-current-actual-value))

  Display and connector output for the measured actual values of the phase currents as peak value.
- Absolute current ([r0027](SINAMICS%20Parameter%20VECTORMV.md#r0027-co-absolute-actual-current-smoothed))

  Displays the smoothed absolute actual current value.

###### Signal processing

| Symbol | Meaning |
| --- | --- |
| ![Signal processing](images/148106391819_DV_resource.Stream@PNG-en-US.png) | [Motor](#mv-motor) |
| ![Signal processing](images/148106318219_DV_resource.Stream@PNG-en-US.png) | [Current controller](#mv-current-controller) |
| ![Signal processing](images/148106318219_DV_resource.Stream@PNG-en-US.png) | [Current controller](#mv-current-controller) |

###### Function diagrams (FD)

###### Additional parameters

- [r0029](SINAMICS%20Parameter%20VECTORMV.md#r0029-co-current-actual-value-field-generating-smoothed)
- [r0030](SINAMICS%20Parameter%20VECTORMV.md#r0030-co-current-actual-value-torque-generating-smoothed)
- r0069
- [r0072](SINAMICS%20Parameter%20VECTORMV.md#r0072-co-output-voltage)
- [r0073](SINAMICS%20Parameter%20VECTORMV.md#r0073-maximum-modulation-depth)
- [r0074](SINAMICS%20Parameter%20VECTORMV.md#r0074-co-modulat_depth)

---

#### Motor

This section contains information on the following topics:

- [MV motor](#mv-motor)

##### MV motor

###### Signal source

| Symbol | Meaning |
| --- | --- |
| ![Signal source](images/148106387595_DV_resource.Stream@PNG-en-US.png) | [Power unit](#mv-power-unit) |

###### Displaying the motor data

The parameters of the motor are clearly displayed here:

- Output voltage smoothed ([r0025](SINAMICS%20Parameter%20VECTORMV.md#r0025-co-output-voltage-smoothed))
- Absolute current value smoothed ([r0027](SINAMICS%20Parameter%20VECTORMV.md#r0027-co-absolute-actual-current-smoothed))
- Actual torque value smoothed ([r0031](SINAMICS%20Parameter%20VECTORMV.md#r0031-co-actual-torque-smoothed))
- Actual active power value smoothed ([r0032](SINAMICS%20Parameter%20VECTORMV.md#r0032-co-active-power-actual-value-smoothed))
- Actual speed value smoothed ([r0021](SINAMICS%20Parameter%20VECTORMV.md#r0021-co-actual-speed-smoothed))
- Speed setpoint smoothed ([r0020](SINAMICS%20Parameter%20VECTORMV.md#r0020-co-speed-setpoint-smoothed))
- Output frequency ([r0024](SINAMICS%20Parameter%20VECTORMV.md#r0024-co-output-frequency-smoothed))
- Motor temperature ([r0035](SINAMICS%20Parameter%20VECTORMV.md#r003501-co-motor-temperature))

The current data is displayed in online mode.

###### Additional parameters

---

#### Motor encoder

This section contains information on the following topics:

- [MV motor encoder](#mv-motor-encoder)

##### MV motor encoder

###### Description

For operation with motor encoder, you can define the actual speed value acquisition and the smoothing of the actual speed value.

For encoderless operation, you can alternatively parameterize just the smoothing of the motor model speed.

###### Signal source

| Symbol | Meaning |
| --- | --- |
| ![Signal source](images/148106508939_DV_resource.Stream@PNG-en-US.png) | [Motor](#mv-motor) |

###### Parameterizing the actual speed value acquisition of the motor encoder

1. If you want to smooth fluctuation peaks in the actual speed value, enter a smoothing time constant in the "Smoothing" ([p1441](SINAMICS%20Parameter%20VECTORMV.md#p14410n-actual-speed-smoothing-time)) field.

   If required, you can use a trace to check whether the controller with the smoothing is still sufficiently dynamic.
2. To activate the actual speed value filter, activate the "Filter 5" ([p1656](SINAMICS%20Parameter%20VECTORMV.md#p16560n-current-setpointspeed-actual-value-filter-activation)[0].4) option.

   This filter can now be parameterized. You will find a description of the filters at "[Filters](Configuring%20SINAMICS%20S-G-MV%20drives.md#filters)".
3. Click the button below the "Filter 5" option.

   The "Actual speed value filter" dialog opens.
4. In the "Actual speed value filter 5 type" ([p1677](SINAMICS%20Parameter%20VECTORMV.md#p16770n-speed-actual-value-filter-5-type)) drop-down list, select one of the following filter types for the actual speed value filter.

   - PT2 low pass
   - General 2nd order filter
5. Parameterize the following detailed values:

   - Numerator frequency ([p1680](SINAMICS%20Parameter%20VECTORMV.md#p16800n-speed-actual-value-filter-5-numerator-natural-frequency))
   - Numerator damping ([p1681](SINAMICS%20Parameter%20VECTORMV.md#p16810n-speed-actual-value-filter-5-numerator-damping))
   - Denominator frequency ([p1678](SINAMICS%20Parameter%20VECTORMV.md#p16780n-speed-actual-value-filter-5-denominator-natural-frequency))
   - Denominator damping ([p1679](SINAMICS%20Parameter%20VECTORMV.md#p16790n-speed-actual-value-filter-5-denominator-damping))
6. Once you have made all the necessary settings, click the "Close" button.

   The dialog closes.
7. Interconnect the signal source in the "Natural frequency tuning" ([p1655](SINAMICS%20Parameter%20VECTORMV.md#p165504-ci-current-setpointspeed-actual-value-filter-nat-frequency-tuning)[4]) field for the tuning of the natural frequency of actual current filter 5.

###### Encoderless operation: Setting smoothing for encoderless operation

For encoderless operation, you can also define a smoothing time constant.

1. Enter a smoothing time constant in the "Smoothing" field ([p1451](SINAMICS%20Parameter%20VECTORMV.md#p14510n-voltage-model-speed-actual-value-smoothing-time)).

###### Signal processing

| Symbol | Meaning |
| --- | --- |
| ![Signal processing](images/148105865739_DV_resource.Stream@PNG-en-US.png) | [Speed controller](#mv-speed-controller) |

###### Additional parameters

- [r0061](SINAMICS%20Parameter%20VECTORMV.md#r006102-co-actual-speed-unsmoothed)
- [r0063](SINAMICS%20Parameter%20VECTORMV.md#r006302-co-speed-actual-value)
- [p0115](SINAMICS%20Parameter%20VECTORMV.md#p011506-sampling-times-for-internal-control-loops)

---

### Drive functions

This section contains information on the following topics:

- [Faults](#faults)
- [Vdc_min/max controller](#vdc_minmax-controller)
- [Flying restart](#flying-restart)
- [Messages/monitoring](#messagesmonitoring)
- [Friction characteristic](#friction-characteristic)

#### Faults

##### General information

If a fault occurs, the drive indicates the corresponding fault and/or alarm.

The following options for displaying faults and alarms are available:

- Display via the fault and alarm buffer for PROFINET.
- Display online via the commissioning software.
- Display and operating unit (e.g. BOP, AOP).

##### Differences between faults and alarms

The differences between faults and alarms are as follows:

| Type | Description |
| --- | --- |
| Faults | - What happens when a fault occurs?    - The appropriate fault response is initiated.   - Status signal ZSW1.3 is set.   - The fault is entered in the fault buffer. - How are faults corrected?    - Eliminate the cause of the fault.   - Acknowledge the fault. |
| Alarms | - What happens when an alarm occurs?    - Status signal ZSW1.7 is set.   - The alarm is entered in the alarm buffer. - How are alarms corrected?    - Alarms acknowledge themselves.      When the cause is no longer present, they automatically reset themselves. |

##### Fault responses

The following table contains the fault responses and their meanings for the entire SINAMICS drive family.

| Fault response | PROFIdrive | Response | Description |
| --- | --- | --- | --- |
| NONE | - | None | No response when a fault occurs.   When the "Basic positioner" function module is activated (r0108.4 = 1), the following applies: When a fault occurs with fault response "NONE", an active motion command is aborted and the system switches to follow-up mode until the fault has been rectified and acknowledged. |
| OFF1 | ON/OFF | Brake along the ramp-function generator deceleration ramp followed by pulse disable | - Speed control (p1300 = 20, 21)    - The immediate specification of n_set = 0 at the ramp generator deceleration ramp (p1121) causes the drive to be braked.   - When standstill is detected, the motor holding brake (if parameterized) is closed (p1215). The pulses are suppressed when the closing time (p1217) expires.      Standstill is detected when the actual speed value falls below the speed threshold (p1226) or when the monitoring time (p1227) started when speed setpoint ≤ speed threshold (p1226) has expired. - Torque control (p1300 = 23)   - The following applies for torque control: Response as for OFF2.   - When switching to torque control via p1501, the following applies:      There is no separate braking response.      If the actual speed value falls below the speed threshold (p1226) or the timer (p1227) has expired, the motor holding brake (if available) is closed. The pulses are suppressed when the closing time (p1217) expires. |
| OFF1_DELAYED | - | As for OFF1, but delayed | Faults with this fault response only take effect after the delay time in p3136 has expired. The remaining time until OFF1 is displayed in r3137. |
| OFF2 | COAST STOP | Internal/external pulse disable | Speed control and torque control   - Immediate pulse suppression, the drive "coasts" to a standstill. - The motor holding brake (if available) is closed immediately. - The "switching on disabled" is activated. |
| OFF3 | QUICK STOP | Brake along the OFF3 deceleration ramp followed by pulse disable | - Speed control (p1300 = 20, 21)    - The drive is braked along the OFF3 deceleration ramp (p1135) by immediately entering n_set = 0.   - When standstill is detected, the motor holding brake (if parameterized) is closed. The pulses are suppressed when the closing time of the holding brake (p1217) expires.      Standstill is detected when the actual speed value falls below the speed threshold (p1226) or when the monitoring time (p1227) started when speed setpoint <= speed threshold (p1226) has expired.   - The "switching on disabled" is activated. - Torque control (p1300 = 23)    - Switchover to speed-controlled operation and other responses as described for speed-controlled operation. |
| STOP2 | - | n_set = 0 | - The drive is braked along the OFF3 deceleration ramp (p1135) by immediately entering n_set = 0. - The drive remains in speed control. |
| IASC/DCBRK | - | - | - For synchronous motors, the following applies:    - If a fault occurs with this fault response, an internal armature short-circuit is triggered.   - The conditions for p1231 = 4 must be observed. - For induction motors, the following applies:    - If a fault occurs with this fault response, DC braking is triggered.   - DC braking must have been commissioned (p1232, p1233, p1234). |
| ENCODER | - | Internal/external pulse disable (p0491) | The ENCODER fault response is applied depending on the setting in p0491.   - Factory setting: p0491 = 0 → encoder error results in OFF2     **Notice**    When changing p0491, it is imperative that the information in the description of this parameter is observed. |

##### Acknowledging faults

For each fault, there is a description of how to acknowledge the fault after the cause has been eliminated.

| Acknowledgment | Description |
| --- | --- |
| POWER ON | The fault is acknowledged via a POWER ON (switch drive unit off and on again).    **Note**    If the fault cause has not been eliminated, the fault is displayed again immediately after ramp-up. |
| IMMEDIATELY | Faults can be acknowledged on a single drive object (steps 1 to 3) or on all drive objects (step 4) as follows:   1. Acknowledging via parameter:     p3981 = 0 → 1 2. Acknowledging via binector inputs:     P2103 BI: 1. Acknowledge faults    p2104 BI: 2. Acknowledge faults     p2105 BI: 3. Acknowledge faults 3. Acknowledging via PROFIBUS control signal:     STW1.7 = 0 → 1 (edge) 4. Acknowledging all faults     p2102 BI: Acknowledging all faults     All of the faults on all of the drive objects of the drive system can be acknowledged via this binector input.    **Note**   - These faults can also be acknowledged by a POWER ON. - If the fault cause has not been eliminated, the fault is deleted after the acknowledgment. - Safety Integrated faults    The "Safe Torque Off" (STO) function must be deselected before these faults are acknowledged. |
| PULSE DISABLE | The fault can only be acknowledged with a pulse disable (r0899.11 = 0).   The same options are available for acknowledging as described under acknowledge IMMEDIATELY. |

#### Vdc_min/max controller

This section contains information on the following topics:

- [Overview](#overview-2)
- [MV Vdc_min/max control](#mv-vdc_minmax-control)

##### Overview

The "Vdc control" function can be activated using the appropriate measures if an overvoltage or undervoltage is present in the DC link.

| Deviation | Typical cause | Remedy |
| --- | --- | --- |
| Overvoltage | The drive is operating in regenerative mode and is supplying too much energy to the DC link. | Reduce the regenerative torque to maintain the DC-link voltage within permissible limits. With the Vdc controller activated, the converter automatically partly extends the ramp-down time of a drive if the shutdown supplies too much energy to the DC link. |
| Undervoltage | Failure of the line voltage or supply for the DC link. | Specify a regenerative torque for the rotating drive to compensate the existing losses, thereby stabilizing the voltage in the DC link. This process is called "kinetic buffering". |

###### Properties

| Control mode | Properties |
| --- | --- |
| Vdc | - This comprises Vdc_max control and Vdc_min control (kinetic buffering), which are independent of each other. - Joint PI controller. The dynamic factor is used to set Vdc_min and Vdc_max control independently of each other. |
| Vdc_max | - This function can be used to control momentary regenerative load without shutdown using "overvoltage in the DC link". - Vdc_max control is only recommended for a supply without active closed-loop control for the DC link and without feedback. |
| Vdc_min  (kinetic buffering) | - With this function, the kinetic energy of the motor is used for buffering the DC-link voltage in the event of a momentary power failure, thereby delaying the drive. |

###### Vdc_min control

![Switching Vdc_min control on/off (kinetic buffering)](images/148106574219_DV_resource.Stream@PNG-en-US.png)

Switching V<sub>dc_min</sub> control on/off (kinetic buffering)

In the event of a power failure, Vdc_min control is activated when the Vdc_min switch-on level is undershot. This controls the DC-link voltage and maintains it at a constant level. The motor speed is reduced.

When the power supply is restored, the DC-link voltage increases again and Vdc_min control is deactivated again at 5% above the Vdc_min switch-on level. The motor continues operating normally.

If the power supply is not re-established, the motor speed continues to drop. When the threshold in p1257 is reached, this results in a response in accordance with p1256.

Once the time threshold (p1255) has elapsed without the line voltage being re-established, a fault is triggered (F07406), which can be parameterized as required (factory setting: OFF3).

The Vdc_min controller can be activated for a drive. Other drives can participate in supporting the DC link, by transferring to them a scaling of their speed setpoint from the controlling drive via BICO interconnection.

> **Note**
>
> If it is expected that the line supply will return, you must make sure that the drive lineup is not disconnected from the power supply. It could become disconnected, for example, if the line contactor drops out. The line contactor must be supplied, e.g. from an uninterruptible power supply (UPS).

###### Vdc_max control

![Switching Vdc_max control on/off](images/148106585483_DV_resource.Stream@PNG-en-US.png)

Switching Vdc_max control on/off

The switch-on level for Vdc_max control (r1242) is calculated as follows:

- When the function for automatically detecting the switch-on level is switched off (p1254 = 0)  
  r1242 = 1.15 • p0210 (device connection voltage, DC link)
- When the function for automatically detecting the switch-on level is switched on (p1254 = 1)  
  r1242 = Vdc_max - 50 V (Vdc_max: Overvoltage threshold of the Motor Module)

##### MV Vdc_min/max control

###### Making basic settings

1. Select the desired control type in the "Vdc controller or Vdc monitoring configuration (V/f)" (p1280) drop-down list.

   Depending on the control type that is selected, the schematic display and the necessary detailed settings change.
2. Make the detailed settings of the selected control type (see below)
3. Save the project settings.

###### Detailed settings "Disable Vdc controller"

No settings are possible for the disabled Vdc controller.

###### Detailed settings "Enable Vdc_max controller"

1. Click the "Switch-on level Vdc_max" button.

   The "Switch-on level Vdc_max" dialog opens.
2. Select whether the automatic acquisition is enabled or disabled in the "Automatic acquisition ON signal level" (p1254) drop-down list.
3. If required, correct the default value in the "Device supply voltage" ([p0210](SINAMICS%20Parameter%20VECTORMV.md#p0210-drive-unit-line-supply-voltage)) field.

   The device supply voltage can only be parameterized with disabled automatic acquisition.
4. Once you have made all the necessary settings, click the "Close" button.

   The dialog closes.
5. Click the "Vdc_max controller" button.

   The "Vdc_min/max controller" dialog opens.
6. If required, correct the default values in the following fields:

   - Proportional gain ([p1250](SINAMICS%20Parameter%20VECTORMV.md#p12500n-vdc-controller-proportional-gain)[0])
   - Integral time ([p1251](SINAMICS%20Parameter%20VECTORMV.md#p12510n-vdc-controller-integral-time)[0])
   - Derivative-action time ([p1252](SINAMICS%20Parameter%20VECTORMV.md#p12520n-vdc-controller-rate-time)[0])
7. Once you have made all the necessary settings, click the "Close" button.

   The dialog closes.
8. Enter the dynamic factor as percentage in the input field ([p1243](SINAMICS%20Parameter%20VECTORMV.md#p12430n-vdc_max-controller-dynamic-factor)) below the "Vdc_max controller" button.

###### Detailed settings "Enable Vdc_min controller (kinetic buffering)"

1. Click the "Switch-on level Vdc_min" button.

   The "Switch-on level Vdc_min" dialog opens.
2. Select how the Vdc_min controller should respond in the "Vdc_min controller response (kinetic buffering)" ([p1256](SINAMICS%20Parameter%20VECTORMV.md#p12560n-vdc_min-controller-response-kinetic-buffering)) drop-down list.
3. If required, correct the default values in the following fields:

   - Switch-on level ([p1245](SINAMICS%20Parameter%20VECTORMV.md#p12450n-vdc_min-controller-switch-in-level-kinetic-buffering))
   - Speed threshold ([p1257](SINAMICS%20Parameter%20VECTORMV.md#p12570n-vdc_min-controller-speed-threshold))
   - Time threshold ([p1255](SINAMICS%20Parameter%20VECTORMV.md#p12550n-vdc_min-controller-time-threshold))

     Can only be parameterized for Vdc_min controller response [1].
4. Once you have made all the necessary settings, click the "Close" button.

   The dialog closes.
5. Click the "Vdc_min controller" button.

   The "Vdc_min/max controller" dialog opens.
6. If required, correct the default values in the following fields:

   - Proportional gain (p1250)
   - Integral time (p1251)
   - Derivative-action time (p1252)
7. Once you have made all the necessary settings, click the "Close" button.

   The dialog closes.
8. Enter the dynamic factor as percentage in the input field ([p1247](SINAMICS%20Parameter%20VECTORMV.md#p12470n-vdc_min-controller-dynamic-factor-kinetic-buffering)) below the "Vdc_min controller" button.
9. Enter an output limitation value for the Vdc_min controller in the input field (p1293).

###### Detailed settings "Enable the Vdc_min controller and Vdc_max controller"

1. Click the "Switch-on level Vdc_max" button.

   The "Switch-on level Vdc_max" dialog opens.
2. Select whether the automatic acquisition is enabled or disabled in the "Automatic acquisition ON signal level" (p1254) drop-down list.
3. If required, correct the default value in the "Device supply voltage" (p0210) field.

   The device supply voltage can only be parameterized with disabled automatic acquisition.
4. Once you have made all the necessary settings, click the "Close" button.

   The dialog closes.
5. Click the "Vdc_max controller" button.

   The "Vdc_min/max controller" dialog opens.
6. If required, correct the default values in the following fields:

   - Proportional gain (p1250)
   - Integral time (p1251)
   - Derivative-action time (p1252)
7. Once you have made all the necessary settings, click the "Close" button.

   The dialog closes.
8. Enter the dynamic factor as percentage in the input field (p1243) below the "Vdc_max controller" button.
9. Click the lower "Switch-on level Vdc_min" button.

   The "Switch-on level Vdc_min" dialog opens.
10. Select how the Vdc_min controller should respond in the "Vdc_min controller response (kinetic buffering)" (p1256) drop-down list.
11. If required, correct the default values in the following fields:

    - Switch-on level (p1245)
    - Speed threshold (p1257)
    - Time threshold (p1255)

      Can only be parameterized for Vdc_min controller response [1].
12. Once you have made all the necessary settings, click the "Close" button.

    The "Switch-on level" dialog closes.
13. Click the "Vdc_min controller" button.

    The "Vdc_min/max controller" dialog opens.
14. If required, correct the default values in the following fields:

    - Proportional gain (p1250)
    - Integral time (p1251)
    - Derivative-action time (p1252)
15. Once you have made all the necessary settings, click the "Close" button.

    The dialog closes.
16. Enter the output limitation of the Vdc_max controller in Hz in the input field (p1247).

###### Detailed settings "Activate Vdc_max monitoring"

1. Click the "Switch-on level Vdc_max" button.

   The "Switch-on level Vdc_max" dialog opens.
2. Select whether the automatic acquisition is enabled or disabled in the "Automatic acquisition ON signal level" (p1254) drop-down list.
3. If required, correct the default value in the "Device supply voltage" (p0210) field.

   The device supply voltage can only be parameterized with disabled automatic acquisition.
4. Once you have made all the necessary settings, click the "Close" button.

   The dialog closes.

###### Detailed settings "Activate Vdc_min monitoring"

1. Click the "Switch-on level Vdc_min" button.

   The "Switch-on level Vdc_min" dialog opens.
2. Select how the Vdc_min controller should respond in the "Vdc_min controller response (kinetic buffering)" (p1256) drop-down list.
3. If required, correct the default values in the following fields:

   - Switch-on level (p1245)
   - Speed threshold (p1257)
   - Time threshold (p1255)

     Can only be parameterized for Vdc_min controller response [1].
4. Once you have made all the necessary settings, click the "Close" button.

   The dialog closes.

###### Detailed settings "Activate Vdc_min monitoring and Vdc_max monitoring"

1. Click the "Switch-on level Vdc_max" button.

   The "Switch-on level Vdc_max" dialog opens.
2. Select whether the automatic acquisition is enabled or disabled in the "Automatic acquisition ON signal level" (p1254) drop-down list.
3. If required, correct the default value in the "Device supply voltage" (p0210) field.

   The device supply voltage can only be parameterized with disabled automatic acquisition.
4. Once you have made all the necessary settings, click the "Close" button.

   The dialog closes.
5. Click the "Switch-on level Vdc_min" button.

   The "Switch-on level Vdc_min" dialog opens.
6. Select how the Vdc_min controller should respond in the "Vdc_min controller response (kinetic buffering)" (p1256) drop-down list.
7. If required, correct the default values in the following fields:

   - Switch-on level (p1245)
   - Speed threshold (p1257)
   - Time threshold (p1255)

     Can only be parameterized for Vdc_min controller response [1].
8. Once you have made all the necessary settings, click the "Close" button.

   The dialog closes.

###### Function diagrams (FD)

Vector control - Vdc_max controller and Vdc_min controller - 6220 -

###### Additional parameters

- [p1240](SINAMICS%20Parameter%20VECTORMV.md#p12400n-vdc-controller-or-vdc-monitoring-configuration)
- [r1242](SINAMICS%20Parameter%20VECTORMV.md#r1242-vdc_max-controller-switch-in-level)
- [r1246](SINAMICS%20Parameter%20VECTORMV.md#r1246-vdc_min-controller-switch-in-level-kinetic-buffering)
- [r1258](SINAMICS%20Parameter%20VECTORMV.md#r1258-co-vdc-controller-output)

---

#### Flying restart

This section contains information on the following topics:

- [MV flying restart](#mv-flying-restart)

##### MV flying restart

The "Flying restart" function allows a Motor Module to be switched on for a running motor. In this case, the Motor Module's output frequency is changed until the current motor speed/velocity has been found. The motor then ramps up with the setting for the ramp-function generator to the setpoint. The "Flying restart" function can be activated during operation with or without an encoder.

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Unplanned movement of the motor when flying restart is activated**  When the "Flying restart" ([p1200](SINAMICS%20Parameter%20VECTORMV.md#p12000n-flying-restart-operating-mode)) function is activated, the drive can still be accelerated by the search current despite the fact that it is at standstill and the setpoint is "0"; this can result in death, severe injury to persons in the danger zone or material damage.   - Ensure that nobody is present in the hazardous zone and that the mechanical system can move freely. |  |

###### Configuring flying restart

1. Select the desired mode of the flying restart in the "Flying restart mode" (p1200) drop-down list in the "Flying restart" screen form:

   - [0] Flying restart inactive
   - [1] Flying restart always active (start in setpoint direction)
   - [2] Flying restart always active (search for pulse enable)
2. Save the project settings.

**Result**

- With an induction motor, the system waits for a demagnetization time to elapse before the search is carried out. The demagnetization time can reduce the voltage at the motor terminals. At the pulse enable, this avoids high equalizing currents due to a phase short-circuit.

  The internal demagnetization time is calculated. In addition, you can define a de-excitation time via parameter [p0347](SINAMICS%20Parameter%20VECTORMV.md#p03470n-motor-de-excitation-time). The system waits for the longer of the two times to elapse. When operated with an encoder (actual speed value is sensed), the search phase is eliminated.
- For an induction or reluctance motor, immediately after the speed has been determined, magnetization starts ([p0346](SINAMICS%20Parameter%20VECTORMV.md#p03460n-motor-excitation-build-up-time)).

  The current speed setpoint in the ramp-function generator is then set to the current actual speed value.

  The ramp-up to the final speed setpoint starts with this value.

###### Application example

After a power failure, a fan drive can be quickly reconnected to the running fan motor by means of the "flying restart" function.

![Flying restart, example of induction motor without encoder](images/148106697739_DV_resource.Stream@PNG-en-US.png)

Flying restart, example of induction motor without encoder

![Flying restart, example of induction motor with encoder](images/148106709003_DV_resource.Stream@PNG-en-US.png)

Flying restart, example of induction motor with encoder

###### Additional parameters

- [p0352](SINAMICS%20Parameter%20VECTORMV.md#p03520n-cable-resistance)
- [p1082](SINAMICS%20Parameter%20VECTORMV.md#p10820n-maximum-speed)
- p1200

---

#### Messages/monitoring

This section contains information on the following topics:

- [MV actual speed value messages](#mv-actual-speed-value-messages)
- [MV speed messages](#mv-speed-messages)
- [MV setpoint / actual value messages](#mv-setpoint-actual-value-messages)
- [MV load torque monitoring](#mv-load-torque-monitoring)

##### MV actual speed value messages

###### Description

Comparators are provided for monitoring the actual speed and setpoint thresholds that activate monitoring functions (e.g. air flow monitor for fans, pressure switch for pumps) or initiate product steps for other plant sections (e.g. open gates for pumps and fans).

###### Configuring the monitoring of the actual speed and setpoint thresholds

1. Enter the time constant of the PT1 element for smoothing the actual speed/velocity value in the "Smoothing" ([p2153](SINAMICS%20Parameter%20VECTORMV.md#p21530n-speed-actual-value-filter-time-constant)) field.

   The smoothed actual speed/velocity is compared with the thresholds and is only used for messages.
2. Set the hysteresis speed (bandwidth) for the message "f or n comparison value reached or exceeded" (BO: [r2199](SINAMICS%20Parameter%20VECTORMV.md#r2199012-cobo-status-word-monitoring-3).1) at "Hysteresis speed 1" ([p2142](SINAMICS%20Parameter%20VECTORMV.md#p21420n-hysteresis-speed-1)).
3. Interconnect the "f or n comparison value reached or exceeded" (r2199) signal sink with the required parameters. Several interconnections are possible.

   Connect binector output:

   The "f or n comparison value reached/exceeded" signal is generated under consideration of hysteresis speed 1, speed threshold 1 and the ON delay.
4. Enter the speed threshold 1 in the "Speed threshold 1" ([p2141](SINAMICS%20Parameter%20VECTORMV.md#p21410n-speed-threshold-1)) field.
5. Enter the ON delay time for signal |n_act| > speed threshold in the "ON delay" ([p2156](SINAMICS%20Parameter%20VECTORMV.md#p21560n-on-delay-comparison-value-reached)) field.
6. Enter the bandwidths for the following messages in the "Hysteresis speed 2" ([p2140](SINAMICS%20Parameter%20VECTORMV.md#p21400n-hysteresis-speed-2)) field:

   - |n_act| < speed threshold 2
   - |n_set| > speed threshold 2
7. Interconnect the following signal sinks with the required parameters:

   - |n_act| ≤ speed threshold 2
   - |n_act| > speed threshold 2
8. Enter speed threshold 2 in the "Speed threshold 2" ([p2155](SINAMICS%20Parameter%20VECTORMV.md#p21550n-speed-threshold-2)) field.
9. Enter the bandwidths for the n_act > n_max message in the "Hysteresis speed n_act > n_max" ([p2162](SINAMICS%20Parameter%20VECTORMV.md#p21620n-hysteresis-speed-n_act-n_max)) field.
10. Interconnect the "n_act > n_max" ([r2197](SINAMICS%20Parameter%20VECTORMV.md#r2197113-cobo-status-word-monitoring-1)) signal sink with the required parameters. Several interconnections are possible.

    Connect binector output:

    Signal n_act > n_max is generated under consideration of hysteresis speed n_act > n_max.

    For a negative speed limit, the hysteresis is effective below the limit value and for a positive speed limit, above the limit value.

    Note:  
    The limits are set in the setpoint channel; see also [MV speed limitation](#mv-speed-limitation).

###### Function diagrams (FD)

- Signals and monitoring functions - speed signals - 8010 -
- Signals and monitoring functions - torque signals, motor blocked/stalled - 8012 -
- Setpoint channel - skip frequency bands and speed limits - 3050 -

###### Additional parameters

---

##### MV speed messages

###### Description

Comparators are provided for monitoring the speed thresholds used to activate monitoring functions (e.g. air flow monitor for fans, pressure switch for pumps) or initiate product steps for other plant sections (e.g. open gates for pumps and fans).

###### Configuring the monitoring of speed thresholds

1. Correct the specified bandwidths for the following messages in the "Hysteresis speed 3" ([p2150](SINAMICS%20Parameter%20VECTORMV.md#p21500n-hysteresis-speed-3)[0]) field:

   - n_act ≥ 0
   - |n_act| < speed setpoint 3
   - n_set < [p2161](SINAMICS%20Parameter%20VECTORMV.md#p21610n-speed-threshold-3)
   - n_set ≥ 0

   The calculation mode is defined using [p0340](SINAMICS%20Parameter%20VECTORMV.md#p03400n-automatic-calculation-motorcontrol-parameters).
2. Interconnect the "n_act ≥ 0" ([r2197](SINAMICS%20Parameter%20VECTORMV.md#r2197113-cobo-status-word-monitoring-1).3) signal sink with the required parameters. Several interconnections are possible.

   Signal n_act ≥ 0 is generated considering hysteresis speed 3.
3. Interconnect the "|n_act| < speed threshold 3" ([r2199](SINAMICS%20Parameter%20VECTORMV.md#r2199012-cobo-status-word-monitoring-3).0) signal sink with the required parameters. Several interconnections are possible.

   Signal |n_act| < speed threshold 3 is generated considering hysteresis speed 3 and speed threshold 3.
4. Correct the speed threshold 3 for |n_act| < speed setpoint 3 in the "Speed threshold 3" (p2161) field.
5. Interconnect the "Speed setpoint for messages" ([p2151](SINAMICS%20Parameter%20VECTORMV.md#p21510n-ci-speed-setpoint-for-messagessignals)) signal source for speed setpoint messages.
6. Interconnect the "Speed setpoint 2" ([p2154](SINAMICS%20Parameter%20VECTORMV.md#p21540n-ci-speed-setpoint-2)) signal source for velocity setpoint 2.

###### Function diagrams (FD)

- Signals and monitoring functions - speed signals - 8010 -
- Signals and monitoring functions - torque signals, motor blocked/stalled - 8012 -

###### Additional parameters

---

##### MV setpoint / actual value messages

###### Description

Comparators are provided for monitoring the actual speed and setpoint thresholds that activate monitoring functions (e.g. air flow monitor for fans, pressure switch for pumps) or initiate product steps for other plant sections (e.g. open gates for pumps and fans).

###### Configuring monitoring

1. Correct the specified bandwidth for the "Speed setp - act val deviation in tolerance t_off" message in the "Hysteresis speed 4" ([p2164](SINAMICS%20Parameter%20VECTORMV.md#p21640n-hysteresis-speed-4)) field.
2. Correct the specified speed threshold in the "Speed threshold 4" ([p2163](SINAMICS%20Parameter%20VECTORMV.md#p21630n-speed-threshold-4)) field.
3. Correct the OFF delay time for the "Speed setpoint - actual value deviation in tolerance t_off" message in the "OFF delay" ([p2166](SINAMICS%20Parameter%20VECTORMV.md#p21660n-off-delay-n_act-n_set)) field.
4. Interconnect the "Setpoint - actual value deviation in tolerance t_off" ([r2197](SINAMICS%20Parameter%20VECTORMV.md#r2197113-cobo-status-word-monitoring-1).7) signal sink for displaying the 1st monitoring status word.
5. Correct the ON delay time for the "Speed setpoint - actual value deviation in tolerance t_off" signal in the "ON delay" ([p2167](SINAMICS%20Parameter%20VECTORMV.md#p21670n-switch-on-delay-n_act-n_set)) field.
6. Interconnect the "Ramp-function generator active" ([p2148](SINAMICS%20Parameter%20VECTORMV.md#p21480n-bi-rfg-active)) signal source for the "RFG active" signal for the following messages:

   - Speed setp - act val deviation in tolerance t_on
   - Ramp-up/ramp-down completed
7. Interconnect the "Setpoint - actual value deviation in tolerance t_on" ([r2199](SINAMICS%20Parameter%20VECTORMV.md#r2199012-cobo-status-word-monitoring-3).4) signal sink for displaying the monitoring 3 status word.
8. Interconnect the "Ramp-up/ramp-down completed" (r2199.5) signal sink for displaying the monitoring 3 status word.

###### Function diagrams (FD)

- Signals and monitoring functions - speed signals - 8010 -
- Signals and monitoring functions - torque signals, motor blocked/stalled - 8012 -

###### Additional parameters

---

##### MV load torque monitoring

###### Description

This function monitors power transmission between the motor and the working machine. Typical applications include V-belts, flat belts, or chains that loop around the belt pulleys or cog wheels for drive and outgoing shafts and transfer the peripheral speeds and forces. Load monitoring can be used here to identify blocking of the driven machine and interruptions to the power transmission.

During load torque monitoring, the current speed/torque curve is compared with the programmed speed/torque curve ([p2182](SINAMICS%20Parameter%20VECTORMV.md#p21820n-load-monitoring-speed-threshold-value-1) to [p2190](SINAMICS%20Parameter%20VECTORMV.md#p21900n-load-monitoring-torque-threshold-3-lower)). If the actual value is outside the programmed tolerance bandwidth, a fault or alarm is triggered depending on parameter [p2181](SINAMICS%20Parameter%20VECTORMV.md#p21810n-load-monitoring-response). Faults or alarms can be delayed using parameter [p2192](SINAMICS%20Parameter%20VECTORMV.md#p21920n-load-monitoring-delay-time). to prevent false messages caused by brief transitional states.

The following responses of the load torque monitoring are possible:

- A07920 for torque/speed too low

  There is a negative difference of the torque to the torque/speed envelope curve (too low).

  - No response
- A07921 for torque/speed too high

  There is a positive difference of the torque to the torque/speed envelope curve (too high).

  - No response
- A07922 for torque/speed out of tolerance

  The torque deviates from the torque/speed envelope curve.

  - No response
- F07923 for torque/speed too low

  There is a negative difference of the torque to the torque/speed envelope curve (too low).

  - OFF1 (OFF2, OFF3, NONE) as response
- F07924 for torque/speed too high

  There is a positive difference of the torque to the torque/speed envelope curve (too high).

  - OFF1 (OFF2, OFF3, NONE) as response
- F07925 for torque/speed outside the tolerance

  The torque deviates from the torque/speed envelope curve.

  - OFF1 (OFF2, OFF3, NONE) as response

###### Configuring of load torque monitoring

1. In the "Load monitoring response" drop-down list (p2181[0]), select the desired response to the results of the load monitoring.

   The view of the screen form is adapted to the setting that was made.
2. If the load monitoring is only to be performed in the 1st quadrant, select the option "Yes" in the drop-down list of the same name ([p2149](SINAMICS%20Parameter%20VECTORMV.md#p21490n-monitoring-configuration)[0]).
3. If required, correct the desired delay time in the "Delay time" field (p2192).
4. Enter the desired values in the fields at the axes of the graphic:

   - Load monitoring speed threshold 1 (p2182)
   - Load monitoring speed threshold 2 ([p2183](SINAMICS%20Parameter%20VECTORMV.md#p21830n-load-monitoring-speed-threshold-value-2))
   - Load monitoring speed threshold 3 ([p2184](SINAMICS%20Parameter%20VECTORMV.md#p21840n-load-monitoring-speed-threshold-value-3))
   - Load monitoring torque threshold 3, upper ([p2189](SINAMICS%20Parameter%20VECTORMV.md#p21890n-load-monitoring-torque-threshold-3-upper))
   - Load monitoring torque threshold 3, lower (p2190)
   - Load monitoring torque threshold 2, upper ([p2187](SINAMICS%20Parameter%20VECTORMV.md#p21870n-load-monitoring-torque-threshold-2-upper))
   - Load monitoring torque threshold 2, lower ([p2188](SINAMICS%20Parameter%20VECTORMV.md#p21880n-load-monitoring-torque-threshold-2-lower))
   - Load monitoring torque threshold 1, upper ([p2185](SINAMICS%20Parameter%20VECTORMV.md#p21850n-load-monitoring-torque-threshold-1-upper))
   - Load monitoring torque threshold 1, lower ([p2186](SINAMICS%20Parameter%20VECTORMV.md#p21860n-load-monitoring-torque-threshold-1-lower))
5. Save the project settings.

###### Function diagrams (FD)

Signals and monitoring functions - load monitoring (r0108.17 = 1) - 8013 -

###### Additional parameters

---

---

**See also**

[MV function modules](#mv-function-modules)

#### Friction characteristic

This section contains information on the following topics:

- [MV friction characteristic](#mv-friction-characteristic)
- [MV friction characteristic recording](#mv-friction-characteristic-recording)

##### MV friction characteristic

###### Description

The friction characteristic is used to compensate the friction torque for the motor and the driven machine. A friction characteristic allows the speed controller to be precontrolled and improves the control response. Use 10 interpolation points for the friction characteristic. You define the coordinates of every interpolation point by a speed parameter ([p3820](SINAMICS%20Parameter%20VECTORMV.md#p38200n-friction-characteristic-value-n0) ... [p3829](SINAMICS%20Parameter%20VECTORMV.md#p38290n-friction-characteristic-value-n9)) and a torque parameter ([p3830](SINAMICS%20Parameter%20VECTORMV.md#p38300n-friction-characteristic-value-m0) ... [p3839](SINAMICS%20Parameter%20VECTORMV.md#p38390n-friction-characteristic-value-m9)). The default coordinates can be changed as required in the "Friction characteristic" screen form.

###### Requirements

- The "Speed/torque control" function module has been activated (see "[Function modules](#mv-function-modules)").
- The friction characteristic can be used only for non-activated V/f control.

###### Features of the friction characteristic

- 10 interpolation points are available for mapping the friction characteristic.
- An automatic function allows you to record the friction characteristic (record friction characteristic).
- A connector output ([r3841](SINAMICS%20Parameter%20VECTORMV.md#r3841-co-friction-characteristic-output)) can be interconnected as friction torque ([p1569](SINAMICS%20Parameter%20VECTORMV.md#p15690n-ci-supplementary-torque-3)).
- The friction characteristic can be activated and deactivated ([p3842](SINAMICS%20Parameter%20VECTORMV.md#p3842-friction-characteristic-activation)).
- Online mode is required for using the friction characteristic.

###### Activate friction characteristic

1. Select the option "[1] Friction characteristic activated" in the "Activation" drop-down list.

   The LED next to the drop-down list lights up green. The switchover switch is set to 1.
2. Correct the actual speed value signal of the friction characteristic via the "Actual speed value input" signal source ([p3848](SINAMICS%20Parameter%20VECTORMV.md#p38480n-ci-friction-characteristic-speed-actual-value-signal-source)) if required.
3. Interconnect the signal for the torque of the friction characteristic via the "Friction characteristic output" signal sink (r3841) depending on the speed or velocity.
4. Save the settings in the project.

   The friction characteristic is activated. It uses the specified coordinates of the 10 interpolation points. These coordinates can be configured together with the settings for recording the friction characteristic (see "[MV friction characteristic recording](#mv-friction-characteristic-recording)").

###### Function diagrams (FD)

Vector control - current setpoint filter - 6710 -

Vector control - current setpoint filter - 6710 -

Vector control - current setpoint filter - 6710 -

Technology functions - friction characteristic - 7010 -

###### Additional parameters

- [p3821](SINAMICS%20Parameter%20VECTORMV.md#p38210n-friction-characteristic-value-n1)
- [p3822](SINAMICS%20Parameter%20VECTORMV.md#p38220n-friction-characteristic-value-n2)
- [p3823](SINAMICS%20Parameter%20VECTORMV.md#p38230n-friction-characteristic-value-n3)
- [p3824](SINAMICS%20Parameter%20VECTORMV.md#p38240n-friction-characteristic-value-n4)
- [p3825](SINAMICS%20Parameter%20VECTORMV.md#p38250n-friction-characteristic-value-n5)
- [p3826](SINAMICS%20Parameter%20VECTORMV.md#p38260n-friction-characteristic-value-n6)
- [p3827](SINAMICS%20Parameter%20VECTORMV.md#p38270n-friction-characteristic-value-n7)
- [p3828](SINAMICS%20Parameter%20VECTORMV.md#p38280n-friction-characteristic-value-n8)
- p3829
- [r3840](SINAMICS%20Parameter%20VECTORMV.md#r384008-cobo-friction-characteristic-status-word).0...8
- p3842
- [p3845](SINAMICS%20Parameter%20VECTORMV.md#p3845-record-friction-characteristic-activation)
- [p3846](SINAMICS%20Parameter%20VECTORMV.md#p38460n-record-friction-characteristic-ramp-upramp-down-time)
- [p3847](SINAMICS%20Parameter%20VECTORMV.md#p38470n-record-friction-characteristic-time-to-warm-up)

---

##### MV friction characteristic recording

###### Description

You can make the following settings in the "Friction characteristic recording" screen form:

- Configuring the recording of the friction characteristic
- Configuring the coordinates of the interpolation points

When the friction characteristic is recorded, the drive can cause the motor to move. As a result, the motor may reach maximum speed.

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Unplanned motor motion while recording the friction characteristic**  Drive motion caused when recording the friction characteristic can result in death, severe injury or material damage.  - Ensure that nobody is present in the hazardous zone and that the mechanical system can move freely. |  |

###### Configuring the recording of the friction characteristic

For configuring, proceed as follows:

1. In the "Record the friction characteristic" screen form, select the desired automatic friction characteristic recording in the "Record activation" drop-down list (p3845). The following options are available:

   - [0] Record friction characteristic deactivated
   - [1] Record friction characteristic activated all directions

     The friction characteristic is recorded in both directions of rotation. The results of the positive and negative measurement are averaged and entered in p3830 ... p3839.
   - [2] Record friction characteristic activated positive direction
   - [3] Record friction characteristic activated negative direction
2. Enter the warm-up time until the maximum speed is to be reached in the "Recording warm-up time" field (p3847).

   After the end of the warm-up period, measurement is started.
3. Enter the ramp-up/ramp-down time of the ramp-up/ramp-down generator for automatic recording of the friction characteristic in the "Recording ramp-up/ramp-down time" field (p3846).
4. Save the configuration in the project.

   After the next switch-on command, the friction characteristic will be automatically recorded.

###### Configuring the coordinates of the interpolation points of the friction characteristic

For the friction characteristic, you can configure the coordinates for all 10 interpolation points.

1. In the "Speed" fields, configure the specified speed (p3820[0] ... p3829[0]) for each interpolation point.
2. In the "Torque" fields, configure the specified torque (p3830[0] ... p3839[0]) for each interpolation point.
3. Save the configuration in the project.

### Technology functions

This section contains information on the following topics:

- [Technology controller](#technology-controller)
- [Bypass operation](#bypass-operation)
- [Technology Extensions](#technology-extensions)

#### Technology controller

This section contains information on the following topics:

- [Overview](#overview-3)
- [Technology motorized potentiometer](#technology-motorized-potentiometer)
- [Technology fixed setpoints](#technology-fixed-setpoints)
- [Technology setpoints / actual values](#technology-setpoints-actual-values)
- [Technology PID controller](#technology-pid-controller)

##### Overview

###### Description

Simple closed-loop control functions can be implemented with the technology controller, e.g.:

- Level control
- Temperature control
- Dancer roll position control
- Pressure control
- Flow control
- Simple closed-loop controls without higher-level controller
- Tension control

The technology controller is designed as a PID controller. Whereby the derivative-action element can be switched to the control deviation channel or the actual value channel (factory setting). The P, I, and D components can be set separately. A value of 0 deactivates the corresponding component. Setpoints can be specified via two connector inputs. Setpoints can be scaled via parameters. A ramp-function generator in the setpoint channel can be used to set the setpoint ramp-up/ramp-down time via parameters. The setpoint and actual value channels each have a smoothing element. The smoothing time can be set via parameters.

###### Requirement

- The "Technology controller" function module is activated (see [MV function modules](#mv-function-modules)).

###### Properties of the technology controller

- Two scalable setpoints
- Scalable output signal
- Integrated fixed values
- Integrated motorized potentiometer
- The output limits are activated and deactivated via the ramp-function generator.
- The D component can be switched to the control deviation or actual value channel.
- The motorized potentiometer of the technology controller is active only when the drive pulses are enabled.

##### Technology motorized potentiometer

This section contains information on the following topics:

- [MV technology motorized potentiometer](#mv-technology-motorized-potentiometer)
- [MV motorized potentiometer ramp-function generator](#mv-motorized-potentiometer-ramp-function-generator)

###### MV technology motorized potentiometer

###### Description

The motorized potentiometer enables a setpoint to be specified for the technology controller. The setpoint is specified via a ramp-function generator.

###### Parameterizing the technology controller motorized potentiometer

1. Interconnect the "Setpoint higher" signal source ([p2235](SINAMICS%20Parameter%20VECTORMV.md#p22350n-bi-technology-controller-motorized-potentiometer-raise-setpoint)) to increase the setpoint.
2. Interconnect the "Setpoint lower" signal source ([p2236](SINAMICS%20Parameter%20VECTORMV.md#p22360n-bi-technology-controller-motorized-potentiometer-lower-setpoint)) to decrease the setpoint.
3. Correct the specified value for the upper limit of the speed setpoint in % in the "Maximum value" field ([p2237](SINAMICS%20Parameter%20VECTORMV.md#p22370n-technology-controller-motorized-potentiometer-maximum-value)).
4. Correct the specified value for the lower limit of the speed setpoint in % in the "Minimum value" field ([p2238](SINAMICS%20Parameter%20VECTORMV.md#p22380n-technology-controller-motorized-potentiometer-minimum-value)).
5. Configure the ramp-function generator of the motorized potentiometer (see "[Motorized potentiometer ramp-function generator](#mv-motorized-potentiometer-ramp-function-generator)").
6. To save the setpoint after switching the motor off, select "Yes" in the "Saving active" drop-down list.
7. To save the setpoint retentively, select "Yes" in the "Save retentively active" drop-down list.
8. Interconnect the "Setpoint after RFG" ([r2250](SINAMICS%20Parameter%20VECTORMV.md#r2250-co-technology-controller-motorized-potentiometer-setpoint-after-rfg)) signal sink to display the effective setpoint after the internal ramp-function generator for the motorized potentiometer of the technology controller.

###### Function diagrams (FD)

- Technology controller - motorized potentiometer (r0108.16 = 1) - 7954 -

###### Additional parameters

---

###### MV motorized potentiometer ramp-function generator

###### Description

The ramp-function generator ramps the setpoint up and down without acceleration jumps. The ramp-function generator is parameterized via the ramp-up time and ramp-down time parameters. The times refer to the time needed to reach the reference setpoint (0% or 100%) in the specified time.

###### Configuring the ramp-function generator

1. Click the "Technology motorized potentiometer" button in the "Ramp-function generator" screen form.

   The "Technology motorized potentiometer ramp-function generator" dialog opens. The initial rounding is active by default.
2. If you do not require an initial rounding, select "No" in the "Initial rounding active" drop-down list.

   The set ramp-up or ramp-down time can be exceeded with the initial rounding.
3. Correct the specified default value in the "Ramp-up time" ([p2247](SINAMICS%20Parameter%20VECTORMV.md#p22470n-technology-controller-motorized-potentiometer-ramp-up-time)) field.
4. Correct the specified default value in the "Ramp-down time" ([p2248](SINAMICS%20Parameter%20VECTORMV.md#p22480n-technology-controller-motorized-potentiometer-ramp-down-time)) field.
5. Enter the desired start value for the motorized potentiometer in the "Start value" ([p2240](SINAMICS%20Parameter%20VECTORMV.md#p22400n-technology-controller-motorized-potentiometer-starting-value)) field.

   This value takes effect when the drive is switched on.
6. Correct the specified maximum value for the motorized potentiometer of the technology controller in the field of the same name ([p2237](SINAMICS%20Parameter%20VECTORMV.md#p22370n-technology-controller-motorized-potentiometer-maximum-value)).
7. Correct the specified minimum value for the motorized potentiometer of the technology controller in the field of the same name ([p2238](SINAMICS%20Parameter%20VECTORMV.md#p22380n-technology-controller-motorized-potentiometer-minimum-value)).
8. Once you have made all the necessary settings, click the "Close" button.

   The dialog closes.

###### Function diagrams (FD)

- Technology controller - motorized potentiometer (r0108.16 = 1) - 7954 -

###### Additional parameters

---

##### Technology fixed setpoints

This section contains information on the following topics:

- [MV technology controller fixed setpoints](#mv-technology-controller-fixed-setpoints)

###### MV technology controller fixed setpoints

###### Description

The fixed setpoints of the technology controller can be selected freely. Fixed setpoints are speed setpoints freely stored by the user.

###### Selecting fixed setpoints via binary selection

1. Interconnect the four signal sources for setting the selection bit of the speed setpoint.

   - Bit 0: [p2220](SINAMICS%20Parameter%20VECTORMV.md#p22200n-bi-technology-controller-fixed-value-selection-bit-0)
   - Bit 2: [p2221](SINAMICS%20Parameter%20VECTORMV.md#p22210n-bi-technology-controller-fixed-value-selection-bit-1)
   - Bit 2: [p2222](SINAMICS%20Parameter%20VECTORMV.md#p22220n-bi-technology-controller-fixed-value-selection-bit-2)
   - Bit 3: [p2223](SINAMICS%20Parameter%20VECTORMV.md#p22230n-bi-technology-controller-fixed-value-selection-bit-3)
2. Interconnect the "Fixed value selected" ([r2225](SINAMICS%20Parameter%20VECTORMV.md#r22250-cobo-technology-controller-fixed-value-selection-status-word)) signal sink to display the status of the fixed setpoints (0/1 = off/on).
3. Enter fixed speed setpoints in the "Fixed value 1...15" ([p2201](SINAMICS%20Parameter%20VECTORMV.md#p22010n-co-technology-controller-fixed-value-1)...[p2215](SINAMICS%20Parameter%20VECTORMV.md#p22150n-co-technology-controller-fixed-value-15)) fields.

   The effective speed setpoint then results from the addition of the individual speed setpoints according to the selection bits.
4. Click the "Interconnections" button.

   The "Technology fixed setpoint interconnection" dialog opens.
5. Interconnect the "Fixed value 1...15" fixed values (p2201...p2215) via the connected signal sources.
6. Once you have made all the necessary settings, click the "Close" button.

   The dialog closes.
7. Interconnect the "Fixed value active" ([r2224](SINAMICS%20Parameter%20VECTORMV.md#r2224-co-technology-controller-fixed-value-effective)) signal source to display the active fixed speed setpoint.

###### Function diagrams (FD)

- Technology controller - fixed values, binary selection (r0108.16 = 1 and p2216 = 2) - 7950 -

###### Additional parameters

---

##### Technology setpoints / actual values

This section contains information on the following topics:

- [MV technology setpoints / actual values](#mv-technology-setpoints-actual-values)
- [MV technology ramp-up/ramp-down time](#mv-technology-ramp-upramp-down-time)

###### MV technology setpoints / actual values

###### Description

SINAMICS contains an integrated technology controller (PID controller) for simple closed-loop control functions such as level control or temperature control. The P, I and D component can each be set and switched off separately. Switching off is performed by entering a "0" in the appropriate parameter ([p2200](SINAMICS%20Parameter%20VECTORMV.md#p22000n-bi-technology-controller-enable)).

###### Parameterizing setpoints 1 and 2

1. Interconnect the signal source for setpoint 1 of the technology controller at "Setpoint 1" ([p2253](SINAMICS%20Parameter%20VECTORMV.md#p22530n-ci-technology-controller-setpoint-1)).

   The PID motorized potentiometer, fixed setpoints, analog inputs or the fieldbus interface can be used as the setpoint source.
2. To scale setpoint 1, enter a value between 0 ... 100% at "Setpoint 1 scaling" ([p2255](SINAMICS%20Parameter%20VECTORMV.md#p2255-technology-controller-setpoint-1-scaling)).
3. Interconnect the signal source for setpoint 2 of the technology controller at "Setpoint 2" ([p2254](SINAMICS%20Parameter%20VECTORMV.md#p22540n-ci-technology-controller-setpoint-2)).

   The additional setpoint is added to the main setpoint.
4. To scale setpoint 2, enter a value between 0 ... 100% at "Setpoint 2 scaling" ([p2256](SINAMICS%20Parameter%20VECTORMV.md#p2256-technology-controller-setpoint-2-scaling)).
5. If required, parameterize the ramp-function generator of the setpoint technology controller (see "[MV technology ramp-up/ramp-down time](#mv-technology-ramp-upramp-down-time)").
6. Enter a value for the smoothing time in the "Setpoint filter" field ([p2261](SINAMICS%20Parameter%20VECTORMV.md#p2261-technology-controller-setpoint-filter-time-constant)).

   The setpoint filter is implemented as a PT1 element.

###### Parameterizing the actual value source and the actual value function

1. Interconnect the signal source for the actual value of the technology controller at "Actual value" ([p2264](SINAMICS%20Parameter%20VECTORMV.md#p22640n-ci-technology-controller-actual-value)).
2. In order to apply a smoothing filter to the actual value, enter a value between 0 ... 60 s in the "Actual value filter" field ([p2265](SINAMICS%20Parameter%20VECTORMV.md#p2265-technology-controller-actual-value-filter-time-constant)).

###### Function diagrams (FD)

- Technology controller - control (r0108.16 = 1) - 7958 -

###### Additional parameters

---

###### MV technology ramp-up/ramp-down time

###### Description

Ramp-up and ramp-down times prevent sudden setpoint jumps and therefore abrupt acceleration. A change at the PID controller input is passed on to the output via a defined ramp.

###### Configuring the ramp-up time and ramp-down time

1. Click the "Ramp-function generator" button in the "Technology setpoints / actual values" screen form.

   The "Technology setpoint ramp-function generator" dialog opens.
2. The "Acceleration/deceleration ramp independent of setpoint sign" option is active by default.

   Deactivate this option if required.
3. Correct the default value in the "Ramp-up time" ([p2257](SINAMICS%20Parameter%20VECTORMV.md#p2257-technology-controller-ramp-up-time)) field.
4. Correct the default value in the "Ramp-down time" ([p2258](SINAMICS%20Parameter%20VECTORMV.md#p2258-technology-controller-ramp-down-time)) field.
5. Once you have made all the necessary settings, click the "Close" button.

   The dialog closes.

###### Function diagrams (FD)

- Technology controller - control (r0108.16 = 1) - 7958 -

###### Additional parameters

---

##### Technology PID controller

This section contains information on the following topics:

- [MV technology PID controller](#mv-technology-pid-controller)
- [Limitation of the MV PID controller](#limitation-of-the-mv-pid-controller)

###### MV technology PID controller

###### Description

The technology controller is configured optionally as P, I, PI, or PID controller.

> **Note**
>
> The value 0 deactivates the corresponding controller component.

###### Configuring the PID controller

To parameterize the PI component of the controller as well as the proportional gain and the integral time, proceed as follows:

1. Enter a value in the "Proportional gain" ([p2280](SINAMICS%20Parameter%20VECTORMV.md#p2280-technology-controller-proportional-gain)) field.
2. Enter a value in the "Integral time" ([p2285](SINAMICS%20Parameter%20VECTORMV.md#p2285-technology-controller-integral-time)) field.
3. Click the large button for the PID controller.

   The "PID controller" dialog opens.
4. To evaluate the integration time of the PID controller with the gain factor Kp (p2280), deactivate the "Integrator independent of Kp" ([p2252](SINAMICS%20Parameter%20VECTORMV.md#p2252-technology-controller-configuration).1) option.
5. Enter a value for the "Differentiation" ([p2274](SINAMICS%20Parameter%20VECTORMV.md#p2274-technology-controller-differentiation-time-constant)).
6. Select one of the following options in the "Technology controller type" ([p2263](SINAMICS%20Parameter%20VECTORMV.md#p2263-technology-controller-type)) drop-down list:

   - [0] D component in the actual value signal

     The differential component of the controller is used on the actual value signal with this setting. Use the setting, for example, if the actual value signal contains large deflections that have to be cleaned up quickly in the setpoint via the D component in the controller.
   - [1] D component in the control deviation

     The differential component of the controller is used on the setpoint / actual value difference with this setting.
7. Once you have made all the necessary settings, click the "Close" button.

   The dialog closes. The settings are accepted on the "Technology PID controller" screen form.
8. Interconnect the signal source for the precontrol at "Precontrol signal" ([p2289](SINAMICS%20Parameter%20VECTORMV.md#p22890n-ci-technology-controller-precontrol-signal)).
9. Interconnect the signal source for the enabling signal at "Enable" ([p2200](SINAMICS%20Parameter%20VECTORMV.md#p22000n-bi-technology-controller-enable)).
10. If required, also configure the limits of the PID controller (see "[Limitation of the MV PID controller](#limitation-of-the-mv-pid-controller)").
11. If required, correct the interconnection of the "Technology controller output scaling" ([p2296](SINAMICS%20Parameter%20VECTORMV.md#p22960n-ci-technology-controller-output-scaling)) signal source for scaling the technology controller output.

    Parameter [p2295](SINAMICS%20Parameter%20VECTORMV.md#p2295-co-technology-controller-output-scaling) is interconnected as default setting. If you want to use a different value for the scaling, change the interconnection.
12. To directly scale the technology controller, enter a value between -100 ... 100% in the "Output scaling" (p2295) field.
13. Interconnect the "Output signal" ([r2294](SINAMICS%20Parameter%20VECTORMV.md#r2294-co-technology-controller-output-signal)) signal sink to display the output signal of the technology controller.

###### Function diagrams (FD)

- Technology controller - control (r0108.16 = 1) - 7958 -

###### Additional parameters

---

###### Limitation of the MV PID controller

###### Description

For some applications, the PID output variable must be limited to defined values. This can be achieved using fixed limits. To prevent large jumps of the PID controller output when the device is switched on, these PID output limits will be ramped-up via the ramp time from 0 to the appropriate values (upper limit for the PID output or lower limit for the PID output). As soon as the limits are reached, the dynamic response of the PID controller is no longer limited by this ramp-up/ramp-down time.

> **Note**
>
> The limits are entered in [%].

###### Configuring the PID controller limits

1. Click the "Controller limited" button.  
   The "Technology PID controller limits" dialog opens.
2. Deactivate the "Output signal without ramp active" ([p2252](SINAMICS%20Parameter%20VECTORMV.md#p2252-technology-controller-configuration).2) option to reduce the output signal [r2294](SINAMICS%20Parameter%20VECTORMV.md#r2294-co-technology-controller-output-signal) via the deceleration ramp [p2293](SINAMICS%20Parameter%20VECTORMV.md#p2293-technology-controller-ramp-upramp-down-time) to zero.
3. Enter a value in the "Maximum limiting" ([p2291](SINAMICS%20Parameter%20VECTORMV.md#p2291-co-technology-controller-maximum-limiting)) field.
4. Interconnect the "Maximum limiting signal source" ([p2297](SINAMICS%20Parameter%20VECTORMV.md#p22970n-ci-technology-controller-maximum-limit-signal-source)) for the maximum limiting of the technology controller.
5. Enter a value in the "Minimum limiting" ([p2292](SINAMICS%20Parameter%20VECTORMV.md#p2292-co-technology-controller-minimum-limiting)) field.
6. Interconnect the "Minimum limiting signal source" ([p2298](SINAMICS%20Parameter%20VECTORMV.md#p22980n-ci-technology-controller-minimum-limit-signal-source)) for the minimum limiting of the technology controller.
7. Enter a value (in seconds) for the ramp-up and ramp-down time for the output signal of the technology controller in the "Ramp-up/ramp-down time" (p2293) field.
8. Once you have made all the necessary settings, click the "Close" button.

   The dialog closes. The settings are accepted on the "Technology PID controller" screen form.

###### Function diagrams (FD)

- Technology controller - control (r0108.16 = 1) - 7958 -

###### Additional parameters

---

#### Bypass operation

This section contains information on the following topics:

- [MV bypass mode](#mv-bypass-mode)
- [MV bypass with synchronization](#mv-bypass-with-synchronization)

##### MV bypass mode

###### Description

The bypass mode allows you to operate a motor using the converter or directly on the line supply. The switches are controlled using the converter; feedback signals of the switch positions must be returned to the converter. The bypass mode can be operated with or without synchronization.

**Bypass with synchronization**

When the bypass with synchronization function is activated, the motor will be passed to and fetched from the line supply synchronized. Switchover occurs with overlap (phase lock synchronization).

In this case, both switches are closed simultaneously during the overlap time. A reactor is used to decouple the converter and line supply voltage.

###### Requirements

- The "Technology controller" function module has been activated.
- The bypass mode can only be used for VECTOR drives.

###### Function diagrams (FD)

Technology functions - synchronizing - 7020 -

###### Additional parameters

[p1260](SINAMICS%20Parameter%20VECTORMV.md#p1260-bypass-configuration)

[r1261](SINAMICS%20Parameter%20VECTORMV.md#r1261013-cobo-bypass-controlstatus-word)

[p1262](SINAMICS%20Parameter%20VECTORM2C.md#p12620n-line-transfer-maximum-overlap-time)

[p1263](SINAMICS%20Parameter%20VECTORM2C.md#p12630n-line-transfer-frequency-gradient-during-overlap)

[p1264](SINAMICS%20Parameter%20VECTORM2C.md#p12640n-line-transfer-voltage-gradient-during-overlap)

p1265

[p1266](SINAMICS%20Parameter%20VECTORMV.md#p1266-bi-bypass-control-command)

[p1267](SINAMICS%20Parameter%20VECTORM2C.md#p12670n-bi-line-transfer-startrequest-transfer-from-line-supply-sig-src)

[p1269](SINAMICS%20Parameter%20VECTORMV.md#p126901-bi-bypass-switch-feedback-signal)

p1274

---

##### MV bypass with synchronization

###### Bypass with synchronization with overlap

The "Bypass synchronize with overlap" is used for drives with low inertia. These are drives in which the speed would decrease very quickly when contactor K1 is opened.

When "Bypass with synchronization with overlap ([p1260](SINAMICS%20Parameter%20VECTORMV.md#p1260-bypass-configuration) = 1)" is activated, the motor is transferred, synchronized to the line supply and is also retrieved again. During the switchover, the two contactors K1 and K2 are simultaneously closed for a time (phase lock synchronization).

A Voltage Sensing Module VSM10 is required for this type of bypass which measures the line supply voltage required for the drive to be synchronized.

A reactor decouples the converter and line supply voltage - the uk value for the reactor is 10% +/- 2%.

![Circuit example: Bypass with synchronization with overlap](images/147862805003_DV_resource.Stream@PNG-en-US.png)

Circuit example: Bypass with synchronization with overlap

###### Parameterizing the bypass

1. Select the following configuration in the "Bypass configuration" (p1260) drop-down list:

   - [1] Bypass with synchronization with overlap
2. Interconnect the signal source for the control command to activate the bypass at "Bypass control command" ([p1266](SINAMICS%20Parameter%20VECTORMV.md#p1266-bi-bypass-control-command)).
3. Interconnect the signals sources via which the feedback signals can be output:

   - "Motor/drive switch" ([p1269](SINAMICS%20Parameter%20VECTORMV.md#p126901-bi-bypass-switch-feedback-signal).0)
   - "Switch motor / line supply" (p1269.1)
4. Correct the specified interconnection "Bypass feedback synchronization completed" ([p1268](SINAMICS%20Parameter%20VECTORMV.md#p1268-bi-bypass-feedback-synchronization-completed)) for the appropriate feedback signal.
5. Interconnect the following signal sinks for the control and feedback signals of the bypass switches:

   - "Synchronization requested" ([r1261](SINAMICS%20Parameter%20VECTORMV.md#r1261013-cobo-bypass-controlstatus-word).2)
   - "Command switch motor - power unit" (r1261.0)
   - "Command switch motor - line supply" (r1261.1)

###### Additional parameters

---

#### Technology Extensions

This section contains information on the following topics:

- [Adding and activating Technology Extensions](#adding-and-activating-technology-extensions)

##### Adding and activating Technology Extensions

###### "Technology Extensions that can be activated for this drive object" view - Current drive object

This tabular overview shows all installed Technology Extensions that are compatible with the drive object currently selected via the project tree for parameterization.

The overview has the following structure:

| Column | Description |
| --- | --- |
| Name | The name of the Technology Extension is displayed here. |
| Usage | Click the "Usage" button to change to the "Current drive object" view of the associated drive object. |
| Selection | Click the "Selection" option to activate or deactivate the Technology Extension for the current Startdrive project. |
| Version | The version of the Technology Extension is displayed here. |
| Info | Click the "Details" button to obtain more information on the Technology Extension. |

###### "Technology Extensions that cannot be activated" view - Current drive object

The "Technology Extensions that cannot be activated" overview is visible only if you select the "Current drive object" option in the drop-down list just to the right of the "Add further Technology Extensions..." button.

This tabular overview shows all installed Technology Extensions that are incompatible with the drive object currently selected via the project tree for parameterization.

The overview has the following structure:

| Column | Description |
| --- | --- |
| Name | The name of the Technology Extension is displayed here. |
| Reason | The reason why the Technology Extension is not compatible with the current drive object is displayed here. Click the button to obtain more information about why the Technology Extension is not compatible with the drive object. |
| Version | The version of the Technology Extension is displayed here. |
| Required FW version | The minimum SINAMICS firmware version required to use the Technology Extension is displayed here. |
| Existing FW version | The SINAMICS firmware version of the current drive object is displayed here. |
| Uninstall | Click the "Remove" button to uninstall the Technology Extension. |
| Info | Click the "Details" button to obtain more information on the Technology Extension. |

###### "Technology Extensions that can be activated for this drive unit" view - All drive objects

This tabular overview shows all of the installed Technology Extensions which you have added for the currently selected drive.

The overview has the following structure:

| Column | Description |
| --- | --- |
| Name | The name of the Technology Extension is displayed here. |
| Usage | Click the "Usage" button to change to the "Current drive object" view of the associated drive object. |
| Selection | Click the "Selection" option to activate or deactivate the Technology Extension for the current Startdrive project. |
| Version | The version of the Technology Extension is displayed here. |
| Parameter number range | The parameters that are relevant for the Technology Extension are displayed here. |
| Uninstall | Click the "Remove" button to uninstall the Technology Extension. |
| Info | Click the "Details" button to obtain more information on the Technology Extension. |

###### Requirements

- A project has been created, or an existing project is open.
- The device configuration contains one of the following SINAMICS drives:

  - SINAMICS S120 (as of firmware version 5.2)
  - SINAMICS MV (as of firmware version 5.2.1)

###### Changing views

To switch to the display of the "Technology Extensions" function view, proceed as follows:

1. In the drop-down list located just to the right of the "Add further Technology Extensions..." button, select the option "Current drive object".  
   The "Technology Extensions" function view now contains two overview tables:

   - "Technology Extensions that can be activated for this drive object"
   - "Technology Extensions that cannot be activated"
2. In the drop-down list located just to the right of the "Add further Technology Extensions..." button, select "All drive objects".  
   The "Technology Extensions" function view now contains only the overview table "Technology Extensions that can be activated for this drive object".

###### Adding Technology Extensions

Proceed as follows to add a Technology Extension to your Startdrive project:

1. Click the "Add further Technology Extension..." button.  
   A dialog opens.
2. In the file system of your PC, select the desired Technology Extension file (file extension *.tec) and click "Open".  
   The Technology Extension is added to your Startdrive installation.  
   Depending on the currently selected view and the compatibility with the current drive object, the Technology Extension is displayed in one of the tabular overviews.

**Note**

When you add a Technology Extension, it is available to you in your current Startdrive installation across all projects.

###### Activating Technology Extensions

To activate a Technology Extension, proceed as follows:

1. Add a Technology Extension to your project as described in the section "Adding Technology Extensions".
2. In the drop-down list located just to the right of the "Add further Technology Extensions..." button, select the required "Technology Extensions" function view from the drop-down.
3. Activate the option "Selection" in the corresponding row of the desired drive object located in the column of the tabular overview with the same name.

###### Deactivating Technology Extensions

To deactivate a Technology Extension, proceed as follows:

1. In the drop-down list located just to the right of the "Add further Technology Extensions..." button, select the required "Technology Extensions" function view from the drop-down.
2. Deactivate the option "Selection" in the corresponding row of the desired drive object located in the column of the tabular overview with the same name.

###### Uninstalling Technology Extensions

You can uninstall Technology Extensions globally via the "All drive objects" view or in the "Technology Extensions that cannot be activated" overview of the respective drive object.

Proceed as follows to remove a Technology Extension from your Startdrive project:

1. Open the "All drive objects" view or the "Technology Extensions that cannot be activated" overview of the desired drive object.
2. Click the "Remove" button in the row of the drive object concerned in the "Uninstall" column.

   The "Remove Technology Extension" dialog opens.
3. Click "Yes" to confirm the uninstallation of the Technology Extension.
4. If the Technology Extension is still activated on drive objects in the project, the "Remove Technology Extension" dialog opens again.  
   All drive objects on which the Technology Extension is still activated are listed.  
   Click "Yes" to uninstall the Technology Extension.

###### Additional information

You can find additional information on the Technology Extensions in the SIOS portal on the Internet.

---

**See also**

[SIOS portal](https://support.industry.siemens.com/cs/ww/en/view/109771648)

### Control logic

#### Definition

The connections for the control and status words are displayed for the drive in the "Control logic" screen form. You can edit these connections:

The connections for the control and status words are arranged in groups. The connections of a group can be displayed in the screen form via two drop-down lists on the left and on the right. Connections can be displayed for the following groups:

- Control word sequence control (r898)
- Control word faults/alarms (r2138)
- Control word speed controller (r1406)
- Control value setpoint channel (r1198)
- Command Data Set CDS selected (r836)
- Status word sequence controls (r899)
- Status word faults/alarms 1 (r2139)
- Status word faults/alarms 2 (r2135)
- Status word speed controller (r1407)
- Status word monitoring 1 (r2197)
- Status word monitoring 2 (r2198)
- Status word monitoring 3 (r2199)
- Encoder control word Gn_STW; Encoder control word Gn_STW (p480[0])
- Encoder control word Gn_STW; Encoder control word Gn_STW (p480[1])
- Encoder control word Gn_STW; Encoder control word Gn_STW (p480[2])
- Encoder status word Gn_ZSW; Encoder 1 (r481[0])
- Encoder status word Gn_ZSW, Encoder 2 (r481[1])
- Encoder status word Gn_ZSW, Encoder 3 (r481[2])
- Missing enables (r46)
- Ramp-function generator status word (r1199)
- Status word, closed-loop controls (r56)

An illuminated LED display means that the corresponding bit of the control or status word is set. If the bit value of the control or status word results from the logical connection of several signal sources, the type of the logical connection is displayed by the associated logic symbol.

#### Selecting and connecting control and status words

1. Select the desired group of control and status words in the drop-down list (on the left or right in the screen form).

   The corresponding display and connection fields are displayed on the side of the screen form on which you made the setting in the drop-down list.
2. Interconnect the signal sources for the displayed parameters (for control words) or the bits (for status words and missing enables).

## Diagnostics

This section contains information on the following topics:

- [Missing enables](#missing-enables)
- [Control/status words](#controlstatus-words)
- [Status parameters](#status-parameters)
- [Communication](#communication)

### Missing enables

The drive does not change to the "Operation" state until all the enables are present. In the "Missing enables" screen form, the LEDs in the function view indicate which enables are still missing. An illuminated LED display indicates that the corresponding enable is missing.

The bits of the missing enables ([r0046](SINAMICS%20Parameter%20VECTORMV.md#r0046029-cobo-missing-enable-sig)) are displayed in the screen form.

#### Additional parameters

---

### Control/status words

#### Description

The control and status words are displayed in the function view for diagnostic purposes in the "Control/status words" screen form. The screen form is split into two vertical sections each displaying a group of control and status words via a drop-down list.

The following groups can be displayed:

- Control word sequence control ([r0898](SINAMICS%20Parameter%20VECTORMV.md#r0898012-cobo-control-word-sequence-control))
- Control word faults/alarms ([r2138](SINAMICS%20Parameter%20VECTORMV.md#r2138715-cobo-control-word-faultsalarms))
- Control word speed controller ([r1406](SINAMICS%20Parameter%20VECTORMV.md#r1406415-cobo-control-word-speed-controller))
- Status word sequence control ([r0899](SINAMICS%20Parameter%20VECTORMV.md#r0899015-cobo-status-word-sequence-control))
- Status word faults/alarms 1 ([r2139](SINAMICS%20Parameter%20VECTORMV.md#r2139015-cobo-status-word-faultsalarms-1))
- Status word faults/alarms 2 ([r2135](SINAMICS%20Parameter%20VECTORMV.md#r2135015-cobo-status-word-faultsalarms-2))
- Status word speed controller ([r1407](SINAMICS%20Parameter%20VECTORMV.md#r1407027-cobo-status-word-speed-controller))
- Status word monitoring 1 ([r2197](SINAMICS%20Parameter%20VECTORMV.md#r2197113-cobo-status-word-monitoring-1))
- Status word monitoring 2 ([r2198](SINAMICS%20Parameter%20VECTORMV.md#r2198412-cobo-status-word-monitoring-2))
- Status word monitoring 3 ([r2199](SINAMICS%20Parameter%20VECTORMV.md#r2199012-cobo-status-word-monitoring-3))
- Status word current controller ([r1408](SINAMICS%20Parameter%20VECTORGL.md#r14080n-co-status-word-current-controller))
- Status word closed-loop control ([r0056](SINAMICS%20Parameter%20VECTORMV.md#r0056215-cobo-status-word-closed-loop-control))

#### Selecting a group of control and status words

1. In one of the two drop-down lists, select the required group of control and status words.

   The corresponding display and interconnection fields are displayed on the side of the screen form on which you made the setting in the drop-down list.

   A highlighted LED display means that the corresponding bit of the control or status word has been set.
2. If you want to display the values of several groups next to one another, set the other desired groups in the other two drop-down lists.

#### Function diagrams (FD)

- Internal control/status words - control word, setpoint channel - 2505 -
- Internal control/status words - status word, monitoring functions 1 - 2534 -
- Internal control/status words - status word, monitoring functions 3 - 2537 -
- Internal control/status words - control word faults/alarms - 2546 -
- Internal control/status words - status word, faults/alarms 1 and 2 - 2548 -
- Internal control/status words - control word, sequence control - 2501 -
- Internal control/status words - status word, sequence control - 2503 -
- Internal control/status words - status word speed controller - 2522 -
- Internal control/status words - status word, closed-loop control - 2526 -
- Internal control/status words - status word, monitoring functions 2 - 2536 -

#### Additional parameters

---

### Status parameters

This dialog displays the values of important parameters, which characterize the operating state of the converter.

The displayed parameters depend on the selected drive object.

More detailed information about the parameters can be found in the following sources:

- Help for the respective parameter
- SINAMICS S120/S150 List Manual

### Communication

This section contains information on the following topics:

- [Receive direction drive MV telegrams](#receive-direction-drive-mv-telegrams)
- [Send direction drive MV telegrams](#send-direction-drive-mv-telegrams)

#### Receive direction drive MV telegrams

##### Description

Here, you specify the interconnections of the PROFIdrive telegram in the receive direction for the drive axis.

In the telegram configuration (![Description](images/147853831051_DV_resource.Stream@PNG-en-US.png)) you can change the configuration of the telegrams or add telegram extensions.

**Telegram structure**

The interconnections for the process data in the receive direction are created automatically for the standard and manufacturer-specific telegrams.

If you select the Free telegram configuration, you can freely define the interconnections for the process data in the receive direction.

Only those telegrams available for the drive object are offered. The interconnections of the control words or receive words have already been created.

| Symbol | Meaning |
| --- | --- |
| ![Description](images/147853827083_DV_resource.Stream@PNG-en-US.png) | Click the button next to "Interconnections" to interconnect the signal for the connector output. |
| ![Description](images/147860084491_DV_resource.Stream@PNG-en-US.png) | Click the button to display and interconnect the signal bit by bit. |

The following information is displayed by the telegrams shown:

| Telegram type | PZD | Display of the value | Format switchover | Control words | Interconnections |
| --- | --- | --- | --- | --- | --- |
|  | The numbering and arrangement of the process data. | Value of the process data (PZD) | Switch value of the process date to other display (hex, bin, dec). | List of the control words that are transmitted in the telegram. | Display or interconnection of the parameter with which the signal is to be interconnected. Several interconnections are possible. |
| PROFIdrive  7, 9, 110, 111 | X | X | X | X | X |
| Telegram extension | X | X | X | X | X |

##### Function diagrams (FD)

- FD-2410 (54)
- FD-2415 (54)
- FD-2416 (54)
- FD-2419 (55)
- FD-2420 (01)
- FD-2421 (54)
- FD-2422 (54)
- FD-2423 (54)
- FD-2425 (54)
- FD-2426 (54)
- FD-2428 (54)
- FD-2429 (54)
- FD-2439 (54)
- FD-2440 (54)
- FD-2441 (54)
- FD-2442 (54)
- FD-2444 (54)
- FD-2449 (54)
- FD-2450 (54)
- FD-2451 (54)
- FD-2452 (54)
- FD-2454 (54)
- FD-2468 (54)
- FD-2472 (54)
- FD-2481 (54)
- FD-2485 (54)
- FD-2489 (54)
- FD-2491 (54)
- FD-2495 (54)
- FD-2496 (54)
- FD-2475 (55)
- FD-2476 (55)
- FD-2479 (55)
- FD-2480 (55)
- FD-2462 (55)
- FD-2463 (55)
- FD-2464 (55)
- FD-2466 (55)
- FD-2467 (55)
- FD-2915 (54)
- FD-2917 (54)

#### Send direction drive MV telegrams

##### Description

Here, you specify the parameters of the PROFIdrive telegram in the send direction for the drive axis.

In the telegram configuration (![Description](images/147853831051_DV_resource.Stream@PNG-en-US.png)) you can change the configuration of the telegrams or add telegram extensions.

**Telegram structure**

The interconnections for the process data in the send direction are created automatically for the standard and manufacturer-specific telegrams.

If you select the Free telegram configuration, you can freely define the interconnections for the process data in the send direction.

| Symbol | Meaning |
| --- | --- |
| ![Description](images/147853860363_DV_resource.Stream@PNG-en-US.png) | Click the button to the left of "Interconnections" to interconnect the signal for the connector input. |

The selected telegram is displayed in the form of a table:

| Telegram type | Interconnections | Status words | Value | Format switchover | PZD |
| --- | --- | --- | --- | --- | --- |
|  | Display or interconnection of the parameter with which the signal is to be interconnected or is interconnected. | List of the status words that are transmitted in the telegram. | Value of the process data (PZD) | Switch value of the process date to other display (hex, bin, dec). | Numbering and arrangement of the process data. |
| PROFIdrive  7, 9, 110, 111 | X | X | X | X | X |
| Telegram extension | X | X | X | X | X |

##### Function diagrams (FD)

- FD-2410 (54)
- FD-2415 (54)
- FD-2416 (54)
- FD-2419 (55)
- FD-2420 (01)
- FD-2421 (54)
- FD-2422 (54)
- FD-2423 (54)
- FD-2425 (54)
- FD-2426 (54)
- FD-2428 (54)
- FD-2429 (54)
- FD-2439 (54)
- FD-2440 (54)
- FD-2441 (54)
- FD-2442 (54)
- FD-2444 (54)
- FD-2449 (54)
- FD-2450 (54)
- FD-2451 (54)
- FD-2452 (54)
- FD-2454 (54)
- FD-2470 (54)
- FD-2472 (54)
- FD-2483 (54)
- FD-2487 (54)
- FD-2489 (54)
- FD-2493 (54)
- FD-2495 (54)
- FD-2496 (54)
- FD-2475 (55)
- FD-2476 (55)
- FD-2479 (55)
- FD-2480 (55)
- FD-2462 (55)
- FD-2463 (55)
- FD-2464 (55)
- FD-2466 (55)
- FD-2467 (55)
- FD-2915 (54)
- FD-2917 (54)

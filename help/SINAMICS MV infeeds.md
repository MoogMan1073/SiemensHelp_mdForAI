---
title: "SINAMICS MV infeeds"
package: Stdr040000UIenUS
topics: 26
source: Siemens TIA Portal Information System (offline help, en-US)
---


# SINAMICS MV infeeds

This section contains information on the following topics:

- [Overview](#overview)
- [Parameterization](#parameterization)
- [Diagnostics](#diagnostics)

## Overview

### Infeeds (Line Modules)

SINAMICS MV uses a so-called "Power Stack Adapter MV" as infeed.

A Power Stack Adapter (PSA) acts as the physical interface between the power unit and the open-loop/closed-loop controller. This is where the galvanic isolation (electrical coupling via light) between the power unit and the open-loop controller takes place. Data is exchanged between the Power Stack Adapter and the Control Unit via the DRIVE-CLiQ high-speed serial communication interface.

## Parameterization

This section contains information on the following topics:

- [Basic parameter assignment](#basic-parameter-assignment)
- [Technology Extensions](#technology-extensions)
- [Control logic](#control-logic)

### Basic parameter assignment

This section contains information on the following topics:

- [Function modules (infeed)](#function-modules-infeed)
- [Line data / operating mode](#line-data-operating-mode)
- [Enable logic](#enable-logic)
- [Data sets](#data-sets)

#### Function modules (infeed)

You can connect the "Free function blocks" function module for the infeed used.

> **Note**
>
> You can only activate or deactivate function modules offline.

##### Activating a function module

1. Activate the "Free function blocks" function module by clicking the option.
2. Save the project to save the settings.

##### Additional parameters

---

#### Line data / operating mode

##### Setting the line data and operating mode

The device supply voltage of an infeed is set in the function view of the "Line data / operating mode" screen form.

1. Enter a value for the device supply voltage in the "Device supply voltage" field ([p0210](SINAMICS%20Parameter%20VECTORMV.md#p0210-drive-unit-line-supply-voltage)).

##### Additional parameters

---

#### Enable logic

You can connect several signal sources for the enables in the function view of the "Enable logic" mask.

##### Procedure

1. Connect the signal source via "[p0840](SINAMICS%20Parameter%20VECTORMV.md#p08400n-bi-on-off-off1)" for "OFF1 (low-active)".
2. Connect the 1st signal source via "[p0844](SINAMICS%20Parameter%20VECTORMV.md#p08440n-bi-no-coast-down-coast-down-off2-signal-source-1)" for "Instantaneous OFF (OFF2) signal source 1".
3. Connect the 2nd signal source via "[p0845](SINAMICS%20Parameter%20VECTORMV.md#p08450n-bi-no-coast-down-coast-down-off2-signal-source-2)" for "Instantaneous OFF (OFF2) signal source 2".
4. Connect the signal source via "[p0852](SINAMICS%20Parameter%20VECTORMV.md#p08520n-bi-enable-operationinhibit-operation)" for "Enable operation".

##### Additional parameters

---

#### Data sets

This section contains information on the following topics:

- [Fundamentals](#fundamentals)
- [Structure of the data set screen form](#structure-of-the-data-set-screen-form)
- [Managing a command data set (CDS)](#managing-a-command-data-set-cds)
- [Activating or editing data sets](#activating-or-editing-data-sets)
- [Switching data sets](#switching-data-sets)

##### Fundamentals

###### Overview

For many applications it is beneficial if multiple parameters can be changed simultaneously by means of an external signal during operation or when the system is ready for operation. This can be carried out with the aid of indexed parameters. For the purpose of this function, the parameters have been combined in such a way that they form groups or data sets and are indexed. By using the indexing, several different settings can be stored for each parameter and activated by changing the data set (i.e. switching back and forth between the data sets).

Those parameters (connector and binector inputs) that are used to control the converter and enter a setpoint are assigned to the command data set (CDS).

You can configure the data sets for each drive within a project:

- You create the corresponding components in the device configuration.
- You configure the available data sets in Startdrive while creating new data sets or deleting existing data sets.

###### Function diagrams (FD)

- FD-8560 (54)

###### Parameters

- [p0170](SINAMICS%20Parameter%20VECTORMV.md#p0170-number-of-command-data-sets-cds)
- [p0809](SINAMICS%20Parameter%20VECTORMV.md#p080902-copy-command-data-set-cds)
- [p0810](SINAMICS%20Parameter%20VECTORMV.md#p0810-bi-command-data-set-selection-cds-bit-0)
- [p0811](SINAMICS%20Parameter%20VECTORMV.md#p0811-bi-command-data-set-selection-cds-bit-1)

---

---

**See also**

[Rules for using data sets](Configuring%20SINAMICS%20S-G-MV%20drives.md#rules-for-using-data-sets)
  
[Data set definitions](Configuring%20SINAMICS%20S-G-MV%20drives.md#data-set-definitions)

##### Structure of the data set screen form

###### Structure of the data set screen forms

![Example: Screen form for command data sets](images/147854087819_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Icons for editing/activating DDS drive data sets in online mode. Not relevant for CDS. |
| ② | Two buttons in the active data set screen form enable the insertion and deletion of individual data sets of the list. |
| ③ | List of created command data sets. The created data sets are numbered chronologically. |
| ④ | Working area for activating a selected data set via BICO interconnections. |

Example: Screen form for command data sets

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

You can switch between different data sets in the configuration screen forms. The switchover is performed via the drop-down list in the toolbar.

![Data set switchover](images/147854165003_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Shows the active command data set (CDS). Enables switchover to a different data set. |

Data set switchover

###### Requirement

- Multiple command data sets have been created.

  If only one data set has been created, the drop-down list for switchover is deactivated.

###### Procedure

1. Open the required configuration screen form.

   The drop-down list for data set switchover shows the active data set. The settings of this data set are shown in the screen form below it.
2. Select another data set from the drop-down list for the data set switchover.
3. Change the signal sources of the BICO interconnections at the bottom of the working area.

###### Result

In the screen form, all data-set-dependent settings are changed to the values of the selected data set (if these values are configured differently).

### Technology Extensions

This section contains information on the following topics:

- [Adding and activating Technology Extensions](#adding-and-activating-technology-extensions)

#### Adding and activating Technology Extensions

##### "Technology Extensions that can be activated for this drive object" view - Current drive object

This tabular overview shows all installed Technology Extensions that are compatible with the drive object currently selected via the project tree for parameterization.

The overview has the following structure:

| Column | Description |
| --- | --- |
| Name | The name of the Technology Extension is displayed here. |
| Usage | Click the "Usage" button to change to the "Current drive object" view of the associated drive object. |
| Selection | Click the "Selection" option to activate or deactivate the Technology Extension for the current Startdrive project. |
| Version | The version of the Technology Extension is displayed here. |
| Info | Click the "Details" button to obtain more information on the Technology Extension. |

##### "Technology Extensions that cannot be activated" view - Current drive object

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

##### "Technology Extensions that can be activated for this drive unit" view - All drive objects

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

##### Requirements

- A project has been created, or an existing project is open.
- The device configuration contains one of the following SINAMICS drives:

  - SINAMICS S120 (as of firmware version 5.2)
  - SINAMICS MV (as of firmware version 5.2.1)

##### Changing views

To switch to the display of the "Technology Extensions" function view, proceed as follows:

1. In the drop-down list located just to the right of the "Add further Technology Extensions..." button, select the option "Current drive object".  
   The "Technology Extensions" function view now contains two overview tables:

   - "Technology Extensions that can be activated for this drive object"
   - "Technology Extensions that cannot be activated"
2. In the drop-down list located just to the right of the "Add further Technology Extensions..." button, select "All drive objects".  
   The "Technology Extensions" function view now contains only the overview table "Technology Extensions that can be activated for this drive object".

##### Adding Technology Extensions

Proceed as follows to add a Technology Extension to your Startdrive project:

1. Click the "Add further Technology Extension..." button.  
   A dialog opens.
2. In the file system of your PC, select the desired Technology Extension file (file extension *.tec) and click "Open".  
   The Technology Extension is added to your Startdrive installation.  
   Depending on the currently selected view and the compatibility with the current drive object, the Technology Extension is displayed in one of the tabular overviews.

**Note**

When you add a Technology Extension, it is available to you in your current Startdrive installation across all projects.

##### Activating Technology Extensions

To activate a Technology Extension, proceed as follows:

1. Add a Technology Extension to your project as described in the section "Adding Technology Extensions".
2. In the drop-down list located just to the right of the "Add further Technology Extensions..." button, select the required "Technology Extensions" function view from the drop-down.
3. Activate the option "Selection" in the corresponding row of the desired drive object located in the column of the tabular overview with the same name.

##### Deactivating Technology Extensions

To deactivate a Technology Extension, proceed as follows:

1. In the drop-down list located just to the right of the "Add further Technology Extensions..." button, select the required "Technology Extensions" function view from the drop-down.
2. Deactivate the option "Selection" in the corresponding row of the desired drive object located in the column of the tabular overview with the same name.

##### Uninstalling Technology Extensions

You can uninstall Technology Extensions globally via the "All drive objects" view or in the "Technology Extensions that cannot be activated" overview of the respective drive object.

Proceed as follows to remove a Technology Extension from your Startdrive project:

1. Open the "All drive objects" view or the "Technology Extensions that cannot be activated" overview of the desired drive object.
2. Click the "Remove" button in the row of the drive object concerned in the "Uninstall" column.

   The "Remove Technology Extension" dialog opens.
3. Click "Yes" to confirm the uninstallation of the Technology Extension.
4. If the Technology Extension is still activated on drive objects in the project, the "Remove Technology Extension" dialog opens again.  
   All drive objects on which the Technology Extension is still activated are listed.  
   Click "Yes" to uninstall the Technology Extension.

##### Additional information

You can find additional information on the Technology Extensions in the SIOS portal on the Internet.

---

**See also**

[SIOS Technology Extension](https://support.industry.siemens.com/cs/ww/en/ps/13231)

### Control logic

#### Definition

The connections for the control and status words are displayed for the infeed in the "Control logic" screen form. You can edit these connections:

The connections for the control and status words are arranged in groups. The connections of a group can be displayed in the screen form via two drop-down lists on the left and on the right. Connections can be displayed for the following groups:

- Control word sequence control infeed
- Control word faults/alarms
- Status word sequence control infeed
- Status word faults/alarms 1
- Status word faults/alarms 2
- Infeed status word
- Missing enables

An illuminated LED display means that the corresponding bit of the control or status word is set. If the bit value of the control or status word results from the logical connection of several signal sources, the type of the logical connection is displayed by the associated logic symbol.

#### Selecting and connecting control and status words

1. Select the desired group of control and status words in the drop-down list (on the left or right in the screen form).

   The corresponding display and connection fields are displayed on the side of the screen form on which you made the setting in the drop-down list.
2. Interconnect the signal sources for the displayed parameters (for control words) or the bits (for status words and missing enables).

## Diagnostics

This section contains information on the following topics:

- [Missing enables](#missing-enables)
- [Status parameters](#status-parameters)
- [Control/status words](#controlstatus-words)
- [Communication](#communication)

### Missing enables

#### Definition

The infeed does not change to the "Operation" state until all the enables are present. In the "Missing enables" mask, the LEDs in the function view indicate which enables are still missing. An illuminated LED display indicates that the corresponding enable is missing.

The bits of the missing enables ([r0046](SINAMICS%20Parameter%20VECTORMV.md#r0046029-cobo-missing-enable-sig)) are displayed in the mask.

#### Additional parameters

---

### Status parameters

The status parameters with the associated numeric values are displayed in the function view in the "Status parameters" mask:

| Column | Meaning of the instruction |
| --- | --- |
| Number | Number of the parameter. |
| Parameter text | Entire parameter text in long form. |
| Value | Numeric value of the parameter. This numeric value can be changed as follows:   | Symbol | Meaning | | --- | --- | | 1. Click the table cell. 2. Enter the numeric value of the parameter and press the Enter key. Values outside the value range are not accepted and the original value is entered automatically. |  | |
| Unit | Unit of the parameter. |

### Control/status words

This section contains information on the following topics:

- [Displaying control/status words](#displaying-controlstatus-words)
- [Control/Status Words Meaning](#controlstatus-words-meaning)

#### Displaying control/status words

##### Definition

The control and status words are displayed in the function view for diagnostic purposes in the "Control/status words" screen form. The screen form is split into two vertical sections each displaying a group of control and status words via a drop-down list.

The following groups can be displayed:

- Control word sequence control infeed ([r0898](SINAMICS%20Parameter%20VECTORMV.md#r0898012-cobo-control-word-sequence-control))
- Status word sequence control infeed ([r0899](SINAMICS%20Parameter%20VECTORMV.md#r0899015-cobo-status-word-sequence-control))
- Control word faults/alarms ([r2138](SINAMICS%20Parameter%20VECTORMV.md#r2138715-cobo-control-word-faultsalarms))
- Status word faults/alarms 1 ([r2139](SINAMICS%20Parameter%20VECTORMV.md#r2139015-cobo-status-word-faultsalarms-1))
- Status word faults/alarms 2 ([r2135](SINAMICS%20Parameter%20VECTORMV.md#r2135015-cobo-status-word-faultsalarms-2))
- Infeed status word ([r3405](SINAMICS%20Parameter%20ACTIVE%20INFEED%20CONTROLMV.md#r340517-cobo-infeed-status-word))

##### Selecting a group of control and status words

1. Select the desired group of control and status words in one of the three drop-down lists.

   The corresponding display and connection fields are displayed on the side of the screen form on which you made the setting in the drop-down list.

   A highlighted LED display means that the corresponding bit of the control or status word has been set.
2. If you want to display the values of several groups next to one another, set the other desired groups in the other two drop-down lists

##### Function diagrams (FD)

Internal control/status words - control word faults/alarms - 2546 -

Internal control/status words - status word, faults/alarms 1 and 2 - 2548 -

Basic Infeed - control word sequence control infeed - 8720 -

Basic Infeed - status word, sequence control, infeed - 8726 -

FD-8920 (64)

FD-8926 (64)

##### Additional parameters

---

#### Control/Status Words Meaning

Active Infeed control words

| Signal name | Internal control word | Binector input | Internal control word display | PROFIBUS telegram 370 |
| --- | --- | --- | --- | --- |
| ON/OFF1 | STWAE.0 | [p0840](SINAMICS%20Parameter%20VECTORMV.md#p08400n-bi-on-off-off1) ON/OFF2 | [r0898](SINAMICS%20Parameter%20VECTORMV.md#r0898012-cobo-control-word-sequence-control).0 | A_STW1.0 |
| OFF2 | STWAE.1 | [p0844](SINAMICS%20Parameter%20VECTORMV.md#p08440n-bi-no-coast-down-coast-down-off2-signal-source-1) 1 OFF2 and [p0845](SINAMICS%20Parameter%20VECTORMV.md#p08450n-bi-no-coast-down-coast-down-off2-signal-source-2) 2 OFF2 | r0898.1 | A_STW1.1 |
| Operation enable | STWAE.3 | [p0852](SINAMICS%20Parameter%20VECTORMV.md#p08520n-bi-enable-operationinhibit-operation) Enable operation | r0898.3 | A_STW1.3 |
| Control by PLC | STWAE.10 | [p0854](SINAMICS%20Parameter%20VECTORMV.md#p08540n-bi-control-by-plcno-control-by-plc) Control by PLC | r0898.10 | A_STW1.10 |

Active Infeed status message

| Signal name | Internal control word | Parameter | PROFIBUS telegram 370 |
| --- | --- | --- | --- |
| Ready for power-up | ZSWAE.0 | [r0899](SINAMICS%20Parameter%20VECTORMV.md#r0899015-cobo-status-word-sequence-control).0 | A_ZSW1.0 |
| Ready to operate | ZSWAE.1 | r0899.1 | A_ZSW1.1 |
| Operation enabled | ZSWAE.2 | r0899.2 | A_ZSW1.2 |
| Fault active | ZSWAE.3 | [r2139](SINAMICS%20Parameter%20VECTORMV.md#r2139015-cobo-status-word-faultsalarms-1).3 | A_ZSW1.3 |
| No OFF2 active | ZSWAE.4 | r0899.4 | A_ZSW1.4 |
| Power-on inhibit active | ZSWAE.6 | r0899.6 | A_ZSW1.6 |
| Warning present | ZSWAE.7 | r2139.7 | A_ZSW1.7 |
| Controlled by PLC | ZSWAE.9 | r0899.9 | A_ZSW1.9 |
| Pre-charging completed | ZSWAE.11 | r0899.11 | A_ZSW1.11 |
| Line contactor closed feedback | ZSWAE.12 | r0899.12 | A_ZSW1.12 |

##### Additional parameters

---

### Communication

This section contains information on the following topics:

- [Receive direction infeed MV telegrams](#receive-direction-infeed-mv-telegrams)
- [Send direction infeed MV telegrams](#send-direction-infeed-mv-telegrams)
- [PZD send/receive direction diagnostics](#pzd-sendreceive-direction-diagnostics)

#### Receive direction infeed MV telegrams

##### Description

This is where you specify the interconnections of the PROFIdrive telegram in the receive direction for infeeds.

In the telegram configuration (![Description](images/147853831051_DV_resource.Stream@PNG-en-US.png)) you can change the configuration of the telegrams or add telegram extensions.

**Telegram structure**

The interconnections for the process data in the receive direction are created automatically for the standard and manufacturer-specific telegrams.

If you select the Free telegram configuration, you can freely define the interconnections for the process data in the receive direction.

Only those telegrams available for the drive object are offered. The interconnections of the control words or receive words have already been created.

| Symbol | Meaning |
| --- | --- |
| ![Description](images/147853827083_DV_resource.Stream@PNG-en-US.png) | Click the button next to "Interconnections" to interconnect the signal for the connector output. |
| ![Description](images/148104188299_DV_resource.Stream@PNG-en-US.png) | Click the button to display and interconnect the signal bit by bit. |

The following information is displayed by the telegrams shown:

| Telegram type | PZD | Display of the value | Format switchover | Control words | Interconnections |
| --- | --- | --- | --- | --- | --- |
|  | The numbering and arrangement of the process data. | Value of the process data (PZD) | Switch value of the process date to other display (hex, bin, dec). | List of the control words that are transmitted in the telegram. | Display or interconnection of the parameter with which the signal is to be interconnected. Several interconnections are possible. |
| PROFIdrive  370, 371 | X | X | X | X | X |
| Telegram extension | X | X | X | X | X |

##### Function diagrams for SINAMICS MV (FD)

- PROFIdrive - manufacturer-specific/free telegrams and process data (PZD) - 2416 -
- PROFIdrive - PZD receive signals, interconnection - 2439 -
- PROFIdrive - STW1 control word, interconnection - 2442 -
- PROFIdrive - PZD send signals, interconnection - 2449 -
- PROFIdrive - ZSW1 status word, interconnection - 2452 -
- Basic Infeed - control word sequence control infeed - 8720 -
- Basic Infeed - status word, sequence control, infeed - 8726 -
- FD-8920 (64)
- FD-8926 (64)

#### Send direction infeed MV telegrams

##### Description

This is where you specify the parameters of the PROFIdrive telegram in the send direction for infeeds.

In the telegram configuration (![Description](images/147853831051_DV_resource.Stream@PNG-en-US.png)) you can change the configuration of the telegrams or add telegram extensions.

**Telegram structure**

The interconnections for the process data in the send direction are created automatically for the standard and manufacturer-specific telegrams.

If you select the Free telegram configuration, you can freely define the interconnections for the process data in the send direction.

| Symbol | Meaning |
| --- | --- |
| ![Description](images/147853860363_DV_resource.Stream@PNG-en-US.png) | Click the button to the left of "Interconnections" to interconnect the signal for the connector input. |

The following information is displayed by the telegrams shown:

| Telegram type | Interconnections | Status words | Value | Format switchover | PZD |
| --- | --- | --- | --- | --- | --- |
|  | Display or interconnection of the parameter with which the signal is to be interconnected or is interconnected. | List of the status words that are transmitted in the telegram. | Value of the process data (PZD) | Switch value of the process date to other display (hex, bin, dec). | Numbering and arrangement of the process data. |
| PROFIdrive  370, 371 | X | X | X | X | X |
| Telegram extension | X | X | X | X | X |

##### Function diagrams for SINAMICS MV (FD)

- PROFIdrive - manufacturer-specific/free telegrams and process data (PZD) - 2416 -
- PROFIdrive - PZD receive signals, interconnection - 2439 -
- PROFIdrive - STW1 control word, interconnection - 2442 -
- PROFIdrive - PZD send signals, interconnection - 2449 -
- PROFIdrive - ZSW1 status word, interconnection - 2452 -
- Basic Infeed - control word sequence control infeed - 8720 -
- Basic Infeed - status word, sequence control, infeed - 8726 -
- FD-8920 (64)
- FD-8926 (64)

#### PZD send/receive direction diagnostics

##### Description

You can display a diagnosis of the status or control words of the selected telegram here.

##### Function diagrams for SINAMICS MV (FD)

- PROFIdrive - manufacturer-specific/free telegrams and process data (PZD) - 2416 -
- PROFIdrive - PZD receive signals, interconnection - 2439 -
- PROFIdrive - STW1 control word, interconnection - 2442 -
- PROFIdrive - PZD send signals, interconnection - 2449 -
- PROFIdrive - ZSW1 status word, interconnection - 2452 -
- Basic Infeed - control word sequence control infeed - 8720 -
- Basic Infeed - status word, sequence control, infeed - 8726 -
- FD-8920 (64)
- FD-8926 (64)

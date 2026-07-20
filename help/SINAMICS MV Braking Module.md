---
title: "SINAMICS MV Braking Module"
package: Stdr035000UIenUS
topics: 13
source: Siemens TIA Portal Information System (offline help, en-US)
---


# SINAMICS MV Braking Module

This section contains information on the following topics:

- [Parameterization](#parameterization)
- [Diagnostics](#diagnostics)

## Parameterization

This section contains information on the following topics:

- [Basic parameter assignment](#basic-parameter-assignment)
- [Technology Extensions](#technology-extensions)

### Basic parameter assignment

This section contains information on the following topics:

- ["Braking Module" function module](#braking-module-function-module)

#### "Braking Module" function module

You can connect the "Free function blocks" function module for the Braking Module used.

> **Note**
>
> You can only activate or deactivate function modules offline.

##### Activating a function module

1. Activate the "Free function blocks" function module by clicking the option.
2. Save the project to save the settings.

##### Additional parameters

---

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

## Diagnostics

This section contains information on the following topics:

- [Missing enables](#missing-enables)
- [Control/status words](#controlstatus-words)
- [Status parameters](#status-parameters)
- [Communication](#communication)

### Missing enables

#### Description

The Braking Modules does not change to the "Operation" state until all enables are present. In the "Missing enables" screen form, the LEDs in the function view indicate which enables are still missing. An illuminated LED display indicates that the corresponding enable is missing.

The bits of the missing enables ([r0046](SINAMICS%20Parameter%20VECTORMV.md#r0046029-cobo-missing-enable-sig)) are displayed in the screen form.

#### Additional parameters

---

### Control/status words

#### Description

The control and status words are displayed in the function view for diagnostic purposes in the "Control/status words" screen form. The screen form is split into two vertical sections each displaying a group of control and status words via a drop-down list.

The following groups can be displayed:

- Control word faults/alarms (r2138)
- Status word faults/alarms 1 (r2139)
- Status word faults/alarms 2 (r2135)

#### Selecting a group of control and status words

1. In one of the two drop-down lists, select the required group of control and status words.

   The corresponding display and interconnection fields are displayed on the side of the screen form on which you made the setting in the drop-down list.

   A highlighted LED display means that the corresponding bit of the control or status word has been set.
2. If you want to display the values of several groups next to one another, set the other desired groups in the other two drop-down lists.

### Status parameters

This dialog displays the values of important parameters, which characterize the operating state of the converter.

The displayed parameters depend on the selected drive object.

More detailed information about the parameters can be found in the following sources:

- Help for the respective parameter
- SINAMICS S120/S150 List Manual

### Communication

This section contains information on the following topics:

- [Receive direction telegram Braking Module MV](#receive-direction-telegram-braking-module-mv)
- [Send direction telegram Braking Module MV](#send-direction-telegram-braking-module-mv)

#### Receive direction telegram Braking Module MV

##### Description

This is where you specify the interconnections of the PROFIdrive telegram in the receive direction for Braking Modules.

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
| PROFIdrive | X | X | X | X | X |
| Telegram extension | X | X | X | X | X |

#### Send direction telegram Braking Module MV

##### Description

This is where you specify the parameters of the PROFIdrive telegram in the send direction for Braking Modules.

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
| PROFIdrive | X | X | X | X | X |
| Telegram extension | X | X | X | X | X |

---
title: "SINAMICS MV Control Units"
package: Stdr007000UIenUS
topics: 21
source: Siemens TIA Portal Information System (offline help, en-US)
---


# SINAMICS MV Control Units

This section contains information on the following topics:

- [CU MV overview](#cu-mv-overview)
- [CU MV interface overview](#cu-mv-interface-overview)
- [CU MV connection example](#cu-mv-connection-example)
- [Parameterization](#parameterization)
- [Diagnostics](#diagnostics)

## CU MV overview

### Control Units

The communication, open-loop control and closed-loop control functions for Motor Modules and Line Modules are performed in the Control Unit, whereby the Control Units are always dimensioned for the operation of multi-motor drives.

The number of controllable Motor Modules and/or Line Modules depends on the required performance including the operating mode and additional functions.

The desired functionality (e.g. current controller, speed controller, number of drives, etc.) can be found in the SW library and the performance requirement for the Control Unit determined. The functionality is defined via the basic parameter assignment.

## CU MV interface overview

![Interface overview CU320-2 PN (without cover and blanking cover)   Interface descriptionsControl Unit CU320-2 PN](images/148046885259_DV_resource.Stream@PNG-en-US.png)

Interface overview CU320-2 PN (without cover and blanking cover)

![Interface X140 and measuring socket - CU320-2 PN (view from below)](images/148046874123_DV_resource.Stream@PNG-en-US.png)

Interface X140 and measuring socket - CU320-2 PN (view from below)

![Mounting a PC board connector (Phoenix Contact) in the measuring socket](images/148046909195_DV_resource.Stream@PNG-en-US.png)

Mounting a PC board connector (Phoenix Contact) in the measuring socket

## CU MV connection example

![Connection example of a Control Unit CU320-2 PN](images/148046963083_DV_resource.Stream@PNG-en-US.png)

Connection example of a Control Unit CU320-2 PN

## Parameterization

This section contains information on the following topics:

- [Basic parameterization](#basic-parameterization)
- [Technology functions](#technology-functions)
- [Inputs/outputs](#inputsoutputs)
- [Control logic](#control-logic)

### Basic parameterization

This section contains information on the following topics:

- [Function modules (Control Unit)](#function-modules-control-unit)
- [Web server MV](#web-server-mv)

#### Function modules (Control Unit)

You can connect the "Free function blocks" function module for the Control Unit used.

> **Note**
>
> You can only activate or deactivate function modules offline.

##### Activating a function module

1. Activate the "Free function blocks" function module by clicking the option.
2. Save the project to save the settings.

##### Additional parameters

---

#### Web server MV

##### Overview

The web server provides information about a SINAMICS device on its web pages. Access is made with an Internet browser.

The web server is configured in a screen form. In general, you can perform the configuration in both online mode and in offline mode of Startdrive.

> **Note**
>
> **Exception: Only in online mode**
>
> The web server password can only be modified or deleted in the online mode.

##### Calling the screen form

1. Select the "Drive control &gt; Parameterization" menu in the project tree.

   The associated details view is displayed on the right-hand side.
2. Call the "Basic parameterization &gt; Web server" menu in the secondary navigation.

   The details view is refreshed. The settings for the web server become active.

##### Disabling the web server

The web server is enabled by default in the configuration. If necessary, the web server can be disabled as follows:

1. Deactivate the option "Activate the web server on this device" in the configuration dialog.
2. Save the project to apply the changes.

##### Restricting web server access to a secure connection

The standard configuration of the web server allows you to access the SINAMICS converter via an HTTP connection and via an encrypted HTTPS connection. The configuration can be changed to allow access only via a secure HTTPS connection.

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Use of non-encrypted connections (HTTP)**  HTTP also supports the transfer of unencrypted login data. This simplifies, for example, damage by third-parties for password stealing attacks with data manipulation.   - To transfer all data encrypted, restrict access to secure connections. |  |

**Procedure:**

Restriction of the connection to HTTPS is possible only when the web server is activated:

1. In the configuration dialog, activate the option "Only permit secure access to the service interface [X127] via HTTPS protocol".
2. If you wish to work with a PROFINET interface, also activate the option "Activate access via the PROFINET interface [X150]. This is only possible as secure HTTPS connection".

##### Setting or changing user accounts

The rights of both user accounts - "SINAMICS" and "Administrator" - are permanently defined, and cannot be changed by users.

The "Administrator" user has full access rights by default. However, only restricted access rights apply for the standard "SINAMICS" user.

For the web server user accounts, you can make the following settings in Startdrive:

- Enable or disable the "SINAMICS" or "Administrator" user
- Create the password of the "SINAMICS" or "Administrator" user
- Change the password of the "SINAMICS" or "Administrator" user
- Delete the password of the "SINAMICS" user

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
> By issuing a message ![Setting or changing user accounts](images/147853400715_DV_resource.Stream@PNG-en-US.PNG), Startdrive recommends that the web server passwords are encrypted using the project protection function ("Security settings").
>
> - Activate the project protection for user administration in the TIA Portal so that all parameters and passwords within the project are encrypted.   
>   This also applies to passwords for the web server users "SINAMICS" and "Administrator".
>
> Detailed information on project protection can be found in the online help under the heading of "User management (UMAC)".

##### Creating a password for the "SINAMICS" user

You can create a password for the "SINAMICS" user as follows:

1. Activate the "Enable SINAMICS user" option if it has not yet been activated.
2. Click the "Specify password" button.

   The "Specify password" dialog opens.
3. Enter the new password in the "New password" input field. Note that these entries are case-sensitive.
4. Enter the same password in the "Confirm password" field.

   For security reasons, the password inputs in the input fields are shown encrypted.
5. Click "OK" to confirm the input in the password dialog.

   If the two password inputs were identical, the input dialog closes. If the two inputs do not match, the input dialog remains open and an error message appears. The two inputs in the input dialog are also cleared. In this case, you must reenter the password in the two input fields.

   A prompt is made once for the password when the web site is called later.
6. Save the project to apply the changes.

##### Creating a password for the "Administrator" user

A password is also required to enable the "Administrator" user. For this reason, the procedure for enabling is slightly different than for the "SINAMICS" user:

1. Click on "Specify password for the activation".

   The "Specify password" dialog opens.
2. Enter the new password in the "New password" input field. Note that these entries are case-sensitive.
3. Enter the same password in the "Confirm password" field.

   For security reasons, the password inputs in the input fields are shown encrypted.
4. Click "OK" to confirm the input in the password dialog.

   If the two password inputs were identical, the input dialog closes. If the two inputs do not match, the input dialog remains open and an error message appears. The two inputs in the input dialog are also cleared. In this case, you must reenter the password in the two input fields. Once the password for the administrator has been assigned, this user also will be enabled automatically. The "Enable Administrator user" option is activated.

   A prompt is made once for the password when the web site is called later.
5. Save the project to apply the changes.

##### Deleting the password of the "SINAMICS" user

In online mode, you can delete the "SINAMICS" user password as follows:

1. Click the "Delete password" button.

   The password is deleted, and the message "The password has been deleted" is displayed.
2. Save the project to apply the changes.

> **Note**
>
> The user "Administrator" mandatorily requires a password. If this user is to remain authorized for the web server, a new password must be created after deletion.

##### Changing an existing password

Existing passwords for "SINAMICS" and "Administrator" users can be changed in the online mode as long as the user in question is enabled.

1. Click the "Change password" button.

   The "Change password" dialog box opens.
2. Enter the new password in the "New password" input field. Note that these entries are case-sensitive.
3. Enter the same password in the "Confirm password" field.

   For security reasons, the password inputs in the input fields are shown encrypted.

   The entry is checked. If all entries were correct, the message "Password has been changed" will appear.
4. Save the project to apply the changes.

### Technology functions

This section contains information on the following topics:

- [Technology Extensions](#technology-extensions)

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

### Inputs/outputs

This section contains information on the following topics:

- [CU MV digital inputs](#cu-mv-digital-inputs)
- [CU MV bidirectional digital inputs/outputs](#cu-mv-bidirectional-digital-inputsoutputs)
- [CU MV measuring sockets](#cu-mv-measuring-sockets)

#### CU MV digital inputs

##### Description

Change the interconnection of the digital inputs 0 ... 7, 16, 17 and 20, 21 to the CU320-2 closed-loop control module.

- Digital inputs are used for the acquisition of digital signals. For example, drive enables can be controlled externally. The interconnection of digital inputs is made by means of BICO technology.
- For every digital input signal there is the corresponding inverted signal which can also be used for interconnection.

##### Simulation mode

The selection box for the terminal evaluation / simulation switchover is only visible online.

##### Interconnect digital inputs 0…7, 16, 17 and 20, 21 ([r0722](SINAMICS%20Parameter%20SINAMICS%20MV.md#r0722021-cobo-cu-digital-inputs-status) and [r0723](SINAMICS%20Parameter%20SINAMICS%20MV.md#r0723021-cobo-cu-digital-inputs-status-inverted))

- Select the parameters with which the signals and the inverted signals of the digital inputs 0 ... 7, 16 ,17 and 20, 21 should be interconnected.

  Several interconnections are possible.

##### Function diagrams (FD)

- CU320-2 input/output terminals - overview - 2119 -
- CU320-2 input/output terminals - electrically isolated digital inputs (DI 0 ... DI 3, DI 16, DI 17) - 2120 -
- CU320-2 input/output terminals - electrically isolated digital inputs (DI 4 ... DI 7, DI 20, DI 21) - 2121 -
- CU320-2 input/output terminals - digital inputs/outputs bidirect. (DI/DO 8 ... DI/DO 9) - 2130 -
- CU320-2 input/output terminals - digital inputs/outputs bidirect. (DI/DO 10 ... DI/DO 11) - 2131 -
- CU320-2 input/output terminals - digital inputs/outputs bidirect. (DI/DO 12 ... DI/DO 13) - 2132 -
- CU320-2 input/output terminals - digital inputs/outputs bidirect. (DI/DO 14 ... DI/DO 15) - 2133 -

##### Additional parameters

---

---

**See also**

[TM31 Inputs/Outputs](TM31%20Terminal%20Module%20%28stdrui200000enUS%29.md#tm31-inputsoutputs)

#### CU MV bidirectional digital inputs/outputs

##### Description

Here you can change the interconnection of the bidirectional digital inputs/outputs on the input/output component.

- You can assign bidirectional digital inputs/outputs in the function. This means they can be parameterized either as an input or an output.
- Digital inputs are used for the acquisition of digital signals. For example, drive enables can be controlled externally. The interconnection of digital inputs is made by means of BICO technology.
- For every digital input signal there is the corresponding inverted signal which can also be used for interconnection.
- Digital outputs are used for the feedback of signals such as enables. The interconnection is made by means of BICO technology.

##### Optimize view

Click Optimize view to reduce the displayed information to the essential parts. Changing the function of one of the bidirectional digital inputs/outputs is not possible in the optimized view. Interconnections can be made in any view.

**Simulation mode**

The selection box for the terminal evaluation/simulation switchover is only visible online.

##### Digital inputs 8…15 and digital outputs 8…15

Each of the bidirectional digital inputs/outputs can be parameterized as an input or output using the change-over switch.

**If digital inputs 8…15 are parameterized ... ([r0722](SINAMICS%20Parameter%20SINAMICS%20MV.md#r0722021-cobo-cu-digital-inputs-status) and [r0723](SINAMICS%20Parameter%20SINAMICS%20MV.md#r0723021-cobo-cu-digital-inputs-status-inverted))**

![Digital inputs 8…15 and digital outputs 8…15](images/148047093643_DV_resource.Stream@PNG-en-US.png)

- Select the parameters with which the signals and the inverted signals of the digital inputs 8...15 should be interconnected.

  Several interconnections are possible.

**If digital outputs 8…15 are parameterized ... ([r0723](SINAMICS%20Parameter%20SINAMICS%20MV.md#r0723021-cobo-cu-digital-inputs-status-inverted))**

![Digital inputs 8…15 and digital outputs 8…15](images/148047097611_DV_resource.Stream@PNG-en-US.png)

- Select the parameters with which the signals of the digital outputs 8...15 should be interconnected.

  In addition, you can invert the outputs.

##### Function diagrams (FD)

- CU320-2 input/output terminals - overview - 2119 -
- CU320-2 input/output terminals - electrically isolated digital inputs (DI 0 ... DI 3, DI 16, DI 17) - 2120 -
- CU320-2 input/output terminals - electrically isolated digital inputs (DI 4 ... DI 7, DI 20, DI 21) - 2121 -
- CU320-2 input/output terminals - digital inputs/outputs bidirect. (DI/DO 8 ... DI/DO 9) - 2130 -
- CU320-2 input/output terminals - digital inputs/outputs bidirect. (DI/DO 10 ... DI/DO 11) - 2131 -
- CU320-2 input/output terminals - digital inputs/outputs bidirect. (DI/DO 12 ... DI/DO 13) - 2132 -
- CU320-2 input/output terminals - digital inputs/outputs bidirect. (DI/DO 14 ... DI/DO 15) - 2133 -

##### Additional parameters

---

---

**See also**

[TM31 Inputs/Outputs](TM31%20Terminal%20Module%20%28stdrui200000enUS%29.md#tm31-inputsoutputs)

#### CU MV measuring sockets

##### Output signals

The measuring sockets output the analog signals. Any freely interconnectable signal can be output at any measuring socket. A measuring socket can be used, for example, to output the actual speed value ([r0063](SINAMICS%20Parameter%20VECTORMV.md#r006302-co-speed-actual-value)) to a measuring instrument connected to the measuring socket.

> **Note**
>
> **Only for commissioning and service**
>
> The measuring sockets should be used only for commissioning and service purposes. The measurements may be performed only by appropriately trained skilled personnel.

##### Select signal source for T0, T1 and T2

- Select the signal source whose signal is to be output via the measuring socket. Important signals, are, for example, speed setpoint before the speed setpoint filter ([r0060](SINAMICS%20Parameter%20VECTORMV.md#r0060-co-speed-setpoint-before-the-setpoint-filter)) or actual speed value (r0063).

##### Define characteristic curve

The scaling specifies the processing of the measured signal. This requires the definition of a straight line with two points.

- Define the output option of the measuring socket via the (linear) characteristic curve. Select individual values within their defined limits, which are displayed in the relevant tooltips.

  - Value X1 ([p0777](SINAMICS%20Parameter%20SINAMICS%20MV.md#p077702-test-socket-characteristic-value-x1))
  - Value X2 ([p0779](SINAMICS%20Parameter%20SINAMICS%20MV.md#p077902-test-socket-characteristic-value-x2))
  - Value Y1 ([p0778](SINAMICS%20Parameter%20SINAMICS%20MV.md#p077802-test-socket-characteristic-value-y1))
  - Value Y2 ([p0780](SINAMICS%20Parameter%20SINAMICS%20MV.md#p078002-test-socket-characteristic-value-y2))

  Example: x1/y1 = 0%/2.49 V x2/y2 = 100%/4.98 V

  - 0.0% is mapped to 2.49 V
  - 100.0% is mapped to 4.98 V
  - -100.0% is mapped to 0.00 V

##### Define the offset ([p0783](SINAMICS%20Parameter%20SINAMICS%20MV.md#p078302-test-sockets-offset))

- Enter an offset.

  The offset is applied additively to the signal to be output. The signal to be output can thus be displayed within the measuring range.

##### Activate/deactivate limiting ([p0784](SINAMICS%20Parameter%20SINAMICS%20MV.md#p078402-test-socket-limit-onoff))

- Select whether the output value of the measuring socket is to be restricted to the limit values of the characteristic curve.

##### Function diagrams (FD)

- Diagnostics - measuring sockets (T0, T1, T2) - 8134 -

##### Additional parameters

---

### Control logic

#### Definition

The connections for the control and status words are displayed for the control unit in the "Control logic" screen form. You can edit these connections:

The connections for the control and status words are arranged in groups. The connections of a group can be displayed in the screen form via two drop-down lists on the left and on the right. Connections can be displayed for the following groups:

- Control word faults/alarms
- Status word faults/alarms

An illuminated LED display means that the corresponding bit of the control or status word is set. If the bit value of the control or status word results from the logical connection of several signal sources, the type of the logical connection is displayed by the associated logic symbol.

#### Selecting and connecting control and status words

1. Select the desired group of control and status words in the drop-down list (on the left or right in the screen form).

   The corresponding display and connection fields are displayed on the side of the screen form on which you made the setting in the drop-down list.
2. Interconnect the signal sources for the displayed parameters (for control words) or the bits (for status words and missing enables).

#### Function diagrams (FD)

FD-2501 (54)

FD-2503 (54)

FD-2520 (54)

FD-2522 (54)

FD-2530 (54)

Internal control/status words - control word faults/alarms - 2546 -

#### Additional parameters

- [p0840](SINAMICS%20Parameter%20VECTORMV.md#p08400n-bi-on-off-off1)
- [p0844](SINAMICS%20Parameter%20VECTORMV.md#p08440n-bi-no-coast-down-coast-down-off2-signal-source-1)
- [p0845](SINAMICS%20Parameter%20VECTORMV.md#p08450n-bi-no-coast-down-coast-down-off2-signal-source-2)
- [p0852](SINAMICS%20Parameter%20VECTORMV.md#p08520n-bi-enable-operationinhibit-operation)
- p3532
- p3533
- [p0854](SINAMICS%20Parameter%20VECTORMV.md#p08540n-bi-control-by-plcno-control-by-plc)
- [p2103](SINAMICS%20Parameter%20VECTORMV.md#p21030n-bi-1st-acknowledge-faults)
- [p2104](SINAMICS%20Parameter%20VECTORMV.md#p21040n-bi-2nd-acknowledge-faults)
- [p2105](SINAMICS%20Parameter%20VECTORMV.md#p21050n-bi-3rd-acknowledge-faults)
- [p2112](SINAMICS%20Parameter%20VECTORMV.md#p21120n-bi-external-alarm-1)
- [p2116](SINAMICS%20Parameter%20VECTORMV.md#p21160n-bi-external-alarm-2)
- [p2117](SINAMICS%20Parameter%20VECTORMV.md#p21170n-bi-external-alarm-3)
- [p2106](SINAMICS%20Parameter%20VECTORMV.md#p21060n-bi-external-fault-1)
- [p2107](SINAMICS%20Parameter%20VECTORMV.md#p21070n-bi-external-fault-2)
- [p2108](SINAMICS%20Parameter%20VECTORMV.md#p21080n-bi-external-fault-3)
- [r0899](SINAMICS%20Parameter%20VECTORMV.md#r0899015-cobo-status-word-sequence-control) (various bits)
- [r2139](SINAMICS%20Parameter%20VECTORMV.md#r2139015-cobo-status-word-faultsalarms-1) (various bits)
- [r0046](SINAMICS%20Parameter%20VECTORMV.md#r0046029-cobo-missing-enable-sig) (various bits)

---

## Diagnostics

This section contains information on the following topics:

- [Communication](#communication)

### Communication

This section contains information on the following topics:

- [Receive direction Control Unit MV telegrams](#receive-direction-control-unit-mv-telegrams)
- [Send direction Control Unit MV telegrams](#send-direction-control-unit-mv-telegrams)
- [CU MV PZD send/receive direction diagnostics](#cu-mv-pzd-sendreceive-direction-diagnostics)

#### Receive direction Control Unit MV telegrams

##### Description

This is where you specify the interconnections of the PROFIdrive telegram in the receive direction for the Control Unit.

In the telegram configuration (![Description](images/147853831051_DV_resource.Stream@PNG-en-US.png)) you can change the configuration of the telegrams or add telegram extensions.

**Telegram structure**

The interconnections for the process data in the receive direction are created automatically for the standard and manufacturer-specific telegrams.

If you select the Free telegram configuration, you can freely define the interconnections for the process data in the receive direction.

Only those telegrams available for the drive object are offered. The interconnections of the control words or receive words have already been created.

| Symbol | Meaning |
| --- | --- |
| ![Description](images/147853827083_DV_resource.Stream@PNG-en-US.png) | Click the button next to "Interconnections" to interconnect the signal for the connector output. |
| ![Description](images/148047146763_DV_resource.Stream@PNG-en-US.png) | Click the button to display and interconnect the signal bit by bit. |

The following information is displayed by the telegrams shown:

| Telegram type | PZD | Display of the value | Format switchover | Control words | Interconnections |
| --- | --- | --- | --- | --- | --- |
|  | The numbering and arrangement of the process data. | Value of the process data (PZD) | Switch value of the process date to other display (hex, bin, dec). | List of the control words that are transmitted in the telegram. | Display or interconnection of the parameter with which the signal is to be interconnected. Several interconnections are possible. |
| PROFIdrive  390, 301, 392, 393, 394, 395 | X | X | X | X | X |
| Telegram extension | X | X | X | X | X |

##### Function diagrams for SINAMICS MV (FD)

- PROFIdrive - PROFIBUS (PB) / PROFINET (PN), addresses and diagnostics - 2410 -
- PROFIdrive - standard telegrams and process data (PZD) - 2415 -
- PROFIdrive - manufacturer-specific/free telegrams and process data (PZD) - 2416 -
- PROFIdrive - PZD receive signals, interconnection - 2439 -
- PROFIdrive - STW1 control word, interconnection - 2442 -
- PROFIdrive - I_STW1 control word, infeed interconnection - 2447 -
- PROFIdrive - PZD send signals, interconnection - 2449 -
- PROFIdrive - ZSW1 status word, interconnection - 2452 -
- PROFIdrive - I_ZSW1 status word, infeed interconnection - 2457 -
- PROFIdrive - IF1 receive telegram, free interconnection via BICO (p0922 = 999) - 2468 -
- PROFIdrive - IF1 send telegram, free interconnection via BICO (p0922 = 999) - 2470 -
- PROFIdrive - IF1 status words, free interconnection - 2472 -
- PROFIdrive - IF1 receive telegram, free interconnection via BICO (p0922 = 999) - 2481 -
- PROFIdrive - IF1 send telegram, free interconnection via BICO (p0922 = 999) - 2483 -
- PROFIdrive - IF2 receive telegram, free interconnection via BICO (p0922 = 999) - 2485 -
- PROFIdrive - IF2 send telegram, free interconnection via BICO (p0922 = 999) - 2487 -
- PROFIdrive - IF2 status words, free interconnection - 2489 -
- PROFIdrive - IF2 receive telegram, free interconnection via BICO (p0922 = 999) - 2491 -
- PROFIdrive - IF2 send telegram, free interconnection via BICO (p0922 = 999) - 2493 -
- PROFIdrive - CU_STW1 control word 1, Control Unit interconnection - 2495 -
- PROFIdrive - CU_ZSW1 status word 1 Control Unit interconnection - 2496 -
- PROFIdrive - O_DIGITAL interconnection - 2497 -
- PROFIdrive - I_DIGITAL interconnection - 2498 -
- Internal control/status words - control word, sequence control - 2501 -

#### Send direction Control Unit MV telegrams

##### Description

This is where you specify the parameters of the PROFIdrive telegram in the send direction for the Control Unit.

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
| PROFIdrive  390, 301, 392, 393, 394, 395 | X | X | X | X | X |
| Telegram extension | X | X | X | X | X |

##### Function diagrams for SINAMICS MV (FD)

- PROFIdrive - PROFIBUS (PB) / PROFINET (PN), addresses and diagnostics - 2410 -
- PROFIdrive - standard telegrams and process data (PZD) - 2415 -
- PROFIdrive - manufacturer-specific/free telegrams and process data (PZD) - 2416 -
- PROFIdrive - PZD receive signals, interconnection - 2439 -
- PROFIdrive - STW1 control word, interconnection - 2442 -
- PROFIdrive - I_STW1 control word, infeed interconnection - 2447 -
- PROFIdrive - PZD send signals, interconnection - 2449 -
- PROFIdrive - ZSW1 status word, interconnection - 2452 -
- PROFIdrive - I_ZSW1 status word, infeed interconnection - 2457 -
- PROFIdrive - IF1 receive telegram, free interconnection via BICO (p0922 = 999) - 2468 -
- PROFIdrive - IF1 send telegram, free interconnection via BICO (p0922 = 999) - 2470 -
- PROFIdrive - IF1 status words, free interconnection - 2472 -
- PROFIdrive - IF1 receive telegram, free interconnection via BICO (p0922 = 999) - 2481 -
- PROFIdrive - IF1 send telegram, free interconnection via BICO (p0922 = 999) - 2483 -
- PROFIdrive - IF2 receive telegram, free interconnection via BICO (p0922 = 999) - 2485 -
- PROFIdrive - IF2 send telegram, free interconnection via BICO (p0922 = 999) - 2487 -
- PROFIdrive - IF2 status words, free interconnection - 2489 -
- PROFIdrive - IF2 receive telegram, free interconnection via BICO (p0922 = 999) - 2491 -
- PROFIdrive - IF2 send telegram, free interconnection via BICO (p0922 = 999) - 2493 -
- PROFIdrive - CU_STW1 control word 1, Control Unit interconnection - 2495 -
- PROFIdrive - CU_ZSW1 status word 1 Control Unit interconnection - 2496 -
- PROFIdrive - O_DIGITAL interconnection - 2497 -
- PROFIdrive - I_DIGITAL interconnection - 2498 -
- Internal control/status words - control word, sequence control - 2501 -

#### CU MV PZD send/receive direction diagnostics

##### Description

You can display a diagnosis of the status or control words of the selected telegram here.

##### Function diagrams (FD)

- PROFIdrive - PROFIBUS (PB) / PROFINET (PN), addresses and diagnostics - 2410 -
- PROFIdrive - standard telegrams and process data (PZD) - 2415 -
- PROFIdrive - manufacturer-specific/free telegrams and process data (PZD) - 2416 -
- PROFIdrive - PZD receive signals, interconnection - 2439 -
- PROFIdrive - STW1 control word, interconnection - 2442 -
- PROFIdrive - I_STW1 control word, infeed interconnection - 2447 -
- PROFIdrive - PZD send signals, interconnection - 2449 -
- PROFIdrive - ZSW1 status word, interconnection - 2452 -
- PROFIdrive - I_ZSW1 status word, infeed interconnection - 2457 -
- PROFIdrive - IF1 receive telegram, free interconnection via BICO (p0922 = 999) - 2468 -
- PROFIdrive - IF1 send telegram, free interconnection via BICO (p0922 = 999) - 2470 -
- PROFIdrive - IF1 status words, free interconnection - 2472 -
- PROFIdrive - IF1 receive telegram, free interconnection via BICO (p0922 = 999) - 2481 -
- PROFIdrive - IF1 send telegram, free interconnection via BICO (p0922 = 999) - 2483 -
- PROFIdrive - IF2 receive telegram, free interconnection via BICO (p0922 = 999) - 2485 -
- PROFIdrive - IF2 send telegram, free interconnection via BICO (p0922 = 999) - 2487 -
- PROFIdrive - IF2 status words, free interconnection - 2489 -
- PROFIdrive - IF2 receive telegram, free interconnection via BICO (p0922 = 999) - 2491 -
- PROFIdrive - IF2 send telegram, free interconnection via BICO (p0922 = 999) - 2493 -
- PROFIdrive - CU_STW1 control word 1, Control Unit interconnection - 2495 -
- PROFIdrive - CU_ZSW1 status word 1 Control Unit interconnection - 2496 -
- PROFIdrive - O_DIGITAL interconnection - 2497 -
- PROFIdrive - I_DIGITAL interconnection - 2498 -
- Internal control/status words - control word, sequence control - 2501 -

---
title: "SINAMICS S/G Control Units"
package: Stdr001000UIenUS
topics: 29
source: Siemens TIA Portal Information System (offline help, en-US)
---


# SINAMICS S/G Control Units

This section contains information on the following topics:

- [Overview](#overview)
- [Interface overview](#interface-overview)
- [Connection example](#connection-example)
- [Parameterization](#parameterization)
- [Diagnostics](#diagnostics)

## Overview

### Control Units

The communication, open-loop control and closed-loop control functions for Motor Modules and Line Modules are performed in the Control Unit, whereby the Control Units are always dimensioned for the operation of multi-motor drives.

The number of controllable Motor Modules and/or Line Modules depends on the required performance including the operating mode and additional functions.

The desired functionality (e.g. current controller, speed controller, number of drives, etc.) can be found in the SW library and the performance requirement for the Control Unit determined. The functionality is defined via the basic parameter assignment.

## Interface overview

![Interface overview CU320-2 PN (without cover and blanking cover)   Interface descriptionsControl Unit CU320-2 PN](images/147853299595_DV_resource.Stream@PNG-en-US.png)

Interface overview CU320-2 PN (without cover and blanking cover)

![Interface X140 and measuring socket - CU320-2 PN (view from below)](images/147853288459_DV_resource.Stream@PNG-en-US.png)

Interface X140 and measuring socket - CU320-2 PN (view from below)

![Mounting a PC board connector (Phoenix Contact) in the measuring socket](images/147853310731_DV_resource.Stream@PNG-en-US.png)

Mounting a PC board connector (Phoenix Contact) in the measuring socket

## Connection example

![Connection example of a Control Unit CU320-2 PN](images/147853336459_DV_resource.Stream@PNG-en-US.png)

Connection example of a Control Unit CU320-2 PN

## Parameterization

This section contains information on the following topics:

- [Basic parameterization](#basic-parameterization)
- [Technology Extensions](#technology-extensions)
- [Inputs/outputs](#inputsoutputs)
- [Control logic](#control-logic)

### Basic parameterization

This section contains information on the following topics:

- [Control Unit](#control-unit)
- [Web server](#web-server)
- [Write and know-how protection (CU310-2/CU320-2)](#write-and-know-how-protection-cu310-2cu320-2)

#### Control Unit

You can connect the "Free function blocks" function module for the Control Unit used.

> **Note**
>
> You can only activate or deactivate function modules offline.

##### Activating a function module

1. Activate the "Free function blocks" function module by clicking the option.
2. Save the project to save the settings.

##### Additional parameters

---

#### Web server

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

   This option cannot be activated for a CU3x0 DP because this Control Unit has a PROFIBUS interface instead of a PROFINET interface.

##### Setting or changing user accounts

The rights of both user accounts - "SINAMICS" and "Administrator" - are permanently defined, and cannot be changed by users.

The "Administrator" user has full access rights by default. However, only restricted access rights apply for the standard "SINAMICS" user.

For the web server user accounts, you can make the following settings in Startdrive:

- Enable or disable the "SINAMICS" or "Administrator" user
- Create the password of the "SINAMICS" or "Administrator" user
- Change the password of a "SINAMICS" or "Administrator" user (only possible in the online mode)
- Delete the password of a "SINAMICS" user (only possible in the online mode)

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

#### Write and know-how protection (CU310-2/CU320-2)

This section contains information on the following topics:

- [Write protection](#write-protection)
- [Know-how protection (KHP)](#know-how-protection-khp)
- [Exception parameters for write protection and know-how protection](#exception-parameters-for-write-protection-and-know-how-protection)

##### Write protection

###### Description

Write protection prevents unintentional as well as inadvertent changes to the drive settings. It can be activated both in the online and offline modes, but is only active in online mode.

###### Requirement

- SINAMICS drive with Control Unit CU310-2 or CU320-2

###### Exceptions to write protection

Some functions are excluded from write protection, e.g.:

- Activating/deactivating write protection
- Changing the access level ([p0003](SINAMICS%20Parameter%20CU.md#p0003-bop-access-level))
- Saving parameters ([p0971](SINAMICS%20Parameter%20CU.md#p0971-save-drive-object-parameters))
- Safe removal of the memory card (p9400)
- Restoring factory settings
- Transferring the settings from an external data backup, e.g. upload into the drive unit from a memory card.

Parameters with attribute "[WRITE_NO_LOCK](#exception-parameters-for-write-protection-and-know-how-protection)" are not write protected.

###### Activating/deactivating write protection

1. Select the "Drive control &gt; Parameters" menu in the project tree.
2. In the secondary navigation, select menu "Basic parameterization &gt; Write and know-how protection".
3. Click on "Activate write protection"

   Write protection is activated. The button labeling has been changed.

   To deactivate write protection, click on "Deactivate write protection".
4. If you enabled write protection in offline mode:  
   Perform a download to transfer the changed settings to the drive.

###### Additional parameters

---

- [r7760](SINAMICS%20Parameter%20CU.md#r7760012-cobo-write-protectionknow-how-protection-status)

##### Know-how protection (KHP)

This section contains information on the following topics:

- [Overview](#overview-1)
- [Maintaining and updating the exception list](#maintaining-and-updating-the-exception-list)
- [Configuring know-how protection](#configuring-know-how-protection)

###### Overview

###### Description

The "Know-how protection" (KHP) in Startdrive is a function to prevent or make it harder to read out a Startdrive project or make unintentional or inadvertent changes to the configuration and parameter assignment of a Startdrive project.

> **Note**
>
> **Know-how protection when write protection is active**
>
> When write protection is enabled, the protection settings of the know-how protection cannot be changed.

When know-how protection is active, the following applies:

- Parameter view:

  In the parameter view, know-how-protected parameters are not shown in the parameter lists.
- Function view:

  - Know-how-protected parameter values ("[KHP_ACTIVE_READ](#maintaining-and-updating-the-exception-list)") that can be read but not changed ① are shown but are protected against modification.
  - Know-how protected parameter values that can neither be read nor changed ② are indicated by "???" and are locked against modification. Exception: Parameters of a (parameterizable) [exception list](#maintaining-and-updating-the-exception-list) and parameters with attribute "[KHP_WRITE_NO_LOCK](#exception-parameters-for-write-protection-and-know-how-protection)".

    ![Description](images/147853473547_DV_resource.Stream@PNG-en-US.png)

    | Symbol | Meaning |
    | --- | --- |
    | ① | Properties: Can be read, cannot be changed (dark orange background) |
    | ② | Properties: Cannot be changed (light orange background) |
- Information regarding the current status of the know-how protection is displayed in the header line of the working area:

  - In the online mode, reference is made to the fact that know-how protection is active, which means that you cannot change all parameters.
  - In offline mode, reference is made to the fact that know-how protection can only be configured in online mode.
- The values of monitoring parameters r … still remain visible in spite of the fact that know-how protection is active.
- The status of the know-how protection is indicated by the ![Description](images/147853478155_DV_resource.Stream@PNG-en-US.png) icon in the project navigation.
- The protection is applicable to the same extent in the web server.

###### Requirements

- SINAMICS drive with Control Unit CU310-2 or CU320-2
- An online connection to the drive has been established.

###### Know-how protection options in Startdrive

4 different protection options can be selected to protect your drive from unauthorized copying:

![Protection option](images/147853468683_DV_resource.Stream@PNG-en-US.png)

Protection option

| Protection option | Explanation |
| --- | --- |
| No know-how protection | The drive is not protected. |
| Know-how protection without copy protection | You can transfer the settings of your drive to other drives using a memory card. |
| Know-how protection with basic copy protection | The drive can only be operated if the associated Siemens memory card with the settings of your drive is inserted into it.   When the drive is replaced, the settings of the replaced drive can be used.   For this purpose, you only need to insert the Siemens memory card of the old drive into the new drive. You do not need to know the password. |
| Know-how protection with extended copy protection | The drive can only be operated if the associated Siemens memory card with the settings of your drive is inserted into it.   You need the password for know-how protection in order to transfer the memory card to another drive. |

###### Detailed effects when know-how protection is active:

| Affected | Protection settings | Description |
| --- | --- | --- |
| Adjustable parameters | Readable, changeable | Several adjustable parameters can be read and changed when know-how protection is active. You can find a list of the adjustable parameters that can be read and changed on the following page under "[KHP_WRITE_NO_LOCK](#exception-parameters-for-write-protection-and-know-how-protection)".  In addition, you can define an exception list of adjustable parameters, which end users may change. |
| Readable | Several adjustable parameters can be read but not changed when know-how protection is active. You can find a list of the read-only adjustable parameters on the following page under "[KHP_ACTIVE_READ](#exception-parameters-for-write-protection-and-know-how-protection)". |  |
| Functions | Locked | Active know-how protection locks the following functions:  - Downloading drive settings - Uploading drive settings - Automatic controller optimization - Stationary or rotating measurement of the motor data identification - Deleting alarm history and fault history - Generating acceptance documents for safety functions |
| Executable | The following functions can be executed when know-how protection is active:  - Restoring factory settings - Acknowledging faults - Displaying faults, alarms, fault history and alarm history - Reading out the diagnostic buffer - Controlling the drive via the control panel - Displaying acceptance documents for safety functions |  |
| Optionally executable | The functions listed below can be executed despite activated know-how protection, provided diagnostic functions were permitted when it was activated:  - Trace function - Measurement function |  |

---

**See also**

[Loading the project data to the drive unit](Configuring%20SINAMICS%20S-G-MV%20drives.md#loading-the-project-data-to-the-drive-unit)

###### Maintaining and updating the exception list

###### Description

The exception list manages all parameters that can be read and changed in your drive unit, even when know-how protection is active.

In Startdrive, you can only create this exception list via the parameter view. In the factory setting, the exception list only includes the password for know-how protection. You do not need to change the exception list, if, with exception of the password, you do not require additional adjustable parameters in the exception list.

A line with the most important data is managed in the table for each parameter.

![Example: Exception list](images/147853506187_DV_resource.Stream@PNG-en-US.PNG)

Example: Exception list

> **Note**
>
> **Exception list parameters can be viewed everywhere**
>
> When know-how protection is activated, all parameters in the exception list can be viewed in the web server and other commissioning tools.
>
> - Therefore, make sure that no critical parameters are entered in the exception list.

###### Requirements

- Write protection is deactivated.
- The know-how protection is deactivated (temporarily or permanently)

###### Expanding the exception list (excluding additional parameters from protection)

1. In Startdrive, call the drive parameters of the drive whose drive parameters you want to exclude from know-how protection.
2. To open the exception list, click the icon ![Expanding the exception list (excluding additional parameters from protection)](images/147853502219_DV_resource.Stream@PNG-en-US.png) (exception list) in the parameter view.

   The parameter view shows the 2 subtabs: Parameter list and exception list (active).
3. In the exception list, for every parameter **NOT** to be protected, enter the parameter number in the "Number" column in the &lt;Add new&gt; input field and confirm with Return.

   - If the parameter that is entered belongs to the general exception parameters, then a message is displayed stating that this parameter is not protected. Adding this parameter to the exception list is then superfluous.
   - If the parameter entered belongs to the previously protected parameters, Startdrive then adds the most important parameter data of the parameter to be protected in the additional column fields of the current line.
4. In the same way, enter the other parameters that you wish to exclude from protection.
5. The exception list cannot be saved separately.

   - If you have changed the exception list offline, upload the project data to the drive.
   - Then save the project data [permanently](Configuring%20SINAMICS%20S-G-MV%20drives.md#permanently-save-the-settings).

**Result**

After activating know-how protection on the drive, only those parameters that are not in the exception list are then know-how protected.

###### Removing parameters from the exception list (and therefore protecting them)

| Symbol | Meaning |
| --- | --- |
| 1. In Startdrive, call the parameter view of the drive whose know-how settings you want to change. 2. To open the exception list, click the icon ![Removing parameters from the exception list (and therefore protecting them)](images/147853502219_DV_resource.Stream@PNG-en-US.png) (exception list) in the parameter view. 3. In the exception list, select the line of the parameter that you wish to remove from the exception list.       | Symbol | Meaning |    | --- | --- |    |  | **Notice** |    | **Unintentional locking of the drive** Parameter p7766 controls password input for the know-how protection. This parameter is therefore automatically contained in the exception list for the know-how protection. If you delete this parameter from the exception list, the affected drive is **permanently** locked after activation of the know-how protection. It can only be unlocked by a reset to factory settings, which overwrites all drive settings made to date.  - Always keep parameter p7766 in the exception list. |  | 4. Click in the parameter number field, enter "0" and then confirm with Return.     The complete parameter entry is deleted from the exception list. 5. In the same way, delete additional parameters that are to be protected from the exception list. 6. The exception list cannot be saved separately.     - If you have changed the exception list offline, upload the project data to the drive.    - Then save the project data [permanently](Configuring%20SINAMICS%20S-G-MV%20drives.md#permanently-save-the-settings). |  |

**Result**

The modified exception list is taken into account after activating know-how protection on the drive. All of the parameters that were removed from the list are now also know-how protected.

###### Additional parameters

---

- [p7760](SINAMICS%20Parameter%20CU.md#r7760012-cobo-write-protectionknow-how-protection-status)
- [p7763](SINAMICS%20Parameter%20CU.md#p7763-khp-oem-exception-list-number-of-indices-for-p7764)
- [p7764](SINAMICS%20Parameter%20CU.md#p77640n-khp-oem-exception-list)

###### Configuring know-how protection

###### Requirements

Before activating know-how protection, the following conditions must be met:

- Write protection is deactivated.
- To configure know-how protection, the know-how protection must either be temporarily or permanently deactivated.
- An online connection to the drive has been established.
- To guarantee know-how protection, it must be ensured that the project does not remain with the end user as a file.

###### Calling know-how protection configuration

1. Select the "Drive control &gt; Parameters" menu in the project tree.
2. In the secondary navigation, select menu "Basic parameterization &gt; Write and know-how protection".

   The "Write and know-how protection" screen form is displayed with the current protection settings of the drive.

   ![Write and know-how protection screen form](images/147853531787_DV_resource.Stream@PNG-en-US.PNG)

   ![Write and know-how protection screen form](images/147853531787_DV_resource.Stream@PNG-en-US.PNG)

   Write and know-how protection screen form

###### Configuring protection settings and activating them

Protection must be deactivated to configure know-how protection.

1. If know-how protection is active, then deactivate it (see below).
2. Check the parameters of the [exception list](#maintaining-and-updating-the-exception-list) before you make the protection settings. Even when protection is active, all parameters of this exception list can be seen.
3. If, despite active know-how protection, you wish to permit diagnostic functions, then activate option "Allow diagnostic functions (trace and measuring functions)".
4. Now activate the required protection function setting with a mouse click. The following options are available:

   - Activate know-how protection without copy protection (default setting)
   - Basic copy protection - linked to memory card
   - Extended copy protection - linked to memory card and CU
5. Once you have configured the protection settings, you must activate know-how protection:

   - If know-how protection is completely deactivated or has never been activated, click on "Specify password for the activation".
   - If know-how protection has only been temporarily deactivated, click on "Activate".

   The password dialog opens.
6. Enter the required password in the appropriate input fields and confirm with "OK".

**Result:**

If know-how protection is enabled, all normal parameters are protected after encryption is complete. The corresponding parameter values can neither be changed in the program screen forms nor in the parameter view.

![KHP activated](images/147853535755_DV_resource.Stream@PNG-en-US.PNG)

KHP activated

###### Changing your password

Proceed as follows to change an existing password for the know-how protection:

1. Click the "Change password" button.

   The dialog with the same name opens.
2. Enter your old password in the uppermost input field.
3. Enter your new password in the following input field and repeat it in the lowest input field.
4. Confirm your entries with "OK".

**Result:**

The dialog closes. The new password becomes immediately valid.

###### Changing know-how protection settings

Proceed as follows to change your know-how protection configuration:

1. Click on "Deactivation".

   A password prompt is displayed. Option "Temporary deactivation ..." is the default setting.

   ![Changing KHP settings](images/147853539723_DV_resource.Stream@PNG-en-US.png)

   ![Changing KHP settings](images/147853539723_DV_resource.Stream@PNG-en-US.png)

   Changing KHP settings
2. Enter your know-how protection password in the input field.
3. Change the know-how protection settings and activate the required option (e.g. "Extended copy protection...").
4. Click on "Activation".

   You are prompted to enter the password for KHP.
5. Enter the KHP password here and confirm with "OK".

**Result:**

The know-how protection settings have been changed and are active in your drive.

###### Deactivating know-how protection

Proceed as follows to completely deactivate the know-how protection of your drive:

1. Click on "Deactivation".

   A password prompt is displayed. Option "Temporary deactivation ..." is the default setting.
2. Enter your know-how protection password in the input field.
3. Activate the "Permanent deactivation ..." setting.
4. Click on "OK" to permanently delete know-how protection and to reset the know-how protection configuration to the factory setting.

   A confirmation prompt is displayed as to whether you wish to permanently remove the protected drive settings.
5. Click "Yes" to confirm the prompt.

**Result:**

All know-how protection settings have been deleted.

###### Permanently saving the settings

The settings made for the know-how protection of your drive only apply until the next time the drive is restarted.

In order that the settings still apply when the drive is restarted, you must permanently (retentively) save the drive settings (see "[Permanently save the settings](Configuring%20SINAMICS%20S-G-MV%20drives.md#permanently-save-the-settings)").

###### Additional parameters

---

- [r7758](SINAMICS%20Parameter%20CU.md#r7758019-khp-control-unit-serial-number)
- [p7759](SINAMICS%20Parameter%20CU.md#p7759019-khp-control-unit-reference-serial-number)
- [r7760](SINAMICS%20Parameter%20CU.md#r7760012-cobo-write-protectionknow-how-protection-status)
- [p7763](SINAMICS%20Parameter%20CU.md#p7763-khp-oem-exception-list-number-of-indices-for-p7764)
- [p7764](SINAMICS%20Parameter%20CU.md#p77640n-khp-oem-exception-list)
- [p7765](SINAMICS%20Parameter%20CU.md#p7765-khp-configuration)
- p7766
- p7767
- p7768
- [p7769](SINAMICS%20Parameter%20CU.md#p7769020-khp-memory-card-reference-serial-number)

##### Exception parameters for write protection and know-how protection

###### Requirement

- SINAMICS drive with Control Unit CU310-2 or CU320-2

###### Overview

The following table lists parameters of various protection classes. In spite of the fact that protection is activated, parameters belonging to these protection classes can be read, and depending on the specific protection class, can also be configured.

The following protection classes exist:

###### Parameters with "WRITE_NO_LOCK"

The following list contains the parameters with the "WRITE_NO_LOCK" attribute.

These parameters are excluded from write protection and can therefore be written to despite enabled write protection.

WRITE_NO_LOCK

| Symbol | Meaning |
| --- | --- |
| [p0003](SINAMICS%20Parameter%20CU.md#p0003-bop-access-level) | BOP access level/ BOP access level |
| [p0009](SINAMICS%20Parameter%20CU.md#p0009-device-commissioning-parameter-filter) | Device commissioning parameter filter / Dev com par filt |
| [p0124](SINAMICS%20Parameter%20CU.md#p01240n-main-component-detection-using-led)[0...n] | Main component detection via LED / M_comp detect LED |
| p0124[0...n] | Power module detection via LED / PM detect LED |
| [p0144](SINAMICS%20Parameter%20ACTIVE%20INFEED%20CONTROL.md#p01440n-voltage-sensing-module-detection-via-led)[0...n] | Sensor Module detection via LED /SM detect LED |
| p0144[0...n] | Voltage Sensing Module detection via LED / VSM detect LED |
| [p0154](SINAMICS%20Parameter%20ACTIVE%20INFEED%20CONTROL.md#p01540n-voltage-sensing-module-2-detection-via-led)[0...n] | Voltage Sensing Module 2 detection via LED / VSM2 detect LED |
| p0154 | Terminal Module detection via LED / TM detect LED |
| p0154 | DRIVE-CLiQ Hub Module detection via LED / Hub detect LED |
| [p0972](SINAMICS%20Parameter%20CU.md#p0972-drive-unit-reset-2) | Drive unit reset / Drive unit reset |
| [p0976](SINAMICS%20Parameter%20CU.md#p0976-reset-and-load-all-parameters-1) | Reset and load all parameters / Reset load all par |
| [p0977](SINAMICS%20Parameter%20CU.md#p0977-save-all-parameters) | Save all parameters / Save all par |
| p1903 | BI: Data identification control / Data ident ctrl |
| [p2035](SINAMICS%20Parameter%20CU.md#p2035-fieldbus-interface-uss-piv-drive-object-number) | Fieldbus interface USS PKW drive object number / Fieldbus USS DO no |
| [p2102](SINAMICS%20Parameter%20CU.md#p2102-bi-acknowledge-all-faults-1) | BI: Acknowledge all faults / Ackn all faults |
| [p2111](SINAMICS%20Parameter%20CU.md#p2111-alarm-counter) | Alarm counter / Alarm counter |
| [p3100](SINAMICS%20Parameter%20CU.md#p3100-rtc-time-stamp-mode) | RTC time stamp mode / RTC t_stamp mode |
| [p3101](SINAMICS%20Parameter%20CU.md#p310101-setting-utc-time)[0...1] | Set UTC time / Set UTC time |
| [p3103](SINAMICS%20Parameter%20CU.md#p3103-utc-synchronization-process-1) | UTC synchronization technique / UTC sync technique |
| [p3950](SINAMICS%20Parameter%20CU.md#p3950-service-parameter) | Service parameter / Service par |
| [p3981](SINAMICS%20Parameter%20CU.md#p3981-acknowledge-drive-object-faults) | Acknowledge drive object faults / Ackn DO faults |
| [p3985](SINAMICS%20Parameter%20ACTIVE%20INFEED%20CONTROL.md#p3985-master-control-mode-selection) | Master control mode selection / PcCtrl mode select |
| [p4700](SINAMICS%20Parameter%20CU.md#p470001-trace-control)[0...1] | Trace control / Trace control |
| [p4701](SINAMICS%20Parameter%20CU.md#p4701-measuring-function-control) | Measurement function control / Meas fct control |
| [p4703](SINAMICS%20Parameter%20CU.md#p470301-trace-options)[0...1] | Trace options / Trace options |
| [p4707](SINAMICS%20Parameter%20CU.md#p4707-measuring-function-configuration) | Measurement function configuration / Meas fct config |
| [p4710](SINAMICS%20Parameter%20CU.md#p471001-trace-trigger-condition)[0...1] | Trace trigger condition / Trace trig cond |
| [p4711](SINAMICS%20Parameter%20CU.md#p471105-trace-trigger-signal)[0...5] | Trace trigger signal / Trace trig signal |
| [p4712](SINAMICS%20Parameter%20CU.md#p471201-trace-trigger-threshold)[0...1] | Trace trigger threshold / Trace trig thr |
| [p4713](SINAMICS%20Parameter%20CU.md#p471301-trace-tolerance-band-trigger-threshold-1)[0...1] | Trace tolerance band trigger threshold 1 / Trace trig thr 1 |
| [p4714](SINAMICS%20Parameter%20CU.md#p471401-trace-tolerance-band-trigger-threshold-2)[0...1] | Trace tolerance band trigger threshold 2 / Trace trig thr 2 |
| [p4715](SINAMICS%20Parameter%20CU.md#p471501-trace-bit-mask-trigger-bit-mask)[0...1] | Trace bit mask trigger bit mask / Trace trig mask |
| [p4716](SINAMICS%20Parameter%20CU.md#p471601-trace-bit-mask-trigger-trigger-condition)[0...1] | Trace bit mask trigger trigger condition / Trace trig cond |
| [p4717](SINAMICS%20Parameter%20CU.md#p4717-measuring-function-number-of-averaging-operations) | Measurement function averaging number / Meas fct avg no |
| [p4718](SINAMICS%20Parameter%20CU.md#p4718-measuring-function-number-of-stabilizing-periods) | Number of measurement function settling periods / MeasFct settle qty |
| [p4720](SINAMICS%20Parameter%20CU.md#p472001-trace-recording-cycle)[0...1] | Trace recording clock cycle / Trace record cycle |
| [p4721](SINAMICS%20Parameter%20CU.md#p472101-trace-recording-time)[0...1] | Trace recording duration / Trace rec duration |
| [p4722](SINAMICS%20Parameter%20CU.md#p472201-trace-trigger-delay)[0...1] | Trace trigger delay / Trace trig delay |
| [p4723](SINAMICS%20Parameter%20CU.md#p472301-trace-time-slice-cycle)[0...1] | Trace time slice clock cycle / Trace cycle |
| [p4724](SINAMICS%20Parameter%20CU.md#p472401-trace-average-in-the-time-range)[0...1] | Trace averaging in the time range / Trace averaging |
| [p4730](SINAMICS%20Parameter%20CU.md#p473005-trace-record-signal-0)[0...5] | Trace record signal 0 / Trace record sig 0 |
| [p4731](SINAMICS%20Parameter%20CU.md#p473105-trace-record-signal-1)[0...5] | Trace record signal 1 / Trace record sig 1 |
| [p4732](SINAMICS%20Parameter%20CU.md#p473205-trace-record-signal-2)[0...5] | Trace record signal 2 / Trace record sig 2 |
| [p4733](SINAMICS%20Parameter%20CU.md#p473305-trace-record-signal-3)[0...5] | Trace record signal 3 / Trace record sig 3 |
| [p4734](SINAMICS%20Parameter%20CU.md#p473405-trace-record-signal-4)[0...5] | Trace record signal 4 / Trace record sig 4 |
| [p4735](SINAMICS%20Parameter%20CU.md#p473505-trace-record-signal-5)[0...5] | Trace record signal 5 / Trace record sig 5 |
| [p4736](SINAMICS%20Parameter%20CU.md#p473605-trace-record-signal-6)[0...5] | Trace record signal 6 / Trace record sig 6 |
| [p4737](SINAMICS%20Parameter%20CU.md#p473705-trace-record-signal-7)[0...5] | Trace record signal 7 / Trace record sig 7 |
| [p4780](SINAMICS%20Parameter%20CU.md#p478001-trace-physical-address-signal-0)[0...1] | Trace physical address signal 0 / Trace phy adr sig0 |
| [p4781](SINAMICS%20Parameter%20CU.md#p478101-trace-physical-address-signal-1)[0...1] | Trace physical address signal 1 / Trace phy adr sig1 |
| [p4782](SINAMICS%20Parameter%20CU.md#p478201-trace-physical-address-signal-2)[0...1] | Trace physical address signal 2 / Trace phy adr sig2 |
| [p4783](SINAMICS%20Parameter%20CU.md#p478301-trace-physical-address-signal-3)[0...1] | Trace physical address signal 3 / Trace phy adr sig3 |
| [p4784](SINAMICS%20Parameter%20CU.md#p478401-trace-physical-address-signal-4)[0...1] | Trace physical address signal 4 / Trace phy adr sig4 |
| [p4785](SINAMICS%20Parameter%20CU.md#p478501-trace-physical-address-signal-5)[0...1] | Trace physical address signal 5 / Trace phy adr sig5 |
| [p4786](SINAMICS%20Parameter%20CU.md#p478601-trace-physical-address-signal-6)[0...1] | Trace physical address signal 6 / Trace phy adr sig6 |
| [p4787](SINAMICS%20Parameter%20CU.md#p478701-trace-physical-address-signal-7)[0...1] | Trace physical address signal 7 / Trace phy adr sig7 |
| [p4789](SINAMICS%20Parameter%20CU.md#p478901-trace-physical-address-trigger-signal)[0...1] | Trace physical address trigger signal / Trace phy adr trig |
| [p4795](SINAMICS%20Parameter%20CU.md#p4795-trace-memory-bank-changeover) | Trace memory bank changeover / Trace mem chgov |
| [p4800](SINAMICS%20Parameter%20CU.md#p4800-function-generator-control) | Function generator control / FG control |
| [p4810](SINAMICS%20Parameter%20CU.md#p4810-function-generator-mode) | Function generator mode / FG mode |
| [p4812](SINAMICS%20Parameter%20CU.md#p4812-function-generator-physical-address) | Function generator physical address / FG phys address |
| [p4813](SINAMICS%20Parameter%20CU.md#p4813-function-generator-physical-address-reference-value) | Function generator physical address reference value / FG phys addr ref |
| [p4815](SINAMICS%20Parameter%20CU.md#p481502-function-generator-drive-number)[0...2] | Function generator drive number / FG drive number |
| [p4816](SINAMICS%20Parameter%20CU.md#p4816-function-generator-output-signal-integer-number-scaling) | Function generator output signal integer number scaling / FG outp integ scal |
| [p4819](SINAMICS%20Parameter%20CU.md#p4819-bi-function-generator-control) | BI: Function generator control / FG control |
| [p4820](SINAMICS%20Parameter%20CU.md#p4820-function-generator-signal-shape) | Function generator signal shape / FG signal shape |
| [p4821](SINAMICS%20Parameter%20CU.md#p4821-function-generator-period) | Function generator period duration / FG period duration |
| [p4822](SINAMICS%20Parameter%20CU.md#p4822-function-generator-pulse-width) | Function generator pulse width / FG pulse width |
| [p4823](SINAMICS%20Parameter%20CU.md#p4823-function-generator-bandwidth) | Function generator bandwidth / FG bandwidth |
| [p4824](SINAMICS%20Parameter%20CU.md#p4824-function-generator-amplitude) | Function generator amplitude / FG amplitude |
| [p4825](SINAMICS%20Parameter%20CU.md#p4825-function-generator-2nd-amplitude) | Function generator 2nd amplitude / FG 2nd amplitude |
| [p4826](SINAMICS%20Parameter%20CU.md#p4826-function-generator-offset) | Function generator offset / FG offset |
| [p4827](SINAMICS%20Parameter%20CU.md#p4827-function-generator-ramp-up-time-to-offset) | Function generator ramp-up time to offset / FG ramp-up offset |
| [p4828](SINAMICS%20Parameter%20CU.md#p4828-function-generator-lower-limit) | Function generator lower limit / FG lower limit |
| [p4829](SINAMICS%20Parameter%20CU.md#p4829-function-generator-upper-limit) | Function generator upper limit / FG upper limit |
| [p4830](SINAMICS%20Parameter%20CU.md#p4830-function-generator-time-slice-cycle) | Function generator time slice clock cycle / FG time slice |
| [p4831](SINAMICS%20Parameter%20CU.md#p4831-function-generator-amplitude-scaling) | Function generator amplitude scaling / FG amplitude scal |
| [p4832](SINAMICS%20Parameter%20CU.md#p483202-function-generator-amplitude-scaling)[0...2] | Function generator amplitude scaling / FG amplitude scal |
| [p4833](SINAMICS%20Parameter%20CU.md#p483302-function-generator-offset-scaling)[0...2] | Function generator offset scaling / FG offset scal |
| [p4835](SINAMICS%20Parameter%20CU.md#p483504-function-generator-free-measurement-function-scaling)[0...4] | Function generator free measurement function scaling / FG fr measFct scal |
| p4840[0...1] | MTrace cycle number setting / Cycle quantity |
| [p7761](SINAMICS%20Parameter%20CU.md#p7761-write-protection) | Write protection / Write protection |
| [p7770](SINAMICS%20Parameter%20ACTIVE%20INFEED%20CONTROL.md#p7770-nvram-action) | NVRAM action / NVRAM action |
| [p8550](SINAMICS%20Parameter%20CU.md#p8550-aop-localremote) | AOP LOCAL/REMOTE / AOP LOCAL/REMOTE |
| [p8806](SINAMICS%20Parameter%20CU.md#p8806053-identification-and-maintenance-1)[0...53] | Identification and Maintenance 1 / I&amp;M 1 |
| [p8807](SINAMICS%20Parameter%20CU.md#p8807015-identification-and-maintenance-2)[0...15] | Identification and Maintenance 2 / I&amp;M 2 |
| [p8808](SINAMICS%20Parameter%20CU.md#p8808053-identification-and-maintenance-3)[0...53] | Identification and Maintenance 3 / I&amp;M 3 |
| [p9210](SINAMICS%20Parameter%20CU.md#p9210-flashing-component-number) | Flashing component number / Flash comp no |
| [p9211](SINAMICS%20Parameter%20CU.md#p9211-flash-function) | Flashing function / Flashing function |
| p9484 | BICO interconnections search signal source / BICO search s_s |

###### Parameters with "KHP_WRITE_NO_LOCK"

The following list contains the parameters with the "KHP_WRITE_NO_LOCK" attribute.

These parameters are excluded from know-how protection and can therefore be written to in spite of the fact that know-how protection is active.

KHP_WRITE_NO_LOCK

| Symbol | Meaning |
| --- | --- |
| p0003 | BOP access level/ BOP access level |
| p0009 | Device commissioning parameter filter / Dev com par filt |
| p0124[0...n] | Main component detection via LED / M_comp detect LED |
| p0124[0...n] | Power module detection via LED / PM detect LED |
| p0144[0...n] | Sensor Module detection via LED /SM detect LED |
| p0144[0...n] | Voltage Sensing Module detection via LED / VSM detect LED |
| p0154[0...n] | Voltage Sensing Module 2 detection via LED / VSM2 detect LED |
| p0154 | Terminal Module detection via LED / TM detect LED |
| p0154 | DRIVE-CLiQ Hub Module detection via LED / Hub detect LED |
| p0972 | Drive unit reset / Drive unit reset |
| p0976 | Reset and load all parameters / Reset load all par |
| p0977 | Save all parameters / Save all par |
| p2035 | Fieldbus interface USS PKW drive object number / Fieldbus USS DO no |
| [p2040](SINAMICS%20Parameter%20CU.md#p2040-fieldbus-interface-monitoring-time) | COMM INT monitoring time / COMM INT t_mon |
| p2040 | Fieldbus interface monitoring time / Fieldbus t_mon |
| p2102 | BI: Acknowledge all faults / Ackn all faults |
| p2111 | Alarm counter / Alarm counter |
| p3100 | RTC time stamp mode / RTC t_stamp mode |
| p3101[0...1] | Set UTC time / Set UTC time |
| p3103 | UTC synchronization technique / UTC sync technique |
| [p3105](SINAMICS%20Parameter%20CU.md#p310503-ntp-server-ip-address)[0...3] | NTP server IP address / NTP IP address |
| [p3106](SINAMICS%20Parameter%20CU.md#p3106-ntp-time-zone) | NTP time zone / Time zone |
| p3950 | Service parameter / Service par |
| p3981 | Acknowledge drive object faults / Ackn DO faults |
| p3985 | Master control mode selection / PcCtrl mode select |
| p7761 | Write protection / Write protection |
| p7770 | NVRAM action / NVRAM action |
| p8550 | AOP LOCAL/REMOTE / AOP LOCAL/REMOTE |
| p8806[0...53] | Identification and Maintenance 1 / I&amp;M 1 |
| p8807[0...15] | Identification and Maintenance 2 / I&amp;M 2 |
| p8808[0...53] | Identification and Maintenance 3 / I&amp;M 3 |
| [p8835](SINAMICS%20Parameter%20CU.md#p8835-cbe20-firmware-selection) | CBE20 firmware selection / CBE20 FW selection |
| [p8839](SINAMICS%20Parameter%20CU.md#p883901-pzd-interface-hardware-assignment)[0...1] | PZD interface hardware assignment / PZD IF HW assign |
| [p8840](SINAMICS%20Parameter%20CU.md#p8840-comm-board-monitoring-time) | COMM BOARD monitoring time / CB t_mon |
| p9210 | Flashing component number / Flash comp no |
| p9211 | Flashing function / Flashing function |
| p9484 | BICO interconnections search signal source / BICO search s_s |

###### Parameters with "KHP_ACTIVE_READ"

The following list contains the parameters with the "KHP_ACTIVE_READ" attribute.

These parameters can also be read even with know-how protection activated - however, cannot be written to.

KHP_ACTIVE_READ

| Symbol | Meaning |
| --- | --- |
| [p0015](SINAMICS%20Parameter%20CU.md#p0015-macro-drive-unit-1) | Macro drive unit / Macro drive unit |
| p0015 | Macro drive object / Macro DO |
| [p0100](SINAMICS%20Parameter%20SERVO.md#p0100-iecnema-standards) | Standard IEC/NEMA / Standard IEC/NEMA |
| [p0101](SINAMICS%20Parameter%20CU.md#p01010n-drive-object-numbers)[0...n] | Drive object numbers / DO numbers |
| [p0103](SINAMICS%20Parameter%20CU.md#p01030n-application-specific-view)[0...n] | Application-specific view / Appl_spec view |
| [p0105](SINAMICS%20Parameter%20CU.md#p0105-activatedeactivate-drive-object) | Activate/deactivate drive object / Act/deact DO |
| [p0107](SINAMICS%20Parameter%20CU.md#p01070n-drive-object-type-7)[0...n] | Drive object type / DO type |
| [p0108](SINAMICS%20Parameter%20CU.md#p01080n-drive-objects-function-module)[0...n] | Drive object function module / DO fct_module |
| [p0120](SINAMICS%20Parameter%20ACTIVE%20INFEED%20CONTROL.md#p0120-number-of-power-unit-data-sets-pds) | Number of valve data sets (PDS) / PDS quantity |
| p0120 | Number of power unit data sets (PDS) / PDS quantity |
| [p0121](SINAMICS%20Parameter%20ACTIVE%20INFEED%20CONTROL.md#p01210n-power-unit-component-number)[0...n] | Power unit component number / PU component no |
| [p0125](SINAMICS%20Parameter%20ACTIVE%20INFEED%20CONTROL.md#p01250n-activatedeactivate-power-unit-components)[0...n] | Activate/deactivate power unit component / Act/deact PU comp |
| [p0130](SINAMICS%20Parameter%20SERVO.md#p0130-number-of-motor-data-sets-mds) | Number of motor data sets (MDS) / MDS quantity |
| [p0131](SINAMICS%20Parameter%20SERVO.md#p01310n-motor-component-number)[0...n] | Motor component number / Motor component no |
| [p0140](SINAMICS%20Parameter%20ACTIVE%20INFEED%20CONTROL.md#p0140-number-of-vsm-data-sets) | Number of encoder data sets (EDS) / EDS quantity |
| p0140 | Number of VSM data sets / VSM quantity |
| [p0141](SINAMICS%20Parameter%20ACTIVE%20INFEED%20CONTROL.md#p01410n-vsm-component-number)[0...n] | Encoder interface (Sensor Module) component number / Enc intf comp no |
| p0141[0...n] | VSM component number / VSM component no |
| [p0142](SINAMICS%20Parameter%20SERVO.md#p01420n-encoder-component-number)[0...n] | Encoder component number / Encoder comp no |
| [p0145](SINAMICS%20Parameter%20ACTIVE%20INFEED%20CONTROL.md#p01450n-voltage-sensing-module-activatedeactivate)[0...n] | Activate/deactivate encoder interface / Act/deact enc intf |
| p0145[0...n] | Activate/deactivate Voltage Sensing Module / Act/deact VSM |
| [p0150](SINAMICS%20Parameter%20ACTIVE%20INFEED%20CONTROL.md#p0150-vsm2-data-sets-selection) | Number of VSM data sets / VSM data sets qty |
| p0150 | Number of VSM2 data sets / VSM2 data sets qty |
| [p0151](SINAMICS%20Parameter%20ACTIVE%20INFEED%20CONTROL.md#p01510n-voltage-sensing-module-2-component-number)[0...n] | Voltage Sensing Module component number / VSM component no |
| p0151[0...n] | Voltage Sensing Module 2 component number / VSM2 component no |
| p0151 | Terminal Module component number / TM component no |
| p0151[0...1] | DRIVE-CLiQ Hub Module component number / Hub component no |
| [p0161](SINAMICS%20Parameter%20SERVO.md#p0161-hf-damping-module-component-number) | Valve component number / Valve component no |
| p0161 | HF Damping Module component number / HF damp comp no |
| p0161 | Option Board component number / Opt Board comp no |
| [p0162](SINAMICS%20Parameter%20SERVO.md#p0162-hf-choke-module-component-number) | HF Choke Module component number / HF choke comp no |
| p0162 | CU-LINK device component number / CU-LINK comp no |
| [p0170](SINAMICS%20Parameter%20ACTIVE%20INFEED%20CONTROL.md#p0170-number-of-command-data-sets-cds) | Number of command data sets (CDS) / CDS quantity |
| [p0171](SINAMICS%20Parameter%20CU.md#p01710n-drive-objects-function-module-1)[0...n] | Drive objects function module 1 / DO fct_module 1 |
| [p0172](SINAMICS%20Parameter%20CU.md#p01720n-drive-objects-function-module-2)[0...n] | Drive objects function module 2 / DO fct_module 2 |
| [p0173](SINAMICS%20Parameter%20CU.md#p01730n-drive-objects-function-module-3)[0...n] | Drive objects function module 3 / DO fct_module 3 |
| [p0180](SINAMICS%20Parameter%20SERVO.md#p0180-number-of-drive-data-sets-dds) | Number of drive data sets (DDS) / DDS quantity |
| [p0199](SINAMICS%20Parameter%20CU.md#p0199024-drive-object-name)[0...24] | Drive objects name / DO name |
| [p0300](SINAMICS%20Parameter%20SERVO.md#p03000n-motor-type-selection-2)[0...n] | Motor type selection / Motor type select |
| [p0304](SINAMICS%20Parameter%20SERVO.md#p03040n-rated-motor-voltage)[0...n] | Rated motor voltage / Motor U_rated |
| [p0305](SINAMICS%20Parameter%20SERVO.md#p03050n-rated-motor-current)[0...n] | Rated motor current / Motor I_rated |
| [p0349](SINAMICS%20Parameter%20SERVO.md#p0349-system-of-units-motor-equivalent-circuit-diagram-data) | System of units motor equivalent circuit diagram data / Unit sys motor ECD |
| [p0400](SINAMICS%20Parameter%20SERVO.md#p04000n-encoder-type-selection)[0...n] | Encoder type selection / Encoder type sel |
| [p0505](SINAMICS%20Parameter%20ACTIVE%20INFEED%20CONTROL.md#p0505-selecting-the-system-of-units) | System of units selection / Unit sys select |
| [p0595](SINAMICS%20Parameter%20SERVO.md#p0595-technological-unit-selection) | Technological unit selection / Tech unit select |
| [p0806](SINAMICS%20Parameter%20ACTIVE%20INFEED%20CONTROL.md#p0806-bi-inhibit-master-control) | BI: Inhibit master control / Inhibit PcCtrl |
| [p0864](SINAMICS%20Parameter%20SERVO.md#p0864-bi-infeed-operation) | BI: System pressure available / p_sys available |
| p0864 | BI: Infeed operation / INF operation |
| [p0870](SINAMICS%20Parameter%20SERVO.md#p0870-bi-close-main-contactor) | BI: Close main contactor / Close main cont |
| p0915[0...29] | TM15 PROFIdrive PZD setpoint assignment / TM15 PD PZD setp |
| p0915[0...35] | TM17 PROFIdrive PZD setpoint assignment / TM17 PD PZD setp |
| p0916[0...29] | TM15 PROFIdrive PZD actual value assignment / TM15 PD PZD ActV |
| p0916[0...35] | TM17 PROFIdrive PZD actual value assignment / TM17 PD PZD ActV |
| [p0922](SINAMICS%20Parameter%20CU.md#p0922-if1-profidrive-pzd-telegram-selection-2) | IF1 PROFIdrive PZD telegram selection / IF1 PZD telegram |
| [p0978](SINAMICS%20Parameter%20CU.md#p09780n-list-of-drive-objects)[0...n] | List of drive objects / List of DO |
| [p1080](SINAMICS%20Parameter%20SERVO.md#p10800n-minimum-velocity-1)[0...n] | Minimum velocity / v_min |
| p1080[0...n] | Minimum speed / n_min |
| [p1082](SINAMICS%20Parameter%20SERVO.md#p10820n-maximum-speed-1)[0...n] | Maximum velocity / v_max |
| p1082[0...n] | Maximum speed / n_max |
| p1082[0...n] | Maximum velocity / v_max |
| [p1520](SINAMICS%20Parameter%20SERVO.md#p15200n-co-torque-limit-uppermotoring-3)[0...n] | CO: Force limit upper/motoring / F_max upper/mot |
| p1520[0...n] | CO: Torque limit upper/motoring / M_max upper/mot |
| p1520[0...n] | CO: Torque limit upper / M_max upper |
| [p1532](SINAMICS%20Parameter%20SERVO.md#p15320n-co-torque-limit-offset-1)[0...n] | CO: Force offset force limit / F_max offset |
| p1532[0...n] | CO: Torque limit offset / M_max offset |
| [p1544](SINAMICS%20Parameter%20SERVO.md#p1544-travel-to-fixed-stop-evaluation-torque-reduction-1) | Travel to fixed stop evaluation torque reduction / TfS M_red eval |
| p1544 | Travel to fixed stop evaluation force reduction / TfS F_red eval |
| [p2000](SINAMICS%20Parameter%20ACTIVE%20INFEED%20CONTROL.md#p2000-reference-frequency) | Reference velocity / v_reference |
| p2000 | Reference speed reference frequency / n_ref f_ref |
| p2000 | Reference velocity reference frequency / v_ref f_ref |
| p2000 | Reference frequency / f_reference |
| [p2001](SINAMICS%20Parameter%20ACTIVE%20INFEED%20CONTROL.md#p2001-reference-voltage) | Reference voltage / Reference voltage |
| [p2002](SINAMICS%20Parameter%20ACTIVE%20INFEED%20CONTROL.md#p2002-reference-current) | Reference pressure / p_reference |
| p2002 | Reference current / I_reference |
| [p2003](SINAMICS%20Parameter%20SERVO.md#p2003-reference-torque-1) | Reference force / F_reference |
| p2003 | Reference torque / M_reference |
| p2003 | Reference force / Reference force |
| [p2005](SINAMICS%20Parameter%20ACTIVE%20INFEED%20CONTROL.md#p2005-reference-angle) | Reference angle / Reference angle |
| [p2006](SINAMICS%20Parameter%20ACTIVE%20INFEED%20CONTROL.md#p2006-reference-temperature) | Reference temperature / Ref temperature |
| [p2007](SINAMICS%20Parameter%20SERVO.md#p2007-reference-acceleration-1) | Reference acceleration / a_reference |
| [p2030](SINAMICS%20Parameter%20CU.md#p2030-field-bus-interface-protocol-selection-1) | Fieldbus interface protocol selection / Fieldbus protocol |
| [p2038](SINAMICS%20Parameter%20SERVO.md#p2038-if1-profidrive-stwzsw-interface-mode-4) | IF1 PROFIdrive STW/ZSW interface mode / PD STW/ZSW IF mode |
| [p2079](SINAMICS%20Parameter%20CU.md#p2079-if1-profidrive-pzd-telegram-selection-extended-1) | IF1 PROFIdrive PZD telegram selection extended / IF1 PZD tel ext |
| [p4956](SINAMICS%20Parameter%20CU.md#p49560n-tec-do-specific-activation)[0...n] | TEC DO-specific activation / TEC DO act |
| [p5043](SINAMICS%20Parameter%20SERVO.md#p504306-spindle-speed-limits-1)[0...6] | Spindle speed limits / n_limits |
| [p7763](SINAMICS%20Parameter%20CU.md#p7763-khp-oem-exception-list-number-of-indices-for-p7764) | KHP OEM exception list number of indices for [p7764](SINAMICS%20Parameter%20CU.md#p77640n-khp-oem-exception-list) / KHP OEM qty p7764 |
| p7764[0...n] | KHP OEM exception list / KHP OEM excep list |
| [p7852](SINAMICS%20Parameter%20CU.md#p7852-number-of-indices-for-r7853) | Number of indices for [r7853](SINAMICS%20Parameter%20CU.md#r78530n-component-availablenot-available) / Qty indices r7853 |
| [p8836](SINAMICS%20Parameter%20CU.md#p8836-sinamics-link-node-address) | SINAMICS Link node address / Node adr |
| [p8864](SINAMICS%20Parameter%20SERVO.md#p8864-if1-profidrive-first-supplementary-telegram-selection) | IF1 PROFIdrive first supplementary telegram selection / IF1 Pd 1st Suppl tel |
| [p8865](SINAMICS%20Parameter%20SERVO.md#p8865-if1-profidrive-second-supplementary-telegram-selection) | IF1 PROFIdrive second supplementary telegram selection / IF1 Pd 2. Suppl tel |
| [p8870](SINAMICS%20Parameter%20CU.md#p8870015-sinamics-link-pzd-receive-word)[0...15] | SINAMICS Link PZD receive word / PZD recv word |
| p8870[0...31] | SINAMICS Link PZD receive word / PZD recv word |
| [p8871](SINAMICS%20Parameter%20CU.md#p8871015-sinamics-link-pzd-send-word)[0...15] | SINAMICS Link PZD send word / PZD send word |
| p8871[0...31] | SINAMICS Link PZD send word / PZD send word |
| [p8872](SINAMICS%20Parameter%20CU.md#p8872015-sinamics-link-pzd-receive-address)[0...15] | SINAMICS Link PZD receive address / PZD recv address |
| p8872[0...31] | SINAMICS Link PZD receive address / PZD recv address |
| [p9500](SINAMICS%20Parameter%20SERVO.md#p9500-si-motion-monitoring-clock-cycle-control-unit-1) | SI Motion monitoring clock cycle (Control Unit) / SI Motion cycle CU |
| [p9601](SINAMICS%20Parameter%20SERVO.md#p9601-si-enable-functions-integrated-in-the-drive-control-unit-2) | SI enable functions integrated in the drive (Control Unit) / SI enable fct CU |
| [p9810](SINAMICS%20Parameter%20SERVO.md#p9810-si-profisafe-address-motor-module) | SI PROFIsafe address (Motor Module) / SI Ps address MM |
| p9902 | Target topology number of indices / Target topo indices |

###### Additional parameters

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

### Inputs/outputs

This section contains information on the following topics:

- [Control Unit digital inputs](#control-unit-digital-inputs)
- [Control Unit bidirectional digital inputs/outputs](#control-unit-bidirectional-digital-inputsoutputs)
- [Control Unit measuring sockets](#control-unit-measuring-sockets)
- [Isolated digital output (only CU310-2)](#isolated-digital-output-only-cu310-2)
- [Analog input (only CU310-2 PN)](#analog-input-only-cu310-2-pn)

#### Control Unit digital inputs

##### Description

Here you can change the interconnection of the digital inputs on the control unit.

- Digital inputs are used for the acquisition of digital signals. For example, drive enables can be controlled externally. The interconnection of digital inputs is made via BICO interconnections.
- For every digital input signal there is the corresponding inverted signal which can also be used for interconnection.
- CU320-2: Digital inputs 0 ... 7, 16, 17 and 20, 21 can be interconnected
- CU310-2: Digital inputs 0 ... 3, 16 ...22 can be interconnected

##### Simulation mode

The selection box for the terminal evaluation / simulation switchover is only visible online.

##### Interconnect digital inputs of a CU320-2 ([r0722](SINAMICS%20Parameter%20CU.md#r0722022-cobo-cu-digital-inputs-status) and [r0723](SINAMICS%20Parameter%20CU.md#r0723022-cobo-cu-digital-inputs-status-inverted))

1. Interconnect the signal sources of the digital inputs 0 to 7, 16, 17, 20 and 21.

   Several interconnections are possible.

##### Interconnect digital inputs of a CU310-2 (r0722 and r0723)

1. Interconnect the signal sources of the digital inputs 0 to 3, 16 to 22.

   Several interconnections are possible.

##### Function diagrams (FD)

- CU320-2 input/output terminals - Overview - 2119 -
- CU320-2 input/output terminals - Electrically isolated digital inputs (DI 0 ... DI 3, DI 16, DI 17) - 2120 -
- CU320-2 input/output terminals - Electrically isolated digital inputs (DI 4 ... DI 7, DI 20, DI 21) - 2121 -
- CU320-2 input/output terminals - Digital inputs/outputs bidirectional (DI/DO 8 ... DI/DO 9) - 2130 -
- CU320-2 input/output terminals - Digital inputs/outputs bidirectional (DI/DO 10 ... DI/DO 11) - 2131 -
- CU320-2 input/output terminals - Digital inputs/outputs bidirectional (DI/DO 12 ... DI/DO 13) - 2132 -
- CU320-2 input/output terminals - Digital inputs/outputs bidirectional (DI/DO 14 ... DI/DO 15) - 2133 -

##### Additional parameters

---

---

**See also**

[TM31 Inputs/Outputs](TM31%20Terminal%20Module%20%28stdrui200000enUS%29.md#tm31-inputsoutputs)

#### Control Unit bidirectional digital inputs/outputs

##### Description

The bidirectional inputs/outputs of terminals X122 and X132 on the Control Unit (DO1) can be used by a drive object as well as by a higher-level controller (resource sharing). The assignment to a terminal is defined by means of BICO interconnections which are either connected to a controller via the DO1 telegram [p0922](SINAMICS%20Parameter%20CU.md#p0922-if1-profidrive-pzd-telegram-selection-2) = 39x or to a drive object.

You can change the interconnection of the bidirectional digital inputs/outputs on the input/output component.

- You can assign bidirectional digital inputs/outputs in the function. This means you can parameterize an input or an output.
- Digital inputs are used for the acquisition of digital signals. For example, drive enables can be controlled externally.
- For every digital input signal there is the corresponding inverted signal which can also be used for interconnection.
- Digital outputs are used for the feedback of signals such as enables.

##### Changing the view of the screen form

The view of this screen form can be reduced to the essentials via a checkbox. Changing the function of one of the bidirectional digital inputs/outputs is not possible in the optimized view. The view of the screen form can also be switched to a simulation mode. However, this switchover only functions in online mode.

1. If you want to optimize the view of the screen form, activate the "Optimize view" option.
2. If you want to switch to a simulation from the terminal evaluation, select "Simulation" in the drop-down list of a digital input.

##### Parameterizing digital inputs 8 to 15 or digital outputs 8 to 15

Each of the bidirectional digital inputs/outputs can be parameterized as an input or output using the change-over switch.

| Change-over switch position | Description |
| --- | --- |
| Digital input    ![Parameterizing digital inputs 8 to 15 or digital outputs 8 to 15](images/147853669771_DV_resource.Stream@PNG-en-US.png) | Default setting when calling the screen form for the first time.   You can interconnect the digital inputs 8 to 15 with this switch position. Several interconnections are possible.  Change-over switch can be switched over from digital input to digital output with a mouse click. |
| Digital output    ![Parameterizing digital inputs 8 to 15 or digital outputs 8 to 15](images/147853673739_DV_resource.Stream@PNG-en-US.png) | You can interconnect the digital outputs 8 to 15 with this switch position. Several interconnections are possible.  Change-over switch can be switched over from digital output to digital input with a mouse click. |

1. Select the digital input/output at the required terminal.
2. Interconnect the signal source of the digital input (8 to 15).   
   OR
3. Proceed as follows to change the digital input to a digital output:

   - Click on the change-over switch.
   - Then interconnect the signal sink of the digital output (8 to 15).
   - If you want to invert the digital output, click on this icon ![Parameterizing digital inputs 8 to 15 or digital outputs 8 to 15](images/147853661579_DV_resource.Stream@PNG-en-US.png).

     When inverted, the icon looks like this ![Parameterizing digital inputs 8 to 15 or digital outputs 8 to 15](images/147853665675_DV_resource.Stream@PNG-en-US.png).
4. Repeat steps 2 or 3 for all digital inputs/outputs of the required terminal.

##### Function diagrams (FD)

- CU320-2 input/output terminals - Overview - 2119 -
- CU320-2 input/output terminals - Electrically isolated digital inputs (DI 0 ... DI 3, DI 16, DI 17) - 2120 -
- CU320-2 input/output terminals - Electrically isolated digital inputs (DI 4 ... DI 7, DI 20, DI 21) - 2121 -
- CU320-2 input/output terminals - Digital inputs/outputs bidirectional (DI/DO 8 ... DI/DO 9) - 2130 -
- CU320-2 input/output terminals - Digital inputs/outputs bidirectional (DI/DO 10 ... DI/DO 11) - 2131 -
- CU320-2 input/output terminals - Digital inputs/outputs bidirectional (DI/DO 12 ... DI/DO 13) - 2132 -
- CU320-2 input/output terminals - Digital inputs/outputs bidirectional (DI/DO 14 ... DI/DO 15) - 2133 -

##### Additional parameters

---

---

**See also**

[TM31 Inputs/Outputs](TM31%20Terminal%20Module%20%28stdrui200000enUS%29.md#tm31-inputsoutputs)

#### Control Unit measuring sockets

##### Description

The measuring sockets output the analog signals. Any freely interconnectable signal can be output at any measuring socket. A measuring socket can be used, for example, to output the actual speed value ([r0063](SINAMICS%20Parameter%20SERVO.md#r0063-co-actual-speed-smoothed-1)) to a measuring instrument connected to the measuring socket.

> **Note**
>
> **Only for commissioning and service**
>
> The measuring sockets should be used only for commissioning and service purposes. The measurements may be performed only by appropriately trained skilled personnel.

You can make the following settings:

- Activate limitation to characteristic curve
- Interconnect signal sources
- Parameterize characteristic
- Define offset

##### Parameterizing the measuring sockets

1. Select one of the two settings in the "Limitation" drop-down list of a measuring socket:

   - Limitation on

     If signals are output outside the permissible measuring range, the signal is limited to 4.98 V or to 0 V.
   - Limitation off

     The output of signals outside the permissible measuring range causes a signal overflow. In the event of an overflow, the signal jumps from 0 V to 4.98 V or from 4.98 to 0 V.
2. For each of the measuring sockets T0, T1 and T2 interconnect the signal sources ([p0771](SINAMICS%20Parameter%20CU.md#p077102-ci-test-sockets-signal-source)[0...2]) whose signal is to be output via the measuring socket.

   | Symbol | Meaning |
   | --- | --- |
   | [r0060](SINAMICS%20Parameter%20SERVO.md#r0060-co-speed-setpoint-before-the-setpoint-filter-1) | CO: Speed setpoint before speed setpoint filter |
   | r0063 | CO: Actual speed value |
   | [r0069](SINAMICS%20Parameter%20ACTIVE%20INFEED%20CONTROL.md#r006908-co-phase-current-actual-value)[0...2] | CO: Phase currents actual value |
   | [r0075](SINAMICS%20Parameter%20ACTIVE%20INFEED%20CONTROL.md#r0075-co-reactive-current-setpoint) | CO: Field-generating current setpoint |
   | [r0076](SINAMICS%20Parameter%20ACTIVE%20INFEED%20CONTROL.md#r0076-co-reactive-current-actual-value) | CO: Field-generating actual current value |
   | [r0077](SINAMICS%20Parameter%20ACTIVE%20INFEED%20CONTROL.md#r0077-co-active-current-setpoint) | CO: Torque-generating current setpoint |
   | [r0078](SINAMICS%20Parameter%20ACTIVE%20INFEED%20CONTROL.md#r0078-co-active-current-actual-value) | CO: Torque-generating actual current value |
3. The scaling specifies the processing of the measured signal. This requires the definition of a straight line with two points.

   In the setting range of a measuring socket, click on the "Scaling" button.

   The "Scaling CU320 measuring socket Tx" dialog opens. You can define the values of a characteristic in this dialog.
4. In the dialog, select individual values within their defined limits, which are displayed in the relevant tooltips.

   - Characteristic value x2 ([p0779](SINAMICS%20Parameter%20CU.md#p077902-test-socket-characteristic-value-x2))
   - Characteristic value y2 ([p0780](SINAMICS%20Parameter%20CU.md#p078002-test-socket-characteristic-value-y2))
   - Characteristic value y1 ([p0778](SINAMICS%20Parameter%20CU.md#p077802-test-socket-characteristic-value-y1))
   - Characteristic value x1 ([p0777](SINAMICS%20Parameter%20CU.md#p077702-test-socket-characteristic-value-x1))

   Example: x1/y1 = 0%/2.49 V x2/y2 = 100%/4.98 V

   - 0.0% is mapped to 2.49 V.
   - 100.0% is mapped to 4.98 V.
   - -100.0% is mapped to 0.00 V.
5. Once all necessary settings have been made, click "Close".

   The dialog closes.
6. Enter the required offset value for the required measuring socket in the "Offset" field.

   The offset is applied additively to the signal to be output. The signal to be output can thus be displayed within the measuring range.

##### Function diagrams (FD)

- Diagnostics - Measuring sockets (T0, T1, T2) - 8134 -

##### Additional parameters

---

#### Isolated digital output (only CU310-2)

##### Description

You can change the interconnection for the digital output of the CU310-2 here.

The digital output is used for the feedback of signals, such as enable signals. The digital output is interconnected via a BICO interconnection.

##### Digital output

1. Interconnect the signal sink of the digital output 16.
2. If required, invert this output via the symbol.

   The symbol ![Digital output](images/147853723915_DV_resource.Stream@PNG-en-US.png) then indicates the inversion.

##### Control via onboard terminals

You can use the onboard terminals for Safety Integrated control by setting the function selection "Control" accordingly (see [Selecting the safety functionality](Servo%20drives%20%28highly%20dynamic%29.md#selecting-the-safety-functionality)).

1. Select the "via onboard terminals" setting.

   For more information, refer to Control.

##### Function diagrams (FD)

- CU310-2 input/output terminals - Digital output (DO 16) - 2038 -

#### Analog input (only CU310-2 PN)

##### Description

Here you can change the interconnection for the analog input.

The analog input is used for the acquisition of external analog signals. These signals can be voltages or currents, for example. Analog inputs are used, for example, for analog definition of a speed or torque.

##### Making basic settings

1. Select the basic configuration of the input signal for the analog input:

   - [0] Unipolar voltage input (0 V...+10 V)

     The analog input is configured as voltage input.
   - [2] Unipolar current input (0 mA...+20 mA)

     The analog input is configured as current input.
   - [3] Monitored unipolar current input (4 mA...+20 mA)

     The analog input is configured as current input. In addition, wire-break monitoring is active (see below).
   - [4] Bipolar voltage input (-10 V...+10 V)

     The analog input is configured as voltage input. The input range is +/-10 V.
   - [5] Bipolar current input (-20 mA...+20 mA)

     The analog input is configured as current input. The input range is +/-20 mA.
2. Enter the offset value for the analog input in the "Offset" field (p0763).

   The offset value is added to the input signal before the standardization characteristic.

##### Configure scaling of the analog input

The scaling serves to adapt to the machine or to the existing components. For example, even when the complete input range of the voltage or the current is not utilized, the input value can still be scaled to 100%.

1. Click the "Scaling" button to configure the scaling.

   The "Scaling TM31 analog input AI 0" dialog opens.
2. Enter the x and y values for two points of the scaling line:

   - y2:   
     Top scaling value as percentage, e.g. y2 = 100% with x 2 = 10 V means that 10 V at the input correspond to 100% at the output.
   - y1:   
     Low scaling value as percentage, e.g. y1 = -100% with x1 = -10 V means that -10 V at the input correspond to -100% at the output.
   - x1:   
     Low input value to be scaled.
   - x2:   
     High input value to be scaled.
3. Click "Close" to confirm the settings.

##### Specify filter for the analog input (optional)

Analog values are always subject to noise. You can suppress this noise with a filter.

The input signal can also be smoothed to suppress strong fluctuations or short-term peaks.

1. Enter the value for smoothing of the input signalin the "Smoothing" field (p0753).

   This value causes a smoothing of the input signal using a PT1 filter. However, a smoothing value which is too high makes the input slow.
2. Enter the value for noise suppression in the "Noise suppression" field(p0768).

   This suppresses the noise of the input signal according to the following function:

   - **|y-x| &gt; noise suppression results in y = x**

     The output value is set to the current input value.
   - **|y-x| ≤ noise suppression results in y = yold**

     The output value retains its value.

##### Configuring wire-break monitoring (optional)

Wire-break monitoring is used when the basic configuration "[3] Unipolar current input monitored (4 mA...+20 mA)" is set. In this case, the screen form is extended by two additional input fields.

1. Enter the wire-break monitoring response threshold in the "Threshold" field (p0761).

   If the threshold value is undershot for longer than the delay time, a wire break is detected.
2. Enter the delay time (p0762) for wire-break monitoring in the field to the right of the "Threshold" field.

   If the wire-break monitoring response threshold is undershot for longer than the delay time, a wire break is detected.

##### Additional functions (optional)

| Function | Description |
| --- | --- |
| Absolute-value generation | | Symbol | Meaning | | --- | --- | | 1. Switch on the absolute-value generation in the screen form if the absolute value of the scaled input value is to be generated.     The activated absolute-value generation is indicated by the ![Additional functions (optional)](images/147853746827_DV_resource.Stream@PNG-en-US.png) icon. |  | |
| Inversion | The signal source for inverting the analog input signals can be interconnected via a BICO interconnection. Inversion is disabled by default.   | Symbol | Meaning | | --- | --- | | 1. If you want to make an inversion, interconnect the signal source in the "Inversion" field. |  | |
| Activate | The signal source for enabling the analog input can be interconnected via a BICO interconnection. Enable is activated by default.   | Symbol | Meaning | | --- | --- | | 1. If required, correct the signal source. |  | |
| Analog input 0 | | Symbol | Meaning | | --- | --- | | 1. Here you interconnect the signal sink for the input value of the analog input.     Several interconnections are possible. |  | |
| Simulation mode | A simulation mode can be activated in online mode. |

##### Function diagrams CU310-2 (FD)

- CU310-2 input/output terminals - Analog input (AI 0) - 2040 -

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

Internal control/status words - Control word sequence control - 2501 -

Internal control/status words - Status word sequence control - 2503 -

Internal control/status words - Control word speed controller - 2520 -

Internal control/status words - Status word speed controller - 2522 -

Internal control/status words - Status word current control - 2530 -

Internal control/status words - Control word faults/alarms - 2546 -

#### Additional parameters

- [p0840](SINAMICS%20Parameter%20ACTIVE%20INFEED%20CONTROL.md#p08400n-bi-on-off-off1)
- [p0844](SINAMICS%20Parameter%20ACTIVE%20INFEED%20CONTROL.md#p08440n-bi-no-coast-down-coast-down-off2-signal-source-1)
- [p0845](SINAMICS%20Parameter%20ACTIVE%20INFEED%20CONTROL.md#p08450n-bi-no-coast-down-coast-down-off2-signal-source-2)
- [p0852](SINAMICS%20Parameter%20ACTIVE%20INFEED%20CONTROL.md#p08520n-bi-enable-operationinhibit-operation)
- [p3532](SINAMICS%20Parameter%20ACTIVE%20INFEED%20CONTROL.md#p3532-bi-infeed-inhibit-motoring)
- [p3533](SINAMICS%20Parameter%20ACTIVE%20INFEED%20CONTROL.md#p3533-bi-infeed-inhibit-generator-mode)
- [p0854](SINAMICS%20Parameter%20ACTIVE%20INFEED%20CONTROL.md#p08540n-bi-control-by-plcno-control-by-plc)
- [p2103](SINAMICS%20Parameter%20CU.md#p2103-bi-1st-acknowledge-faults)
- [p2104](SINAMICS%20Parameter%20CU.md#p2104-bi-2nd-acknowledge-faults)
- [p2105](SINAMICS%20Parameter%20CU.md#p2105-bi-3rd-acknowledge-faults)
- [p2112](SINAMICS%20Parameter%20CU.md#p2112-bi-external-alarm-1)
- [p2116](SINAMICS%20Parameter%20CU.md#p2116-bi-external-alarm-2)
- [p2117](SINAMICS%20Parameter%20CU.md#p2117-bi-external-alarm-3)
- [p2106](SINAMICS%20Parameter%20CU.md#p2106-bi-external-fault-1)
- [p2107](SINAMICS%20Parameter%20CU.md#p2107-bi-external-fault-2)
- [p2108](SINAMICS%20Parameter%20CU.md#p2108-bi-external-fault-3)
- [r0899](SINAMICS%20Parameter%20CU.md#r0899015-cobo-status-word-drive-object-1) (various bits)
- [r2139](SINAMICS%20Parameter%20CU.md#r2139015-cobo-status-word-faultsalarms-1) (various bits)
- [r0046](SINAMICS%20Parameter%20ACTIVE%20INFEED%20CONTROL.md#r0046029-cobo-missing-enable-signal) (various bits)

---

## Diagnostics

This section contains information on the following topics:

- [Communication](#communication)

### Communication

This section contains information on the following topics:

- [S120 Control Unit telegrams receive direction](#s120-control-unit-telegrams-receive-direction)
- [S120 Control Unit telegrams send direction](#s120-control-unit-telegrams-send-direction)
- [Servo PZD Send/Receive Direction Diagnostics](#servo-pzd-sendreceive-direction-diagnostics)

#### S120 Control Unit telegrams receive direction

##### Description

Here you specify the interconnections of the PROFIdrive telegram in the receive direction for the Control Unit.

Use the telegram configuration (![Description](images/147853831051_DV_resource.Stream@PNG-en-US.png)) to change the configuration of the telegrams or add telegram extensions.

**Telegram structure**

The interconnections for the process data in the receive direction are created automatically for the standard and manufacturer-specific telegrams.

If you select the Free telegram configuration, you can freely define the interconnections for the process data in the receive direction.

Only those telegrams available for the drive object are offered. The interconnections of the control words or receive words have already been created.

| Symbol | Meaning |
| --- | --- |
| ![Description](images/147853827083_DV_resource.Stream@PNG-en-US.png) | Click the button next to "Interconnections" to interconnect the signal for the connector output. |
| ![Description](images/147853816203_DV_resource.Stream@PNG-en-US.png) | Click the button to display and interconnect the signal bit by bit. |

The following information of the displayed telegrams is displayed:

| Telegram type | PZD | Display of the value | Format switchover | Control words | Interconnections |
| --- | --- | --- | --- | --- | --- |
|  | The numbering and arrangement of the process data. | Value of the process data (PZD) | Switching the value of the process data to a different display (hex, bin, dec). | List of the control words that are transmitted in the telegram. | Display or interconnection of the parameter with which the signal is to be interconnected. Several interconnections are possible. |
| PROFIdrive  390, 301, 392, 393, 394, 395 | X | X | X | X | X |
| Telegram extension | X | X | X | X | X |

##### S120 function diagrams (FD)

- PROFIdrive - PROFIBUS (PB) / PROFINET (PN), addresses and diagnostics - 2410 -
- PROFIdrive - Standard telegrams and process data 1 - 2415 -
- PROFIdrive - Standard telegrams and process data 2 - 2416 -
- PROFIdrive - Manufacturer-specific telegrams and process data 1 - 2419 -
- PROFIdrive - Manufacturer-specific telegrams and process data 2 - 2420 -
- PROFIdrive - Manufacturer-specific telegrams and process data 3 - 2421 -
- PROFIdrive - Manufacturer-specific telegrams and process data 4 - 2422 -
- PROFIdrive - Supplementary telegrams/free telegrams and process data - 2423 -
- PROFIdrive - STW1_BM control word metal industry interconnection - 2425 -
- PROFIdrive - STW2_BM control word metal industry interconnection - 2426 -
- PROFIdrive - ZSW1_BM status word metal industry interconnection - 2428 -
- PROFIdrive - ZSW2_BM status word metal industry interconnection - 2429 -
- PROFIdrive - PZD receive signals profile-specific interconnection - 2439 -
- PROFIdrive - PZD receive signals manufacturer-specific interconnection - 2440 -
- PROFIdrive - STW1 control word interconnection (p2038 = 2) - 2441 -
- PROFIdrive - STW1 control word interconnection (p2038 = 0) - 2442 -
- PROFIdrive - STW2 control word interconnection (p2038 = 0) - 2444 -
- PROFIdrive - PZD send signals profile-specific interconnection - 2449 -
- PROFIdrive - PZD send signals manufacturer-specific interconnection - 2450 -
- PROFIdrive - ZSW1 status word interconnection (p2038 = 2) - 2451 -
- PROFIdrive - ZSW1 status word interconnection (p2038 = 0) - 2452 -
- PROFIdrive - ZSW2 status word interconnection (p2038 = 0) - 2454 -
- PROFIdrive - IF1 receive telegram free interconnection via BICO (p0922 = 999) - 2468 -
- PROFIdrive - IF1 status words free interconnection - 2472 -
- PROFIdrive - IF1 receive telegram free interconnection via BICO (p0922 = 999) - 2481 -
- PROFIdrive - IF2 receive telegram free interconnection - 2485 -
- PROFIdrive - IF2 status words free interconnection - 2489 -
- PROFIdrive - IF2 receive telegram free interconnection - 2491 -
- PROFIdrive - CU_STW1 control word 1 Control Unit interconnection - 2495 -
- PROFIdrive - CU_ZSW1 status word 1 Control Unit interconnection - 2496 -
- PROFIdrive - STW1 control word 1 interconnection (r0108.4 = 1) - 2475 -
- PROFIdrive - SATZANW block selection interconnection (r0108.4 = 1) - 2476 -
- PROFIdrive - ZSW1 status word 1 interconnection (r0108.4 = 1) - 2479 -
- PROFIdrive - MDI_MOD MDI mode interconnection (r0108.4 = 1) - 2480 -
- PROFIdrive - POS_STW positioning control word interconnection (r0108.4 = 1) - 2462 -
- PROFIdrive - POS_STW1 positioning control word 1 interconnection (r0108.4 = 1) - 2463 -
- PROFIdrive - POS_STW2 positioning control word 2 interconnection (r0108.4 = 1) - 2464 -
- PROFIdrive - POS_ZSW1 positioning status word 1 interconnection (r0108.4 = 1) - 2466 -
- PROFIdrive - POS_ZSW2 positioning status word 2 interconnection (r0108.4 = 1) - 2467 -
- SI PROFIsafe - Standard telegrams - 2915 -
- SI PROFIsafe - Manufacturer-specific telegrams - 2917 -

#### S120 Control Unit telegrams send direction

##### Description

Here you specify the parameters of the PROFIdrive telegram in the send direction for the Control Unit.

Use the telegram configuration (![Description](images/147853831051_DV_resource.Stream@PNG-en-US.png)) to change the configuration of the telegrams or add telegram extensions.

**Telegram structure**

The interconnections for the process data in the send direction are created automatically for the standard and manufacturer-specific telegrams.

If you select the Free telegram configuration, you can freely define the interconnections for the process data in the send direction.

| Symbol | Meaning |
| --- | --- |
| ![Description](images/147853860363_DV_resource.Stream@PNG-en-US.png) | Click to the left next to "Column 1 / Column 2" on the button to interconnect the signal for the connector input. |

The following information of the displayed telegrams is displayed:

| Telegram type | Interconnections | Status words | Value | Format switchover | PZD |
| --- | --- | --- | --- | --- | --- |
|  | Display or interconnection of the parameter with which the signal is to be interconnected or is interconnected. | List of the status words that are transmitted in the telegram. | Value of the process data (PZD) | Switching the value of the process data to a different display (hex, bin, dec). | Numbering and arrangement of the process data. |
| PROFIdrive  390, 301, 392, 393, 394, 395 | X | X | X | X | X |
| Telegram extension | X | X | X | X | X |

##### S120 function diagrams (FD)

- PROFIdrive - PROFIBUS (PB) / PROFINET (PN), addresses and diagnostics - 2410 -
- PROFIdrive - Standard telegrams and process data 1 - 2415 -
- PROFIdrive - Standard telegrams and process data 2 - 2416 -
- PROFIdrive - Manufacturer-specific telegrams and process data 1 - 2419 -
- PROFIdrive - Manufacturer-specific telegrams and process data 2 - 2420 -
- PROFIdrive - Manufacturer-specific telegrams and process data 3 - 2421 -
- PROFIdrive - Manufacturer-specific telegrams and process data 4 - 2422 -
- PROFIdrive - Supplementary telegrams/free telegrams and process data - 2423 -
- PROFIdrive - STW1_BM control word metal industry interconnection - 2425 -
- PROFIdrive - STW2_BM control word metal industry interconnection - 2426 -
- PROFIdrive - ZSW1_BM status word metal industry interconnection - 2428 -
- PROFIdrive - ZSW2_BM status word metal industry interconnection - 2429 -
- PROFIdrive - PZD receive signals profile-specific interconnection - 2439 -
- PROFIdrive - PZD receive signals manufacturer-specific interconnection - 2440 -
- PROFIdrive - STW1 control word interconnection (p2038 = 2) - 2441 -
- PROFIdrive - STW1 control word interconnection (p2038 = 0) - 2442 -
- PROFIdrive - STW2 control word interconnection (p2038 = 0) - 2444 -
- PROFIdrive - PZD send signals profile-specific interconnection - 2449 -
- PROFIdrive - PZD send signals manufacturer-specific interconnection - 2450 -
- PROFIdrive - ZSW1 status word interconnection (p2038 = 2) - 2451 -
- PROFIdrive - ZSW1 status word interconnection (p2038 = 0) - 2452 -
- PROFIdrive - ZSW2 status word interconnection (p2038 = 0) - 2454 -
- PROFIdrive - IF1 send telegram free interconnection via BICO (p0922 = 999) - 2470 -
- PROFIdrive - IF1 status words free interconnection - 2472 -
- PROFIdrive - IF1 send telegram free interconnection via BICO (p0922 = 999) - 2483 -
- PROFIdrive - IF2 send telegram free interconnection - 2487 -
- PROFIdrive - IF2 status words free interconnection - 2489 -
- PROFIdrive - IF2 send telegram free interconnection - 2493 -
- PROFIdrive - CU_STW1 control word 1 Control Unit interconnection - 2495 -
- PROFIdrive - CU_ZSW1 status word 1 Control Unit interconnection - 2496 -
- PROFIdrive - STW1 control word 1 interconnection (r0108.4 = 1) - 2475 -
- PROFIdrive - SATZANW block selection interconnection (r0108.4 = 1) - 2476 -
- PROFIdrive - ZSW1 status word 1 interconnection (r0108.4 = 1) - 2479 -
- PROFIdrive - MDI_MOD MDI mode interconnection (r0108.4 = 1) - 2480 -
- PROFIdrive - POS_STW positioning control word interconnection (r0108.4 = 1) - 2462 -
- PROFIdrive - POS_STW1 positioning control word 1 interconnection (r0108.4 = 1) - 2463 -
- PROFIdrive - POS_STW2 positioning control word 2 interconnection (r0108.4 = 1) - 2464 -
- PROFIdrive - POS_ZSW1 positioning status word 1 interconnection (r0108.4 = 1) - 2466 -
- PROFIdrive - POS_ZSW2 positioning status word 2 interconnection (r0108.4 = 1) - 2467 -
- SI PROFIsafe - Standard telegrams - 2915 -
- SI PROFIsafe - Manufacturer-specific telegrams - 2917 -

#### Servo PZD Send/Receive Direction Diagnostics

##### Description

You can display a diagnosis of the status or control words of the selected telegram here.

##### Function diagrams (FD)

- PROFIdrive - PZD receive signals profile-specific interconnection - 2439 -
- PROFIdrive - STW1 control word interconnection (p2038 = 2) - 2441 -
- PROFIdrive - STW1 control word interconnection (p2038 = 1) - 2443 -
- PROFIdrive - POS_STW positioning control word interconnection (r0108.4 = 1) - 2462 -
- PROFIdrive - POS_STW1 positioning control word 1 interconnection (r0108.4 = 1) - 2463 -
- PROFIdrive - POS_STW2 positioning control word 2 interconnection (r0108.4 = 1) - 2464 -
- PROFIdrive - POS_ZSW1 positioning status word 1 interconnection (r0108.4 = 1) - 2466 -
- PROFIdrive - POS_ZSW2 positioning status word 2 interconnection (r0108.4 = 1) - 2467 -
- SI PROFIsafe - Standard telegrams - 2915 -
- SI PROFIsafe - Manufacturer-specific telegrams - 2917 -

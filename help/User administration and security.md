---
title: "User administration and security"
package: StdrSecurityUMACenUS
topics: 48
source: Siemens TIA Portal Information System (offline help, en-US)
---


# User administration and security

This section contains information on the following topics:

- [Overview](#overview)
- [Security default settings for projects (as of SINAMICS FW V6.1)](#security-default-settings-for-projects-as-of-sinamics-fw-v61)
- [Security settings for the drive (as of SINAMICS FW V6.1)](#security-settings-for-the-drive-as-of-sinamics-fw-v61)
- [User management and access control (UMAC)](#user-management-and-access-control-umac)
- [Security Wizard (from SINAMICS firmware V6.1)](#security-wizard-from-sinamics-firmware-v61)
- [Secure communication with Trusted Devices (from SINAMICS firmware V6.1)](#secure-communication-with-trusted-devices-from-sinamics-firmware-v61)

## Overview

The security functions are automatically extended with the introduction of the new SINAMICS drives. All drives from firmware V6.1, are automatically assigned an extended security functionality.

### Expansion stages of the security functionality

Multi-level security functionality is available for SINAMICS drives in the TIA Portal application "Startdrive".

- [Security default settings for projects](#security-default-settings-for-projects-as-of-sinamics-fw-v61) as of SINAMICS FW V6.1

  You make standard security settings across projects via the TIA Portal.
- [Security settings for the drive](#security-settings-for-the-drive-as-of-sinamics-fw-v61) as of SINAMICS FW V6.1

  In the inspector window, make specific protection settings for the selected drive.
- [User management and access control (UMAC)](#user-management-and-access-control-umac)

  With the help of the user administration you can activate a project protection for Startdrive projects. Furthermore, as an "administrator" you specify the general roles and rights in the user administration and manage individual user accounts. Users can then only access the project in Startdrive by logging in. The drive itself can also be protected from SINAMICS firmware V6.1 and higher. If the drive is protected, then you must always log in to access the drive online. Drive protection (runtime) can only be deactivated by a completely restoring the factory settings (using an SD Card)
- [Security Wizard](#security-wizard-from-sinamics-firmware-v61) from SINAMICS firmware V6.1

  Using this wizard, you can already make the most important security settings for the drive when creating it in the Startdrive project. The wizard uses, for example, important basic settings from the user administration (e.g. roles and rights) for this purpose.
- [Secure communication with Trusted Devices](#secure-communication-with-trusted-devices-from-sinamics-firmware-v61) from SINAMICS firmware V6.1

  Connections between the operating unit and drives must be secure. By accepting certificates with secure connections, you classify drives as so-called "trusted devices".

### More information

> **Note**
>
> **Configuration Manual Industrial Cybersecurity**
>
> Detailed explanations on cybersecurity in SINAMICS and Startdrive can also be found in the Configuration Manual [SINAMICS Industrial Cybersecurity](https://support.industry.siemens.com/cs/us/en/view/109810578).

> **Note**
>
> **Protection when inserting SIMATIC controllers**
>
> SIMATIC controllers can also be protected in the project.
>
> For details on the required security settings, see the [Protection &amp; Security](Functional%20description%20of%20S7-1200%20CPUs%20%28S7-1200%29.md#using-the-security-settings-wizard-s7-1200) section.

> **Note**
>
> **Security information**
>
> In the "Basic security information", also observe the information provided in Chapter [Security information](Startdrive.md#cybersecurity-information).

## Security default settings for projects (as of SINAMICS FW V6.1)

This section contains information on the following topics:

- [Configuring access protection](#configuring-access-protection)
- [Configuring a timeout/project lock](#configuring-a-timeoutproject-lock)
- [Configuring default security settings](#configuring-default-security-settings)

### Configuring access protection

#### Overview

The security settings for user access are preset centrally in the TIA Portal settings. You can make the following access settings:

- Standard procedure for user authentication

  Defines the authentication procedure to be used (see below).
- Automatic project lock after a timeout

  For details, see "[User authentication after inactivity](#configuring-a-timeoutproject-lock)".

#### Default settings for access protection

| Group | Setting | Description |
| --- | --- | --- |
| User authentication | Standard authentication procedure | Specifies the authentication procedure to be used by default. You have the following selection:  - Request user name and password   When the project is opened, the logon dialog is displayed in which you can log on with an existing user account. - Use anonymous user   The anonymous user account does not require a password. Therefore, the project is opened directly without displaying the logon dialog. - Use a single sign-on session   When the project is opened, the user of the active single sign-on session is applied. The single sign-on logon dialog opens if a single sign-on session is not yet active. |
| Project lock | Activate automatic project lock | Specifies that the project is locked after the session inactivity timeout has expired. Authentication is required again to continue working on the project.   The project lock does not offer any protection when the anonymous user is used. |
| Session timeout for project user (minutes) | Specifies the duration of the session timeout on inactivity for project users and the anonymous user. For global users, this setting is taken from UMC. |  |

> **Note**
>
> **Project lock not available when control panel is active**
>
> An activated control panel results in the following restrictions:
>
> - The project lock cannot be activated.
> - The automatic project lock is not activated during inactivity.

#### Procedure

1. Select the "Options &gt; Settings" menu in Startdrive.

   The "Settings" screen is displayed in the work area.
2. In the secondary navigation, select menu "Security &gt; Access protection".
3. Select the standard procedure for user authentication (see Table "Default settings for access protection").
4. Optional: Select the option "Activate automatic project lock".
5. Assign a timeout time for local project users.

#### Result

The security settings made are automatically saved. The settings apply automatically to the current project and all additional projects that are subsequently processed.

### Configuring a timeout/project lock

#### Overview

In case of inactivity, a timeout can be set for the currently displayed project. This timeout applies to the entire project with activated project protection. The maximum time that can be set until a timeout is 60 minutes.

#### Procedure

If you want to activate or configure the timeout, proceed as follows:

1. Select the "Options &gt; Settings" menu in Startdrive.
2. In the secondary navigation of the settings, select the "Security &gt; Access protection" menu.
3. If you want to define a timeout, enable the "Activate automatic project lock for all user types" option.
4. In the "Session timeout for local project users (minutes)" field, enter the time in minutes after which the project is automatically locked.

   The timeout applies only to local users and single sign-on users.
5. Then save the project.

#### Result

The project is automatically locked after the timeout period. A new authentication is then required to obtain access.

> **Note**
>
> **Timeout settings are not synchronized**
>
> Timeout settings can differ in Startdrive and the web server. Example: You use both the web server and Startdrive to configure the drive. When doing this, different timeout settings of the two tools are not synchronized.
>
> Timeout settings can be set in the web server for each user account individually. In Startdrive, timeout settings apply across all user accounts.

### Configuring default security settings

#### Overview

In the standard security settings, you define whether the Security Wizard automatically opens when creating a drive in the displayed project.

You configure the security settings of the drive using the wizard.

#### Procedure

1. Select the "Options &gt; Settings" menu in Startdrive.

   The "Settings" screen is displayed in the work area.
2. In the secondary navigation, select menu "Security &gt; Default settings".
3. Activate or deactivate option "Do not display the wizard for the security settings for the drive after adding a drive".

#### Result

The default settings made are automatically saved.

---

**See also**

[User login](#user-login)

## Security settings for the drive (as of SINAMICS FW V6.1)

This section contains information on the following topics:

- [Overview](#overview-1)
- [Manually starting the Security Wizard](#manually-starting-the-security-wizard)
- [User Management &amp; Access Control (features)](#user-management-access-control-features)
- [Activating ports and protocols (features)](#activating-ports-and-protocols-features)
- [Interfaces and communication relations](#interfaces-and-communication-relations)
- [Encryption of the drive data](#encryption-of-the-drive-data)

### Overview

Separate security settings can be made in the inspector window for each drive in the project.

In the "Settings" tab, you find the following security settings under the navigation item "Protection &amp; Security":

- Wizard for security settings
- User Management and Access Control
- Ports and protocols
- Encryption of drive data

Details can be found on the following pages.

### Manually starting the Security Wizard

#### Overview

The Security Wizard opens automatically when you create a drive in the project. To correct the security configuration, you can manually call the Security Wizard again via the properties of the Inspector window.

#### Requirement

- To call the Security Wizard, you need a user account with the following function rights:

  - Open and edit the project
  - Edit hardware configuration
  - Manage users and roles

#### Procedure

1. In the Inspector window of a drive, select the "Protection &amp; Security &gt; Wizard for Security Settings" menu.
2. Click the "Start Security Wizard" button on the right.

   The "Security settings..." dialog opens. The "Select security configuration" step is displayed.

#### Result

The Security Wizard opens. You can configure the security settings.

Details on the settings are provided on Page [Security Wizard (from SINAMICS firmware V6.1)](#security-wizard-from-sinamics-firmware-v61).

### User Management & Access Control (features)

#### Overview

You can view the following UMAC settings for the drive in the "User Management &amp; Access Control" view:

- Activate UMAC for the drive
- Number of activated users with the right "Manage users and roles"
- The "Anonymous" user is activated.
- The "Anonymous" user is allowed to read data and acknowledge errors via all interfaces.
- The "Anonymous" user is allowed to write at least some data via all interfaces.
- The "Anonymous" user is allowed to read and write data via the fieldbus (when writing, changes to functional safety and user and role management are excluded).
- The "Anonymous" user is allowed to read and write data via the integrated Panel (SDI Standard).

  Note: This setting does not apply to SINAMICS S200 or S210 drives.

All the settings shown are made in the Security Wizard.

#### Requirement

- For the option "Activate UMAC for the drive" you need a user account with the following function rights:

  - Open and edit the project
  - Edit hardware configuration
  - Manage users and roles

#### Procedure

You can also activate the "Activate UMAC for the drive" option in the current view.

1. In the Inspector window, select the "Protection &amp; Security &gt; User Management &amp; Access Control" menu.
2. Then select or clear the "Activate UMAC for the drive" option.
3. Then load the project data with the UMAC settings into the drive.
4. Save the project data in the drive retentively.

**Note**

This option can be activated here independently of the project protection.

#### Result

The protection settings (UMAC) are applied to the drive.

> **Note**
>
> You can also deactivate the "Activate UMAC for the drive" option again in the project. However, if this security setting has already been loaded onto the drive, deactivation will be denied. A corresponding message then appears when loading the drive data.

---

**See also**

[Download UMAC to device (from SINAMICS firmware V6.1)](#download-umac-to-device-from-sinamics-firmware-v61)

### Activating ports and protocols (features)

#### Overview

In the "Ports and protocols" section, you activate the required protocols for the network interfaces to access the active drive.

| Security setting for interfaces | Parameter | Factory setting | Details |  |
| --- | --- | --- | --- | --- |
| **Ports and protocols** |  |  |  |  |
| X150: Web server access via HTTPS (port 443) | c8997[1] | Inactive | Communication security via TLS 1.2 and TLS 1.3. |  |
| X127: Web server access via HTTPS (port 443) | c8995[1] | Active | Communication security via TLS 1.2 and TLS 1.3. |  |
| X127: Web server access via HTTP (port 80) | c8995[3] | Inactive | No encryption  With Man-in-the-Middle and Replay attacks, data can be intercepted and manipulated. |  |
| **Configuration of fieldbus and associated protocols** |  |  |  |  |
| X150: Fieldbus protocol |  | PROFINET | The PROFINET Context Manager provides an endpoint mapper in order to establish an application relationship (PROFINET AR).   The setting options are drive-specific: |  |
| PROFINET | G220, S210, S200 |  |  |  |
| EtherNet/IP | G220, S210 |  |  |  |
| Modbus TCP | G220 |  |  |  |
| No protocol | G220 |  |  |  |
| X127 and X150: DCP (always activated) |  | Always active Cannot be changed | Discovery and Configuration Protocol (DCP)  Identifies PROFINET devices and allows basic settings to be made. |  |
| X127 and X150: SNMP (port 161) |  | Inactive | The Simple Network Management Protocol (SNMP) enables the reading out and setting of network management data (SNMP managed Objects) by an SNMP manager. SNMP V1 is used. |  |
| **Configuration of the S7 commissioning protocol** |  |  |  |  |
| X150: Access via the S7 protocol PCS7 (port 102) | c8997[2] | Inactive | No encryption and no authentication protection.  The Siemens S7 commissioning protocol can be used in secure PCS7 environments. |  |
| X127: Access via the S7 protocol PCS7 (port 102) | c8995[2] | Inactive |  |  |
| X150: Access via the secure S7 protocol Startdrive (port 102) | c8997[0] | Active | Communication security via TLS 1.2 and TLS 1.3.  The secure S7 commissioning protocol is used to establish communication between the Startdrive engineering tool and the drive. |  |
| X127: Access via the secure S7 protocol Startdrive (port 102) | c8995[0] | Active |  |  |
| **DHCP configuration** |  |  |  |  |
| X150: DHCP (port 68) |  | Inactive | SINAMICS drives can be integrated into industrial networks using the Dynamic Host Configuration Protocol (DHCP). A DHCP server automatically assigns information that is required, such as IP address, subnet mask and gateway. |  |
| X127: DHCP (port 68) |  | Inactive |  |  |

#### Requirement

- For the settings under "Ports &amp; Protocols", you need a user account with the following function rights:

  - Open and edit the project
  - Edit hardware configuration

#### Procedure

1. In the Inspector window of a drive, select the "Protection &amp; Security &gt; Ports and protocols" menu.
2. Activate all protocols required to access the drive.

   For security reasons, deactivate all protocols that you currently do not require to access the drive.
3. In the "Fieldbus protocol" selection, specify whether interface X150 should act as a PROFINET connection or as Modbus TCP connection.
4. Then load the project data with the interface settings into the drive.
5. Save the project data in the drive retentively.

#### Result

The interface settings are applied to the drive. Deactivated protocols cannot be used.

### Interfaces and communication relations

Different communication protocols are used for data transfer between drives and components or operating units. The following graphic shows a simplified representation of the possible connections and communication relations.

![Communication relations example](images/170621870475_DV_resource.Stream@PNG-en-US.png)

Communication relations example

### Encryption of the drive data

This section contains information on the following topics:

- [Fundamentals](#fundamentals)
- [Configuring encryption (features)](#configuring-encryption-features)
- [Configuring the encryption (Online &amp; Diagnostics)](#configuring-the-encryption-online-diagnostics)

#### Fundamentals

##### Overview

Sensitive drive data in the backup file and on the SD Card of the drive can be encrypted. Sensitive data are:

- UMAC user names
- Passwords

Encryption does not affect the commissioning procedure (going online, reading and changing data, downloading or uploading data). The drive parameters are not part of the encrypted data.

> **Note**
>
> **Saving the password in the project?**
>
> If the "Enable UMAC for the project" option is not enabled, the password cannot be saved in the project. A corresponding note appears.

> **Note**
>
> The encryption password is not subject to aging. It is independent of the higher-level security settings (see [Password policies](#setting-password-policies)). For this reason, it does not need to be renewed regularly.

##### Applications

You can use encryption both when project protection is enabled and when it is not. This results in different consequences:

| Protection setting | Consequence and measure |
| --- | --- |
| UMAC is activated for the project  UMAC is activated for the drive  Encryption is enabled | If project protection is enabled, the encryption password is saved with the project.   By loading the UMAC data into a drive, the UMAC settings from the project can also be assigned to a swapped drive. |
| UMAC is **not** activated for the project  UMAC is activated for the drive  Encryption is enabled | If project protection is disabled, the encryption password is not saved with the project. The password is then only stored in the drive.   This may require you to enter the password each time you access the drive's UMAC data.   **Lost password:**    Without the password it is not possible to disable encryption or restore from an encrypted backup file or SD Card. The UMAC data of the drive can no longer be changed in this case. In this case, the drive can only be completely reset via an SD Card.   - If you do not use project protection, store the password in a secure place, for example, in a password manager.    **Drive exchange:**   Encryption passwords may differ between the old drive and the new drive. For example, if the encryption passwords are different, you cannot transfer the UMAC data of a backup to the new drive.   - Therefore, assign the encryption password of the device still to be replaced before replacing the drive for the replacement drive. |

##### Tips and rules

- Manage your passwords in a password manager.
- Use the TIA Portal's password policy verification settings to check newly entered passwords for compliance in order to prevent trivial and thus insecure passwords, for example.
- If you use the same password for the individual drives of a plant, the risk increases if the password of a drive is compromised. In this case, all drives are vulnerable to attack through the same password.

#### Configuring encryption (features)

##### Overview

Sensitive drive data in the backup file and on the SD Card of the drive can be encrypted.

You can make the settings for this offline in the drive inspector window.

##### Requirements

- The password rules defined in Startdrive are known (see [Centrally defining password rules](#activating-project-protection)).
- For the encryption of drive data you need a user account with the following function rights:

  - Open and edit the project
  - Edit hardware configuration

##### Enabling encryption offline

1. Select the required drive in the project tree.
2. In the inspector window, select the menu "Protection &amp; Security &gt; Encryption of the drive data".
3. Activate the "Encrypt sensitive drive data" option.

   The "Specify password" button is activated.
4. To configure a password, click on button "Specify password".

   - Enter the required password twice in the password dialog.
   - Confirm your entry with "OK".
5. Complete the drive configuration and then save the project.
6. Load the drive data into the device.

##### Changing the password offline

1. Select the required drive in the project tree.
2. In the inspector window, select the menu "Protection &amp; Security &gt; Encryption of the drive data".
3. Click on "Change password" to change an existing password.

   A change dialog opens.
4. First enter the old password.

   Then enter the new password twice. Click "OK" to confirm.
5. Load the drive data into the device.

##### Canceling encryption completely

1. Select the required drive in the project tree.
2. In the inspector window, select the menu "Protection &amp; Security &gt; Encryption of the drive data".
3. Deactivate the "Encrypt sensitive drive data" option.

   A password dialog is displayed. A password must be entered in order that protection can be deactivated.
4. Enter the existing password in the password dialog. Confirm your entry with "OK".

   Protection is disabled.
5. Complete the drive configuration and then save the project.
6. Load the drive data into the device.

##### Result

You have configured the encryption of sensitive drive data in the Startdrive project. The data must be loaded onto the drive and retentively saved there for these settings to become active.

---

**See also**

[Download UMAC to device (from SINAMICS firmware V6.1)](#download-umac-to-device-from-sinamics-firmware-v61)
  
[Configuring the encryption (Online &amp; Diagnostics)](#configuring-the-encryption-online-diagnostics)

#### Configuring the encryption (Online & Diagnostics)

##### Overview

If there is an online connection to the drive, you can configure encryption for sensitive data directly in the drive. You then make the settings via Online &amp; Diagnostics.

UMAC user names and passwords are sensitive data.

##### Requirements

- The password rules centrally defined in Startdrive are known (see [Centrally defining password rules](#setting-password-policies)).
- You require Drive Administrator rights to protect confidential data.
- There is an online connection between the drive and the operating unit.

  The direct functions can only be executed in the online mode.

##### Activating protection online

1. Select the required drive in the project tree.
2. In the drive project tree, select menu "Online &amp; diagnostics".
3. Call up the "Functions &gt; Set password for encrypting drive data" menu in the secondary navigation.
4. Activate the "Encrypt sensitive drive data" option.

   The "Specify password" button is activated.
5. Click the "Specify password" button in the screen form to assign a password.

   - Enter the required password twice in the password dialog.
   - Confirm your entry with "OK".

   Protection for the drive is activated. You can make additional drive settings and subsequently save them.

##### Changing the password online

1. Select the required drive in the project tree.
2. In the drive project tree, select menu "Online &amp; diagnostics".
3. Call up the "Functions &gt; Set password for encrypting drive data" menu in the secondary navigation.
4. Click on "Change password" to change an existing password.

   A change dialog opens.
5. First enter the old password.

   Then enter the new password twice. Click "OK" to confirm.

   Protection for the drive is activated. You can make additional drive settings and subsequently save them.

##### Completely removing protection

1. Select the required drive in the project tree.
2. In the drive project tree, select menu "Online &amp; diagnostics".
3. Call up the "Functions &gt; Set password for encrypting drive data" menu in the secondary navigation.
4. Deactivate the "Encrypt sensitive drive data" option.

   A password dialog is displayed. A password must be entered in order that protection can be deactivated.
5. Enter the existing password in the password dialog. Confirm your entry with "OK".

   Protection is disabled.

##### Result

You have configured the encryption of sensitive drive data directly in the drive. The data must be retentively saved for these settings to be permanently active.

---

**See also**

[Configuring encryption (features)](#configuring-encryption-features)

## User management and access control (UMAC)

This section contains information on the following topics:

- [Fundamentals](#fundamentals-1)
- [Central user administration with UMC](#central-user-administration-with-umc)
- [Activating project protection](#activating-project-protection)
- [Project protection &amp; "Anonymous" user](#project-protection-anonymous-user)
- [Setting password policies](#setting-password-policies)
- [User administration](#user-administration)
- [Access control](#access-control)
- [User login](#user-login)
- [Logging in users with memorized credentials](#logging-in-users-with-memorized-credentials)
- [Changing a user](#changing-a-user)
- [User logoff](#user-logoff)
- [Activating or deactivating a project lock](#activating-or-deactivating-a-project-lock)
- [Download UMAC to device (from SINAMICS firmware V6.1)](#download-umac-to-device-from-sinamics-firmware-v61)

### Fundamentals

#### Overview

TIA Portal offers the possibility to use user management and access control (UMAC) for projects. This allows you to create and manage user accounts and roles in your project. The roles bundle different access rights for the project. Different users can thus also be granted different access rights to functions. Once the project protection has been activated, the project can only be opened and edited by authorized users.

> **Note**
>
> An activated project protection cannot be canceled.

#### More information

Detailed information on project protection can be found in the information system of the TIA Portal under "[Manage users and roles](Managing%20users%20and%20roles.md#managing-users-and-roles)".

### Central user administration with UMC

#### Overview

Optionally, you can install the "User Management Component UMC" TIA Portal software package on one or multiple computers; it provides a central user management. This creates a system of possibly collaborating UMC installations (UMC ring server, UMC server). Then you can define users and user groups in the UMC system or import them from the Windows Active Directory. When UMC is installed, you can access the UMC server from the TIA Portal to add the users and user groups defined there to the user management of the TIA Portal and use roles to assign them the required function rights in a TIA Portal project.

#### More information

Detailed information on the central user management of the UMC can be found in the information system of the TIA Portal under the keyword "[Basic information on global users and user groups](Managing%20users%20and%20roles.md#basics-of-global-users-and-user-groups)".

### Activating project protection

#### Overview

To protect your project from unauthorized access, use the user administration of the TIA Portal. By activating the project protection, you automatically create a project administrator. Additional user accounts can then be set up using this user account.

A project with activated project protection can only be opened and changed with a user account with sufficient rights.

> **Note**
>
> **No deactivation of the project protection**
>
> Once project protection has been activated, it cannot be deactivated again.

> **Note**
>
> For users that were created before activation of project protection, the password needs to be entered again. It is not possible to log into the project without entering the password again.
>
> The same applies to passwords in the protected drive after reloading the UMAC data into the drive.

#### Requirement

A project has been created.

#### Procedure

To activate project protection, follow these steps:

1. Open the "Security settings" folder in the project tree.
2. Double-click on the "Settings" navigation item.

   The editor for the user administration is opened and the area for project protection is displayed.
3. Click on "Protect this project".

   The "Protect project" dialog opens.
4. Enter an administrator name.
5. Enter a password.
6. Re-enter the password to confirm.
7. Optional: Enter a comment.
8. Confirm your entries with "OK".

**Note**

**Password policy**

The following policies are defined for the password when the user administration is activated for the first time:

- Minimum password length: 8 characters
- Minimum number of digits: 1
- Minimum number of special characters: 0
- At least one uppercase and one lowercase letter: Activated
- Number of recently used passwords blocked for reuse: 5
- Activate password aging: Deactivated

As project administrator, you can adapt these password policies afterwards to address your requirements.

#### Result

The project protection was activated. You are logged in as the project administrator with the user name and password you just entered. Now you can create additional local users, add global users or user groups from UMC, or create new roles.

#### Optional:

**Transferring protection settings from the project to the device (from SINAMICS FW V6.1)**

The "Download to device" function is used to transfer the drive data including the protection settings (user accounts, roles, password guidelines) from the project to the drive. The "Download UMAC to device" function transfers only the UMAC settings to the drive.

Details on this are provided on Page "[Download UMAC to device](#download-umac-to-device-from-sinamics-firmware-v61)".

---

**See also**

[User Management &amp; Access Control (features)](#user-management-access-control-features)

### Project protection & "Anonymous" user

#### "Anonymous" user account

When activating project protection, the "Anonymous" user account is automatically created in the project. This user account is used for unauthenticated access to the drive (no login required) and represents a security risk if used incorrectly. For security reasons, the anonymous user is deactivated when activating the project protection and must be activated before use (in the user administration).

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Data manipulation through access by anonymous users**  Users who are not logged in can read out the data of your project, and with the appropriate access rights they can also manipulate data and therefore destroy the machine. When activating the "Anonymous" user account, you will receive a security notice about the potential risk.   - For this reason, prevent regular access to the project using this user account. Do not assign roles with engineering access rights to the "Anonymous" user account. If UMAC is disabled on the drive or the "Anonymous" user has corresponding access rights for the drive, he could access the drive via the project without logging in. - Perform a risk analysis. Assign the user "Anonymous" only those roles with engineering access rights that do not pose a security risk as a result of the risk analysis. |  |

---

**See also**

[User Management &amp; Access Control (features)](#user-management-access-control-features)

### Setting password policies

#### Overview

You can specify the structure and complexity of the user passwords. Configure the following settings for this purpose:

| Setting | Meaning |
| --- | --- |
| Minimum password length | The minimum number of characters that the user password must have. |
| Minimum number of numerals | The minimum number of numeric characters that the user password must contain. |
| Minimum number of special characters | The minimum number of special characters that the user password must contain. |
| At least one uppercase and one lowercase letter | Specifies that the user password must contain at least one uppercase and one lowercase letter. |
| Number of last used locked passwords | Sets the number of recently used passwords that cannot be used as a new password. |
| Enable password aging | Specifies that the password only has a certain validity period and then expires. If this option is selected, the password must be changed within the password validity. If the password is not changed in time, the corresponding user can no longer log on to the configured project. A project administrator can still change the password for this user afterwards. |
| Password validity (days) | Sets the password validity in days, in which the password must be changed when the password is activated. |
| Prewarning time (days) | Sets how many days before the user's password expires, a warning is provided to the user. The warning time must be less than that for the password validity. |

#### Requirements

- A project is open.
- If the project is protected, you must be logged on with a user account that has the function rights "Open and edit the project" and "Manage users and roles".

#### Procedure

To set the password policies, follow these steps:

1. Open the project for which you want to set the password policies.
2. Open the "Security settings" folder in the project tree.
3. Double-click the "Settings" command.

   The editor for the user administration is opened and the area for project protection is displayed.
4. Select the navigation entry "Password settings for runtime and engineering".
5. Make all the desired settings.
6. Save the project.

#### Result

The rules apply to the entire project and, if protection is activated, also in the drive.

> **Note**
>
> The password complexity rules are checked the next time a password is changed.

### User administration

This section contains information on the following topics:

- [Rules](#rules)
- [Configuring user accounts](#configuring-user-accounts)
- [Assign roles to the user accounts](#assign-roles-to-the-user-accounts)
- [Changing your own password](#changing-your-own-password)

#### Rules

##### Description

The following rules apply when creating user accounts:

| Setting | Number |
| --- | --- |
| Maximum number of roles | In addition to the system-defined roles, you can create 20 user-defined roles. |
| Maximum number of user accounts | 64 |
| Maximum assignable roles to a user account | 10 |
| Role names (maximum number of digits) | 32 |
| User account name (maximum number of digits) | 100 |
| Maximum password length (maximum number of digits) | 120 |

#### Configuring user accounts

##### Overview

To manage local users in your project, you can perform the following actions:

- Create new local users (user account)
- Change data of a local user:

  - User name
  - Password
  - Authentication procedures
  - Runtime timeout
  - Comment
- Activate or deactivate users

  Only activated user accounts can log in to a protected project.

  All activated user accounts and the Anonymous user account (whether activated or not) are loaded onto the drive when loading UMAC settings.
- Delete local users
- Global users or user groups can also be used for the project.

> **Note**
>
> In a protected project, the "Engineering-Administrator" role must be assigned to at least one user.

##### Requirements

- A project is open.
- If the project is protected, you must be logged on with a user account that has the function rights "Open and edit the project" and "Manage users and roles".
- The "Users and roles" function view is open in the "Security settings".

##### Creating a user account

Proceed as follows to create a new local user:

1. Open the "Users" tab.
2. Click "&lt;Add new user&gt;".

   A submenu is opened in which you can select the user type.
3. Click "Add new local user".
4. Enter a user name.
5. Click on the arrow in the field "Password".
6. Enter a password.
7. Re-enter the password to confirm.
8. Select the "Password" authentication method.
9. Enter the desired runtime timeout.

   Runtime timeout is the time after which a user is logged out from a device. For drives, logout takes place when there is no activity.
10. If necessary, enter a comment.

    The new local user is created and activated by default. To work with this user account in the project and on the drive, assign the necessary roles to it.

> **Note**
>
> You can also create a new local user by copying an existing user. As a result, the assigned roles are also assigned to the copied user. However, you must assign a new password for the copied user.

##### Activating or deactivating a user account

Proceed as follows to activate or deactivate a user:

1. Open the "Users" tab.
2. Select the check box in the column before the user name to activate the respective user.
3. Clear the check box in the column before the user name to deactivate the respective user. The role assignment is maintained for deactivated users.

**Note**

Disabled users are not loaded onto the drive when loading UMAC settings.

**"Anonymous" user account**

You can also activate or deactivate the "Anonymous" user account in the same way. For security reasons, the anonymous user is deactivated and must be activated before use. Note that you can neither delete the anonymous user nor change his data. However, you can assign him function rights by means of roles, and deactivate him again at any time.

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Data manipulation through access by anonymous users**  Some functions of the drive, such as fieldbus communication, often require the use of the "Anonymous" user. Since this user basically does not require authentication, the attack surface on the drive is increased. This is because users can read and possibly even modify data from the project without logging in.  When you activate the anonymous user, the project security is reduced according to the extent of the rights that you grant to this user. When activating the "Anonymous" user account, you will receive a security notice about the potential risk.   - For this reason, prevent regular access to the project using this user account. Do not assign roles with engineering access rights to the "Anonymous" user account. Via the project, an anonymous user could access the drive without logging in. - Perform a risk analysis. Analyze the resulting risks and take the correspondingly required external security precautions. - Assign the "Anonymous" user only those engineering and runtime roles that do not pose a security risk as a result of your risk analysis. |  |

##### Editing a user account

Proceed as follows to change the data of a local user:

1. Open the "Users" tab.
2. Click in the field whose data you want to change. Note that you can change the time for "Runtime timeout" only if the check box is selected.
3. Change the user name, password, authentication method, runtime timeout or comment.

##### Deleting a user account

Proceed as follows to delete a local user:

1. Open the "Users" tab.
2. Select the user you want to delete.
3. Ensure that "Password" is set as authentication procedure. Appropriately correct this setting if required.
4. In the shortcut menu select the "Delete" command or use the &lt;Del&gt; key.

#### Assign roles to the user accounts

##### Overview

You can assign different roles and thus also function rights to the user accounts.

> **Note**
>
> For detailed information on managing roles, see the "[Managing roles](#managing-roles)" section.

##### Requirements

- A project is open.
- If the project is protected, you must be logged on with a user account that has the function rights "Open and edit the project" and "Manage users and roles".
- In "Security settings", screen form "Users and roles" is open.

##### Assigning roles to users

To assign roles to a user, follow these steps:

1. Open the "Users" tab.
2. Select the user to whom you want to assign roles.

   Multiple selection is not possible.
3. Enable the desired roles in the "Assigned roles" section.

##### Revoking role assignments for users

To revoke a role for a user, follow these steps:

1. Open the "Users" tab.
2. Select the user for whom you want to revoke role assignments.

   Multiple selection is not possible.
3. In the "Assigned roles" section, clear check marks for the roles that are no longer to be assigned to the user.

##### Displaying assigned function rights of a user account

Proceed as follows to display the assigned function rights of a local user:

1. Open the "Users" tab.
2. Select the user for whom you want to view the assigned function rights.

   Multiple selection is not possible.
3. In the bottom area of the "Users" tab open the "Assigned rights" tab.

#### Changing your own password

##### Overview

In principle, there are several options for changing the password. However, not every option is available for every user type:

- When a protected project is opened:

  Project users and global users that do not use the single sign-on procedure can change their password in the logon dialog.
- When working in a protected project, using the toolbar:

  Project users and global users that do not use the single sign-on procedure can change their password via the toolbar.
- When working in a protected or unprotected project, via the "Users and roles" menu:

  Project users can change their password via the menu "Security settings &gt; Users and roles". For protected projects, the two function rights "Open and edit the project" and "Manage users and roles" are required.

  A description for changing the password via the "Users and Roles" editor is provided in Chapter "[Configuring user account](#configuring-user-accounts)" in Section "Changing user account".

If you change your password as a project user, the password for this project will be changed. After loading the UMAC data into the drive, the password is then also changed in the drive.

##### Requirement

You are logged on with a user account with the "Open and edit the project" function right.

##### Changing the password when a protected project is opened

To change your password when you log on to the project, follow these steps:

1. Select the "Open" command in the "Project" menu.

   The "Open project" dialog opens. The list of the projects last used is displayed.
2. Select a protected project from the list.
3. Click "Open".

   The "Log on" dialog opens.
4. Click "Change password".

   The "Change password" dialog opens.
5. Enter your user name.
6. Enter your current password.
7. Enter your new password.
8. Enter your new password again for confirmation.
9. Click "OK" to change your password.

**Result:**

If you enter all the data correctly, your password will be changed. You can then use the new password when you log into this protected project.

After loading the UMAC data into the drive, the password is then also changed in the drive.

##### Changing a password when working in a protected project

To change your password while working in a protected project, follow these steps:

1. Open the project view.
2. Click the down arrow in the toolbar next to the button "User administration" (![Changing a password when working in a protected project](images/163309040139_DV_resource.Stream@PNG-de-DE.png)).

   A drop-down list is opened in which the user management functions are listed.
3. Click "Change password".

   The "Change password" dialog opens.
4. Enter your user name.
5. Enter your current password.
6. Enter your new password.
7. Enter your new password again for confirmation.
8. Click "OK" to change your password.

**Result:**

If you enter all the data correctly, your password will be changed. You can then use the new password when you log into this protected project.

After loading the UMAC data into the drive, the password is then also changed in the drive.

### Access control

This section contains information on the following topics:

- [Overview](#overview-2)
- [Managing roles](#managing-roles)
- [Engineering rights](#engineering-rights)
- [Runtime rights (from SINAMICS firmware V6.1)](#runtime-rights-from-sinamics-firmware-v61)
- [Example: Function rights required for specific activities](#example-function-rights-required-for-specific-activities)

#### Overview

Each user requires "function rights" to access protected drive data. These function rights are summarized in roles and define which data and functions the respective user can access.

Each user can be assigned multiple system-defined roles. In addition, user-specific roles can also be created and assigned. This is done by a user who has the function right "Manage users and roles".

In regard to function rights, a distinction must be made between two groups:

- [Engineering rights](#engineering-rights)

  These always refer to a protected Startdrive project (UMAC for the project is enabled). However, these rights are also checked when accessing a protected drive.
- [Runtime rights](#runtime-rights-from-sinamics-firmware-v61)

  These always refer to a protected device accessed in online mode (UMAC for the drive is enabled).   
  Runtime rights are available for SINAMICS drives from SINAMICS firmware version V6.1.

  SINAMICS Startdrive and web server use the same runtime rights.

#### Managing roles

##### Overview

Rights are assigned to users via roles. Some system-defined roles are already available in the TIA Portal. In a protected project, these are the two roles "Engineering-Administrator" and "Engineering-Standard". Further system-defined roles exist for the drive itself.

You cannot rename or remove these roles. You cannot change the assignment of the function rights to these roles.

You can, however, define some roles and assign specific function rights to them. For self-created roles, you can change the following data of a role:

- Role name
- (Runtime timeout)

  This setting is only used for drives with a later program version.
- Comment
- Assignment of function rights

You can also delete your self-defined roles at any time.

You can display the assigned roles and function rights for each project user. This will give you an overview of the assigned rights at any time.

##### Requirements

- A project is open.
- If the project is protected, you must be logged on with a user account that has the function rights "Open and edit the project" and "Manage users and roles".
- The "Users and roles" function view is open in the "Security settings".

##### Defining a new role

To define a new role, follow these steps:

1. Open the "Roles" tab.
2. Click "Add new role".
3. Enter a name for the role.
4. Optional: Correct the runtime Timeout.

   This setting is only used for drives with a later program version.
5. Optional: Enter a comment.

   The new role has been created.

> **Note**
>
> You can also create a new role by copying an existing role. This means the assigned role permissions are also assigned to the new role.

##### Assigning function rights or removing assignments

To assign function rights to a role or remove assigned function rights, follow these steps:

1. Open the "Roles" tab.
2. Select a role.

   Multiple selection is not possible.
3. In the lower area, open the tab with the category from which you want to assign or delete function rights.
4. Activate the function rights that you wish to assign to the role.
5. Deactivate the function rights that are no longer assigned to the role.

##### Changing the role

To change a role, follow these steps:

1. Open the "Roles" tab.
2. Click in the field whose data you want to change.
3. Change the name, runtime timeout or comment.

##### Deleting a role

To delete a role, follow these steps:

1. Open the "Roles" tab.
2. Select the role that you want to delete.

   System-defined roles "Engineering-Administrator" and "Engineering-Standard" cannot be deleted.
3. Select "Delete" from the shortcut menu or press key &lt;Del&gt;.

#### Engineering rights

##### Assignment of the engineering function rights to the individual roles

Engineering function rights are required for the offline configuration of the converter of the TIA Portal application Startdrive. But even with online access, engineering function rights are additionally checked in many working areas.

| Engineering function rights | System-defined roles |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Engineering-Administrator | Engineering-Standard | Drive Administrator <sup>1)</sup> | Drive Safety Engineer <sup>1)</sup> | Drive Engineer and Service <sup>1)</sup> | Drive Operator <sup>1)</sup> | Drive Guest <sup>1)</sup> |  |
| Open the project read-only | X | X | ‑ | ‑ | ‑ | ‑ | ‑ |
| Open and edit the project | X | X | X | X | X | ‑ | ‑ |
| Edit hardware configuration | X | X | X | X | X | ‑ | ‑ |
| Download to drives | X | X | X | X | X | ‑ | ‑ |
| Perform drive firmware update | X | X | X | X | X | ‑ | ‑ |
| Perform drive backup | X | X | X | X | X | ‑ | ‑ |
| Edit drive applications | X | X | X | X | X | ‑ | ‑ |
| Edit Safety Integrated drive application | X | ‑ | X | X | - | ‑ | ‑ |
| Create and edit traces | X | X | X | X | X | ‑ | ‑ |
| Control drive in manual mode | X | X | X | ‑ | ‑ | ‑ | ‑ |
| Download to other devices | X | X | ‑ | ‑ | ‑ | ‑ | ‑ |
| Import project texts | X | X | ‑ | ‑ | ‑ | ‑ | ‑ |
| Edit library types | X | X | ‑ | ‑ | ‑ | ‑ | ‑ |
| Upgrade project | X | ‑ | ‑ | ‑ | ‑ | ‑ | ‑ |
| Manage users and roles | X | ‑ | X | ‑ | ‑ | ‑ | ‑ |
| Display users and roles | X | - | X | - | - | ‑ | ‑ |
| Change project via Openness API | X | X | ‑ | ‑ | ‑ | ‑ | ‑ |
| Download to PLC | X | X | ‑ | ‑ | ‑ | ‑ | ‑ |
| Edit PLC program | X | X | ‑ | ‑ | ‑ | ‑ | ‑ |
| Edit safety-related project data | X | ‑ | ‑ | ‑ | ‑ | ‑ | ‑ |
| Monitor PLC program | X | X | ‑ | ‑ | ‑ | ‑ | ‑ |
| Control PLC program online | X | X | ‑ | ‑ | ‑ | ‑ | ‑ |
| Show the configuration of security modules | X | ‑ | ‑ | ‑ | ‑ | ‑ | ‑ |
| Edit the configuration of security modules | X | ‑ | ‑ | ‑ | ‑ | ‑ | ‑ |
| <sup>1)</sup> These roles are applicable as of SINAMICS FW V6.1 |  |  |  |  |  |  |  |

> **Note**
>
> **Maximum number of roles**
>
> In addition to the system-defined roles listed above, you can define an additional 20 roles (see "[Manage roles](Managing%20users%20and%20roles.md#managing-roles)").

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Data manipulation through access by anonymous users**  Users without login can read data from the project and possibly modify even it under the following conditions:   - The "Anonymous" user account is activated. - The "Anonymous" user account is assigned the function rights "Open the project read-only" or "Open and write project".   Unauthenticated access increases the attack surface on the drive. Therefore, proceed as follows:   - Perform a risk analysis and prevent unauthenticated access to the project using this user account if this is a result of the risk analysis.  Do not assign engineering access rights to the "Anonymous" user account. Via the project, an anonymous user could access the drive without logging in. |  |

##### Explanation of the engineering function rights

The following is an explanation of the engineering function rights for SINAMICS converters in Startdrive. The minimum requirement for opening a project is either the "Open project read-only" right or the "Open and edit project" right.

Without the "Open project read-only" right or the "Open and edit project" right, all other editing rights are not possible.

| Engineering function rights | Group | Explanation |
| --- | --- | --- |
| Open the project read-only | General | Allows a user to open the corresponding project, but not to modify it.   For all other activities, you need additional function rights. |
| Open and edit the project | General | Permits a user to open the corresponding project and also to modify it. Additional function rights may be required to perform specific functions. |
| Edit hardware configuration | General | Allows a user to edit the hardware configuration in the project. |
| Download to other devices | General | Permits a user to load project data into devices other than PLCs, operating panels or drives. |
| Import project texts | General | Permits a user to import project texts.   This function right is not required for exporting project texts. |
| Edit library types | General | Permits a user to edit the types in the project library. It merely controls the editing of types in the protected project, but does not protect the types themselves if the function right is not assigned to a user. Despite a missing function right, the user can copy types into an unprotected project, edit them there, and paste them back into the protected project. |
| Upgrade project | General | Permits a user to upgrade the project of an older version of TIA Portal to a newer version. |
| Manage users and roles | General | Permits a user to display and manage the users and roles within the project. |
| Display users and roles | General | Permits a user to view the users and roles within the project. |
| Change project via Openness API | General | Permits a user to access and modify the project via the Openness API.  When modifying via the Openness API, further function rights are necessary to change users and roles. |
| Create and edit traces | General | Allows a user to use trace functions and create trace configurations. Without this function right, the trace functions of the project tree can only be accessed in the read mode. Settings are then locked. |
| Download to drives | Drives | Permits a user to load project data and/or a backup of drive data into the drive. |
| Edit drive applications | Drives | Permits a user to edit the configuration of drives with Startdrive. This includes all parameterization, diagnostics, commissioning and DCC settings in the function view and parameter view.   Excluded from this are:   - Generally the safety configuration - Device configuration settings in the inspector window |
| Edit Safety Integrated drive application | Drives | Permits a user to edit the safety configuration of drives using Startdrive. This includes the safety configuration in the parameter lists. This also includes all settings for PROFIsafe telegrams (e.g. in the quick startup).  Using the Safety Integrated acceptance test also requires this function right. |
| Control drive in manual mode | Drives | Permits a user to access the control panel of a selected drive in the project. |
| Perform drive firmware update | Drives | Permits a user to perform a firmware update for the drive via the "Online &amp; diagnostics" function view. |
| Perform drive backup | Drives | Permits a user to create a backup of the drive data (zip file) and save it in a file directory on the operating unit. |
| Show the configuration of security modules | Security | Permits a user to display the configuration of security modules. However, changes cannot be made to the configuration. |
| Edit the configuration of security modules | Security | Allows a user to view and edit the configuration of security modules. |
| Download to PLC | PLC | Permits a user to upload the program to a CPU. This includes restoring the configuration of a device from an online backup. |
| Edit PLC program | PLC | Allows a user to edit the program settings of a PLC. |
| Edit safety-related project data | PLC | Allows a user to edit STEP 7 Safety project data. |
| Monitor PLC program | PLC | Permits a user to monitor the program of a CPU with an existing online connection and to perform related actions. |
| Control PLC program online | PLC | Permits a user to make changes to the data loaded in the device. |

#### Runtime rights (from SINAMICS firmware V6.1)

##### Assignment of runtime function rights to the individual roles

Runtime function rights are required in addition to engineering function rights for online access to the drive.

Web server uses the same runtime function rights to access the drive.

Assignment table

| Runtime right | System-defined roles |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Drive Administrator | Drive Safety Engineer | Drive Engineer and Service | Drive Operator | Drive Guest | Drive Ext. Role SDI Standard/Adv<sup>1)</sup> | Drive Ext. Role Fieldbus |  |
| Read drive data or acknowledge messages | X | X | X | X | X | X | X |
| Control drive in manual mode | X | X | X | X | ‑ | X | X |
| Perform drive diagnostics | X | X | X | ‑ | ‑ | X | X |
| Perform firmware update | X | X | X | ‑ | ‑ | X | X |
| Create backup or load drive data to Startdrive | X | X | X | ‑ | ‑ | X | X |
| Edit web server configuration | X | X | X | ‑ | ‑ | X | X |
| Edit device configuration or drive applications | X | X | X | ‑ | ‑ | X | X |
| Edit Safety Integrated application | X | X | ‑ | ‑ | ‑ | ‑ | ‑ |
| Manage users and roles | X | ‑ | ‑ | ‑ | ‑ | ‑ | ‑ |
| <sup>1)</sup> This role is not used for a SINAMICS S210 or S200 drive. These drives do not use SDI standard panels. |  |  |  |  |  |  |  |

> **Note**
>
> **Maximum number of roles**
>
> In addition to the system-defined roles listed above, you can define an additional 20 roles (see "[Manage roles](Managing%20users%20and%20roles.md#managing-roles)").

##### Extended roles for unauthenticated access via a fieldbus or SINAMICS SDI standard panel

Two extended roles are available for access via a fieldbus or SDI standard panel. These include both read and write rights for online access to the drive (see assignment table). Both extended roles can basically be assigned to all user accounts. If you are assigned to the "Anonymous" user, this allows unauthenticated access.

> **Note**
>
> **No SDI standard panel available?**
>
> Not all SINAMICS drives are equipped with an SDI standard panel. Example: SINAMICS S210 or S200.
>
> Without drives with SDI standard panel, the extended role "Drive Ext. Role SDI Standard/Adv" cannot be used via the "Anonymous" user account.

| Extended role | Explanation |
| --- | --- |
| Drive Ext. Role Fieldbus | If this role is assigned to user "Anonymous", then every user can read and write the settings without logging on via the supported fieldbus protocols. Fieldbus protocols are, for example, PROFINET, DCP, SNMP or S7 protocols PCS7.  Settings for Safety Integrated and for user and role administration cannot be edited with this role.   Since the supported fieldbus protocols do not support an explicit login process for users, the assignment of this extended role is often necessary for functioning fieldbus communication. It is also required for communication with PCS7 systems.   The function rights of this role only affect access via fieldbus protocols, which do not support an explicit user login process.   **Exception**:  Cyclic communication and data reading via DCP are not checked for access rights. |
| Drive Ext. Role SDI Standard/Adv | If this role is assigned to the "Anonymous" user, then every user can read and write the settings without logging on via the integrated SDI standard panel. Settings for Safety Integrated and for the user and role administration are the exception to this rule.   However, this role is also suitable for granting a small group of trusted users extended access to the drive via the SDI standard panel.   However, the requirement is that the converter is located in a lockable control cabinet or control cabinet room.   If a user is assigned this role, the function rights it contains only affect access via the integrated SDI standard panel. |

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Data manipulation through access by anonymous users**  Some functions of the drive, such as fieldbus communication, often require the use of the "Anonymous" user. Since this user basically does not require authentication, the attack surface on the drive is increased. This is because users can read and possibly even modify data from the project and the drive without logging in.  - Therefore, verify the assigned runtime roles and rights for the "Anonymous" user.  Analyze the resulting risks and take the correspondingly required external security precautions. |  |

#### Example: Function rights required for specific activities

Below you will find a list of the necessary function rights for standard activities.

In general, the following rules apply in Startdrive:

- Access to the project

  You only need engineering function rights in your user account.
- Access to the drive

  You need runtime function rights in your user account. Engineering function rights are also necessary, however, as they are queried when accessing the system.

| Activity | Engineering function rights (if offline and online) | Runtime function rights (if online) |
| --- | --- | --- |
| Acknowledge alarms | - Open the project read-only | - Read drive data or acknowledge messages |
| Create, delete or rename drive | - Open and edit the project - Edit hardware configuration | ‑ |
| Device view, Network view, Topology view | - Open and edit the project - Edit hardware configuration | ‑ |
| All settings under the "Properties" tab of the inspector window  (Exception: Safety telegram configuration) | - Open and edit the project - Edit hardware configuration | ‑ |
| Use control panel | - Open and edit the project - Control drive in manual mode | - Control drive in manual mode |
| Rotate &amp; optimize | - Open and edit the project - Control drive in manual mode - Edit drive applications | - Edit device configuration or drive applications - Control drive in manual mode |
| Execute the measuring functions | - Open and edit the project - Control drive in manual mode - Edit drive applications | - Edit device configuration or drive applications - Control drive in manual mode - Perform drive diagnostics |
| Evaluate traces | - Open and edit the project - Create and edit traces | - Perform drive diagnostics |
| Perform safety acceptance test | - Open and edit the project - Control drive in manual mode - Edit Safety Integrated drive application | - Control drive in manual mode - Perform drive diagnostics - Edit Safety Integrated application |
| Perform guided quick startup | - Open and edit the project - Control drive in manual mode - Edit hardware configuration - Edit drive applications - Download to drives | - Edit device configuration or drive applications - Control drive in manual mode - Create backup or load drive data to Startdrive |
| Load configuration from drive to project | - Open and edit the project - Edit hardware configuration - Edit drive applications - Edit Safety Integrated drive application | - Create backup or load drive data to Startdrive |
| Load configuration from project to drive | - Open and edit the project - Download to drives - Manage users and roles    (= if the user and role configuration is to be loaded onto the drive) | - Manage users and roles    (= if UMAC is part of the download) - Edit device configuration or drive applications - Edit Safety Integrated application    (= if the Safety Integrated configuration is changed) |
| Make all settings in the function view (except Safety) | - Open and edit the project - Edit drive applications | - Edit device configuration or drive applications |
| Make safety settings in the function view | - Open and edit the project - Edit Safety Integrated drive application   (= if safety settings were changed) | - Edit Safety Integrated application |
| Manage user-defined parameter lists | Depending on the parameter settings that are changed via the user-defined lists.  For safety parameters, the "Edit Safety Integrated application" function right is explicitly required. | Depending on the parameter settings that are changed via the user-defined lists.  For safety parameters, the "Edit Safety Integrated application" function right is explicitly required. |
| Configure signal interconnections | Edit hardware configuration  The required function rights depend on the settings and parameters used. | The required function rights depend on the settings and parameters used. |
| Restore factory settings | - Open and edit the project - Edit drive applications - Edit Safety Integrated drive application   (= if safety settings were changed) | - Edit device configuration or drive applications - Edit Safety Integrated application  The required runtime function rights depend on which factory settings are restored. |
| Restore Safety Integrated factory settings | - Open and edit the project - Edit Safety Integrated drive application | - Edit Safety Integrated application |
| Retentively save | - Open and edit the project - Edit drive applications | - Edit device configuration or drive applications |
| Restart the drive | - Open and edit the project - Edit drive applications | - Edit device configuration or drive applications |
| Perform firmware update in "Online &amp; diagnostics" | - Open and edit the project - Perform drive firmware update | - Perform firmware update |
| Save drive data to backup file | - Open and edit the project - Perform drive backup | - Create backup or load drive data to Startdrive |
| Restore drive data from backup file | - Open and edit the project - Download to drives | - Edit device configuration or drive applications |
| Online access by searching for accessible participants  (working with the life list) | ‑ | - Edit device configuration or drive applications - Perform firmware update  The required function rights depend on which actions are performed. |
| "Start Security Wizard" in the inspector window | - Open and edit the project - Edit hardware configuration - Manage users and roles | ‑ |
| All settings in the inspector window under "Protection &amp; Security" | - Open and edit the project - Edit hardware configuration | ‑ |
| Use Openness | - Modify project via Openness API | ‑ |

### User login

#### Overview

For SINAMICS drives (from SINAMICS FW V6.1), access protection comprises the following elements:

- Project protection for the Startdrive project
- Dedicated access protection for the drive (see "[Security Wizard](#security-wizard-from-sinamics-firmware-v61)")

If the project and drive are protected, you require the appropriate access rights for your user account and you must authenticate yourself by logging in.

If a Startdrive project is provided with a project protection, user authentication takes place when the project is opened. A successful login in the project also automatically enables access to the device data in online mode if the access rights of a user in the drive are configured accordingly. If the drive is protected, but the project is not, registration is required for online access to the drive.

A user name to which certain access rights are assigned via system-defined or self-defined roles is required for logging in. It is also necessary to enter a valid password. An administrator configures the login data of your user account (see [User administration](#user-administration)).

With the "Anonymous" user account, a simplified login without user name and password is only possible in exceptional cases (if the project settings allow it).

> **Note**
>
> **Multiple access**
>
> Several users with the appropriate function rights can simultaneously access a drive. No priority is given to any particular user.

#### Requirements

- UMAC is activated for the project (project protection)

  - Or -
- UMAC is activated for the drive (which you wish to access)

#### Procedure

You must authenticate yourself when opening a protected project or after a timeout:

1. Click "Open existing project" in the secondary navigation in the portal view of Startdrive.

   A selection of the projects last used is displayed to the right in the detailed view.
2. Select the required project from the list, and then click "Open".

   - Or -

   - Click "Browse", double-click the required project in your directory structure, select project file "*.ap18.x".
   - Then click the "Open" button.

   Since there is an active project protection, the "Login" dialog will open.
3. Select the user type. If you selected "Anonymous user" or "Single Sign-on", continue with Step 6. Otherwise, continue with Step 4.
4. Enter your user name.
5. Enter your password.
6. Click "OK".

**Note**

At this point you can change your password. A password change is mandatory in the following cases:

- If a global user logs on for the first time, if this has been specified in UMC.
- If a project user logs on after the password validity has expired.

Then perform the steps for changing the password; see [Changing the password](#changing-your-own-password).

#### Result

The selected project opens after you have successfully logged in. If the function rights of your user account permit it, you can now change the drive settings in the project. You can then establish an online connection to the device or load the configuration data to the drive.

An appropriate error message is output if the login was not successful.

#### Error messages for user login

| Message | Cause | Remedy |
| --- | --- | --- |
| The drive cannot be accessed with the current login information. | - The login was made with a user account that does not have the necessary access rights. - The user account used is deactivated. - The passwords entered during login were incorrect. - The user name is invalid. | As user, check whether you have access rights to the drive with your user account.   Check your password data (user name, password) Enter this data correctly when logging in. |
| The user was not able to be automatically authenticated. It is probable that different login data are configured for the project user and the device user. | - For the user account, different login data exist for the project and drive. | As administrator, you transfer the current user account data from the project to the drive, if applicable.   As user, you change the password of your user account in the drive. |
| The user password has expired. | - The user password has expired. | Change the password for your user account. |
| The password was not successfully changed. | - When changing the password, the existing password was not correctly entered. - Password rules were violated when entering the new password. | When changing the password, enter the existing and new password according to the valid password rules. The password rules are displayed when the password is entered. |

---

**See also**

[Configuring a timeout/project lock](#configuring-a-timeoutproject-lock)
  
[Logging in users with memorized credentials](#logging-in-users-with-memorized-credentials)

### Logging in users with memorized credentials

#### Overview

If project protection is activated in a Startdrive project, user authentication takes place when the project is opened. If the user's access rights are configured accordingly, a successful login to the project automatically also enables online access to drives and their device data.

In the following cases, logging in to the protected drive is still necessary when going online:

- The drive is protected. The Startdrive project through which you are accessing is not protected.
- The user account with which the user is currently logged into Startdrive does not exist in the drive, is disabled in the drive, has no rights in the drive, or has a different password there.
- The protected drive is accessed via the Life list.

In the above cases, a login would be required each time a user goes online. If there are frequent access changes to different drives, the user's complete login credentials must be entered in full when logging in.

To simplify operation, the login credentials of all drives in the project can remain active in a TIA Portal session. For this purpose, however, the corresponding flag options must be activated when logging in to the drive for the first time.

As long as the TIA Portal session is not terminated (e.g. by closing, logging off or a timeout), the login credentials for all drives that are called up via the project are then retained.

| Login credentials are retained after the initial login: | Login credentials are not retained in the following cases: |
| --- | --- |
| - For the selected user account. - For all drives that are to be accessed online from the project. - When accessing the drive via the Life list. | - For any other user account for new online connections. - For drives from another project that did not have flag options enabled when first accessed. |

#### Requirements

- Optional: UMAC is activated for the project (project protection).
- UMAC is activated for the drive (which you wish to access).
- The TIA Portal session must not be interrupted.

#### Procedure

When opening a protected drive, you must authenticate yourself and then you can enable specific flag options for the current Startdrive session:

1. Start online access to a protected drive from within the project.

   If a separate login is required for online access (see "Overview"), the "Log on to device" dialog opens.
2. Select the user type "Project user".
3. Enter your user name.
4. Enter your password.
5. Determine whether the login credentials you have just entered should be retained during the current Startdrive session.

   To do this, activate the "Remember login credentials for all drives in the project" option.
6. If the current user password of the TIA Portal is to overwrite the current password of the drive, activate the option "Overwrite the user's password in the device with the password from the currently logged in TIA Portal user".

   In this case, the deviating password of the drive is overwritten.
7. Click "OK".

#### Result

If you activated the flag options when logging in for the first time, the login process will be simplified the next time you log in.

In the login dialog you do not have to enter the user name and password again. To log in, simply close the login dialog with "OK".

An appropriate error message is output if the login was not successful.

---

**See also**

[Changing your own password](#changing-your-own-password)

### Changing a user

#### Overview

In a protected project you can change the logged-in user. The user can be changed in the same way as for online access to a protected drive.

> **Note**
>
> When changing users during online access to a protected drive, the credentials for existing online connections are not changed. Extended access rights of an administrator remain valid when changing to a user with lower rights.
>
> - Therefore, before changing the user, close all online connections to the drives where you are still logged in as a user.

#### Requirements

- A protected project is open.

  - Or -
- There is an online connection to a protected drive.

#### Procedure

To change the user, follow these steps:

1. Open the project view.
2. Click the down arrow in the toolbar next to the button "User administration" (![Procedure](images/163309040139_DV_resource.Stream@PNG-de-DE.png)).

   A drop-down list is opened in which the user management functions are listed.
3. Click "Change user".

   If there are still unsaved changes, the "Save project" dialog opens. You have the option of saving your changes.

   The "Change user" dialog opens.
4. Select the user type.
5. Enter your user name.

   This step is not necessary if you selected "Anonymous user" or "Single sign-on" as the user type.
6. Enter your password.

   This step is not necessary if you selected "Anonymous user" or "Single sign-on" as the user type.
7. Click "OK".

#### Result

The system automatically closes the project and opens it again if you change from a user without write permission to a user with write rights or vice versa. Editors for which the newly logged in user have no rights may also be closed.

### User logoff

#### Overview

You can log off explicitly from a protected project. The project is closed. Note that if you are logged on via single sign-on, you are then also logged out of the single sign-on session. To prevent this, close the project without logging off. This will keep you logged on to the single sign-on session and allow you to open other projects without repeating authentication if you have sufficient rights.

#### Requirement

A protected project is open.

#### Procedure

To log off the project, follow these steps:

1. Open the project view.
2. Click the down arrow in the toolbar next to the "User management" button.

   A drop-down list is opened in which the user management functions are listed.
3. Click "Log off and close the project".
4. If you have made changes to the project since the last time you saved it, a message is displayed. Then, specify whether the changes should be saved.

#### Result

If there are no unsaved changes, the project is closed directly.

### Activating or deactivating a project lock

#### Overview

Using the project lock, you can prevent unauthorized persons from accessing the project in your absence. This allows you to leave the project open while you are briefly away from your work station. You have two options for using the project lock:

- Lock project manually

  For users logged on with single sign-on, the single sign-on session is closed first. Then the project is locked.
- Lock project automatically on inactivity

  For local project users, you can define the duration of inactivity in the TIA Portal. For users logged on with single sign-on, the project is locked in the following cases:

  - The session timeout for the logged on global user expires. The single sign-on session is also closed.
  - The single sign-on session changes.
  - The single sign-on session is closed.

  If you have initiated a process in the TIA Portal that takes longer than this, the process is first completed and then the project is locked. If a dialog requiring user action is open, the project is only locked after the dialog is closed.

> **Note**
>
> **Increase security with a project lock:**
>
> - As a user, always lock the project when you leave your work station.
> - As an administrator, you should make the project lock mandatory for the entire company. For this purpose, you can define the automatic project lock on inactivity with a corresponding session timeout via an internal company settings file.
>
>   See also: [Exporting and importing settings](Introduction%20to%20the%20TIA%20Portal.md#exporting-and-importing-settings-1)

> **Note**
>
> **Anonymous user**
>
> You cannot lock the project if you are logged in as an anonymous user. This applies to both the manual and the automatic project lock.

> **Note**
>
> **Project lock is not available when control panel is active in Startdrive**
>
> As long as the control panel is active and you have master control over a drive, you cannot activate the project lock and the automatic project lock is also suspended in case of inactivity.

#### Requirements

- A protected project is open.
- You are not logged in as an anonymous user.

#### Lock project manually

To lock the project manually, follow these steps:

1. Open the project view.
2. Click the down arrow in the toolbar next to the "User management" button.

   A drop-down list is opened in which the user management functions are listed.
3. Click "Lock the project".

   The "Project locked" dialog opens. In this dialog, you can remove the project lock again or close the project.

#### Lock project automatically on inactivity

Details on this are provided on Page "[Timeout/Configuring a project lock](#configuring-a-timeoutproject-lock)".

#### Unlock projects for local project users

Proceed as follows to remove the project lock for local project users:

1. In the "Project locked" dialog, enter the correct password for the logged-on user.
2. Confirm the entries with &lt;Enter&gt; or click "Unlock".

   Alternatively, you can also close the project if you do not want to log on again. Changes that have not been saved are discarded.

#### Remove project lock for single sign-on users

To remove the project lock for single sign-on users, follow these steps:

1. In the "Project locked" dialog, click "Unlock".

   If there is still an active single sign-on session for the user who caused the project to be locked, the project is unlocked. However, if there is no single sign-on session or if the single sign-on session is for another user, the logon window for the single sign-on session is displayed. In this case, perform step 2.

   Alternatively, you can also close the project if you do not want to log on again. Changes that have not been saved are discarded.
2. Log on with the user data of the user who locked the project. A different user cannot remove the project lock.

### Download UMAC to device (from SINAMICS firmware V6.1)

#### Overview

The UMAC settings of the project are optionally loaded with the project data into the drive ("Downloading project data to the device"). If required, you can also load the UMAC settings separately from the project into the drive. The following UMAC data can be loaded:

- UMAC password policy
- UMAC assignment of roles to function rights
- UMAC user accounts (including assigned roles)

#### Requirements

- There is an online connection between the operating unit and the drive.
- The protection (UMAC) is activated in the project settings for the drive.
- There is an active user account in the project that is assigned the "Drive Administrator" role (see [Runtime rights](#runtime-rights-from-sinamics-firmware-v61)).

  - Or -

  An active user account exists in the project, which is assigned the "Manage users and roles" right for the drive via a role.

#### Procedure

Follow these steps to download the UMAC settings to the device in online mode:

1. Select the required drive in the project tree.
2. Call shortcut menu "Download UMAC to device".

   The requirements for downloading the UMAC settings are checked.

   If the check is successful, a notice appears stating that the UMAC settings will be overwritten in the drive.
3. Confirm this notice.

#### Result

The UMAC settings are loaded into the drive and can be saved there permanently.

## Security Wizard (from SINAMICS firmware V6.1)

This section contains information on the following topics:

- [Overview](#overview-3)
- [Configuring security settings](#configuring-security-settings)
- [Editing security settings](#editing-security-settings)

### Overview

#### Description

For drives belonging to the latest SINAMICS generation (e.g. SINAMICS firmware V6.1), a Security Wizard supports you when making the basic security settings for the drive. After creating a new project, the basic setting of the project requires that the wizard is automatically started. One of the following conditions must additionally apply:

- You insert a new SINAMICS drive in the project tree.
- You insert a new SINAMICS drive in the hardware selection.
- You load project data from a drive (for which the factory settings have not yet been changed) into the project.  
  (applies only to loading for the first time or loading after resetting to factory settings)

The Security Wizard uses the user accounts managed in the user management (UMAC) and their assigned roles.

> **Note**
>
> **Deactivating automatic start**
>
> You can deactivate automatic start if you do not want this Security Wizard to open automatically.
>
> - Directly in the Security Wizard (see ③)
> - In the [overarching security presets](#configuring-default-security-settings)
>
> With this setting, the default settings of the Security Wizard are automatically applied to the drive. The only exception to this is the activation of project protection.

#### Structure of the Security Wizard

You can quickly and conveniently make the most important security settings for a drive in the project using the Security Wizard.

![Example: Security Wizard](images/164828040459_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Navigation of the individual configuration screens in the Security Wizard |
| ② | Displayed configuration screen in the wizard |
| ③ | Disable switch for future automatic opening of the Security Wizard |
| ④ | Toolbar for scrolling through the wizard or for completing or canceling the security settings |

Example: Security Wizard

#### Setting ranges

The following basic settings are possible in the Wizard:

- Make basic selection
- Configure access control
- Configure administrator
- Configure guest access for non-logged-in (anonymous) users
- Configuring fieldbus communication
- Configure access via a SINAMICS SDI standard panel

  Not visible for SINAMICS S210 or S200.
- Configure web server access
- Configure encryption of drive data

Each of these settings is explained in detail in the Security Wizard. At the end, all settings are once again summarized in an overview.

#### Starting/exiting

You can [manually start](#editing-security-settings) the Security Wizard again at any time via the "Start Security Wizard" button in the "Protection &amp; Security" area of the device configuration.

| Variant | Explanation |
| --- | --- |
| Close or cancel the Security Wizard | If you cancel the Security Wizard with "Close" or "X", the Security Wizard is closed. However, the wizard can be reopened later for the current drive.   Result: The default settings are transferred from the wizard. |
| **RELIABLY** exiting the Security Wizard | Use the "Exit" button if you wish to reliably exit the Security Wizard. In this case, the security settings that have been made are applied. However, the settings can also be subsequently changed.   The UMAC settings can only be subsequently loaded into the drive when the security configuration is safely completed. |

#### Download to device

For the security settings to become valid in the drive, this configuration data must be loaded into the drive with the UMAC settings.

> **Note**
>
> **Transferring UMAC data**
>
> Ensure that option "Refresh UMAC" is activated in dialog "Load preview". The activated option is the requirement that the UMAC data are also transferred to the drive.
>
> To download data to the device, your active user account must have function right "Download to drives".

Details are provided here:

- "[Download UMAC to device (from SINAMICS firmware V6.1)](#download-umac-to-device-from-sinamics-firmware-v61)"

### Configuring security settings

This section contains information on the following topics:

- [Making security settings](#making-security-settings)
- [Optional: Making low security settings](#optional-making-low-security-settings)

#### Making security settings

##### Overview

SINAMICS drives from SINAMICS firmware V6.1 and higher can already be protected via a Security Wizard when they are created in the project. The Security Wizard guides you through the settings when you create them and informs you about the effects of the settings. This allows you to determine at an early stage which protection you want to assign to the newly created drive. As a rule, you should set the best possible security level.

> **Note**
>
> **Dynamic default settings**
>
> Due to default settings elsewhere, security options may already be active in the Security Wizard settings areas. Not every individual default setting is described in the subsequent description.

> **Note**
>
> **Complete settings**
>
> The sequence of the security configuration subsequently described corresponds to achieving the best possible security level. If you configure individual steps other than as recommended, then the wizard does not always provide the next possible configuration step. However, in "Step 10 Overview", you are provided with an overview as to whether your security settings are valid. If this is not the case, then you are provided with information as to which settings are still missing or must be configured differently.

##### Requirements

- Ideally, project protection is enabled for the active project.

  This allows the user accounts created in the user administration settings to be used in the Security Wizard as well. In addition, the password for the encryption of the drive data is then stored in the project.

  If project protection is enabled, you need a user account with the "Manage users and roles" right to start the Security Wizard.
- Option "Do not show this dialog again" was not activated when creating another drive in this project.   
  - OR -

  The automatic start of the wizard has not been deactivated in the drive's default settings.
- The "Read drive data or acknowledge messages" function right is only assigned to the Anonymous user account via the Drive Guest role.

  If other roles with the same function right are assigned to the user account, guest access cannot be enabled.

##### Step 1: Start Security Wizard

With the appropriate default setting, the Security Wizard opens automatically when a SINAMICS drive is added to the project (via the project tree or the hardware catalog). The start page of the wizard is displayed.

1. To create a new security configuration for the drive, click the "Configure security settings" button.

   The setting area "Select security configuration" is displayed (Step 2).

   - Or -

   If you want to perform the security configuration at a later time, click the option "Continue with low security settings" instead (see [Security settings with low protection](#optional-making-low-security-settings)).

##### Step 2: Select security configuration

Proceed as follows if you wish to create a completely new configuration:

1. Activate option "Start new configuration with default settings".
2. Click "Next".

   The setting area "Activate user administration and access control" is displayed.

If, however, you wish to use the security configuration of another drive, then proceed as follows:

1. Activate option "Copy security settings of another drive".

   All security settings that should be applied in your drive are displayed below the option.
2. Then select the drive from which you want to copy the security settings.
3. Click "Next".

   The security settings of the selected drive are applied. In the next steps you can adapt the settings that have been applied.

   Setting area "Activate User Management and Access Control" is displayed.

##### Step 3: Activate User Management and Access Control

For a high level of security, the "Activate UMAC for the drive" setting is mandatory. As long as UMAC is not activated for the drive, no further detailed settings (Step 4ff.) are possible in the wizard for this. The "Activate UMAC for the project" protection is not mandatory. However, we recommend that you also activate this protection.

1. If project protection is not activated for the project, activate option "Activate UMAC for the project ...".

   If the project protection was already active, this option is automatically active. This option is also automatically active with a new security configuration.
2. Then activate option "Activate UMAC for the drive ...".

   This option is automatically active with a new security configuration.
3. Read through the information in the setting area and activate the option "I have read the information above and I understand the consequences of enabling UMAC".
4. Click "Next".

   The "Administrator setup" setting area is displayed.

##### Step 4: Administrator setup

In this step, an administrator with the runtime function right "Manage users and roles" is required. Only an administrator may subsequently change the user administration of the drive. The further procedure depends on whether you have activated UMAC only for the drive or additionally also for the TIA project in step 3.

**Case 1: UMAC is activated exclusively for the drive:**

If UMAC is only enabled for the drive, only a Drive Administrator can be defined at this point. When the Security Wizard is called for the first time, no user account exists yet for the Drive Administrator.

> **Note**
>
> When the Security Wizard is called again, a user account usually already exists. In this case, you can simply select the administrator.

1. In the "Create new user" area, enter the name and two times the password of the administrator.
2. To confirm all settings in this setting range, click "Next".

   The "Next" button becomes active only after all settings have been made in this area.   
   The Security Wizard then displays the "Guest access configuration" area.

**Case 2: UMAC is activated for the project and the drive:**

If UMAC is activated for the project and the drive, you can also define an administrator user account at this point.

| Requirement | Settings |
| --- | --- |
| Project protection is deactivated | There is no project administrator yet.   | Symbol | Meaning | | --- | --- | | 1. Enter the user name of a new project and drive administrator. 2. Then enter his user password two times. |  | |
| Project protection is activated. | With project protection, a project administrator automatically exists and is set by default. If other users with project administrator rights exist, you can choose between several users.   | Symbol | Meaning | | --- | --- | | 1. Select the desired user in the "Use existing user" drop-down list.     This project administrator is thus granted additional administrator rights for the drive. |  |   Alternatively, you can create a new user account for a drive administrator.   | Symbol | Meaning | | --- | --- | | 1. Activate the "Create new user" option. 2. Enter the user name of a new drive administrator. 3. Then enter his user password two times. |  | |
| Project protection is activated.  The project administrator also has administrator rights for the drive | No further action required. The project administrator is automatically set as the drive administrator as well. |

1. To confirm all settings in this setting range, click "Next".

   The "Next" button becomes active only after all settings have been made in this area.   
   The Security Wizard then displays the "Guest access configuration" area.

##### Step 5: Guest access configuration

In this step, you define whether users who are not logged in are to have guest access to the drive.

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Data manipulation through access by anonymous users**  Guest access by anonymous users represents a potential security risk. Through guest access, a potential attacker can identify security vulnerabilities in the system, and use this to gain unauthorized access.   - Apply suitable measures to ensure that only persons classified as trusted are assigned guest access to the drive data. |  |

If you enable guest access for users who are not logged in ("Anonymous"), this user has guest access via:

- The web server (on a selected drive)
- The "Startdrive" application in the TIA Portal
- Any other permitted interfaces

> **Note**
>
> By activating guest access, the user ("Anonymous") is not only activated for the selected drive, but for all drives within the project!
>
> The user ("Anonymous") is assigned the Drive Guest role for all drives in the project.

1. If you want to activate guest access for Anonymous, select the option "Activate guest access to the drive".

   The runtime function right "Read drive data or acknowledge messages" is associated with guest access.
2. To confirm all settings in this setting range, click "Next".

   The Security Wizard then displays the "Fieldbus communication" area.

**Note**

**Guest access cannot be activated**

Guest access for the user account Anonymous cannot be activated in the following case:

- The Anonymous user account is assigned a role (except Drive Guest) which also includes the function right "Read drive data or acknowledge messages" (e.g Drive Operator)

##### Step 6: Fieldbus communication

In this step you define whether drive data may be changed via fieldbus communication (e.g. PROFINET, DCP, SNMP, Siemens S7 commissioning protocol). Changes are then allowed via the "Anonymous" user without entering user name and password. This setting is enabled by default in the wizard.

By activating the access, the "Anonymous" user is automatically assigned the "Drive Ext. Role Fieldbus" role. This setting applies to all drives in the project as of SINAMICS firmware V6.1.

> **Note**
>
> By activating fieldbus communication, the user ("Anonymous") is not only activated for the selected drive, but for all drives within the project!
>
> The user ("Anonymous") is assigned the Drive Guest role for all drives in the project.

Proceed as follows, if you want to allow data changes via fieldbus communication:

1. Activate option "Allow data to be changed via fieldbus communication".
2. Click "Next".

   The "SINAMICS SDI Standard Panel access" area is displayed.

**Note**

**Fieldbus communication cannot be activated**

Fieldbus communication for the Anonymous user account cannot be activated when the following condition prevails:

- The Anonymous user account is assigned a role (except Drive Guest) which also includes the function right "Read drive data or acknowledge messages" (e.g Drive Operator)

##### Step 7: SINAMICS SDI standard panel access

In this step you define whether drive data may be changed via an SDI standard panel. Changes are then allowed via the "Anonymous" user without entering user name and password. This setting is enabled by default in the wizard.

> **Note**
>
> SINAMICS S210 does not use SDI standard panels. Therefore, access to the drive is not possible in this case. As a consequence, "SINAMICS SDI Standard Panel access" cannot be configured for an S210 or S200 drive.

By activating the access, the "Anonymous" user is automatically assigned the "Drive Ext. Role SDI Standard/Adv" role. This setting applies to all drives in the project as of SINAMICS firmware V6.1 (exception: S210 or S200).

> **Note**
>
> By activating the access, the user ("Anonymous") is not only activated for the selected drive, but for all drives within the project!
>
> The user ("Anonymous") is assigned the Drive Guest role for all drives in the project.

If you want to allow data changes via the SDI standard panel, proceed as follows:

1. Activate the "Allow drive data to be changed via the SDI Standard Panel" option.
2. Click "Next".

   The Security Wizard then displays the "Web server activation" area.

**Note**

**Communication via the SDI standard panel cannot be activated**

Communication for the Anonymous user account cannot be activated under the following condition:

- The Anonymous user account is assigned a role (except Drive Guest) which also includes the function right "Read drive data or acknowledge messages" (e.g Drive Operator)

##### Step 8: Web server activation

The SINAMICS web server access is deactivated in the factory setting.

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Data manipulation due to unprotected fieldbus cable**  In accordance with the Defence in Depth concept, the PROFINET interface must be isolated from the remaining plant network (see [Industrial Security](https://new.siemens.com/global/en/products/services/digital-enterprise-services/industrial-security-services.html)) in order to prevent unauthorized access and, in turn, data manipulation.   - Protect against access to cables and possibly open connections, for example, by installing in a control cabinet. |  |

1. Activate the option "Activate SINAMICS web server access via the PROFINET interface [X150] with HTTPS protocol".
2. To confirm all settings in this setting range, click "Next".

   The "Encryption of drive data" setting area is displayed.

##### Step 9: Encryption of the drive data

UMAC data can be encrypted in the backup files and on the SD Card of the drive.

Encryption does not affect the commissioning procedure (going online, reading and changing data, downloading or uploading data). The drive parameters are not part of the encrypted data.

> **Note**
>
> The encryption password is not subject to aging. For this reason, it does not need to be renewed regularly.
>
> However, follow the password complexity rules (see [Password policies](#setting-password-policies)).

You assign an appropriate password for encryption in this step.

1. Activate the "Encrypt sensitive drive data" option.
2. Click on "Specify password".

   The "Specify password" dialog opens.
3. Assign a password for the sensitive drive data and confirm the entry in the second input field.

   The password is displayed in encrypted form.
4. Click "Next".

   The "Overview" area is displayed.

**Note**

You can change the assigned password via the "Change password" button.

**Note**

**Saving the password in the project?**

If the "Enable UMAC for the project" option is not enabled, the password cannot be saved in the project. A corresponding note appears.

- If you wish to use encryption, also activate the "Enable UMAC for the project ..." option (step 3).

**Note**

**Storing a password securely**

Store your encryption password securely, because this password is needed for the following operations:

- Exchange of the drive
- Importing backups into the drive

##### Step 10: Summary (completing the security settings)

In the "Summary" area, the previous settings are summarized once again. You are also informed whether read and write access to all drives is possible via a fieldbus protocol or the SINAMICS SDI standard panel.

> **Note**
>
> **Security settings valid?**
>
> The Wizard checks your security settings. If your settings are incorrect or incomplete, then you obtain the corresponding information in the area. You cannot complete the configuration in the Security Wizard without correcting these settings. The "Finish" button is then locked.

1. Click on "Finish" if you wish to complete and accept the valid security settings.

   The security settings for the current drive are applied in the project.

##### Result

The drive is created in the project with the selected security settings. You can change these security settings at a later point in time via the "Protection &amp; Security" menu in the inspector window.

In order that the security settings are valid in the drive, the project data must be subsequently downloaded to the drive.

Details are provided on Page "[Download UMAC to device (from SINAMICS firmware V6.1)](#download-umac-to-device-from-sinamics-firmware-v61)".

---

**See also**

[Editing security settings](#editing-security-settings)
  
[Fundamentals](#fundamentals)

#### Optional: Making low security settings

##### Overview

SINAMICS drives from SINAMICS firmware V6.1 and higher can already be protected via a Security Wizard when they are created in the project.

If necessary, you can postpone the configuration of the security settings to a later time. However, the protection of the drive is then very low.

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Data manipulation due to low level of protection**  Inadequately protected drive data makes it easier for potential attackers to have unauthorized access to the drive. Data manipulation can cause the drive to malfunction or damage it.   - Only use low protection in absolute exceptional cases and only if you are certain that an outsider cannot access the drive (e.g. if the drive is not yet integrated into a network). - By applying suitable measures, ensure that the drive interfaces are mechanically protected and secured. - Make the settings that provide [complete protection](#making-security-settings) at the earliest time possible. |  |

##### Requirements

- Ideally, project protection is enabled for the active project.

  If project protection is enabled, you need a user account with the "Manage users and roles" right to start the Security Wizard.
- Option "Do not show this dialog again" was not activated when creating another drive in this project.

##### Step 1: Starting the Security Wizard

The Security Wizard usually opens automatically when a SINAMICS drive is created in the project (via the project tree or the hardware catalog). The start page of the wizard is displayed.

1. If you want to perform the security configuration at a later time, click the option "Continuing with low security settings".

   A safety note indicates that you have selected a low degree of protection. This security setting is not recommended.
2. Click "OK" to confirm the alarm.

   The "Overview" area is displayed.

##### Step 2: Summary (completing the security settings)

In the "Summary" area, the resulting settings are summarized once again.

1. If you want to change the settings, you can jump to the corresponding setting area of the wizard and make changes there.
2. Click on "Finish" if you want to complete and accept the settings.

   The security settings are applied to the newly created drive.

##### Result

The drive is created in the project with the selected security settings. You can change these security settings at a later point in time via the "Protection &amp; Security" menu in the Inspector window, for example, in order to correct a security setting.

In order that the security settings are active in the drive, the UMAC settings must be subsequently downloaded to the drive.

Details are provided on Page "[Download UMAC to device (from SINAMICS firmware V6.1)](#download-umac-to-device-from-sinamics-firmware-v61)".

### Editing security settings

#### Overview

You can adjust the existing security settings of a SINAMICS drive at any time via the properties of the drive in the inspector window. There you can also call up the Security Wizard again.

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Data manipulation due to low level of protection**  Inadequately protected drive data makes it easier for potential attackers to have unauthorized access to the drive. Data manipulation can disrupt or damage the drive and its environment.   - Observe the Defence in Depth concept (see [Industrial Security](https://new.siemens.com/global/en/products/services/digital-enterprise-services/industrial-security-services.html)) and disconnect all unnecessary interfaces from the rest of the plant network to prevent unauthorized access and thus data manipulation. - Make the settings that provide [complete protection](#making-security-settings) at the earliest time possible. |  |

#### Requirements

- The project manages SINAMICS drives from SINAMICS firmware V6.1.

  Drives with older firmware versions cannot be configured using the Security Wizard!
- Ideally, project protection is activated.

  If project protection is enabled, you need a user account with the "Manage users and roles" right to start the Security Wizard.
- Ideally, the drive has already been configured using the Security Wizard.

#### Procedure

> **Note**
>
> The following description refers to UMAC changes via the Security Wizard. You can also make further changes in the inspector window via the "Protection &amp; Security" menu.

You want to change the existing security settings for the drive. Proceed as follows:

1. Select the required drive in the project tree.
2. In the inspector window, select menu "Protection &amp; Security &gt; for Security Settings Wizard".
3. Click the "Start Security Wizard" button on the right.

   Dialog "Security settings..." opens and setting area "Select security configuration" is displayed.
4. Activate option "Edit current settings".

   If the security settings were previously configured with the wizard, you can change the settings in each setting area (see [Configuring security settings](#configuring-security-settings)).

   - Or -

   If you want to use the security settings of another drive in the project instead (if available):

   - Activate option "Copy security settings of another drive".
   - Then select the drive from which you want to copy the security settings.
5. Correct the necessary security settings and click "Next" in each setting area.
6. Click on "Finish" if you want to complete and accept the settings.

#### Result

The security settings are applied to the drive.

## Secure communication with Trusted Devices (from SINAMICS firmware V6.1)

This section contains information on the following topics:

- [Fundamentals](#fundamentals-2)
- [Certificate types](#certificate-types)

### Fundamentals

#### Overview

Connections between operating units and drives must be secure. By exchanging digital certificates, drives are classified as "Trusted Devices" and therefore as "secure". Secure communication is possible with these Trusted Devices.

When the SINAMICS drive is accessed for the first time, the required certificates are generated. Examples:

- When calling the "Online &amp; diagnostics" screen
- When calling the "Download to device" or "Extended download to device" dialogs
- When accessing the drive online via the search for "Accessible devices"

  Note: For this access, it is not necessary that a drive has been created in the project.

For subsequent access, the previously generated certificate is then valid. New certificates are generated only when needed (IP address changed or certificate expired).

#### Possible error messages

If you try to connect to a drive marked as "untrusted", the following error message may appear:

- The device certificate cannot be classified as "trusted" as the chain of trust is not complete.

**Remedy:**

Establish a new online connection to the drive. A new certificate is then automatically generated.

### Certificate types

#### Overview

A certificate is required to establish a secure connection to a SINAMICS drive. For drive generation from SINAMICS FW V6.1, the required certificates are generated automatically when the drive is accessed for the first time. Here, the drive acts as a certification authority, issuing the necessary certificates for communication.

> **Note**
>
> **Restoring factory settings**
>
> Saved digital certificates are not affected when executing the "Restore factory setting" Startdrive function. They are neither deleted nor overwritten. Certificates can only be removed again after a complete reset of all device settings (with SD Card).

#### Certificate attributes

In digital certificates, attributes provide information about the issuer of the certificate. The most common attributes are:

| Attribute | Meaning | Example |
| --- | --- | --- |
| O | Organization | SIEMENS |
| C | Country/region | DE |
| CN | Common name | SINAMICS Embedded Root CA  SINAMICS Embedded Issuing CA, serial number=&lt;SN&gt; |
| OU | Organizational unit | Copyright (C) SIEMENS AG 2022 All rights reserved |

> **Note**
>
> **Displaying certificates**
>
> You can view the details of your certificates when you initially connect to the drive.
>
> - To do this, click the "Show certificates" button in the "Connect to drive" message dialog.

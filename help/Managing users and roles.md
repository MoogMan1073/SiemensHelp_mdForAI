---
title: "Managing users and roles"
package: PEUMACenUS
topics: 53
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Managing users and roles

This section contains information on the following topics:

- [Basics of user management in the TIA Portal](#basics-of-user-management-in-the-tia-portal)
- [Single sign-on in the TIA Portal](#single-sign-on-in-the-tia-portal)
- [User management settings](#user-management-settings)
- [Function rights in the user management](#function-rights-in-the-user-management)
- [Activating project protection](#activating-project-protection)
- [Setting password policies](#setting-password-policies)
- [Managing local project users](#managing-local-project-users)
- [Managing global users and user groups](#managing-global-users-and-user-groups)
- [Activating or deactivating anonymous user](#activating-or-deactivating-anonymous-user)
- [Managing roles](#managing-roles)
- [Assigning roles](#assigning-roles)
- [Opening protected projects](#opening-protected-projects)
- [Changing your own password](#changing-your-own-password)
- [Changing a user](#changing-a-user)
- [Locking a project](#locking-a-project)
- [Logging off the project](#logging-off-the-project)

## Basics of user management in the TIA Portal

### Introduction

The TIA Portal provides the possibility to perform user management (UMAC - User Management and Access Control) for projects. This allows you to create and manage users and roles in your project. You can also protect your project and define the users who are allowed to perform specific functions. When you set up project protection, you are created as project administrator. You can then create additional users and assign them roles with specific rights. Once the project protection has been activated, the project can only be opened and edited by authorized users. Note that project protection cannot be revoked.

The project administrator can add the following users and user groups to a project:

- Local project users:

  Local project users are those defined and managed in a TIA Portal project. These user accounts are only valid for this one project. It makes sense to use project user accounts if the entire automation solution is created in one project.

  The system additionally creates the local project user "Anonymous". Authentication with a password is not required for this user. You can grant specific rights to this user by means of roles. Please note that the security of your project is greatly reduced if you assign too many rights to this user. The anonymous user is disabled by default and cannot be deleted.
- Global users and user groups:

  These user accounts are defined and managed outside the TIA Portal in UMC (User Management Component). Global users and user groups can be imported into the various TIA Portal projects in which these users will work. To add users and user groups from UMC, the corresponding rights are required in UMC. Global users can also use the single sign-on method for authentication.

For a user or a member of a user group to be able to log on to a protected project or runtime, the user or user group must be activated in the respective project.

You can assign specific roles to users or user groups, which in turn can be linked to the following function rights:

- General and specific engineering function rights
- System-defined Runtime function rights
- User-defined Runtime function rights

Several function rights can be assigned to a role. You can find additional information on function rights under "[Overview of function rights](#overview-of-function-rights)".

The following system-defined roles are available in a protected project:

- "Engineering administrator"

  The "Engineering administrator" role is assigned to the project user who was created first. This role has all engineering function rights by default. Each project needs at least one administrator who is allowed to edit the project and the security settings. In addition, other users may be assigned the right to manage users and roles.
- "Engineering standard"

  This role also has all engineering function rights with the exception of "Manage users and roles", "View security device configuration", "Edit security devices configuration", "Edit safety-related project data" and "Upgrade project".

You cannot change or delete these system roles. You can create additional roles and assign them the required function rights.

> **Note**
>
> **Additional local user managements**
>
> In addition to the user management for projects, there are additional user managements in certain areas of the TIA Portal, e.g. for WinCC Panels with Advanced Runtime.

### Settings for users

The following settings can be specified for a local project user:

- User name:

  Name of the local project user who must be used to log on to the project.
- Password:

  The password assigned by the administrator with which the project user can log on to the project. The project user can change the password later.
- Authentication method:

  Authentication method for runtime defined by the administrator. The authentication method is not evaluated in the TIA Portal. The following two methods are available:

  - Password: Logon is via a password which was defined in the TIA Portal or in UMC.
  - Radius: Logon is via a RADIUS server on which the password is stored. This option can only be used for devices that support logon via a RADIUS server.
- Runtime timeout

  The time after which a user is logged off from a device. Depending on the device, the logoff occurs only in case of inactivity or always after the set time. For more information, refer to the documentation of the corresponding device.
- Comment

  Comment on the respective project user.

### UMC - User Management Component

In addition, you can install the "User Management Component UMC" software package on one or multiple computers; it provides a central user management. This creates a system of possibly interactive UMC installations (UMC ring server, UMC server). Then you can define users and user groups in the UMC system or import them from the Windows Active Directory. When UMC is installed, you can access the UMC server from the TIA Portal to add the users and user groups defined there to the user management of the TIA Portal and use roles to assign them the required function rights in a TIA Portal project.

However, you cannot change the data of users and user groups added from UMC within the TIA Portal. For example, even as administrator in the project you cannot change passwords or other data of UMC users or UMC user groups. This is only possible in UMC. However, you have the option to synchronize user management in the TIA Portal with UMC or to check the synchronization status. This enables you to eliminate inconsistencies between the global users and user groups in UMC and the UMC users or UMC user groups already imported in the TIA Portal.

**Licensing on the UMC server**

- The UMC server is part of the installation data storage medium of the TIA Portal.
- With the installation of the software you can manage up to 10 user accounts without a license. You need a license for other user accounts.
- You can accumulate this license. If you have several licenses, the permissible quantity structure for user accounts is the sum of the licenses.
- The license is required for the ring server of the User Management Component domain. The license is offered as a rental license for 365 days, the Certificate of License (CoL) can be downloaded directly.

| Software/license | Article number |
| --- | --- |
| TIA Portal User Management Component (UMC)  Rental license for 100 user accounts and 365 days  Certificate of License for download | 6ES7823-1UE30-0YA0 |
| TIA Portal User Management Component (UMC)  Rental license for 4000 user accounts and 365 days  Certificate of License for download | 6ES7823-1UE10-0YA0 |

> **Note**
>
> **UMC documentation**
>
> The UMC installation file and the UMC documentation in English is available on the TIA Portal installation data storage medium ("..\support", "...\Documents\Readme\English").
>
> We highly recommend that you read the UMC documentation completely before you start working with the user management, especially the sections on "Secure Application Data Support (SADS)". SADS is mandatory for working with the user management in the TIA Portal.

See also: [User Management Component (UMC) in Siemens Industry Online Support](https://support.industry.siemens.com/cs/ww/en/view/109780337)

### User management in the TIA Portal and Multiuser Engineering

Note the following information when working with the user management in the TIA Portal in combination with Multiuser Engineering:

- You can only make changes to the user management of a multiuser project in a server session and not in the local sessions.
- When you upload a single-user project that is protected with user management to a multiuser server, the resulting multiuser project is also protected. The users and user groups contained in the project continue to exist with their passwords and can therefore continue to log into the local sessions of the multiuser project, provided they have the corresponding user rights.
- If you protect a previously unprotected local session using the user management, this protection is removed once again after checking-in and updating the local session, as the multiuser project on the server is not protected as a result. This also applies when several operators are protecting their local sessions.
- If you protect the multiuser project on the server using the user management, the local sessions created by this multiuser project are also protected as soon as these are updated.
- When you log off from your local session, which is protected using the user management, other users remain logged on to their local sessions of the multiuser project. You only log yourself off. Your local session is the closed as a result.
- If the multiuser project on the server is protected using the user administration during processing of your unprotected local session and your user account has not been assigned the "Open and edit the project" function right, you cannot check in any changes to your local session or update your local session.

More information on Multiuser Engineering can be found under "[Introduction to Multiuser Engineering](Using%20Multiuser%20Engineering.md#introduction-to-multiuser-engineering)".

### User management in the TIA Portal and technology objects

Note the following information when working with the user management in the TIA Portal in combination with technology objects:

- **Technology objects S7-1500/1500T Motion Control as of V3.0**

  To configure technology objects as of V3.0, the user needs the "Edit PLC program" function right.

  To use the editors for commissioning, kinematics trace and calibration online and to change values online, a user requires these three function rights:

  - Edit PLC program
  - Modify PLC program online
  - Monitor PLC program

  To be able to calibrate a kinematics offline, a user requires the "Edit PLC program" right.

  For diagnostics of technology objects, a user requires the "Monitor PLC program" right.
- **Technology objects S7-1200 Motion Control and PID**

  To configure the technology objects, a user needs the "Edit PLC program" function right.

  To configure hardware-dependent parameters, a user also needs the "Edit hardware configuration" function right.

  To use the editors for commissioning online and to change values online, a user requires these three rights:

  - Edit PLC program
  - Modify PLC program online
  - Monitor PLC program

  For diagnostics of technology objects, a user requires the "Monitor PLC program" right.
- **Openness**

  To edit technology objects with the Openness API, a user needs the same rights as for editing directly in STEP 7, in addition to the "Edit project via Openness API" function right.

### User management in the TIA Portal and SIMOTION configuration in SCOUT TIA

Note the following information when working with the user management in the TIA Portal with SIMOTION configuration in SCOUT TIA:

- To open and edit the SIMOTION configuration, the user needs the "Edit hardware configuration" function right.
- In the absence of the "Edit hardware configuration" function right, only SCOUT data are saved. In such a case, consistent synchronization with the TIA Portal is not possible.

---

**See also**

[Single sign-on in the TIA Portal](#single-sign-on-in-the-tia-portal)
  
[Basics of global users and user groups](#basics-of-global-users-and-user-groups)
  
[Useful information on the local user administration and access control (S7-1500)](Functional%20description%20of%20S7-1500%20CPUs%20%28S7-1500%29.md#useful-information-on-the-local-user-administration-and-access-control-s7-1500)
  
[User management settings](#user-management-settings)
  
[Function rights in the user management](#function-rights-in-the-user-management)
  
[Activating project protection](#activating-project-protection)
  
[Setting password policies](#setting-password-policies)
  
[Managing local project users](#managing-local-project-users)
  
[Activating or deactivating anonymous user](#activating-or-deactivating-anonymous-user)
  
[Managing roles](#managing-roles)
  
[Assigning roles](#assigning-roles)
  
[Opening protected projects](#opening-protected-projects)
  
[Changing your own password](#changing-your-own-password)
  
[Changing a user](#changing-a-user)
  
[Locking a project](#locking-a-project)
  
[Logging off the project](#logging-off-the-project)
  
[Protection concept for project data](Editing%20project%20data.md#protection-concept-for-project-data)

## Single sign-on in the TIA Portal

### Introduction

There is the option to use single sign-on for authentication in the TIA Portal using UMC (User Management Component). This means that a user only needs to authenticate once to work in a protected project or a Runtime. This requires that the default authentication procedure is set to "Single sign-on" in the TIA Portal settings and that there is a global user or global user group in the corresponding projects with the necessary function rights.

You can find more information about UMC and the path to the documentation under "[Basics of user management in the TIA Portal](#basics-of-user-management-in-the-tia-portal)".

### Configuring single sign-on

You can configure the single sign-on via either the command line of UMC or via the TIA Administrator.

You can find more information on this in the UMC documentation located on the TIA Portal installation data storage medium or in the online help for the TIA Administrator.

### UMC status application

If UMC is installed and single sign-on is configured, you can find the UMC status application in the notification area of the Windows taskbar. This application allows you to perform the following functions:

- Log on or off from a single sign-on session
- Changing a user
- Changing your password

The UMC status application also displays the user currently logged on.

## User management settings

This section contains information on the following topics:

- [Overview of user management settings](#overview-of-user-management-settings)
- [Changing user management settings](#changing-user-management-settings)

### Overview of user management settings

#### Overview

The following table shows the settings you can make for user management under "Security &gt; Access protection":

| Group | Setting | Description |
| --- | --- | --- |
| User authentication | Standard procedure | Specifies the authentication method to be used by default. You can choose between:  - "Request user name and password":   When the project is opened, the logon dialog is displayed in which you can log on with an existing user account.   See also: [Opening protected projects](#opening-protected-projects) - "Use anonymous user":   The anonymous user account does not need to enter a password. Therefore, the project is opened directly without displaying the logon dialog.   See also: [Activating or deactivating anonymous user](#activating-or-deactivating-anonymous-user) - "Use single sign-on session":   When the project is opened, the user of the active single sign-on session is applied. If no single sign-on session is active yet, the single sign-on logon dialog is opened. |
| Automatic project lock | Activate automatic project lock for all user types | Specifies that the project is locked after the session timeout has expired. Authentication is required again to continue working on the project. Note that you cannot lock the project if you are logged in as an anonymous user. |
| Session timeout for local project users (minutes) | Sets the duration of the session timeout for project users. For global users and single sign-on users, this setting is taken from UMC. |  |

In addition, under "General &gt; User Name", you can specify that the name of the logged-on user should be used as the user name.

See also: [Overview of the program settings](Introduction%20to%20the%20TIA%20Portal.md#overview-of-the-program-settings)

---

**See also**

[Changing user management settings](#changing-user-management-settings)

### Changing user management settings

#### Procedure

To change the user management settings, follow these steps:

1. Select the "Settings" command in the "Options" menu.

   The "Settings" window is displayed in the work area.
2. Select the group "Security &gt; Access protection" or "General &gt; General &gt; User name" in the navigation area.
3. Change the desired setting.

#### Result

The change becomes effective with the next logon.

---

**See also**

[Overview of user management settings](#overview-of-user-management-settings)

## Function rights in the user management

This section contains information on the following topics:

- [Overview of function rights](#overview-of-function-rights)
- [Function right "Open the project read-only"](#function-right-open-the-project-read-only)
- [Function right "Open and edit the project"](#function-right-open-and-edit-the-project)
- [Function right "View users and roles"](#function-right-view-users-and-roles)
- [Function right "Manage users and roles"](#function-right-manage-users-and-roles)
- [Function right "View security device configuration"](#function-right-view-security-device-configuration)
- [Function right "Edit security devices configuration"](#function-right-edit-security-devices-configuration)
- [Function right "View and edit SiVArc rules"](#function-right-view-and-edit-sivarc-rules)
- [Function right "Edit hardware configuration"](#function-right-edit-hardware-configuration)
- ["Creating and editing Traces" function right](#creating-and-editing-traces-function-right)
- [Function right "Edit library types"](#function-right-edit-library-types)
- [Function right "Edit project via Openness API"](#function-right-edit-project-via-openness-api)
- [Function right "Configure HMI"](#function-right-configure-hmi)
- [Function right "Download HMI device"](#function-right-download-hmi-device)
- [Function right "Maintain HMI device"](#function-right-maintain-hmi-device)
- [Function right "Edit safety-related project data"](#function-right-edit-safety-related-project-data)
- [Function right "Edit PLC program"](#function-right-edit-plc-program)
- [Function right "Download PLC"](#function-right-download-plc)
- [Function right "Modify PLC program online"](#function-right-modify-plc-program-online)
- [Function right "Monitor PLC program"](#function-right-monitor-plc-program)
- [Function right "Edit drive applications"](#function-right-edit-drive-applications)
- [Function right "Edit Safety Integrated application of the drive"](#function-right-edit-safety-integrated-application-of-the-drive)
- ["Control the drive in manual mode" function right](#control-the-drive-in-manual-mode-function-right)
- [Function right "Perform drive backup"](#function-right-perform-drive-backup)
- [Function right "Download to drives"](#function-right-download-to-drives)
- [Function right "Download to other devices"](#function-right-download-to-other-devices)
- [Function right "Import project texts"](#function-right-import-project-texts)
- [Function right "Upgrade project"](#function-right-upgrade-project)
- [Function right "Perform drive firmware update"](#function-right-perform-drive-firmware-update)

### Overview of function rights

You can assign specific roles to users or user groups, which in turn can be linked to different function rights. These function rights define which functions of the TIA Portal can be used by a user. The function rights are divided into engineering function rights and runtime function rights.

#### Engineering function rights

The following table provides an overview of the engineering function rights of a protected project in the TIA Portal:

| Function right | Description | Protection target |
| --- | --- | --- |
| [Open the project read-only](#function-right-open-the-project-read-only) | A user who has only this function right can open the project, but not modify it. | Project data |
| [Open and edit the project](#function-right-open-and-edit-the-project) | A user with this function right can open and modify the project. | Project data |
| [Upgrade project](#function-right-upgrade-project) | A user with this function right can upgrade the project. | Project data |
| [Import project texts](#function-right-import-project-texts) | A user with this function right can import project texts. | TIA Portal user interface |
| [View users and roles](#function-right-view-users-and-roles) | A user with this function right can view the users and roles of the project. | Project data |
| [Manage users and roles](#function-right-manage-users-and-roles) | A user with this function right can manage the users and roles of the project. | Project data |
| [View security device configuration](#function-right-view-security-device-configuration) | A user with this function right can view the configuration of security modules. | Project data |
| [Edit security devices configuration](#function-right-edit-security-devices-configuration) | A user with this function right can view and edit the configuration of security modules. | Project data |
| [View and edit SiVArc rules](#function-right-view-and-edit-sivarc-rules) | A user with this function right can view and edit SiVArc rules. | TIA Portal user interface |
| [Edit hardware configuration](#function-right-edit-hardware-configuration) | A user with this function right can change the hardware configuration. | TIA Portal user interface |
| [Creating and editing Traces](#creating-and-editing-traces-function-right) | A user with this function right can use the Trace functions. | TIA Portal user interface |
| [Edit library types](#function-right-edit-library-types) | A user with this function right can change library types. | TIA Portal user interface |
| [Edit project via Openness API](#function-right-edit-project-via-openness-api) | A user with this function right can edit a project via TIA Portal Openness. | TIA Portal Openness API |
| [Configure HMI](#function-right-configure-hmi) | A user with this function right can configure an HMI device. | TIA Portal user interface |
| [Download HMI device](#function-right-download-hmi-device) | A user with this function right can load a project onto an HMI device. | TIA Portal user interface |
| [Maintain HMI device](#function-right-maintain-hmi-device) | A user with this function right can perform maintenance tasks for an HMI device. | TIA Portal user interface |
| [Edit safety-related project data](#function-right-edit-safety-related-project-data) | A user with this function right can edit project data from STEP 7 Safety. | Project data |
| [Edit PLC program](#function-right-edit-plc-program) | A user with this function right can edit the PLC program offline. | TIA Portal user interface |
| [Download PLC](#function-right-download-plc) | A user with this function right can load the PLC program into a PLC or restore the configuration of a device from an online backup. | TIA Portal user interface |
| [Modify PLC program online](#function-right-modify-plc-program-online) | A user with this function right can modify the PLC program online. | TIA Portal user interface |
| [Monitor PLC program](#function-right-monitor-plc-program) | A user with this function right can monitor the PLC program. | TIA Portal user interface |
| [Download to other devices](#function-right-download-to-other-devices) | A user with this function right can download to devices that are not HMI devices or CPUs. | TIA Portal user interface |
| [Edit drive applications](#function-right-edit-drive-applications) | A user with this function right can edit the configuration of drives with Startdrive. All safety settings are excluded. | TIA Portal user interface |
| [Edit Safety Integrated application of the drive](#function-right-edit-safety-integrated-application-of-the-drive) | A user with this function right can edit the safety configuration of drives and carry out safety acceptance tests. | TIA Portal user interface |
| [Control the drive in manual mode](#control-the-drive-in-manual-mode-function-right) | A user with this function right may activate master control over the drive through the project, and then carry out targeted drive optimizations. | TIA Portal user interface |
| [Download to drives](#function-right-download-to-drives) | A user with this function right can use Startdrive to download the configuration from a project and/or a backup of drive data into the drive. | TIA Portal user interface |
| [Perform drive firmware update](#function-right-perform-drive-firmware-update) | A user with this function right can perform a firmware update for the drive via the "Online &amp; Diagnostics" function view. | TIA Portal user interface |
| [Perform drive backup](#function-right-perform-drive-backup) | A user with this function right can create a backup of the drive data (as a zip file) and save it in a directory on the operating unit. | TIA Portal user interface |

Each engineering function right has a specific protection target. The protection target is the area that is protected by the function right. The following protection targets are available:

- Project data

  The data in the project is protected with function rights aimed at "Project data" as the protection target. This is independent of whether the project is accessed via the TIA Portal user interface or via TIA Portal Openness API.
- TIA Portal user interface

  For the functional rights aimed at the "TIA Portal user interface" as the protection target, working with the corresponding interface area is protected. These can be entire editors or only specific functions. The project data is not explicitly protected.
- TIA Portal Openness API

  Write access to the project via TIA Portal Openness API is protected with function rights aimed at the "TIA Portal Openness API" as the protection target. The project data is not explicitly protected.

Some function rights can only be used when certain other function rights are also assigned. The dependent function rights are then also activated when you activate such a function right. For example, if you activate the "Edit PLC program" function right, the "Open and edit the project" function right is also activated at the same time. When the primary function right is deselected, the dependent function right is not deactivated, however.

#### Runtime function rights for WinCC Unified

In addition to the engineering function rights, there are Runtime function rights defined by the system for WinCC Unified. You also have the possibility to define your own function rights and organize them in groups.

You can find additional information under:

- [System-defined Runtime rights](Configuring%20users%20and%20roles%20%28RT%20Unified%29.md#system-defined-function-rights-rt-unified)
- [Managing user-defined Runtime rights](Configuring%20users%20and%20roles%20%28RT%20Unified%29.md#user-defined-function-rights-rt-unified)

#### Runtime function rights for SINAMICS Unified

For online access to protected SINAMICS drives, in addition to engineering function rights, runtime function rights are also required.

You can find additional information under:

- Runtime rights (from SINAMICS firmware V6.1)

---

**See also**

[Basics of user management in the TIA Portal](#basics-of-user-management-in-the-tia-portal)
  
[Users and roles with OPC UA function rights (S7-1500, S7-1500T)](Configuring%20automation%20systems.md#users-and-roles-with-opc-ua-function-rights-s7-1500-s7-1500t)
  
Function right "Compile HMI"

### Function right "Open the project read-only"

#### Description

The "Open the project read-only" function right allows a user to open the corresponding project, but not to modify it. This protects the data of the project. To be able to make changes, the user must receive the appropriate function rights in addition. However, the online and diagnostics view can be opened without additional function rights.

---

**See also**

[Overview of function rights](#overview-of-function-rights)
  
[Opening projects](Editing%20projects.md#opening-projects)

### Function right "Open and edit the project"

#### Description

The "Open and edit the project" function right allows a user to open the corresponding project and also to modify it. Additional function rights may be required to perform specific functions. S7-1500 Motion Control V1.0 and V2.0 technology objects can be used in full.

---

**See also**

[Overview of function rights](#overview-of-function-rights)
  
[Opening projects](Editing%20projects.md#opening-projects)

### Function right "View users and roles"

#### Description

The function right "View users and roles" allows a user to view the users and roles within the project.

> **Note**
>
> **Required additional function rights**
>
> - "Open and edit the project"

---

**See also**

[Overview of function rights](#overview-of-function-rights)

### Function right "Manage users and roles"

#### Description

The function right "Manage users and roles" allows a user to manage the users and roles within the project.

> **Note**
>
> **Required additional function rights**
>
> - "Open and edit the project"
> - "View users and roles"

---

**See also**

[Overview of function rights](#overview-of-function-rights)

### Function right "View security device configuration"

#### Description

The function right "View security device configuration" allows a user to display the configuration of security modules. However, changes cannot be made to the configuration.

> **Note**
>
> **Required additional function rights**
>
> - "Open the project read-only"

#### Additional information

You can find additional information in the section "Special features of user management for security functions".

---

**See also**

[Overview of function rights](#overview-of-function-rights)

### Function right "Edit security devices configuration"

#### Description

The function right "Edit security devices configuration" allows a user to view and edit the configuration of security modules.

> **Note**
>
> **Required additional function rights**
>
> - "Open and edit the project"
> - "Edit hardware configuration"

#### Additional information

You can find additional information in the section "Special features of user management for security functions".

---

**See also**

[Overview of function rights](#overview-of-function-rights)

### Function right "View and edit SiVArc rules"

#### Description

The function right "View and edit SiVArc rules" allows a user to display and edit the SiVArc rules.

> **Note**
>
> **Required additional function rights**
>
> - "Open and edit the project"

#### Additional information

You can find additional information in the section "SIMATIC Visualization Architect".

---

**See also**

[Overview of function rights](#overview-of-function-rights)

### Function right "Edit hardware configuration"

#### Description

The function right "Edit hardware configuration" allows a user to edit the hardware configuration in the project.

> **Note**
>
> **Required additional function rights**
>
> - "Open and edit the project"

Without the "Edit hardware configuration" function right, all actions that would lead to a change of the hardware configuration in the project are blocked in the following user interfaces:

- All tables and views in the hardware and network editor, including the device properties in the Inspector window
- Project navigation
- Supported connection parameter assignment for Open User Communication, for example, for configuration of the "TSEND_C" communication block (also requires the "Edit PLC program" right)
- Device-specific parameter assignment editors
- S7-1200 Motion Control configuration for hardware-dependent parameters
- SIMOTION configuration

---

**See also**

[Overview of function rights](#overview-of-function-rights)
  
[Configuring devices](Configuring%20devices%20and%20networks.md#configuring-devices)

### "Creating and editing Traces" function right

#### Description

The "Creating and editing Traces" function right makes it possible for a user to use Trace functions and generate Trace configurations.

> **Note**
>
> **Required additional function rights**
>
> - "Open and edit the project"

Without the "Creating and editing Traces" function right:

- All actions are blocked in the project tree in the device under "Traces".
- All actions are blocked in the project tree in "Pan-device functions" under "Project traces".

---

**See also**

[Overview of function rights](#overview-of-function-rights)

### Function right "Edit library types"

#### Description

The function right "Edit library types" allows a user to edit the types in the project library. It merely controls the editing of types in the protected project, but does not protect the types themselves if the function right is not assigned to a user. Despite a missing function right, the user can copy types into an unprotected project, edit them there, and paste them back into the protected project.

> **Note**
>
> **Required additional function rights**
>
> - "Open and edit the project"

The following table provides an overview of the use cases when working with types and versions and of whether the "Edit library types" function right is required for them:

| Object type | Use case | Function right required? |
| --- | --- | --- |
| Type | Create and release | Yes |
| Type | Edit | Yes |
| Type | Discard | Yes |
| Type | Duplicate | Yes |
| Type | Assign version | Yes |
| Type | Rename | Yes |
| Type | Copy, cut, paste, move, drag-and-drop, delete types | No |
| Type | Terminate connection | No |
| Type | Export and import library texts | Yes |
| Type | Upgrade | Yes |
| Type | Update library | No |
| Type | Update project | No |
| Type | Edit instance | Yes |
| Type | Rename instance | No |
| Type | Harmonize | No |
| Type | Clean up | No |
| Type | Instantiate | No |
| Type | Replace | No |
| Type | Fix inconsistencies in library management | No |
| Version | Edit | Yes |
| Version | Duplicate | Yes |
| Version | Copy, paste, delete | No |
| Version | Set as default | No |

---

**See also**

[Overview of function rights](#overview-of-function-rights)
  
[Library basics](Using%20libraries.md#library-basics)

### Function right "Edit project via Openness API"

#### Description

The function right "Edit project via Openness API" allows a user to access the project via the Openness API.

> **Note**
>
> **Required additional function rights**
>
> - "Open and edit the project"
> - The "Manage users and roles" function right is also required to manage users and roles.
> - For technology objects, the function rights that are required for the task directly in STEP 7 are needed also.

#### Additional information

You can find additional information in the section "Openness: Automating project creation".

---

**See also**

[Overview of function rights](#overview-of-function-rights)

### Function right "Configure HMI"

#### Description

The function right "Configure HMI" allows a user to configure HMI devices.

> **Note**
>
> **Required additional function rights**
>
> - "Open and edit the project"

#### Additional information

You can find additional information in the sections "Visualizing processes" and "Visualizing processes (RT Unified)".

---

**See also**

[Overview of function rights](#overview-of-function-rights)

### Function right "Download HMI device"

#### Description

The function right "Download HMI device" allows a user to download a project to an HMI device.

> **Note**
>
> **Required additional function rights**
>
> - "Open and edit the project"

#### Additional information

You can find additional information in the sections "Visualizing processes &gt; Compiling and downloading" and "Visualizing processes (RT Unified) &gt; Compiling and downloading".

---

**See also**

[Overview of function rights](#overview-of-function-rights)

### Function right "Maintain HMI device"

#### Description

The function right "Maintain HMI device" allows a user to carry out maintenance tasks on an HMI device.

> **Note**
>
> **Required additional function rights**
>
> - "Open the project read-only"

#### Additional information

You can find additional information in the sections "Visualizing processes &gt; Compiling and downloading" and "Visualizing processes (RT Unified) &gt; Compiling and downloading".

---

**See also**

[Overview of function rights](#overview-of-function-rights)

### Function right "Edit safety-related project data"

#### Description

The function right "Edit safety-related project data" allows a user to edit STEP 7 Safety project data.

> **Note**
>
> **Required additional function rights**
>
> - "Open and edit the project"

#### Additional information

You can find additional information in the help on "SIMATIC Safety".

---

**See also**

[Overview of function rights](#overview-of-function-rights)

### Function right "Edit PLC program"

#### Description

The function right "Edit PLC program" allows a user to edit the program of a PLC.

> **Note**
>
> **Required additional function rights**
>
> - "Open and edit the project"

A user without the "Edit PLC program" function right cannot use commands in the project tree, toolbars or menus if this would change the offline data of the program. The following work areas and the associated properties in the Inspector window are therefore opened write-protected:

- Programming editors and programming windows for the languages LAD, FBD, STL, SCL, GRAPH, ProDiag and CEM
- Editors of technology objects

  - Configuration
  - Commissioning
  - Kinematics trace (S7-1500T)
- Declaration tables for data blocks
- Declaration tables for PLC data types
- PLC tag tables
- Watch tables
- Force tables
- ProDiag overview editor and alarm editor (PLC alarms)
- Relation tables for software units
- ProDiag supervision settings
- Compare editor
- Detailed comparison for blocks
- Detailed comparison for PLC tag tables
- Detailed comparison for PLC data types
- Editor for OPC UA client interfaces
- Editor for OPC UA server interfaces
- Cross-reference list
- Call structure, dependency structure, assignment diagram and resources
- System diagnostics settings
- Message class editor

The following areas in the project tree cannot be opened without the "Edit PLC program" function right:

- Instruction profile editor
- Calibration of the kinematics technology object (S7-1500T)

In contrast, the following actions can also be performed by a user who does not have the "Edit PLC program" function right. Other function rights may be required:

- Import CAx data
- Import project texts
- Compile and go online
- Import data of a project server by updating the local session
- Automatically create system and clock memory bits in the device configuration with the "System and clock memory" setting

#### Additional information

You can find additional information in the section "Programming a PLC".

---

**See also**

[Overview of function rights](#overview-of-function-rights)

### Function right "Download PLC"

#### Description

The "Download PLC" function right allows a user to download the program to a CPU. This includes restoring the configuration of a device from an online backup.

> **Note**
>
> **Required additional function rights**
>
> - "Open and edit the project"

---

**See also**

[Overview of function rights](#overview-of-function-rights)
  
[Basics for compiling and downloading PLC programs](Compiling%20and%20downloading%20PLC%20programs.md#basics-for-compiling-and-downloading-plc-programs)
  
[Restoring the software and hardware configuration of a device (S7-300, S7-400, PC)](Creating%20a%20backup%20of%20an%20S7%20CPU.md#restoring-the-software-and-hardware-configuration-of-a-device-s7-300-s7-400-pc)
  
[Restoring the configuration of a device (S7-1200, S7-1500)](Creating%20a%20backup%20of%20an%20S7%20CPU.md#restoring-the-configuration-of-a-device-s7-1200-s7-1500)

### Function right "Modify PLC program online"

#### Description

The "Modify PLC program online" function right allows a user to make changes to the data downloaded to the device.

> **Note**
>
> **Required additional function rights**
>
> - "Open and edit the project"

The function right is required for the following actions:

- Modifying tags in all editors, menus and toolbars
- Loading snapshots as actual values
- Loading start values as actual values (all or only set values)
- Deleting blocks online (S7-300, S7-400)
- Commissioning technology objects online

#### Additional information

You can find additional information in the section "Programming a PLC".

---

**See also**

[Overview of function rights](#overview-of-function-rights)

### Function right "Monitor PLC program"

#### Description

The "Monitor PLC program" function right allows a user to monitor the program of a CPU with an existing online connection and to perform related actions.

> **Note**
>
> **Required additional function rights**
>
> - "Open the project read-only"

The function right is required for the following actions:

- Monitor PLC program online
- Edit breakpoints (set, activate, deactivate, delete)
- Change call environment
- Monitoring, commissioning and diagnosing technology objects online

---

**See also**

[Overview of function rights](#overview-of-function-rights)
  
[Introduction to testing with the watch table](Testing%20with%20the%20watch%20table.md#introduction-to-testing-with-the-watch-table)

### Function right "Edit drive applications"

#### Description

The function right "Edit drive applications" allows a user to edit the configuration of drives with Startdrive. This includes all parameterization, diagnostics and commissioning settings in the function view and in the parameter view. Without this function right, only read rights exist for most configuration screen forms.

All settings for "Safety Integrated" are excepted from this. You need the function right "Edit Safety Integrated application of the drive" for configuring "Safety Integrated".

> **Note**
>
> **Required additional function rights**
>
> In order to be able to use the "Edit drive applications" function right in a role in Startdrive, this role also requires the following additional function rights:
>
> - "Open and edit the project"
> - "Open the project read-only"

#### Additional information

You can find more information in the section "Configuring drives" under "Access control".

---

**See also**

[Overview of function rights](#overview-of-function-rights)

### Function right "Edit Safety Integrated application of the drive"

#### Description

The function right "Edit Safety Integrated application of the drive" allows a user to edit the Safety Integrated configuration of drives with Startdrive. This includes the Safety Integrated configuration in parameter lists.

The application of the Safety Integrated acceptance test also requires this function right.

> **Note**
>
> **Required additional function rights**
>
> In order to be able to use the "Edit Safety Integrated application of the drive" function right in a role in Startdrive, this role also requires the following additional function rights:
>
> - "Open and edit the project"
> - "Open the project read-only"

#### Additional information

You can find more information in the section "Configuring drives" under "Access control".

---

**See also**

[Overview of function rights](#overview-of-function-rights)

### "Control the drive in manual mode" function right

#### Description

The "Control the drive in manual mode" function right allows a user to access the control panel of a selected drive in the Startdrive project.

> **Note**
>
> **Required additional function rights**
>
> In order to be able to use the "Control the drive in manual mode" function right in a role in Startdrive, this role also requires the following additional function rights:
>
> - "Open the project read-only"
> - "Open and edit the project"

#### Additional information

You can find more information in the section "Configuring drives" under "Access control".

---

**See also**

[Overview of function rights](#overview-of-function-rights)

### Function right "Perform drive backup"

#### Description

The "Perform drive backup" function right allows a user to create a backup of the drive data (zip file) and save it in a directory on the operating unit.

> **Note**
>
> **Required additional function rights**
>
> In order to be able to use the "Perform drive backup" function right in a role in Startdrive, this role also requires the following additional function rights:
>
> - "Open the project read-only"
> - "Open and edit the project"

#### Additional information

You can find more information in the section "Configuring drives" under "Access control".

---

**See also**

[Overview of function rights](#overview-of-function-rights)

### Function right "Download to drives"

#### Description

The function right "Download to drives" allows a user to download project data and/or a backup of drive data to the drive.

> **Note**
>
> **Required additional function rights**
>
> - "Open and edit the project"

#### Additional information

You can find more information in the section "Configuring drives" under "Access control".

---

**See also**

[Overview of function rights](#overview-of-function-rights)

### Function right "Download to other devices"

#### Description

The function right "Download to other devices" allows a user to download project data to devices other than CPUs or HMI devices.

> **Note**
>
> **Required additional function rights**
>
> - "Open and edit the project"

---

**See also**

[Overview of function rights](#overview-of-function-rights)
  
[Compiling and loading project data](Editing%20project%20data.md#compiling-and-loading-project-data)

### Function right "Import project texts"

#### Description

The "Import project texts" function right allows a user to import project texts. You can also export the project texts without this function right.

Users without this function right cannot import the project texts in any of the following ways:

- Menu "Tools &gt; Import project texts"
- "Import project texts" button in the toolbar of the project texts editor
- "Import project texts" button in the "Texts" tab of the device properties

Importing library texts depends on the "Edit library types" function right and not on the "Import project texts" function right**.**

> **Note**
>
> **Required additional function rights**
>
> - "Open and edit the project"

---

**See also**

[Overview of function rights](#overview-of-function-rights)
  
[Importing project texts](Editing%20project%20data.md#importing-project-texts)

### Function right "Upgrade project"

#### Description

The "Upgrade project" function right allows a user to upgrade the project of an older version of the TIA Portal to a newer version.

> **Note**
>
> **Required additional function rights or roles**
>
> - Upgrading projects from TIA Portal V15.1 to TIA Portal V16:
>
>   - "Open the project with write rights"
>   - "Manage users and roles"
> - Upgrading projects from TIA Portal V16 to TIA Portal V17:
>
>   - The user requires the system-defined role "Engineering administrator".
> - Upgrading projects from TIA Portal V17 to a higher version:
>
>   - "Upgrade project"
>   - "Open and edit the project"

---

**See also**

[Overview of function rights](#overview-of-function-rights)
  
[Upgrading projects](Editing%20projects.md#upgrading-projects)

### Function right "Perform drive firmware update"

#### Description

The "Perform drive firmware update" function right allows a user to carry out a firmware update for the drive via the "Online &amp; Diagnostics" function view.

> **Note**
>
> **Required additional function rights**
>
> In order to be able to use the "Perform drive firmware update" function right in a role in Startdrive, this role also requires the following additional function rights:
>
> - "Open the project read-only"
> - "Open and edit the project"

#### Additional information

You can find more information in the section "Configuring drives" under "Access control".

---

**See also**

[Overview of function rights](#overview-of-function-rights)

## Activating project protection

You can use the user management in a TIA Portal project to protect your project against unauthorized access. A project administrator is automatically created when you activate the project protection. The administrator can then create additional users. When the project protection is activated, the project can only be opened and changed with a user account with sufficient rights.

> **Note**
>
> **Deactivation of project protection not possible**
>
> Note that project protection cannot be deactivated once it has been activated. This also means that the protection of the project cannot be reversed.

For users that were created before activation of project protection, the password needs to be entered again. Logon to the project will not be possible without entering the password again.

### Procedure

To activate project protection, follow these steps:

1. Open the "Security settings" folder in the project tree.
2. Double-click the "Settings" command.

   The editor for the user management is opened and the area for project protection is displayed.
3. Click on "Protect this project".

   The "Protect project" dialog opens.
4. Enter a user name.
5. Enter a password.
6. Re-enter the password to confirm.
7. If necessary, enter a comment.
8. Confirm your entries with "OK".

**Note**

**Password guideline**

The following guidelines are defined for the password when the user management is activated for the first time:

- Minimum password length: 8 characters
- Minimum number of numeric characters: 1
- Minimum number of special characters: 0
- At least one uppercase and one lowercase letter: Activated
- Number of recently used passwords blocked for reuse: 5
- Activate password aging: Deactivated

As project administrator you can adapt these password guidelines afterwards to meet your requirements.

> **Note**
>
> **Project administrator**
>
> The first user created is the project administrator. The administrator can create additional administrators. Each project needs at least one administrator.

### Result

The project protection was activated. You are logged on as project administrator and you can now create further local users or add global users or user groups from UMC or create new roles.

---

**See also**

[Basics of user management in the TIA Portal](#basics-of-user-management-in-the-tia-portal)

## Setting password policies

You can define the structure and complexity of the user passwords. To do this, you can specify the following policies:

- "Minimum password length"

  The minimum number of characters that the user password must have.
- "Minimum number of numeric characters"

  The minimum number of numeric characters that the user password must contain.
- "Minimum number of special characters"

  The minimum number of special characters that the user password must contain.
- "At least one uppercase letter and one lowercase letter"

  Specifies that the user password must contain at least one uppercase and one lowercase letter.
- "Number of recently used passwords blocked for reuse"

  Sets the number of recently used passwords that cannot be used as a new password.
- "Enable password aging"

  Specifies that the password only has a certain validity period and then expires. If this option is selected, the password must be changed within the password validity. If the password is not changed in time, the corresponding user can no longer log on to the configured project. A project administrator can still change the password for this user afterwards.
- "Password validity (days)"

  Sets the password validity in days, in which the password must be changed when the password is activated.
- "Prewarning time (days)"

  Sets how many days before the user's password expires, a warning is provided to the user. The warning time must be less than that for the password validity.

### Requirement

If you want to set the password policy for a protected project, you must have a user account as project user or as global user with the following two functional rights:

- Open and edit the project

- Manage users and roles

### Procedure

To set the password policies, follow these steps:

1. Open the project for which you want to set the password policies.
2. Open the "Security settings" folder in the project tree.
3. Double-click the "Settings" command.

   The editor for the user management is opened and the area for project protection is displayed.
4. Click "Password policies".
5. Make all the desired settings.
6. Save the project.

---

**See also**

[Basics of user management in the TIA Portal](#basics-of-user-management-in-the-tia-portal)

## Managing local project users

To manage local project users in your project, you can perform the following actions:

- Create new local project users
- Activating or deactivating a project user

  Only activated project users can log on to a configured project.
- Change data of a local project user:

  - User name
  - Password
  - Authentication method (runtime)
  - Runtime timeout
  - Comment
- Delete local project users

Please note the following restrictions:

- A maximum of 256 local project users can be added.
- The user name may not exceed 255 characters.
- The password may not exceed 120 characters and must meet the defined password policies.
- The comment may not exceed 1000 characters.
- The system creates an anonymous user. You cannot delete this user or change the user's data.

In contrast, the following restrictions apply to CPs:

- A maximum of 33 local project users can be added.
- The user name may not exceed 32 characters.
- The password may not exceed 32 characters and must meet the defined password policies.

### Requirement

- A project is open.
- If the project is protected, you must be logged on with a user account that has the function rights "Open and edit the project" and "Manage users and roles".
- The editor "Security settings &gt; Users and roles" is open.

### Create new local project users

To create a new project user, follow these steps:

1. Open the "Users" tab.
2. Click "Add new user".

   A submenu is opened in which you can select the user type.
3. Click "Add new local user".
4. Enter a user name.
5. Click on the arrow in the field "Password".
6. Enter a password.
7. Re-enter the password to confirm.
8. Select the authentication method and the runtime timeout.
9. If necessary, enter a comment.

   The new local project user is created and activated by default. To work with this user account in the project, assign the necessary roles to it.

> **Note**
>
> You can also create a new local project user by copying an existing project user. The roles assigned to the original project user are also assigned to the copied project user. However, you must assign a new password for the copied project user.

### Activating or deactivating a project user

To activate or deactivate a project user, do the following:

1. Open the "Users" tab.
2. Select the check box in the column before the user name to activate the respective user.
3. Clear the check box in the column before the user name to deactivate the respective user. The role assignment is maintained for deactivated project users.

### Changing data of a local project user

To change the data of a local project user, follow these steps:

1. Open the "Users" tab.
2. Click in the field whose data you want to change. Note that you can change the time for "Runtime timeout" only if the check box is selected.
3. Change the user name, password, authentication method, runtime timeout or comment.

### Deleting a local project user

To delete a local project user, follow these steps:

1. Open the "Users" tab.
2. Select the local project user you want to delete.
3. In the shortcut menu select the "Delete" command or use the &lt;Del&gt; key.

> **Note**
>
> In a protected project, the "Engineering administrator" role must be assigned to at least one project user or global group.
>
> Take into consideration the following:
>
> - Local project users: "Password" must be set as the authentication procedure.
> - Global group: There should be at least one user in the group; otherwise, there is no administrator for the project.

---

**See also**

[Basics of user management in the TIA Portal](#basics-of-user-management-in-the-tia-portal)

## Managing global users and user groups

This section contains information on the following topics:

- [Basics of global users and user groups](#basics-of-global-users-and-user-groups)
- [Managing global users](#managing-global-users)
- [Managing global user groups](#managing-global-user-groups)
- [Synchronizing global users and user groups with UMC](#synchronizing-global-users-and-user-groups-with-umc)
- [Changing the UM domain](#changing-the-um-domain)

### Basics of global users and user groups

#### Introduction

You can add global users and global user groups, which are managed in UMC (User Management Component), to a project. This allows these users and user groups to work in all projects in which they are activated and for which have been assigned the appropriate rights. Changes that are made in UMC for these global users and user groups can be synchronized with the projects. This avoids inconsistencies between UMC and the projects. To determine whether synchronization is necessary, you can check the synchronization status. You can find information on synchronization in the banner of the user management.

Please note the following restrictions with regard to global users and user groups:

- You can add a maximum of 256 global users.
- You can add a maximum of 50 global user groups.
- You cannot copy global users and user groups.

You can display the following information for global users and user groups:

- User groups: The users they contain and whether they have already been imported into the user management.
- User: The user groups of which the user is a member and whether they have already been imported into the user management.

#### UM domain

To be able to work with UMC, the computers that wish to access the global users and user groups must be assigned to a UM domain. UM domains are created by the network administrator and do not correspond to the Windows domains. You can use synchronization to move the global users and user groups of a TIA Portal project from one UM domain to another UM domain. This enables you to use a TIA Portal project in another UM domain or, for example, to swap the UMC ring server.

See also: [Changing the UM domain](#changing-the-um-domain)

---

**See also**

[Basics of user management in the TIA Portal](#basics-of-user-management-in-the-tia-portal)
  
[Managing global users](#managing-global-users)
  
[Managing global user groups](#managing-global-user-groups)
  
[Synchronizing global users and user groups with UMC](#synchronizing-global-users-and-user-groups-with-umc)

### Managing global users

#### Requirement

- A project is open.
- If the project is protected, you must be logged on with a user account that has the function rights "Open and edit the project" and "Manage users and roles".
- The connection to UMC is configured and you have a user account with the corresponding rights in UMC.

  For further information on installation and configuration of UMC, refer to the English documentation on UMC on the installation data carrier in the directory "/document/Readme/English".
- The editor "Security settings &gt; Users and roles" is open.

#### Adding global users

To add a global user from UMC, follow these steps:

1. Open the "Users" tab.
2. Click "Add new user".

   A submenu is opened in which you can select the user type.
3. Click "Add global user".

   If you have not yet logged on to UMC, the "UMC logon" dialog opens. Then also perform steps 4 and 5.
4. Enter your UMC user name and the corresponding password.
5. Click "OK".

   As soon as you are logged on in UMC, the "Add new user from UMC" dialog opens. All the available users from UMC are displayed in this dialog. Already activated users are activated and write-protected.
6. Activate the users you wish to add to your TIA Portal project.
7. Click "OK" to add the selected users.

   The selected users are added as global users and activated by default. Data of this user is write-protected and cannot be changed within the TIA Portal project. However, a global user can change his own password.

**Note**

To find the required users more quickly, you can filter the table by the columns "Name" and "Long name". To do this, enter part of the name or long name in the first line. All users whose names or long names contain the text entered are displayed. To cancel filtering, click the Filter button or select "*" from the drop-down list.

#### Activating or deactivating global users

To activate or deactivate a global user, do the following:

1. Open the "Users" tab.
2. Select the check box in the column before the name of the global user to activate it.
3. Clear the check box in the column before the name of the global user to deactivate it. The role assignment is maintained for deactivated users.

#### Displaying user groups of a global user

To display the user groups for an added global users of which they are a member, follow these steps:

1. Open the "Users" tab.
2. Select the user for which you want to display the user groups of which the user is a member. Note that you cannot use multiple selection.
3. In the bottom area of the "Users" tab, open the "Assigned user groups" tab.

   The user groups of which the user is a member are displayed. The check box is selected in the "Imported" column for user groups that have already been imported into the user administration.

#### Deleting global users

To delete a global user from the TIA Portal project, follow these steps:

1. Open the "Users" tab.
2. Select the global user you want to delete. You can also delete several users at the same time via multi-selection.
3. In the shortcut menu, select the "Delete" command or press the &lt;Del&gt; button.

---

**See also**

[Basics of global users and user groups](#basics-of-global-users-and-user-groups)
  
[Managing global user groups](#managing-global-user-groups)
  
[Synchronizing global users and user groups with UMC](#synchronizing-global-users-and-user-groups-with-umc)
  
[Changing the UM domain](#changing-the-um-domain)

### Managing global user groups

#### Requirement

- A project is open.
- If the project is protected, you must be logged on with a user account that has the function rights "Open and edit the project" and "Manage users and roles".
- The connection to UMC is configured and you have a user account with the corresponding rights in UMC.

  For further information on installation and configuration of UMC, refer to the English documentation on UMC on the installation data carrier in the directory "/document/Readme/English".
- The editor "Security settings &gt; Users and roles" is open.

#### Adding a global user group

To add a global user group from UMC, follow these steps:

1. Open the "User groups" tab.
2. Click "Add new user group".

   If you have not yet logged on to UMC, the "UMC logon" dialog opens. Then also perform steps 3 and 4.
3. Enter your UMC user name and the corresponding password.
4. Click "OK".

   As soon as you are logged on in UMC, the "Add user group from UMC" dialog opens. All the available user groups from UMC are displayed in this dialog. Already activated user groups are activated and write-protected.
5. Activate the user groups that you wish to add to your TIA Portal project.
6. Click "OK" to add the selected user groups.

   The selected user groups are added as global user groups and activated by default. The data of the global user groups is write-protected and cannot be changed within the TIA Portal project.

#### Activating or deactivating a global user group

To activate or deactivate a global user group, do the following:

1. Open the "User groups" tab.
2. Select the check box in the column before the name of the global user group to activate it.
3. Clear the check box in the column before the name of the global user group to deactivate it. The role assignment is maintained for deactivated user groups.

#### Displaying users of an added global user group

To display the users included in a global user group, follow these steps:

1. Open the "User groups" tab.
2. Select the user group for which you want to display the users. Note that you cannot use multiple selection.
3. In the bottom area of the "User groups" tab open the "Users" tab.

   The users of the selected group are displayed. The check box is selected in the "Imported" column for users who have already been imported into the user administration.

#### Deleting a global user group

To delete a global user group from the TIA Portal project, follow these steps:

1. Open the "User groups" tab.
2. Select the global user group that you want to delete. You can also delete several user groups at the same time via multi-selection.
3. In the shortcut menu select the "Delete" command or use the &lt;Del&gt; key.

> **Note**
>
> In a protected project, the "Engineering administrator" role must be assigned to at least one project user or global group.
>
> Take into consideration the following:
>
> - Local project users: "Password" must be set as the authentication procedure.
> - Global group: There should be at least one user in the group; otherwise, there is no administrator for the project.

---

**See also**

[Basics of global users and user groups](#basics-of-global-users-and-user-groups)
  
[Managing global users](#managing-global-users)
  
[Synchronizing global users and user groups with UMC](#synchronizing-global-users-and-user-groups-with-umc)
  
[Changing the UM domain](#changing-the-um-domain)

### Synchronizing global users and user groups with UMC

You can check whether synchronization is necessary at any time, and then carry it out.

#### Requirement

- A project is open.
- If the project is protected, you must be logged on with a user account that has the function rights "Open and edit the project" and "Manage users and roles".
- The connection to UMC is configured and you have a user account with the corresponding rights in UMC.

  For more information on installation and configuration of UMC, refer to the English documentation on UMC on the installation data carrier in the directory "/Documents/Readme/English".
- The editor "Security settings &gt; Users and roles" is open.

#### Procedure

To check the synchronization status or to carry out the synchronization, follow these steps:

1. Show the banner with the synchronization information.
2. To check the synchronization status, click the "Check status" link.
3. To carry out the synchronization, click on the "Synchronize" link.

Or:

1. Open the "Users" tab or the "User groups" tab.
2. To check the synchronization status, click "Check status" in the toolbar.
3. To carry out the synchronization, click "Synchronize" in the toolbar.

---

**See also**

[Basics of global users and user groups](#basics-of-global-users-and-user-groups)
  
[Managing global users](#managing-global-users)
  
[Managing global user groups](#managing-global-user-groups)
  
[Changing the UM domain](#changing-the-um-domain)

### Changing the UM domain

#### Requirement

The connection to UMC is configured and you have a user account with the corresponding rights in UMC.

#### Procedure

To change the UM domain, proceed as follows:

1. Copy the TIA Portal project to another UM domain.
2. Open the project in the new UM domain. If the project is protected, you must be logged on with a user account that has the function rights "Open and edit the project" and "Manage users and roles".
3. Open the "Security settings" folder in the project tree.
4. Double-click the command "Users and roles".

   The editor for the user management is opened.
5. Open either the "Users" tab or the "User groups" tab.

   The previous UM domain is displayed in the "UM domain ID" column.
6. Show the banner with the synchronization information.
7. Click the "Synchronize" link.

   The "Synchronize UMC data" dialog opens. This dialog explains to you the effects of a synchronization.
8. Click "Yes" to carry out the synchronization.

   The new UM domain is displayed in the UM Domain ID column.

#### Result

The global users and user groups of the project that are also in the new UM domain now use the new UM domain. Global users and user groups that are not in the new UM domain are disabled.

---

**See also**

[Basics of global users and user groups](#basics-of-global-users-and-user-groups)
  
[Managing global users](#managing-global-users)
  
[Managing global user groups](#managing-global-user-groups)
  
[Synchronizing global users and user groups with UMC](#synchronizing-global-users-and-user-groups-with-umc)

## Activating or deactivating anonymous user

In a project, the system creates the "Anonymous" user by default. This user can log on without a password. For security reasons, the anonymous user is deactivated and needs to be activated before use. Note that you can neither delete the anonymous user nor change his data. However, you can assign him function rights by means of roles, and deactivate him again at any time. Note that in a protected project, the function right "Manage users and roles" is necessary for editing users.

You can set the default authentication procedure so that the anonymous user account is always used when opening the project.

See also: [User management settings](#user-management-settings)

> **Note**
>
> **Reduced project security**
>
> When you activate the anonymous user, the project security is reduced according to the extent of the rights that you grant to this user.

### Requirement

- A project is open.
- Only in protected projects: You are logged on with a user account with the "Manage users and roles" and "Open and edit the project" function rights.
- The editor "Security settings &gt; Users and roles" is open.

### Procedure

To activate or deactivate the anonymous user, follow these steps:

1. Open the "Users" tab.
2. Select or clear the check box in front of the "Anonymous" user name.

---

**See also**

[Basics of user management in the TIA Portal](#basics-of-user-management-in-the-tia-portal)

## Managing roles

Rights are assigned to users via roles. Some roles defined by the system are already available in the TIA Portal, for example, in a protected project, the two roles "Engineering administrator" and "Engineering standard". You cannot rename or remove these roles. You cannot change the assignment of the function rights to these roles.

You can, however, define some roles and assign specific function rights to them. You can change the following role data for existing roles that you have defined yourself:

- Role name
- Runtime timeout
- Comment
- Assignment of function rights

You can also delete your self-defined roles at any time.

You can display the assigned role permissions for each project user or global user and for each global user group. This will give you an overview of the assigned rights at any time.

### Requirement

- A project is open.
- If the project is protected, you must be logged on with a user account that has the function rights "Open and edit the project" and "Manage users and roles".
- The editor "Security settings &gt; Users and roles" is open.

### Defining a new role

To define a new role, follow these steps:

1. Open the "Roles" tab.
2. Click "Add new role".
3. Enter a name for the role.
4. If necessary, change the runtime timeout.
5. If necessary, enter a comment.

   The new role has been created. Next, you need to assign the necessary function rights to it.

> **Note**
>
> You can also create a new role by copying an existing role. This means the assigned role permissions are also assigned to the new role.

### Assigning function rights or removing assignments

To assign function rights to a role or remove assigned function rights, follow these steps:

1. Open the "Roles" tab.
2. Select a role. Please note that you cannot use multi-selection for assignment.
3. In the lower area, open the tab with the category from which you want to assign or delete function rights.
4. Activate the function rights that you wish to assign to the role.
5. Deactivate the function rights that are no longer assigned to the role.

### Changing the role

To change a role, follow these steps:

1. Open the "Roles" tab.
2. Click in the field whose data you want to change.
3. Change the name, runtime timeout or comment.

### Deleting a role

To delete a role, follow these steps:

1. Open the "Roles" tab.
2. Select the role that you want to delete. Please note that you cannot delete the "Engineering administrator" and "Engineering standard" roles defined by the system.
3. In the shortcut menu select the "Delete" command or use the &lt;Del&gt; key.

### Display assigned function rights of a local project user or of a global user

To display the assigned function rights of a local project user or of a global user, follow these steps:

1. Open the "Users" tab.
2. Select the local project user or the global user for which you want to display the assigned function rights. Note that you cannot use multiple selection.
3. In the bottom area of the "Users" tab open the "Assigned rights" tab.

### Display assigned function rights of a global user group

To display the assigned function rights of a global user group, follow these steps:

1. Open the "User groups" tab.
2. Select the global user group for which you want to display the assigned function rights. Note that you cannot use multiple selection.
3. In the bottom area of the "User groups" tab open the "Assigned rights" tab.

---

**See also**

[Basics of user management in the TIA Portal](#basics-of-user-management-in-the-tia-portal)

## Assigning roles

You can assign roles to project users or global users and user groups that have different function rights. You can revoke the assignments at any time.

### Requirement

- A project is open.
- If the project is protected, you must be logged on with a user account that has the function rights "Open and edit the project" and "Manage users and roles".
- The editor "Security settings &gt; Users and roles" is open.

### Assigning roles to project users and global users

To assign roles to a user, follow these steps:

1. Open the "Users" tab.
2. Select the user to whom you want to assign roles. Note that you cannot use multiple selection.
3. Enable the desired roles in the "Assigned roles" section.

### Assigning roles to global user groups

To assign roles to a global user group, follow these steps:

1. Open the "User groups" tab.
2. Select the user group to which you want to assign roles. Note that you cannot use multiple selection.
3. Enable the desired roles in the "Assigned roles" section.

### Revoking role assignments for project users and global users

To revoke a role for a user, follow these steps:

1. Open the "Users" tab.
2. Select the user for which you want to revoke role assignments. Note that you cannot use multiple selection.
3. In the "Assigned roles" section, clear check marks for the roles that are no longer to be assigned to the user.

### Revoking role assignments for global user groups

To revoke a role assignment for a global user group, follow these steps:

1. Open the "User groups" tab.
2. Select the user group for which you want to revoke the role assignments. Note that you cannot use multiple selection.
3. In the "Assigned roles" section, clear check marks for the roles that are no longer to be assigned to the user group.

---

**See also**

[Basics of user management in the TIA Portal](#basics-of-user-management-in-the-tia-portal)

## Opening protected projects

The requirements and procedures for opening a protected project differ depending on the user type used:

- Project users and global users without single sign-on must explicitly authenticate themselves in the TIA Portal with user name and password.
- An anonymous user is not authenticated, so no password needs to be entered.
- Global users with single sign-on authenticate themselves via an existing single sign-on session, therefore no explicit password entry is required for the project.

In TIA Portal settings, you can specify the authentication procedure to be used by default when opening a protected project. The following procedures are available:

- Request user name and password:

  The logon dialog is displayed when the project is opened. This allows you to log on to the project with an existing user account. To do this, select the user type and enter the user name and password if necessary.
- Use anonymous user:

  The anonymous user account does not need to enter a password. If the anonymous user has the function right to open the protected project, the project is opened directly without displaying the logon dialog.
- Use single sign-on session:

  Authentication occurs via the single sign-on session. If a single sign-on session already exists for the user and the user has the function right to open the protected project, the project is opened directly without displaying the logon dialog. If there is no single sign-on session yet, the single sign-on logon dialog is displayed, enabling you to establish a single sign-on session.

See also: [User management settings](#user-management-settings)

### Requirement

- All user types:

  - You have a user account for the project that has either the "Open the project read-only" or "Open and edit the project" function right or both function rights.
  - The user account is activated.
- Additional requirement for single sign-on:

  - There is a single sign-on session to which the user is logged on.

### Procedure

To open a protected project, follow these steps:

1. Select the "Open" command in the "Project" menu.

   The "Open project" dialog box opens and the list of recently used projects is displayed.
2. If you want to check whether the project has been changed without permission outside the TIA Portal when you open the selected project, select the "Activate basic integrity check" check box. The basic integrity check may take some time to complete.

   See also: [The basics of projects](Editing%20projects.md#the-basics-of-projects)
3. Select the protected project from the list that you want to open. If the desired project does not exist in the list, perform the following steps:

   - Click "Browse".

     The "Open existing project" dialog opens.
   - Navigate to the desired project folder and select the project file.
4. Click "Open".

   Depending on your settings for the default authentication procedure and whether the corresponding requirements are met, the project is either opened directly or the "Logon" dialog opens. The additional steps are only required if the "Logon" dialog has been opened.
5. Select the required user type. If you have selected "Anonymous user" or "Single sign-on", continue with Step 9. Otherwise, continue with Step 6.
6. Enter your user name.
7. Enter your password.
8. If you want to change the password for your user account, click "Change password".

   See also: [Changing your own password](#changing-your-own-password)
9. Click "OK".

**Note**

A password change is mandatory in the following cases:

- When a global user logs on for the first time, if this has been specified in UMC.
- When a project user logs on after the password validity has expired.

Then perform the steps for changing the password.

### Result

The project is opened if you have logged on with a user account that meets the requirements. To change the project, additional function rights may be required.

---

**See also**

[Basics of user management in the TIA Portal](#basics-of-user-management-in-the-tia-portal)

## Changing your own password

In principle, there are several options for changing the password. However, not every option is available for every user type:

- When a protected project is opened:

  Project users and global users that do not use the single sign-on procedure can change their password in the logon dialog.
- When working in a protected project, using the toolbar:

  Project users and global users that do not use the single sign-on procedure can change their password via the toolbar.
- When working in a protected or unprotected project, via the "Users and Roles" editor:

  Project users can change their password via the "Users and Roles" editor. For protected projects, the two function rights "Open and edit the project" and "Manager users and roles" are required.

  The description for changing the password via the "Users and Roles" editor can be found under "[Managing project users](#managing-local-project-users)" in the section "Changing the data of a project user".
- Via the UMC status application:

  Global users that use the single sign-on procedure can change their password via the UMC status application.

  You can find more information on this in the UMC status application documentation.

If you change your password as a project user, only the password for this project will be changed. If you change your password as a global user, your password will be changed in UMC. This will change your password for all projects for which you are registered as a user.

### Requirement

You are logged on with a user account with the "Open and edit the project" function right.

### Changing the password when a protected project is opened

To change your password when you log on to the project, follow these steps:

1. Select the "Open" command in the "Project" menu.

   The "Open project" dialog box opens and the list of recently used projects is displayed.
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

   If you enter all the data correctly, your password will be changed. You can then use this new password when you log on to a protected project.

### Changing a password when working in a protected project

To change your password while working in a protected project, follow these steps:

1. Open the project view.
2. Click the down arrow in the toolbar next to the "User management" button.

   A drop-down list is opened in which the user management functions are listed.
3. Click "Change password".

   The "Change password" dialog opens.
4. Enter your user name.
5. Enter your current password.
6. Enter your new password.
7. Enter your new password again for confirmation.
8. Click "OK" to change your password.

   If you enter all the data correctly, your password will be changed. You can then use this new password when you log on to a protected project.

---

**See also**

[Basics of user management in the TIA Portal](#basics-of-user-management-in-the-tia-portal)

## Changing a user

In a protected project you can change the logged-in user without closing the project beforehand. However, if you switch from a user with no write permissions to a user with write permissions or vice versa, the project is automatically closed by the system and opened again. Editors for which the new user has no rights may also be closed.

### Requirement

- A protected project is open.
- The new user must have at least the "Open the project read-only" function right.

### Procedure

To change the user, follow these steps:

1. Open the project view.
2. Click the down arrow in the toolbar next to the "User management" button.

   A drop-down list is opened in which the user management functions are listed.
3. Click "Change user".

   If there are still unsaved changes, the "Save project" dialog opens and you can save your changes.

   The "Change user" dialog opens.
4. Select the required user type.
5. Enter your user name. This step is not necessary if you have selected "Anonymous user" or "Single sign-on" as the user type.
6. Enter your password. This step is not necessary if you have selected "Anonymous user" or "Single sign-on" as the user type.
7. Click "OK".

---

**See also**

[Basics of user management in the TIA Portal](#basics-of-user-management-in-the-tia-portal)

## Locking a project

By means of the project lock, you can prevent unauthorized persons from accessing the project in your absence. This allows you to leave the project open while you are briefly away from your work station. You have two options for using the project lock:

- Lock project manually

  For users logged on with single sign-on, the single sign-on session is closed first. Then the project is locked.
- Lock project automatically on inactivity

  For local project users, you can define the duration of inactivity in the TIA Portal. For global users, it is configured in UMC. For users logged on with single sign-on, the project is locked in the following cases:

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
> **The project lock is not available in the following cases:**
>
> - Startdrive: As long as the control panel is active and you have master control over a drive, you cannot activate the project lock and the automatic project lock is also suspended in case of inactivity.
> - SIMOTION: As long as SIMOTION SCOUT TIA is open, the automatic project lock is suspended in case of inactivity.

### Requirement

- A protected project is open.
- You are not logged in as an anonymous user.

### Lock project manually

To lock the project manually, follow these steps:

1. Open the project view.
2. Click the down arrow in the toolbar next to the "User management" button.

   A drop-down list is opened in which the user management functions are listed.
3. Click "Lock the project".

   The "Project locked" dialog opens. In this dialog, you can remove the project lock again or close the project.

### Lock project automatically on inactivity

To lock the project automatically on inactivity, follow these steps:

1. Select the "Settings" command in the "Options" menu.

   The "Settings" window is displayed in the work area.
2. Select the "Security" group in the area navigation.
3. Select the check box "Activate automatic project lock for all user types".
4. Only for project users: In the "Session timeout for local project users (minutes)" text box, enter the duration of inactivity after which the project should be locked automatically.

### Remove project lock for local project users and global users

To remove the project lock again for local project users and global users, follow these steps:

1. In the "Project locked" dialog, enter the correct password for the logged-on user.
2. Confirm the entries with &lt;Enter&gt; or click "Unlock".

   Alternatively, you can also close the project if you do not want to log on again. Changes that have not been saved are discarded.

### Remove project lock for single sign-on users

To remove the project lock for single sign-on users, follow these steps:

1. In the "Project locked" dialog, click "Unlock".

   If there is still an active single sign-on session for the user who caused the project to be locked, the project is unlocked. However, if there is no single sign-on session or if the single sign-on session is for another user, the logon window for the single sign-on session is displayed. In this case, perform step 2.

   Alternatively, you can also close the project if you do not want to log on again. Changes that have not been saved are discarded.
2. Log on with the user data of the user who locked the project. A different user cannot remove the project lock.

---

**See also**

[Basics of user management in the TIA Portal](#basics-of-user-management-in-the-tia-portal)

## Logging off the project

You can log off explicitly from a protected project. The project is closed. Note that if you are logged on via single sign-on, you are then also logged out of the single sign-on session. To prevent this, close the project without logging off. This will keep you logged on to the single sign-on session and allow you to open other projects without repeating authentication if you have sufficient rights.

### Requirement

A protected project is open.

### Procedure

To log off the project, follow these steps:

1. Open the project view.
2. Click the down arrow in the toolbar next to the "User management" button.

   A drop-down list is opened in which the user management functions are listed.
3. Click "Log off and close the project".
4. If you have made changes to the project since the last time you saved it, a message is displayed. Then, specify whether the changes should be saved. If there are no unsaved changes, the project is closed directly.

---

**See also**

[Basics of user management in the TIA Portal](#basics-of-user-management-in-the-tia-portal)

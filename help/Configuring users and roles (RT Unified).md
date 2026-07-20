---
title: "Configuring users and roles (RT Unified)"
package: UserAdminWCCUenUS
topics: 72
devices: [RT Unified]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Configuring users and roles (RT Unified)

This section contains information on the following topics:

- [Configuring users and roles (RT Unified)](#configuring-users-and-roles-rt-unified-1)
- [Basics (RT Unified)](#basics-rt-unified)
- [Configuring user management in the engineering system for Runtime (RT Unified)](#configuring-user-management-in-the-engineering-system-for-runtime-rt-unified)
- [Using user management on the Unified Panel (RT Unified)](#using-user-management-on-the-unified-panel-rt-unified)
- [Using user management on the WinCC Unified PC (RT Unified)](#using-user-management-on-the-wincc-unified-pc-rt-unified)

## Configuring users and roles (RT Unified)

![Figure](images/172259332491_DV_resource.Stream@PNG-en-US.png)

## Basics (RT Unified)

This section contains information on the following topics:

- [User management in the TIA Portal (RT Unified)](#user-management-in-the-tia-portal-rt-unified)
- [Local user management (RT Unified)](#local-user-management-rt-unified)
- [Central user management and UMC (RT Unified)](#central-user-management-and-umc-rt-unified)
- [Central user management (RT Unified)](#central-user-management-rt-unified)
- [Roles and function rights (RT Unified)](#roles-and-function-rights-rt-unified)

### User management in the TIA Portal (RT Unified)

The user management in the TIA Portal allows for the plant-wide, central user management including optional connection of Microsoft Active Directories. The user management forms the basis for an efficient and integrated management of personalized access rights in the plant. The safety risks are significantly reduced through this approach. Thanks to the specific assignment of roles and rights to individuals, maintenance is minimized while achieving a high degree of transparency.

#### Functions

The user management in the TIA Portal offers:

- Central, cross-project management of user groups and users in the system.
- Import of user groups and users from Microsoft Active Directory.
- Failsafe performance thanks to redundant design of a User Management Control domain (UMC domain).
- Load distribution thanks to multiple UMC stations in one UMC domain.

You can also find this information on the Internet in the "Centralized user management in TIA Portal" tile on the [Software in TIA Portal](https://new.siemens.com/global/en/products/automation/industry-software/automation-software/tia-portal/software/tia-portal-options.html) page.

You can configure the user management for:

- Engineering System
- Runtime

In the engineering system, you specify whether you are using a local or a central user management. By default, the use of the local user management is specified in the engineering system.

#### Protection in the engineering system

In the engineering system, you can protect the project from unintentional or unauthorized changes.

When you set up project protection in the engineering system, you will become the project administrator. Only authorized users can open and edit the protected project.

To protect the project, follow these steps:

1. Click "Security settings > Settings > Password policies" in the project tree.
2. You can define your own password policies.
3. Click on "Project protection > Protect this project".
4. Specify the login information for the project administrator.
5. The project administrator with the system-defined role "Engineering administrator" is created. The project is protected.

Project protection cannot be revoked.

#### Protection in Runtime

In Runtime, you can protect:

- Access to Runtime.
- Operation of objects from authorized use.

You can also use the user management without project protection. The system-defined engineering roles are not available in an unprotected project.

#### User management for the runtime

All information for user management in runtime is available in the following sections.

---

**See also**

[Configuring user management in the engineering system for Runtime (RT Unified)](#configuring-user-management-in-the-engineering-system-for-runtime-rt-unified)

### Local user management (RT Unified)

In the Engineering System, you specify whether you are using a local or a central user management. By default, the use of the local user management is specified in the Engineering System.

#### Local users and local user management

You define and manage the local users in a TIA Portal project. The local users are only valid for this project. You assign users different functions with system-defined or user-defined roles. You assign the function rights to the roles.

You cannot configure user groups in the local user management.

The following figure shows how you assign a role to a user and how you assign different function rights to the role:

![Local users and local user management](images/142428643467_DV_resource.Stream@PNG-en-US.png)

#### Options for local user management

A local user management is always part of the specific project in which the user management is configured.

The following figure shows the options of the local user management.

- Engineering system:

  - Configuring local users.
  - Adding roles and assigning function rights to the roles.
  - Assigning the roles to local users.
- WinCC Unified Runtime:

  - Managing local users.
  - Managing data of the local users.
  - Assigning the available roles to local users.

![Options for local user management](images/142428152715_DV_resource.Stream@PNG-en-US.png)

#### Logon via RFID with local user management for Unified PCs

If local user management is used, WinCC Unified Runtime supports login with RFID and PM-LOGON for local web clients. The prerequisite is that PM-LOGON is installed on the UMC server and the teach-in of the RFID cards has been completed.

Additional information on licensing and installing PM-LOGON as well as on the teach-in for the RFID cards is available in the [PM-LOGON Operating Manual](https://support.industry.siemens.com/cs/de/en/view/109810587).

#### Logon via RFID with local user management for Unified Control Panels

Additional information on using RFID on Unified Control Panels is available in the [Unified Comfort Panels](https://support.industry.siemens.com/cs/ww/en/view/109810754) Operating Instructions TIA V18 or higher.

### Central user management and UMC (RT Unified)

The TIA User Management Component (UMC) option allows for the setup of a project-wide, central user management. You can also apply user groups and users from a Microsoft Active Directory.

From the TIA Portal, you can add the centrally defined user groups and users to the user management of the project. To add user groups and users from UMC, the corresponding rights are required in UMC.

#### Installing the User Management Component UMC

To use the central user management, install the "User Management Component UMC" software package. The UMC installation file and the UMC documentation in English is available on the TIA Portal installation data storage medium ("..\support", "...\Documents\Readme\English").

Install the UMC files on the PC on which you are managing the data of the central user management.

> **Note**
>
> We highly recommend that you read the UMC documentation completely before you start working with the user management, especially the sections on "Secure Application Data Support (SADS)". SADS is mandatory for working with the user management in the TIA Portal.

#### Licenses for central user management

The number of UMC domains is cumulative.

The license is free for up to 10 users.

The following licenses are available if you are managing more users:

| Software/license | Article number |
| --- | --- |
| TIA Portal User Management Component (UMC)  Rental license for 100 user accounts and 365 days | 6ES7823-1UE30-0YA0 |
| TIA Portal User Management Component (UMC)  Rental license for 4000 user accounts and 365 days | 6ES7823-1UE10-0YA0 |

- [Certificates of license](https://mall.industry.siemens.com/mall/en/WW/Catalog/Search?searchTerm=user%20management%20component&tab=Product)
- Details about license concepts: [Software and licenses](https://new.siemens.com/global/en/products/automation/topic-areas/simatic/licenses.html)
- [Trial license](https://support.industry.siemens.com/cs/ww/en/view/109772992) for registered users in the Siemens Industry Online Support. The software is subject to export restrictions.

### Central user management (RT Unified)

In the Engineering System, you specify whether you are using a local or a central user management. By default, the use of the local user management is specified in the Engineering System.

#### Central user groups, users and central user management

Outside of the TIA Portal, you define and manage the following in the central user management:

- User groups
- Central users

You organize the users in various user groups.

In the TIA Portal, you assign:

- The different functions to the user groups with the help of system-defined or user-defined roles.
- The function rights to the roles.

The following figure shows you how to you assign a role to a user group and function rights to the role:

![Central user groups, users and central user management](images/142428920587_DV_resource.Stream@PNG-en-US.png)

You can repeatedly import the user groups and central users from the central user management into the TIA Portal projects. You require the corresponding rights in the central user management for importing.

#### Options of the central user management

The following figure shows the options of the central user management.

- Engineering system:

  - Importing user groups and central users into a TIA Portal project.
- Central user management:

  - Managing user groups and their data.
  - Managing central users and their data.

![Options of the central user management](images/142428161547_DV_resource.Stream@PNG-en-US.png)

---

**See also**

[Examples (RT Unified)](#examples-rt-unified)

### Roles and function rights (RT Unified)

In the user management, you assign users or user groups different functions through system-defined or user-defined roles. The roles are assigned system-defined and user-defined function rights by the system or by you.

- System-defined roles are specified by the system.

  You cannot rename or delete the system-defined roles. The function rights are assigned to the roles by the system. You cannot change the assignment.
- You can add user-defined roles.

  You can rename or delete the user-defined roles. You assign different function rights to a role.

#### Relevant roles in the engineering system

The system creates the following system-defined roles that are relevant for the engineering system.

Engineering roles:

- Engineering administrator
- Engineering standard

The roles are only available in a protected project.

#### Relevant roles in runtime

The system creates the following system-defined roles that are relevant for runtime.

HMI roles:

- HMI Administrator
- HMI Operator
- HMI Monitor
- HMI Monitor Client

The roles are also available in an unprotected project.

#### Function rights

The function rights specify which functions a user or a user group may use in a specific role. You can link different function rights to multiple roles. You can also add user-specific runtime rights.

You can assign multiple function rights to a role.

> **Note**
>
> **User - Role - Function right**
>
> If you do not assign a role to a user or a function right to a role, the user or role is not downloaded to the device.

## Configuring user management in the engineering system for Runtime (RT Unified)

This section contains information on the following topics:

- [Specifying local or central user management (RT Unified)](#specifying-local-or-central-user-management-rt-unified)
- [Configuring a connection to the central user management (RT Unified)](#configuring-a-connection-to-the-central-user-management-rt-unified)
- [Server ID (RT Unified)](#server-id-rt-unified)
- [Users and user groups (RT Unified)](#users-and-user-groups-rt-unified)
- [HMI roles (RT Unified)](#hmi-roles-rt-unified)
- [Function rights (RT Unified)](#function-rights-rt-unified)
- [Examples (RT Unified)](#examples-rt-unified)

### Specifying local or central user management (RT Unified)

In the Engineering System, you specify whether you are using local or central user management. By default, the use of the local user management is specified in the Engineering System.

#### Requirement

- A project is open.
- A device has been created.
- Password settings for Runtime and engineering are defined.

#### Specify password settings

To set the password settings for the runtime and engineering, follow these steps:

1. Open "Security settings > Settings" in the project tree.
2. In the "Settings" editor, select the "Password policies" menu command.
3. Specify the password settings.

#### Specifying the user management

To define the user management, follow these steps:

1. Open the "Runtime settings" of the device in the project tree of the project.
2. Under "Security > Access control", select:

   - Local user management: User data is stored on the device.
   - Central user management: User data is loaded from the UMC.
3. Under "Security > Account deactivation in Runtime", you can specify whether and after how many failed login attempts a user is logged out.

   ![Specifying the user management](images/171009014027_DV_resource.Stream@PNG-en-US.png)

   ![Specifying the user management](images/171009014027_DV_resource.Stream@PNG-en-US.png)

---

**See also**

[Managing local users (RT Unified)](#managing-local-users-rt-unified)
  
[Managing central users and user groups (RT Unified)](#managing-central-users-and-user-groups-rt-unified)

### Configuring a connection to the central user management (RT Unified)

You have specified in the Engineering System that you are using central user management.

#### Configuring a connection to the central user management

Follow these steps to configure the connection to the central user management:

1. Enter the UMC server address in "User management configuration".
2. Enter the server ID. The server ID can be determined from the configuration of the UMC server.

   The server ID is the fingerprint of the web certificate (https) on which the UMC server is installed. For more information, refer to [Server ID](#server-id-rt-unified).
3. Enter the address of the identity provider.

![Configuring a connection to the central user management](images/172363181451_DV_resource.Stream@PNG-en-US.png)

You are connected with the central user management.

> **Note**
>
> If you cannot connect to the central user management or you do not know the server ID, leave the entry field for the server ID empty.
>
> The configuration is nevertheless downloaded to Runtime. Enter the server ID:
>
>
>
> 1. On the PC using Runtime Manager.
> 2. On the Panel using the Control Panel.

### Server ID (RT Unified)

The WinCC Unified PC Station or the Unified Panel communicate via an encrypted HTTPS connection to the UMC server to verify the authentication.

The server ID is the fingerprint of the Internet Information Service (IIS) web certificate (HTTPS) on the computer where the UMC server is installed.

> **Note**
>
> In a distributed UMC domain with UMC ring server and multiple UMC servers / UMC RT servers, you decide which server of the UMC domain is used for user authentication of the respective Unified Station.

#### Take over server ID via the IIS Manager

If you want to apply the server ID via the IIS Manager, follow these steps:

1. Open the IIS Manager on the computer to which the WinCC Unified PC Station or the SIMATIC WinCC Unified Panel is to connect for authentication.

   ![Take over server ID via the IIS Manager](images/153870377227_DV_resource.Stream@PNG-en-US.png)

   ![Take over server ID via the IIS Manager](images/153870377227_DV_resource.Stream@PNG-en-US.png)
2. Edit the bindings of the default web page in IIS.

   ![Take over server ID via the IIS Manager](images/153870387595_DV_resource.Stream@PNG-en-US.png)

   ![Take over server ID via the IIS Manager](images/153870387595_DV_resource.Stream@PNG-en-US.png)
3. Edit the bindings of the 'HTTPS' type.

   ![Take over server ID via the IIS Manager](images/153984642827_DV_resource.Stream@PNG-en-US.png)

   ![Take over server ID via the IIS Manager](images/153984642827_DV_resource.Stream@PNG-en-US.png)
4. Open the stored SSL certificate.

   ![Take over server ID via the IIS Manager](images/153984868363_DV_resource.Stream@PNG-en-US.png)

   ![Take over server ID via the IIS Manager](images/153984868363_DV_resource.Stream@PNG-en-US.png)
5. Open the details of the SSL certificate. Scroll to the "Fingerprint" attribute.

   ![Take over server ID via the IIS Manager](images/153984653195_DV_resource.Stream@PNG-en-US.png)

   ![Take over server ID via the IIS Manager](images/153984653195_DV_resource.Stream@PNG-en-US.png)
6. Transfer the fingerprint of the certificate into the runtime settings of the WinCC Unified Station.

**Note**

If WinCC Unified is already installed on the same computer (single-user station system), select the "WinCC Unified SCADA" web page as the web page.

#### Take over server ID via a browser

You can also take over the server ID via a browser and without administrator rights.

You can find the procedure under the following link to "[Fingerprints](https://www.grc.com/fingerprints.htm)" in the section "How to display this page's (or any page's) SSL certificate fingerprint".

### Users and user groups (RT Unified)

This section contains information on the following topics:

- [Managing local users (RT Unified)](#managing-local-users-rt-unified)
- [Configuring the display of the login dialog (RT Unified)](#configuring-the-display-of-the-login-dialog-rt-unified)
- [Configuring automatic logoff (RT Unified)](#configuring-automatic-logoff-rt-unified)
- [Downloading local user management (RT Unified)](#downloading-local-user-management-rt-unified)
- [Managing central users and user groups (RT Unified)](#managing-central-users-and-user-groups-rt-unified)
- [Loading central user management (RT Unified)](#loading-central-user-management-rt-unified)

#### Managing local users (RT Unified)

You have specified in the Engineering System that you are using local user management. To manage the local users in your project, you have the option of:

- Adding users
- Specifying data of a user
- Copying, pasting, deleting users

##### Requirement

- A project is open.
- The "Security Settings > Users and Roles" editor is open.
- The "Users" tab is open.

##### Restrictions

Please note the following restrictions:

- You can add a maximum of 256 users.
- The user name may not exceed 255 characters.
- The password must be a minimum of 8 and a maximum of 120 characters long and must comply with the defined password guidelines.
- The comment may not exceed 1000 characters.

> **Note**
>
> **Permissible characters for user names and passwords**
>
> You can use the following numbers, letters and special characters for user names and passwords:
>
> - 0123456789
> - A...Z a...z
> - !#$%&()*+,-./:;<=>?@\[]^_`{}~|
> - Spaces within the user name or password

##### Displaying columns for user data

To display the columns for user data, follow these steps:

1. Right-click in the row with the user data.

   ![Displaying columns for user data](images/171016332299_DV_resource.Stream@PNG-en-US.png)

   ![Displaying columns for user data](images/171016332299_DV_resource.Stream@PNG-en-US.png)
2. Select from the following columns:

   - User name
   - Password
   - Alias
   - Authentication procedure
   - Runtime timeout
   - UM Domain ID
   - Comment

##### Creating users

To create a user, follow these steps:

1. Click "Add new user".
2. Click "Add new local user" in the submenu.

   ![Creating users](images/172316642955_DV_resource.Stream@PNG-en-US.png)

   ![Creating users](images/172316642955_DV_resource.Stream@PNG-en-US.png)
3. Enter a user name according to the password policies.
4. Select the authentication procedure for the user:

   - Password: Enter a password according to the password policies. Enter the password again to confirm.
   - Radius: The logon is made via a RADIUS server on which the password is saved. This option is only used for devices that support logon using a RADIUS server.
5. Configure "Runtime timeout" for the user. The configured time defines the time of inactivity in Runtime, after which the user is automatically logged off. To change the specification for "Runtime timeout", select the option in the "Runtime timeout" column. The option is activated by default.
6. You can enter a comment for the project user.

A new project user has been created. Assign the roles to the user.

| Symbol | Meaning |
| --- | --- |
| ![Creating users](images/145494195723_DV_resource.Stream@PNG-de-DE.png) | **Tips for working efficiently** |
| - You can also create a new user by copying an existing user. As a result, the assigned roles are also assigned to the copied user. You must re-assign the password for the copied user. |  |

##### "Anonymous" user

As of V18, a default "Anonymous" user is available. When enabled, the "Anonymous" user does not require a password.

You cannot use the "Anonymous" user to log in to Runtime.

##### Changing local user data

Proceed as follows to change the data of a local user:

1. Open the "Users" tab.
2. Click in the text box with the data you want to change.
3. Change the user name, password, authentication procedure, "Runtime timeout" or comment.

The user data has been changed.

##### Deleting users

To delete a project user, proceed as follows:

1. Select the user in the "Users" tab that is open.
2. In the shortcut menu, select the "Delete" command or press the <Del> key.

The user has been deleted.

---

**See also**

[Configuring automatic logoff (RT Unified)](#configuring-automatic-logoff-rt-unified-1)

#### Configuring the display of the login dialog (RT Unified)

You can configure the display of the login dialog in the Engineering System. A pop-up window with the "User Login" dialog is displayed in Runtime via the "ShowLoginDialog" system function. A new user can log in to Runtime.

##### Requirement

- A project is open.
- A device has been created.
- A screen is open.

##### Configuring "ShowLoginDialog" system function

To configure the "ShowLoginDialog" system function, follow these steps:

1. Configure a button in the screen.
2. Enter the "ShowLoginDialog" name in the "Static value" column under "Properties > General > Content > Text".
3. Under "Events > Click left mouse button" in the "Name" column under "Screen > Account management", select the system function "ShowLoginDialog".

   ![Configuring "ShowLoginDialog" system function](images/172364936971_DV_resource.Stream@PNG-en-US.png)

   ![Configuring "ShowLoginDialog" system function](images/172364936971_DV_resource.Stream@PNG-en-US.png)

##### Result

When you click the button in Runtime, the "User Login" dialog is displayed. A new user can log in to Runtime.

![Result](images/172406088715_DV_resource.Stream@PNG-en-US.png)

#### Configuring automatic logoff (RT Unified)

This section contains information on the following topics:

- [Configuring automatic logoff (RT Unified)](#configuring-automatic-logoff-rt-unified-1)
- [Configuring website after automatic logoff (RT Unified)](#configuring-website-after-automatic-logoff-rt-unified)

##### Configuring automatic logoff (RT Unified)

In the Engineering System you can configure the automatic logoff, "Runtime timeout". You are automatically logged off after the configured inactivity time in runtime.

In the Engineering System you can configure the "Runtime timeout" for:

- Users
- Roles

If the values differ for a user and their roles, the lowest value is transferred when loading the project.

After automatic logoff you are by default shown the "User login" dialog. This page requires a network connection to the Unified server.

![Figure](images/171399785867_DV_resource.Stream@PNG-en-US.png)

###### Configuring automatic logoff for a user

To configure the automatic logoff, "Runtime timeout" for a user, proceed as follows:

1. Open the editor "Security settings > Users and roles".
2. Open the "Users" tab.
3. Select the check box in the "Runtime timeout" column of the selected user.
4. Enter the inactivity time in the text box. The user is automatically logged off after the specified time.

   ![Configuring automatic logoff for a user](images/171492252683_DV_resource.Stream@PNG-en-US.png)

   ![Configuring automatic logoff for a user](images/171492252683_DV_resource.Stream@PNG-en-US.png)

###### Configuring automatic logoff for a role

To configure the automatic logoff, "Runtime timeout", for a role proceed as follows:

1. Open the editor "Security settings > Users and roles".
2. Open the "Roles" tab.
3. Click in the text box in the "Runtime timeout" column of the selected role.
4. Enter the inactivity time in the text box. The role is automatically logged off after the specified time.

   ![Configuring automatic logoff for a role](images/171496651403_DV_resource.Stream@PNG-en-US.png)

   ![Configuring automatic logoff for a role](images/171496651403_DV_resource.Stream@PNG-en-US.png)

---

**See also**

[Managing local users (RT Unified)](#managing-local-users-rt-unified)

##### Configuring website after automatic logoff (RT Unified)

You can specify in the Engineering System which website is shown to you in your browser after the automatic logoff in runtime. By default, the "User login" dialog is displayed. This page requires a network connection to the Unified server.

In the runtime settings in the Engineering System you can configure a URL address of the website shown to you in your browser after the automatic logoff in runtime.

###### Requirement

- A WinCC Unified PC as of Version V19 is installed.

###### Configuring the display of the website after an automatic logoff

To configure the display of the website after an automatic logoff, proceed as follows:

1. Under "Runtime settings > General > Automatic logoff", select the option "Activate URL for automatic logoff".

   The option is disabled by default and the text box is empty.

   ![Configuring the display of the website after an automatic logoff](images/172376879371_DV_resource.Stream@PNG-en-US.png)

   ![Configuring the display of the website after an automatic logoff](images/172376879371_DV_resource.Stream@PNG-en-US.png)
2. Enter a URL address into the text box. Note the following information:

   - The maximum length of the URL address is 2048 characters.
   - If you exceed the maximum length of the URL address, an error message is displayed.
   - The address is shortened if you enter a URL address that contains more than 2048 characters via copy and paste.

   ![Configuring the display of the website after an automatic logoff](images/172376883851_DV_resource.Stream@PNG-en-US.png)

   ![Configuring the display of the website after an automatic logoff](images/172376883851_DV_resource.Stream@PNG-en-US.png)

After automatic logoff in runtime the corresponding website is displayed.

> **Note**
>
> If you deselect the option again, the URL address is still shown in the text box and the text box is grayed out. After automatic logoff in runtime, the "User login" dialog is displayed.

#### Downloading local user management (RT Unified)

You have added at least one user. Compile and download the local user management.

##### Compiling and downloading local user management

Note that you need to set the setting in the "Preview load" differently for the first load than for each subsequent load.

- For the first download of a TIA Portal project to a runtime device, select the option "Reset to start values" for "Runtime values" when loading the user data.
- For all subsequent loading processes, select the option "Keep current values" or "Keep selected" for "Runtime values".

On the runtime device, the user configuration is not project-specific, but device-specific. The defined user management is used in all projects in a device.

All system-defined roles are included in each runtime project.

##### Compiling and downloading local user management initially

To load the local user management for the first time, follow these steps:

1. Select the device in the project tree.
2. Select "Download to device > Software (all)" from the shortcut menu.

   The compilation of the project is checked and content that has not been compiled is compiled. The compilation result is displayed in the Inspector window under "Info > Compile".
3. The "Load Preview" dialog is displayed.
4. Check the displayed defaults and change the settings if necessary:

   - Specify whether runtime should start on the target system after the download.
   - Select "Reset to start values".
   - Specify whether all logs are reset in runtime.

   The setting is only accepted when you have selected "Start runtime".

   ![Compiling and downloading local user management initially](images/166028374539_DV_resource.Stream@PNG-en-US.png)

   ![Compiling and downloading local user management initially](images/166028374539_DV_resource.Stream@PNG-en-US.png)
5. Click "Download".

Runtime starts after loading the settings.

##### Keep current values when reloading

If you want to keep the current values during the next download, select "Keep current values" during download.

- "Keep current values"

  ![Keep current values when reloading](images/166048340875_DV_resource.Stream@PNG-en-US.png)
- "Keep selected"

  With the "Keep selected" option, you specify which values you want to keep in Runtime:

  - Current values of tags and pending alarms
  - Current user management data

  ![Keep current values when reloading](images/166048351243_DV_resource.Stream@PNG-en-US.png)

> **Note**
>
> To prevent the users created in the user administration from being overwritten in runtime by the complete download of the project, activate the "Keep current user administration data in runtime" option.

##### Retained data

If you have enabled the "Keep current user management data in Runtime" option, the following user management data will be kept:

- User name
- Password
- Password guidelines
- Comment
- Language
- Function rights
- User role
- User group
- User management mode - local or central
- Data of the central user management: Server address, server ID, identity provider address

---

**See also**

[Managing local users (RT Unified)](#managing-local-users-rt-unified)
  
[Initial download of a project (RT Unified)](Compiling%20and%20loading%20%28RT%20Unified%29.md#initial-download-of-a-project-rt-unified)
  
[Complete reloading of a project (RT Unified)](Compiling%20and%20loading%20%28RT%20Unified%29.md#complete-reloading-of-a-project-rt-unified)

#### Managing central users and user groups (RT Unified)

You have specified in the Engineering System that you are using central user management.

You can add central users and user groups that were created in the central user management to a project. Central users and user groups are managed in the central user management. The changes affect the project to which these users or user groups belong.

You can synchronize the user management in the engineering system with the central user management or check the synchronization status.

##### Main advantage of the central user management

The main advantage of the central user management is the management of the user groups.

- In the user groups, you manage the central users independent of the engineering system. You add the central users to the user groups.
- The function rights of a user are known via the role assignment in the user group in the Unified Runtime.
- Changes to the user data are effective in Runtime even without loading the project.
- When you import the user group into the TIA Portal, the users and their data including passwords is automatically imported into the project.

##### Requirement

- A project is open.
- The connection to the central user management is configured.
- You have a user account with the corresponding rights in the central user management.
- The "Security Settings > Users and Roles" editor is open.
- The "User groups" tab is open.

##### Restrictions

Please note the following restrictions:

- You can add a maximum of 256 central users.
- You can add a maximum of 50 central user groups.
- You cannot copy central users and user groups.

##### Information about user groups and users

You can display the following information for central users and user groups:

- User groups: The users they contain and whether they have already been imported into the user management.
- User: The user groups of which the user is a member and whether they have already been imported into the user management.

##### Adding user group

To add a user group from the central user management to a TIA Portal project, follow these steps:

1. Open the "User groups" tab.
2. Click "Add new user group".

   If you have not yet logged in to the central user management yet, the "UMC Login" dialog opens:

   - Enter your UMC user name and the corresponding password.
   - Click "OK".
3. If you are logged in to the central user management, the "Add new user group from UMC" dialog opens. All available user groups from the central user management are displayed. Already added user groups are activated and write-protected.
4. Activate the user groups that you want to add to the TIA Portal project. Click "OK".
5. The selected user groups are added as central user groups. Their data is write-protected, and you cannot change the data within the TIA Portal project.

##### Deleting a user group

To delete a user group from the TIA Portal project, follow these steps:

1. Open the "User groups" tab.
2. Select one or more user groups.
3. In the shortcut menu, select the "Delete" command or press the <Del> key.

##### Adding central users

You can also import the individual central users into a TIA Portal project.

To add a central user from the central user management, follow these steps:

1. Open the "Users" tab.
2. Click "Add new user".
3. Click "Add global users" in the submenu.

   If you have not yet logged in to the central user management yet, the "UMC Login" dialog opens:

   - Enter your UMC user name and the corresponding password.
   - Click "OK".

   If you are logged in to the central user management, the "Add new user from UMC" dialog opens. All available users from the central user management are displayed. Already activated users are activated and write-protected.
4. Activate the user that you want to add to the TIA Portal project. Click "OK".
5. The selected users are added as central users. Their data is write-protected, and you cannot change the data within the TIA Portal project.

| Symbol | Meaning |
| --- | --- |
| ![Adding central users](images/145494195723_DV_resource.Stream@PNG-de-DE.png) | **Tips for effective procedure** |
| - To find the required users, filter the table by the columns "Name" and "Long name". Enter the name in the first line. All users with this name are displayed. To cancel filtering, click on the "Filter" button or select "*" in the drop-down list. |  |

##### Deleting a central user

To delete a central user from the TIA Portal project, follow these steps:

1. Open the "Users" tab.
2. Select one or more central users.
3. In the shortcut menu, select the "Delete" command or press the <Del> key.

---

**See also**

[Simulating a central user management (RT Unified)](Simulate%20runtime%20%28RT%20Unified%29.md#simulating-a-central-user-management-rt-unified-1)
  
[Server ID (RT Unified)](#server-id-rt-unified)

#### Loading central user management (RT Unified)

You have added at least one user group. Compile and load the central user management.

##### Compiling and loading central user management

Note that you need to set the setting in the "Preview load" differently for the first load than for each subsequent load.

- For the first download of a TIA Portal project to a runtime device, select the option "Reset to start values" for "Runtime values" when loading the user data.
- For all subsequent loading processes, select the option "Keep current values" or "Keep selected" for "Runtime values".

On the runtime device, the user configuration is not project-specific, but device-specific. The defined user management is used in all projects in a device.

All system-defined roles are included in each runtime project.

##### Compiling and downloading central user management initially

To load the central user management for the first time, follow these steps:

1. Select the device in the project tree.
2. Select "Download to device > Software (all)" from the shortcut menu.

   The compilation of the project is checked and content that has not been compiled is compiled. The compilation result is displayed in the Inspector window under "Info > Compile".
3. The "Load Preview" dialog is displayed.
4. Check the displayed defaults and change the settings if necessary:

   - Specify whether runtime should start on the target system after the download.
   - Select "Reset to start values".
   - Specify whether all logs are reset in runtime.

   The setting is only accepted when you have selected "Start runtime".

   ![Compiling and downloading central user management initially](images/166028374539_DV_resource.Stream@PNG-en-US.png)

   ![Compiling and downloading central user management initially](images/166028374539_DV_resource.Stream@PNG-en-US.png)
5. Click "Download".

The connection to the central user management is established after loading the settings.

Depending on the selected options, runtime is started during loading.

> **Note**
>
> Enter the settings loaded for the central user management:
>
> - On the PC in the SIMATIC Runtime Manager
> - On the Panel in the Control Panel.
>
> Depending on the setting, data is overwritten during loading.

##### Keep current values when reloading

If you want to keep the current values during the next download, select "Keep current values" during download.

- "Keep current values"

  ![Keep current values when reloading](images/166048340875_DV_resource.Stream@PNG-en-US.png)
- "Keep selected"

  With the "Keep selected" option, you can specify which values you want to keep in Runtime:

  - Current values of tags and pending alarms
  - Current user management data

  ![Keep current values when reloading](images/166048351243_DV_resource.Stream@PNG-en-US.png)

> **Note**
>
> To prevent the users created in the user administration from being overwritten in runtime by the complete download of the project, activate the "Keep current user administration data in runtime" option.

##### Retained data

If you have enabled the "Keep current user management data in Runtime" option, the following user management data will be kept:

- User name
- Password
- Password guidelines
- Comment
- Language
- Function rights
- User role
- User group
- User management mode - local or central
- Data of the central user management: Server address, server ID, identity provider address

##### Behavior of the runtime after the download

If all your entries are correct, runtime uses the downloaded settings.

If the entries are incomplete or incorrect, runtime exhibits the following behavior:

- If the data of the central user management has already been downloaded successfully once before, runtime uses the user data that was downloaded last.

  Enter missing settings for central user management:

  - On the PC in the SIMATIC Runtime Manager
  - On the Panel in the Control Panel.
- If the data of the central user management has never been downloaded, runtime does not start.   
  Enter missing settings for central user management:

  - On the PC in the SIMATIC Runtime Manager
  - On the Panel in the Control Panel.

---

**See also**

[Initial download of a project (RT Unified)](Compiling%20and%20loading%20%28RT%20Unified%29.md#initial-download-of-a-project-rt-unified)
  
[Complete reloading of a project (RT Unified)](Compiling%20and%20loading%20%28RT%20Unified%29.md#complete-reloading-of-a-project-rt-unified)

### HMI roles (RT Unified)

This section contains information on the following topics:

- [Managing HMI roles (RT Unified)](#managing-hmi-roles-rt-unified)
- [Assigning HMI roles (RT Unified)](#assigning-hmi-roles-rt-unified)
- [HMI role "HMI Monitor Client" (RT Unified)](#hmi-role-hmi-monitor-client-rt-unified)

#### Managing HMI roles (RT Unified)

You assign users the roles with the function rights. You can manage the user-defined HMI roles in your project.

##### System-defined roles relevant for HMI

System-defined HMI roles without engineering function rights are created in an unprotected project:

- HMI Administrator
- HMI Operator
- HMI Monitor
- HMI Monitor Client

You cannot rename or delete system-defined HMI roles. Also, you cannot change the assignment of the function rights to system-defined roles.

##### User-defined roles relevant for HMI

You can perform the following actions to manage the user-defined HMI roles in your project:

- Add a new user-defined role.
- Change the data of the user-defined role:

  - Name
  - Runtime timeout
  - Comment
- Assign the function rights to the role.
- Change or delete the assignment of the function rights.
- Delete a role.

> **Note**
>
> - When setting the runtime timeout, observe the information in the individual manuals.
> - In the Engineering System, you can configure a runtime timeout both for a role and for a user. If the values are different, only the smaller of the two values is transferred to the Panel during loading.

##### Requirement

- A project is open.
- A device has been created.
- The "Security Settings > Users and Roles" editor is open.
- The "Roles" tab is open.

##### Adding a user-defined HMI role

To add a user-defined HMI role, follow these steps:

1. Double-click "Add new role".
2. Enter a name, runtime timeout and a comment, if required.

A user-defined HMI role has been created. Assign the function rights to the role.

| Symbol | Meaning |
| --- | --- |
| ![Adding a user-defined HMI role](images/145494195723_DV_resource.Stream@PNG-de-DE.png) | **Tips for effective procedure** |
| - You can also create a user-defined HMI role by copying an existing HMI role. As a result, the assigned function rights are also assigned to the copied HMI role. |  |

##### Change the data of a user-defined role

To change the data of a user-defined role, follow these steps:

1. Click in the field whose data you want to change.
2. Change the role name, runtime timeout or comment.

##### Delete user-defined role

To delete a user-defined role, follow these steps:

1. Select the user-defined role.
2. In the shortcut menu, select the "Delete" command or press the <Del> key.

#### Assigning HMI roles (RT Unified)

You can assign HMI roles with different function rights to local users and global user groups.

##### Requirement

- A project is open.
- A device has been created.
- Users and user groups have been created.
- The "Security Settings > Users and Roles" editor is open.

##### Assigning HMI roles to local users

To assign roles to a user, follow these steps:

1. Open the "Users" tab.
2. Select the user.
3. Activate the desired HMI roles in the "Assigned roles" tab.

##### Assigning HMI roles to global user groups

To assign roles to a global user group, follow these steps:

1. Open the "User groups" tab.
2. Select the user group.
3. Activate the desired HMI roles in the "Assigned roles" tab.

##### Revoking role assignments for local users

To revoke a role for a user, follow these steps:

1. Open the "Users" tab.
2. Select the user.
3. In the "Assigned roles" tab, disable the roles that you no longer want to assign to the user.

##### Revoking role assignments for global user groups

To revoke a role assignment for a global user group, follow these steps:

1. Open the "User groups" tab.
2. Select the user group. Note that you cannot use multiple selection.
3. In the "Assigned roles" tab, clear the roles that you no longer want to assign to the user group.

#### HMI role "HMI Monitor Client" (RT Unified)

The system-defined role "HMI Monitor Client" contains the function right "WinCC Unified Client Monitor - Limited Access". No other function rights can be assigned to this role.

The "HMI Monitor Client" role allows you to monitor and analyze the production process without influencing the processes in the PLC unintentionally or without authorization.

The following description applies to Unified PC and Unified Panel.

> **Note**
>
> To operate the "HMI Monitor Client", you need one or more "HMI Monitor Client" licenses depending on the number of accesses.

##### "HMI Monitor Client" role

A user who is assigned the "HMI Monitor Client" role or the "Enable HMI Monitor Client" function right contained in the role cannot make any changes or write operations in the processes, regardless of other assigned roles and function rights.

##### Restrictions of the "HMI Monitor Client" role

A user with the function right "WinCC Unified Client Monitor - Limited access" may monitor the processes but only operate them to a limited extent.

The following table shows which operations the user cannot carry out:

| Symbol | Meaning |
| --- | --- |
| Tags | Transfer value changes from external tags (PowerTags) to the PLC |
| Data logging | Clear logs |
| Write log values manually |  |
| Comment log values |  |
| Write correction values |  |
| Alarms | Acknowledge active alarms |
| Reset active alarms |  |
| Disable alarms |  |
| Enable alarms |  |
| Alarm logging | Delete alarm log |
| Comment logged alarms |  |
| Parameter set control | Process values cannot be written to the PLC with the "Write to PLC" button of the parameter set control. |
| Process values cannot be written to the PLC with the system function "LoadAndWriteParameterSet". |  |
| Process values cannot be written to the PLC with the snippet "Load Parameter Set from storage and write to PLC". |  |
| Parameters sets cannot be loaded from the parameter set memory using control tags.  Process values cannot be written to the PLC using control tags. |  |

##### Visualization in Runtime

In Runtime, the Monitor Client mode is visualized by an orange frame around the root screen.

![Visualization in Runtime](images/143146788875_DV_resource.Stream@PNG-en-US.png)

##### Activating Monitor Client mode

To activate the Monitor Client mode, follow these steps:

1. Create a user or select an existing user.
2. Assign one of the following roles to the user:

   - The system-defined role "HMI Monitor Client".
   - A user-defined role that contains the function right "WinCC Unified Client Monitor - Limited access".

   ![Activating Monitor Client mode](images/168412146699_DV_resource.Stream@PNG-en-US.png)
3. The user logs on to Runtime.
4. The Monitor Client mode is activated.

The user is allowed to monitor the process but not to change any values that are relevant for the process. These values are listed at the top of the table.

---

**See also**

[System-defined function rights (RT Unified)](#system-defined-function-rights-rt-unified)
  
[Managing HMI roles (RT Unified)](#managing-hmi-roles-rt-unified)

### Function rights (RT Unified)

This section contains information on the following topics:

- [System-defined function rights (RT Unified)](#system-defined-function-rights-rt-unified)
- [User-defined function rights (RT Unified)](#user-defined-function-rights-rt-unified)
- [Assigning function rights to an HMI role (RT Unified)](#assigning-function-rights-to-an-hmi-role-rt-unified)

#### System-defined function rights (RT Unified)

You can assign the different system-defined function rights to the HMI roles. These function rights specify which functions a user may use in Runtime. You cannot rename or delete the system-defined function rights.

##### Function rights on the screen objects

The following table shows an overview of the function rights that are set on the screen objects. These function rights have no pre-defined meaning.

The meaning of the function rights comes from the objects that are protected and trigger an action.

| Function right | Example application | HMI roles |
| --- | --- | --- |
| Operate | The user may operate access-protected objects in runtime. | HMI Administrator  HMI Operator |
| Monitor | The user may only monitor but not operate the objects. | HMI Administrator  HMI Operator  HMI Monitor |
| Remote access | The user may use Unified Collaboration to access an HMI device. | HMI Administrator |
| Remote access - Monitor only | The user may use Unified Collaboration to access an HMI device.   The user may only monitor but not operate the objects. | HMI Administrator  HMI Operator  HMI Monitor |

##### Specific function rights

The following table shows an overview of the specific function rights in the TIA Portal. These function rights are automatically checked and activate the associated functionality.

These rights are not set on the screen objects.

| Function right | Description | HMI roles |
| --- | --- | --- |
| Importing and exporting users | The user may import and export user management data in runtime.  This function right is not supported on Unified Panels. | User-defined role |
| User management | The user has permission to manage the existing users and add and manage the new users in Runtime. | HMI Administrator |
| Enable HMI Monitor Client | The user may observe the process on an HMI device to a limited extent without unintentionally or unauthorizedly influencing the processes in the PLC. | HMI Monitor Client |
| OPC UA read and write access | The user may access the data of a different device with read and write permission via OPC UA. | HMI Administrator |
| Openness Runtime read and write access | The user may access the data of a Unified runtime with read and write permission via Openness. | HMI Administrator |
| Reset UMC password | The user may reset the UMC password. | User-defined role |
| Control Panel access | The user may change the settings in the Control Panel of a Unified Panel. | HMI Administrator |

Additional function rights may be available that are associated with additional products and options that are installed.

---

**See also**

[Protecting the Control Panel from being accessed (RT Unified)](#protecting-the-control-panel-from-being-accessed-rt-unified)
  
[HMI role "HMI Monitor Client" (RT Unified)](#hmi-role-hmi-monitor-client-rt-unified)

#### User-defined function rights (RT Unified)

You can assign different runtime rights to the HMI roles. These function rights specify which functions a user may use in WinCC Unified Runtime in Runtime.

You can implement your protection concepts with the user-defined runtime rights.

##### Restrictions

Please note the following restrictions:

- You can add a maximum of 999 user-defined Runtime rights.
- The name of the user-defined runtime right and the name of the group of runtime rights can be up to 128 characters long.
- The comment may not exceed 1000 characters.

> **Note**
>
> You can use the following numbers, letters, and special characters for the names and groups of the user-defined runtime rights:
>
> - 0123456789
> - A...Z a...z
> - !#$%&()*+,-./:;<=>?@\\[]^_`{}~|
> - Spaces within the user name or password

##### Requirement

- A project is open.
- A device has been created.
- The "Security Settings > Users and Roles" editor is open.
- The "Roles" tab is open.

##### Adding a user-defined Runtime right

To add a user-defined runtime right, follow these steps:

1. Click on the "User defined runtime rights" tab.
2. In the "Function rights" area, double-click "Add new right" in the "Name" column.
3. Enter a name, a group and a comment, if required.

**Note**

The "Group" column is used to group the user-defined runtime rights in the engineering system. The assignment of the runtime rights to a group has no effect on the runtime.

A user-defined runtime right has been created. Assign the runtime right to a role.

| Symbol | Meaning |
| --- | --- |
| ![Adding a user-defined Runtime right](images/145494195723_DV_resource.Stream@PNG-de-DE.png) | **Tips for effective procedure** |
| - You can also create a user-defined runtime right by copying an existing runtime right. |  |

##### Changing the data of a user-defined runtime right

To change the data of a user-defined runtime right, follow these steps:

1. Click in the field whose data you want to change.
2. Change the name, the group or the comment.

##### Deleting a user-defined runtime right

To delete a user-defined runtime right, follow these steps:

1. Select the user-defined runtime right.
2. In the shortcut menu, select the "Delete" command or press the <Del> key.

#### Assigning function rights to an HMI role (RT Unified)

You assign the function rights to the roles.

##### Assign function rights to a user-defined role

To assign the function rights to a user-defined role, follow these steps:

1. Select the user-defined role.
2. In the "Runtime rights" tab, open the category from which you want to assign the function rights.
3. In the "Function rights" area, enable the function rights that you want to assign to the role.

##### Changing or deleting the assignment of the function rights

To change or delete the assignment of the function rights to a user-defined role, follow these steps:

1. Select the user-defined role.
2. In the "Runtime rights" tab, open the category from which you want to assign the function rights or revoke the assignment:

   - In the "Function rights" area, enable the function rights that you want to assign to the role.
   - In the "Function rights" area, disable the function rights that you no longer want to assign to the role.

##### Displaying assigned function rights of a local user

To display the assigned function rights of a local user, follow these steps:

1. Open the "Users" tab.
2. Select the user.
3. Open the "Assigned rights" tab in the lower area.
4. Expand the categories of function rights in the "Categories of function rights" column.

   The assigned function rights are displayed in the "List of rights" column.

   The roles by which the function rights are assigned to the user are displayed in the "Rights derived from role" column.

##### Display assigned function rights of a global user group

To display the assigned function rights of a global user group, follow these steps:

1. Open the "User groups" tab.
2. Select the global user group.
3. The assigned function rights are displayed in the lower area of the "Assigned rights" tab.

### Examples (RT Unified)

This section contains information on the following topics:

- [Example: Setup of the local user management (RT Unified)](#example-setup-of-the-local-user-management-rt-unified)
- [Example: Add user and assign to a role (RT Unified)](#example-add-user-and-assign-to-a-role-rt-unified)
- [Example: Add roles and assign function rights (RT Unified)](#example-add-roles-and-assign-function-rights-rt-unified)
- [Example: Configuring a button with access protection (RT Unified)](#example-configuring-a-button-with-access-protection-rt-unified)

#### Example: Setup of the local user management (RT Unified)

##### Task

In the following example, you set up a user management for different users. The example orientates itself to a typical requirement profile from manufacturing engineering.

##### Principle

Users with various roles are involved in a project. Create the users and assign them to the roles.

You can reproduce different views through the roles.

Example:

- Organizational view: Commissioners, Operators, Shift I, Shift II.
- Technological view: Axis control, Tool changers, Plant North, Plant South.

The following example orientates itself to the organizational view.

Each user has function rights for specific applications.

In the example, you create Mr. Meier, Ms. Ramos, Ms. Greenwood, Messrs. Peters and Santini. You assign roles to each user.

##### Requirements

- A new project has been created.
- The "Users and roles" editor in "Security settings" is open.

##### Procedures overview

To assign the users one or more roles, follow these steps:

1. Create the users.
2. Create the roles and assign the users one or more roles. Note the following information:

   - The function rights have been defined for the system-defined roles.
   - You assign the required function rights to the user-defined roles.
3. Configure a button with access protection.

##### Result

The goal is the following structure of the user management consisting of users, roles and function rights:

The user "Meier" has the "HMI administrator" role.

> **Note**
>
> Not all function rights that have been specified for the system-defined "HMI Administrator" role are displayed in the table.

| Users | Role | Function rights |  |  |
| --- | --- | --- | --- | --- |
| User management | Operation | Remote access |  |  |
| Meier | HMI Administrator | x | x | x |

You assign the required roles to the other persons.

| Users | Role | Function rights |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Operation | Monitoring | Remote access | User-defined runtime right  Screen change | User-defined runtime right  Toggle language | User-defined runtime right  Change parameter sets | User-defined runtime right  Delete parameter sets | User-defined runtime right  Stop Runtime |  |  |
| Ramos | HMI Operator | x | x | x |  |  |  |  |  |
| Greenwood | Operator |  |  |  | x | x |  |  |  |
| Peters | LineManager |  |  |  | x | x | x | x |  |
| Santini | Service |  |  |  | x | x | x | x | x |

#### Example: Add user and assign to a role (RT Unified)

##### Task

In the following example, you create the users and assign them to their roles. The users are sorted alphabetically immediately after the name has been entered.

##### Procedure

1. Open the "Users" work area.
2. Double-click "Add new user" in the "Users" table.
3. Enter "Meier" as the user name.
4. Click the ![Procedure](images/70589889163_DV_resource.Stream@PNG-de-DE.png) button in the "Password" column. The dialog box for entering the password is opened.
5. Enter "Meier123" as the password. The password must meet the defined password policies.
6. To confirm the password, enter it a second time in the lower field.
7. Close the dialog box by using the ![Procedure](images/84603740299_DV_resource.Stream@PNG-de-DE.png) icon.
8. Enable the "HMI Administrator" role in the "Assigned Roles" table.

##### Interim result

![Interim result](images/134930676619_DV_resource.Stream@PNG-en-US.png)

##### Procedure

1. Double-click "Add new user" in the "Users" table.
2. Enter "Ramos" as the user name.
3. Click the ![Procedure](images/70589889163_DV_resource.Stream@PNG-de-DE.png) button in the "Password" column. The dialog box for entering the password is opened.
4. Enter "Ramos123" as the password.
5. To confirm the password, enter it a second time in the lower field.
6. Close the dialog box by using the ![Procedure](images/84603740299_DV_resource.Stream@PNG-de-DE.png) icon.
7. Enable the "HMI Operator" role in the "Assigned Roles" table.
8. Repeat steps 2 to 6 for the users "Greenwood", "Peters" and "Santini".
9. Enable the user-defined roles "Operator", "LineManager" and "Service" of the individual users in the "Assigned Roles" table.

##### Result

![Result](images/138874991499_DV_resource.Stream@PNG-en-US.png)

#### Example: Add roles and assign function rights (RT Unified)

##### Task

In the following example, you create the roles and assign the function rights to the roles.

##### Procedure

1. Open the "Roles" work area.
2. Double-click "Add new role" in the "Roles" table and enter a name for the role.
3. In the "Runtime rights" table, click on "Runtime rights > WinCC Unified devices > HMI_RT_1" in the "Categories of function rights" column.
4. In the "Function rights" column, assign the desired function rights to the role.

##### Result

![Result](images/138876961163_DV_resource.Stream@PNG-en-US.png)

#### Example: Configuring a button with access protection (RT Unified)

##### Task

In the following example, you use a system function to create a button for a screen change. You protect the "To Recipe view" button against unauthorized operation. To do so, you configure the "Change parameter sets" function right at the "To Recipe view" button.

##### Requirements

- A "Change parameter sets" function right has been created.
- A "Recipes" screen has been created.
- A "Start" screen has been created and opened.
- A button has been created and marked in the "Start" screen.

##### Procedure

1. In the Inspector window, click "Properties > Properties > General > Text".
2. Enter "To Recipe view" as the text.
3. Click "Properties > Events > Click left mouse button" in the Inspector window.
4. Click the "Add function" entry in the first line of the "Function list" table.
5. Select the system function "ChangeScreen" from the "Screen" group.
6. Click on the ![Procedure](images/30890839819_DV_resource.Stream@PNG-de-DE.png) button in the "Screen name" row of the "Value" column. A dialog box for selecting the screen opens.
7. Select the "Recipes" screen and use the ![Procedure](images/84603740299_DV_resource.Stream@PNG-de-DE.png) button to close the dialog box.
8. Click "Properties > Properties > Security" in the Inspector window.
9. Select "Change parameter sets" as function right.

##### Result

![Result](images/138899563787_DV_resource.Stream@PNG-en-US.png)

Access to the "To Recipe view" button is protected. If the user "Greenwood" clicks the button in Runtime, for example, the "Recipes" screen opens. Requirement:

- The user "Greenwood" has logged on correctly and has the required function right.
- The "Recipes" screen contains a recipe view and other screen objects.

> **Note**
>
> If the logged-on user does not have the required function right or if no user is logged on, the "Logon dialog box" is displayed. An alarm indicating that no operator authorization is available for this user appears in Runtime.

## Using user management on the Unified Panel (RT Unified)

This section contains information on the following topics:

- [Notes on commissioning (RT Unified)](#notes-on-commissioning-rt-unified)
- [User management on the Unified Panel (RT Unified)](#user-management-on-the-unified-panel-rt-unified)
- [Protecting the Control Panel from being accessed (RT Unified)](#protecting-the-control-panel-from-being-accessed-rt-unified)
- [Managing local users (RT Unified)](#managing-local-users-rt-unified-1)
- [Using central user management (RT Unified)](#using-central-user-management-rt-unified)

### Notes on commissioning (RT Unified)

#### Commissioning with central user management

To ensure that the connection to the central user management is set up during initial commissioning of the Panel, we recommend that you do not activate any access protection for the Control Panel on the Panel.

If the access protection is not activated for the Control Panel, configure the connection to the central user management in the Control Panel.

If the access protection for the Control Panel is activated and no connection could be set up during commissioning for the central user management, you have the following options:

- Download the project and the settings for user management from the engineering system.
- Reset the Panel to the factory settings.

> **Note**
>
> **Failure of the network connection**
>
> If the network connection to the central user management fails, all users who have already logged on to the project once before can still log on for some time. When the connection to the central user management has been restored, other users can log on once again as well.

### User management on the Unified Panel (RT Unified)

In the engineering system, you can specify whether you want to work with local or central users and user groups from the central user management on a Unified Panel. By default, the use of the local user management is specified in the engineering system.

> **Note**
>
> You can only switch between local and central user management in the engineering system.

To manage users in Runtime, you require the "User management" function right. Configure a user with the required rights in the engineering system and load the user into Runtime.

### Protecting the Control Panel from being accessed (RT Unified)

In the engineering system, you can protect the Control Panel of a Unified Panel from unauthorized access. You can assign a user the access right for changes on the Control Panel.

#### Requirement

- A project is open.
- A user has been created in the engineering system.
- A user-defined role has been created.
- A Unified Panel has been created.

#### Assign access right to Control Panel to a user

To assign a user the function right "Control Panel access" to access the Control Panel, follow these steps:

1. Open the "Security settings" folder in the project tree.
2. Double-click on "Users and roles".

   The "Users and roles" editor opens in the work area.
3. Open the "Roles" tab.
4. Select a user-defined role.
5. In the lower area "Function rights categories", open the category of the Runtime rights.
6. Click on the Unified Panels category.
7. In the lower area "Function rights", activate the function right "Control Panel access ".
8. Open the "Users" tab.
9. Select a user.
10. In the area "Assigned roles", activate the user-defined role to which you have assigned the function right for access to the Control Panel.

The user receives the access right for the Unified Control Panel and is permitted to change the Panel settings.

#### Activate access control for Control Panel

In addition, activate the access control in the Control Panel:

1. Start the Panel.
2. Open the Control Panel.
3. Under "Security > Control Panel Access", activate the access control for the Control Panel.

> **Note**
>
> In contrast to the Unified PC Runtime, no login in required. When you open the protected Control Panel, your user rights are checked. If you do not have the necessary rights, a login window is displayed.

---

**See also**

[System-defined function rights (RT Unified)](#system-defined-function-rights-rt-unified)
  
[Using central user management in the Control Panel (RT Unified)](#using-central-user-management-in-the-control-panel-rt-unified)

### Managing local users (RT Unified)

This section contains information on the following topics:

- [Options for local user management (RT Unified)](#options-for-local-user-management-rt-unified)
- [Using local user management in the Control Panel (RT Unified)](#using-local-user-management-in-the-control-panel-rt-unified)
- [Opening local user management in the "Browser" screen object (RT Unified)](#opening-local-user-management-in-the-browser-screen-object-rt-unified)
- [Opening local user management in the Internet browser (RT Unified)](#opening-local-user-management-in-the-internet-browser-rt-unified)
- [Managing local users in Runtime (RT Unified)](#managing-local-users-in-runtime-rt-unified)

#### Options for local user management (RT Unified)

To manage local users in Runtime, the user requires the "User management" function right on the HMI device.

##### Managing local users

You have the following options for managing local users:

1. Control Panel of the Unified Panel. You can find all information in the "[SIMATIC HMI devices Unified Comfort Panels](https://support.industry.siemens.com/cs/ww/en/view/109773257)" manual.
2. Via the "Browser" screen object in a project.
3. Using an Internet browser on a PC.

#### Using local user management in the Control Panel (RT Unified)

If access protection is configured for the Control Panel in the Engineering System, you need the "Control Panel access" function right. If you do not have the necessary rights, a login window is displayed.

You cannot make any changes to the user management in the Control Panel.

##### Local user management in the Control Panel

To use the user management on the Unified Panel, follow these steps:

1. Select "Security" in the navigation.
2. Click "User management settings".
3. In the "Configuration of user management" dialog, you can see whether the local or central user management is enabled.

![Local user management in the Control Panel](images/142544803723_DV_resource.Stream@PNG-en-US.png)

> **Note**
>
> If you have made changes to the Runtime settings in the "Security" area in the Engineering System, you must ensure before loading that the page "Security > User management settings" is closed in the Control Panel of the Unified Panel. Otherwise, the changes may not be applied after loading.

#### Opening local user management in the "Browser" screen object (RT Unified)

In Runtime, you access local user management of a Panel by using the "Browser" screen object in a screen.

The detailed description of the individual steps in Runtime can be found in the section "[Managing local users in Runtime](#managing-local-users-in-runtime-rt-unified)".

> **Note**
>
> The specific possible operations depend on the function right.

##### Requirement

- To access the user management, the user must have the "User management" or "Monitor" function right.
- To access the Control Panel, the user must have the "Control Panel access" function right.
- A screen with the "Browser" screen object is displayed in Runtime.

##### Managing local user in the "Browser" screen object

If you want to manage local users in the "Browser" screen object, follow these steps:

1. Enter the address "https://localhost/umc" in the "Browser" screen object. The "User login" dialog is displayed.
2. Log in to the user management. The home page of the user management opens.

   ![Managing local user in the "Browser" screen object](images/159514733451_DV_resource.Stream@PNG-en-US.png)

   ![Managing local user in the "Browser" screen object](images/159514733451_DV_resource.Stream@PNG-en-US.png)
3. Select "Users" in the menu. The user list is displayed.
4. You manage the user information in the user list with the buttons "Add user", "Details", "Edit" and "Delete".

##### Users without "User management" function right

If you do not have the "User management" function right, you can only select your own "User profile" and change your own password.

#### Opening local user management in the Internet browser (RT Unified)

From a PC, you access local user management of a Panel via an Internet browser.

The detailed description of the individual steps in Runtime can be found in the section "[Managing local users in Runtime](#managing-local-users-in-runtime-rt-unified)".

> **Note**
>
> The specific possible operations depend on the function right.

##### Requirement

- To access the user management, the user must have the "User management" or "Monitor" function right.
- To access the Control Panel, the user must have the "Control Panel access" function right.
- Internet browser is open.

##### Managing local users in the web browser

If you want to manage local users in the Internet browser, follow these steps:

1. In the address line of the browser, enter the IP address of the Unified Panel "https://<UCP-IP>/umc". The "User login" dialog is displayed.
2. Log in to the user management. The home page of the user management opens.

   ![Managing local users in the web browser](images/159514733451_DV_resource.Stream@PNG-en-US.png)

   ![Managing local users in the web browser](images/159514733451_DV_resource.Stream@PNG-en-US.png)
3. Select "Users" in the menu. The user list is displayed.
4. You manage the user information in the user list with the buttons "Add user", "Details", "Edit" and "Delete".

##### Users without "User management" function right

If you do not have the "User management" function right, you can only select your own "User profile" and change your own password.

#### Managing local users in Runtime (RT Unified)

This section contains information on the following topics:

- [Changing your password (RT Unified)](#changing-your-password-rt-unified)
- [Editing password, status or role (RT Unified)](#editing-password-status-or-role-rt-unified)
- [Adding users (RT Unified)](#adding-users-rt-unified)
- [Deleting users (RT Unified)](#deleting-users-rt-unified)

##### Changing your password (RT Unified)

###### Introduction

You can change your own password in the user management.

###### Requirement

- You have the "User management" function right.
- The home page of the user management is open.

  ![Requirement](images/159514733451_DV_resource.Stream@PNG-en-US.png)

###### Procedure

To change the password, follow these steps:

1. Select "User profile" directly on the home page or in the menu.

   The "Change Password" dialog is displayed.

   ![Procedure](images/159527654795_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/159527654795_DV_resource.Stream@PNG-en-US.png)
2. Change the password and save the change with the "Change" button. The password must meet the password policies.

##### Editing password, status or role (RT Unified)

###### Introduction

In the user list you can edit the password, the status or the role of a user.

###### Requirement

- You have the "User management" function right.
- The home page of the user management is open.

###### Changing the password

To change the password of a user, follow these steps:

1. Select "Users" in the menu. The user list is displayed.
2. Select a user and click the "Details" button.
3. Enter the new password in the "Password" tab and confirm the password.
4. Confirm your entries with the "Apply" button.  
   Save the settings with "OK".

   ![Changing the password](images/159528166283_DV_resource.Stream@PNG-en-US.png)

   ![Changing the password](images/159528166283_DV_resource.Stream@PNG-en-US.png)

###### Changing the status

To edit the status of a user, follow these steps:

1. Select "Users" in the menu. The user list is displayed.
2. Select a user and click the "Details" button.
3. In the "Status" tab, you can disable the user or keep this user from changing the password. You cannot change the "Locked" property.
4. Confirm your entries with the "Apply" button.  
   Save the settings with "OK".

   ![Changing the status](images/159528170635_DV_resource.Stream@PNG-en-US.png)

   ![Changing the status](images/159528170635_DV_resource.Stream@PNG-en-US.png)

###### Changing the role

To edit the role of a user, follow these steps:

1. Select "Users" in the menu. The user list is displayed.
2. Select a user and click the "Details" button.
3. In the "Roles" tab, you can change the roles and thus the associated function rights of the user:

   - Select a role from the "Available roles" or "Assigned roles" list.
   - Change the assignment of this role using the buttons between the two lists.
   - Confirm your entries with the "Apply" button.  
     Save the settings with "OK".

   The figure below shows you how to assign the "HMI Monitor" role to a user in addition to the "HMI Operator" role.

   ![Changing the role](images/159528174987_DV_resource.Stream@PNG-en-US.png)

   ![Changing the role](images/159528174987_DV_resource.Stream@PNG-en-US.png)

> **Note**
>
> Note that at least one user in the project has the "HMI Administrator" role and at least one user has access to the Control Panel. If access to the user management or the Control Panel is not possible, a complete download from the TIA Portal is necessary.

##### Adding users (RT Unified)

###### Introduction

You can add a new user in the user list.

###### Requirement

- You have the "User management" function right.
- The home page of the user management is open.

###### Adding a new user

To add a new user, follow these steps:

1. Select "Users" in the menu. The user list is displayed.
2. In the user list, click "Add User".

   ![Adding a new user](images/159529051659_DV_resource.Stream@PNG-en-US.png)

   ![Adding a new user](images/159529051659_DV_resource.Stream@PNG-en-US.png)
3. A new row is displayed for the new user in the user list. Enter the information of the new user in the row.
4. Click "Details" in the user list. Assign roles to the new user.

   ![Adding a new user](images/159529056011_DV_resource.Stream@PNG-en-US.png)

   ![Adding a new user](images/159529056011_DV_resource.Stream@PNG-en-US.png)
5. Confirm your entries with the "Apply" button.  
   Save the settings with "OK".

##### Deleting users (RT Unified)

###### Introduction

You can delete a user in the user list.

###### Requirement

- You have the "User management" function right.
- The home page of the user management is open.

###### Deleting users

To delete a user, follow these steps:

1. Select "Users" in the menu. The user list is displayed.
2. Select the user.
3. Click the "Delete" button in the row. The user is deleted.

Deleting the user from the user list will become effective once the user logs off in Runtime.

### Using central user management (RT Unified)

This section contains information on the following topics:

- [Using central user management in the Control Panel (RT Unified)](#using-central-user-management-in-the-control-panel-rt-unified)
- [Simulating a central user management (RT Unified)](#simulating-a-central-user-management-rt-unified)

#### Using central user management in the Control Panel (RT Unified)

In the engineering system, you can specify whether you want to work with local or central users and user groups from the central user management on a Unified Panel. By default, the use of the local user management is specified in the engineering system.

> **Note**
>
> You can only switch between local and central user management in the engineering system.

##### Requirement

- User management has been configured in the engineering system.
- A user with the access right to the Control Panel "Access Control Panel" has been created.
- A Unified Panel has been started.

> **Note**
>
> In contrast to the Unified PC Runtime, no login in required. When you open the protected Control Panel, your user rights are checked. If you do not have the necessary rights, a login window is displayed.

##### Using user management on the Unified Panel

To use the user management on the Unified Panel, follow these steps:

1. Select "Security" in the navigation.
2. Select the "User management settings" tile.
3. In the "Configuration of user management" dialog, you can see whether the local or central user management is enabled. You can only switch between local and central user management in the engineering system.

![Using user management on the Unified Panel](images/142030480267_DV_resource.Stream@PNG-en-US.png)

##### Establishing a connection to the central user management

If you have not entered any information in the engineering system, follow these steps:

1. Enter the server address.
2. The "Connect to server" button is activated.
3. Enter the server ID manually or click the "Connect to server" button. The server ID is read in from the central user management.
4. In the "Verify user management server" dialog, confirm the displayed server.

   All input fields are filled in and write-protected. Status of the connection is "Connected".

   - The "Connect to server" button is changed to "Check connection".
   - You can check or reset the connection.

##### Adapting the connection to the central user management

If you have only entered some information in the engineering system, the input field for the missing information is marked in red. Proceed as follows in this case:

1. Enter the missing information.
2. The "Connect to server" button is activated.
3. Click "Connect to server". The server ID is read in from the central user management.
4. In the "Verify user management server" dialog, confirm the displayed server.

   All input fields are filled in and write-protected. Status of the connection is "Connected".

   - The "Connect to server" button is changed to "Check connection".
   - You can check or reset the connection.

If the entered server ID is not the same as the online server ID, you can apply the online server ID.

1. Confirm this in the "Verify user management server" dialog.

   The online server ID is read in. All input fields are filled in and write-protected. Status of the connection is "Connected".

   - The "Connect to server" button is changed to "Check connection".
   - You can check or reset the connection.

##### Verifying the connection to the central user management

You have entered all information in the engineering system. When the server ID in the engineering system and on the Panel match, the Panel is automatically connected to the central user management.

Status of the connection is not displayed. To verify the central user management on the Unified Panel, follow these steps:

1. Click "Check connection".
2. The connection to the central user management is established.

When the Panel is not connected to the central user management and no status is displayed, change the server ID.

1. The "Check connection" button is changed to "Connect to server".
2. You can make or reset the connection.

##### Resetting the connection to the central user management

If you have entered all information in the engineering system, the Panel is connected to the central UMC server. If you want to reset the central user management, follow these steps:

1. Click "Reset configuration".
2. In the "Reset central user management" dialog, confirm the reset.
3. The default is set:

   - The input field for the server address is empty and marked in red.
   - The input field for the server ID is empty.
   - The "Connect to server" button is hidden.
   - The "Reset configuration" button is hidden.

#### Simulating a central user management (RT Unified)

You want to simulate a project in which a central user management is configured for a customer. You have two options if you do not have access to the central user management of the customer:

- Configure your own central user management.
- Configure a local user management.

##### Requirement

- You know which groups and their function rights are contained in the central user management of the customer.

##### Configuring a central user management

Configure a central user management for the simulation project.

1. Create the users.
2. Create the user groups according to the customer project.
3. Assign the users to the groups.
4. Establish the connection to the central user management.
5. Start the simulation.
6. Log on in runtime.

Changes can be downloaded.

##### Configuring a local user management

Configure a local user management.

1. Create one or more users.
2. Assign the roles to the users.
3. Start the simulation.

Changes cannot be downloaded.

---

**See also**

[Simulate Unified Comfort Panel (RT Unified)](Simulate%20runtime%20%28RT%20Unified%29.md#simulate-unified-comfort-panel-rt-unified)

## Using user management on the WinCC Unified PC (RT Unified)

This section contains information on the following topics:

- [Notes on commissioning (RT Unified)](#notes-on-commissioning-rt-unified-1)
- [Setting the user management with WinCC Unified Configuration (RT Unified)](#setting-the-user-management-with-wincc-unified-configuration-rt-unified)
- [Managing multiple projects in the SIMATIC Runtime Manager (RT Unified)](#managing-multiple-projects-in-the-simatic-runtime-manager-rt-unified)
- [SIMATIC Runtime Manager users (RT Unified)](#simatic-runtime-manager-users-rt-unified)
- [Managing local users (RT Unified)](#managing-local-users-rt-unified-2)
- [Using central user management (RT Unified)](#using-central-user-management-rt-unified-1)

### Notes on commissioning (RT Unified)

#### Commissioning with central user management

To establish the connection to the central user management, configure the connection to the central user management on the PC with SIMATIC Runtime Manager.

> **Note**
>
> **Failure of the network connection**
>
> If the network connection to the central user management fails, all users who have already logged on to the project once before can still log on for some time. When the connection to the central user management has been restored, other users can log on once again as well.

---

**See also**

[SIMATIC Runtime Manager users (RT Unified)](#simatic-runtime-manager-users-rt-unified)

### Setting the user management with WinCC Unified Configuration (RT Unified)

The "WinCC Unified Configuration" application is installed with the installation of WinCC Unified. A link is automatically created on your desktop for "WinCC Unified Configuration".

You can change the setting made during setup at any time.

#### Local user management

If you exclusively edit projects with local user management in TIA Portal, use the setting "Select local or central user management in TIA Portal".

![Local user management](images/171006517771_DV_resource.Stream@PNG-en-US.png)

#### Central user management

If you exclusively edit projects with central user management in TIA Portal, use the setting "Use central user management with the following configuration".

![Central user management](images/171006522123_DV_resource.Stream@PNG-en-US.png)

#### Using local and central user management

When you edit projects with local as well as central user management, note the following special features:

"Select local or central user management in TIA Portal" setting:

- You cannot simulate projects with central user management.
- Groups and users of the central server cannot be imported into projects with central user management.

"Use central user management with the following configuration" setting:

- You cannot simulate projects with local user management.

### Managing multiple projects in the SIMATIC Runtime Manager (RT Unified)

The SIMATIC Runtime Manager is installed with the installation of WinCC Unified Runtime. A link for the SIMATIC Runtime Manager is automatically created on your desktop.

You manage the Runtime projects in the SIMATIC Runtime Manager. Multiple projects can be available on one PC. In SIMATIC Runtime Manager, you enable the matching configuration of the user data for a selected project or you adapt the configuration.

You cannot switch between local and central user management in the Runtime Manager.

---

**See also**

[Checking local user management in the SIMATIC Runtime Manager (RT Unified)](#checking-local-user-management-in-the-simatic-runtime-manager-rt-unified)
  
[Setting central user management in the SIMATIC Runtime Manager (RT Unified)](#setting-central-user-management-in-the-simatic-runtime-manager-rt-unified)

### SIMATIC Runtime Manager users (RT Unified)

#### Groups for the user management

Groups are created during the installation of WinCC Unified that enable a user to access specific WinCC Unified functions:

- **umcd_domain_manager**
- **umcd_um**
- **umcd_dsso**

To log in with single sign-on (SSO), the user must be added to the following group:

- **umcd_dsso**

#### Groups for the Runtime Manager

For a Windows user to be able to change user data in the Runtime Manager, add the user to the following groups:

- **umcd_domain_manager**
- **umcd_um**
- “SIMATIC HMI”

---

**See also**

[Notes on commissioning (RT Unified)](#notes-on-commissioning-rt-unified-1)

### Managing local users (RT Unified)

This section contains information on the following topics:

- [Checking local user management in the SIMATIC Runtime Manager (RT Unified)](#checking-local-user-management-in-the-simatic-runtime-manager-rt-unified)
- [Managing local users in Runtime (RT Unified)](#managing-local-users-in-runtime-rt-unified-1)

#### Checking local user management in the SIMATIC Runtime Manager (RT Unified)

Multiple projects can be available on one PC. In SIMATIC Runtime Manager, you can activate the matching configuration of the user data for a selected project.

You cannot switch between local and central user management.

##### Requirement

- At least one project with user management is loaded on the Runtime PC.
- WinCC Unified Runtime is installed.
- SIMATIC Runtime Manager has been started.

##### Checking local user management in the SIMATIC Runtime Manager

You cannot configure the local user management in the SIMATIC Runtime Manager.

1. In the SIMATIC Runtime Manager, click "Settings" on the home page.

   ![Checking local user management in the SIMATIC Runtime Manager](images/143147444747_DV_resource.Stream@PNG-de-DE.png)

   ![Checking local user management in the SIMATIC Runtime Manager](images/143147444747_DV_resource.Stream@PNG-de-DE.png)
2. Select the "User management" tab.
3. When multiple projects are available on the PC, select the configuration of the user management of a project under "Select configuration".
4. To activate the local user data of the selected project, click "Load user management".
5. The status of the local user management is displayed. You check the status of the local user management with the "Check status" button.

   ![Checking local user management in the SIMATIC Runtime Manager](images/143147448203_DV_resource.Stream@PNG-de-DE.png)

   ![Checking local user management in the SIMATIC Runtime Manager](images/143147448203_DV_resource.Stream@PNG-de-DE.png)

**Note**

When you click "Load user management", the changes of the user management that you have made in runtime are overwritten by the configuration of the last download.

---

**See also**

[Managing multiple projects in the SIMATIC Runtime Manager (RT Unified)](#managing-multiple-projects-in-the-simatic-runtime-manager-rt-unified)

#### Managing local users in Runtime (RT Unified)

This section contains information on the following topics:

- [User logon (RT Unified)](#user-logon-rt-unified)
- [Structure of the start page (RT Unified)](#structure-of-the-start-page-rt-unified)
- [Changing your password (RT Unified)](#changing-your-password-rt-unified-1)
- [Managing the user list (RT Unified)](#managing-the-user-list-rt-unified)
- [Changing the password of a different user (RT Unified)](#changing-the-password-of-a-different-user-rt-unified)
- [Editing password, status or role (RT Unified)](#editing-password-status-or-role-rt-unified-1)
- [Adding users (RT Unified)](#adding-users-rt-unified-1)
- [Deleting users (RT Unified)](#deleting-users-rt-unified-1)
- [Logging a user out (RT Unified)](#logging-a-user-out-rt-unified)

##### User logon (RT Unified)

###### Introduction

From a PC, you access local user management via an Internet browser.

To manage the local users on a Unified PC, you require the "User management" function rights. Configure a user with the required rights in the engineering system and load the user into Runtime.

> **Note**
>
> The specific possible operations depend on the function right.

###### Requirement

- The user has the "User management" function rights.
- Internet browser is open.

###### Logging on to the user management

To log on to the user management in Runtime, follow these steps:

1. In the browser, enter the IP address of the Runtime PC "https://<PC-IP>/umc". If runtime is installed on the same PC as the browser, enter the address "https://localhost/umc".

   The start page of Runtime is displayed.

   ![Logging on to the user management](images/159584693387_DV_resource.Stream@PNG-en-US.png)

   ![Logging on to the user management](images/159584693387_DV_resource.Stream@PNG-en-US.png)
2. Click the "User management" button. The "User login" dialog is displayed.

   ![Logging on to the user management](images/172398963339_DV_resource.Stream@PNG-en-US.png)

   ![Logging on to the user management](images/172398963339_DV_resource.Stream@PNG-en-US.png)
3. Type in the user name and password.
4. If required, use the selection list to change the displayed language.
5. Click "Login".

   The user management start page opens in Runtime.

   ![Logging on to the user management](images/159514733451_DV_resource.Stream@PNG-en-US.png)

   ![Logging on to the user management](images/159514733451_DV_resource.Stream@PNG-en-US.png)

---

**See also**

[Managing local users in Runtime (RT Unified)](#managing-local-users-in-runtime-rt-unified-1)

##### Structure of the start page (RT Unified)

###### Introduction

In menu on the start page, select whether you want to manage the users, change the password or language, or log out. You can find the menu via the drop-down list in the upper right corner.

> **Note**
>
> Users with the "User management" function right have access to all functions.
>
> Users without the "User management" function right can change their password under "User profile".

###### Menu

The following options are available to you under the symbols in the menu:

- "Home"

  This takes you to the start page of the user management.
- "Users"

  You can create new users or manage the existing users.
- "User profile"

  You can change your password and switch the language.
- "Logoff"

  You will be logged out directly and can log in again.

![Menu](images/159514733451_DV_resource.Stream@PNG-en-US.png)

##### Changing your password (RT Unified)

###### Introduction

You can change your own password in the user management.

###### Requirement

- You have the "User management" function right.
- The home page of the user management is open.

  ![Requirement](images/159514733451_DV_resource.Stream@PNG-en-US.png)

###### Procedure

To change the password, follow these steps:

1. Select "User profile" directly on the home page or in the menu.

   The "Change Password" dialog is displayed.

   ![Procedure](images/159527654795_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/159527654795_DV_resource.Stream@PNG-en-US.png)
2. Change the password and save the change with the "Change" button. The password must meet the password policies.

##### Managing the user list (RT Unified)

###### Introduction

In the user list you can manage the data of the other users.

###### Requirement

- You have the "User management" function right.
- The home page of the user management is open.

  ![Requirement](images/159514733451_DV_resource.Stream@PNG-en-US.png)

###### Opening a user list

To display the user list, click "Users" in the menu on the homepage.

The user list is displayed.

![Opening a user list](images/159589745547_DV_resource.Stream@PNG-en-US.png)

###### Options in the user list

In the user list you can manage the data of the user via the following buttons:

- "Add users"
- "Details"
- "Edit"
- "Clear"

In the user list, you can:

- Sort users by user name or comment.
- Filter users by user name or comment.
- Display 20 users on one page. Additional users are displayed on a new page. You can switch between the pages.

##### Changing the password of a different user (RT Unified)

###### Introduction

In the user management you can change the password of a different user. You can also edit the comment.

###### Requirement

- You have the "User management" function right.
- The home page of the user management is open.

###### Changing the password and comment

To change the password or comment of a user in the user list, follow these steps:

1. Select "Users" in the menu.

   The user list is displayed.

   ![Changing the password and comment](images/159527898379_DV_resource.Stream@PNG-en-US.png)

   ![Changing the password and comment](images/159527898379_DV_resource.Stream@PNG-en-US.png)
2. Select a user and click on "Edit" in the respective row.
3. Change the password or the comment and save the change with the "Update" button.

   ![Changing the password and comment](images/159527928331_DV_resource.Stream@PNG-en-US.png)

   ![Changing the password and comment](images/159527928331_DV_resource.Stream@PNG-en-US.png)

##### Editing password, status or role (RT Unified)

###### Introduction

In the user list you can edit the password, the status or the role of a user.

###### Requirement

- You have the "User management" function right.
- The home page of the user management is open.

###### Changing the password

To change the password of a user, follow these steps:

1. Select "Users" in the menu. The user list is displayed.
2. Select a user and click the "Details" button.
3. Enter the new password in the "Password" tab and confirm the password.
4. Confirm your entries with the "Apply" button.  
   Save the settings with "OK".

   ![Changing the password](images/159528166283_DV_resource.Stream@PNG-en-US.png)

   ![Changing the password](images/159528166283_DV_resource.Stream@PNG-en-US.png)

###### Changing the status

To edit the status of a user, follow these steps:

1. Select "Users" in the menu. The user list is displayed.
2. Select a user and click the "Details" button.
3. In the "Status" tab, you can disable the user or keep this user from changing the password. You cannot change the "Locked" property.
4. Confirm your entries with the "Apply" button.  
   Save the settings with "OK".

   ![Changing the status](images/159528170635_DV_resource.Stream@PNG-en-US.png)

   ![Changing the status](images/159528170635_DV_resource.Stream@PNG-en-US.png)

###### Changing the role

To edit the role of a user, follow these steps:

1. Select "Users" in the menu. The user list is displayed.
2. Select a user and click the "Details" button.
3. In the "Roles" tab, you can change the roles and thus the associated function rights of the user:

   - Select a role from the "Available roles" or "Assigned roles" list.
   - Change the assignment of this role using the buttons between the two lists.
   - Confirm your entries with the "Apply" button.  
     Save the settings with "OK".

   The figure below shows you how to assign the "HMI Monitor" role to a user in addition to the "HMI Operator" role.

   ![Changing the role](images/159528174987_DV_resource.Stream@PNG-en-US.png)

   ![Changing the role](images/159528174987_DV_resource.Stream@PNG-en-US.png)

> **Note**
>
> Note that at least one user in the project has the "HMI Administrator" role. If access to the user management is not possible, a complete download from the TIA Portal is necessary.

##### Adding users (RT Unified)

###### Introduction

You can add a new user in the user list.

###### Requirement

- You have the "User management" function right.
- The home page of the user management is open.

###### Adding a new user

To add a new user, follow these steps:

1. Select "Users" in the menu. The user list is displayed.
2. In the user list, click "Add User".

   ![Adding a new user](images/159529051659_DV_resource.Stream@PNG-en-US.png)

   ![Adding a new user](images/159529051659_DV_resource.Stream@PNG-en-US.png)
3. A new row is displayed for the new user in the user list. Enter the information of the new user in the row.
4. Click "Details" in the user list. Assign roles to the new user.

   ![Adding a new user](images/159529056011_DV_resource.Stream@PNG-en-US.png)

   ![Adding a new user](images/159529056011_DV_resource.Stream@PNG-en-US.png)
5. Confirm your entries with the "Apply" button.  
   Save the settings with "OK".

##### Deleting users (RT Unified)

###### Introduction

You can delete a user in the user list.

###### Requirement

- You have the "User management" function right.
- The home page of the user management is open.

###### Deleting users

To delete a user, follow these steps:

1. Select "Users" in the menu. The user list is displayed.
2. Select the user.
3. Click the "Delete" button in the row. The user is deleted.

Deleting the user from the user list will become effective once the user logs off in Runtime.

##### Logging a user out (RT Unified)

###### Introduction

You can log out from the user management.

###### Logging out

To log out, proceed as follows:

1. Close all open pages.
2. Select "Logout" from the menu.

   ![Logging out](images/159514733451_DV_resource.Stream@PNG-en-US.png)

   ![Logging out](images/159514733451_DV_resource.Stream@PNG-en-US.png)

   You are logged out from runtime and from the user management.

Newly loaded data from the TIA Portal will not be applied until the next time you log in.

### Using central user management (RT Unified)

This section contains information on the following topics:

- [Setting central user management in the SIMATIC Runtime Manager (RT Unified)](#setting-central-user-management-in-the-simatic-runtime-manager-rt-unified)
- [Simulating a central user management (RT Unified)](#simulating-a-central-user-management-rt-unified-1)
- [SwacLogin: Errors after complete download (RT Unified)](#swaclogin-errors-after-complete-download-rt-unified)

#### Setting central user management in the SIMATIC Runtime Manager (RT Unified)

Multiple projects can be available on one PC. In SIMATIC Runtime Manager, you can activate the matching configuration of the user data for a selected project.

You cannot switch between local and central user management.

##### Requirement

- At least one project with user management is loaded on the Runtime PC.
- WinCC Unified Runtime is installed.
- SIMATIC Runtime Manager has been started.

##### Checking central user management in the SIMATIC Runtime Manager

When you have entered all information in the engineering system and the connection to the central user management can be established, all information is write-protected.

1. In the SIMATIC Runtime Manager, click "Settings" on the home page.
2. Select the "User management" tab.

   ![Checking central user management in the SIMATIC Runtime Manager](images/143147451915_DV_resource.Stream@PNG-de-DE.png)

   ![Checking central user management in the SIMATIC Runtime Manager](images/143147451915_DV_resource.Stream@PNG-de-DE.png)
3. When multiple projects are available on the PC, select the configuration of the user management of a project under "Select configuration".
4. Check the information in the area "Connection to UMC server".
5. Click the "Connect to server" button.
6. If the connection was successfully established, the status of the connection changes to "Connected" and the "Connect to server" button changes to "Check connection". You can reset the connection via "Reset configuration".

##### Configuring central user management

When the connection to the central user management could not be established, you can complete the information in the SIMATIC Runtime Manager.

1. In WinCC Unified Runtime, click "Settings" on the start page.
2. Select the "User management" tab.
3. When multiple projects are available on the PC, select the configuration of the user management of a project under "Activate configuration".
4. Complete the information. The setting "Authenticate server using server ID" is not changeable.
5. Click the "Connect to server" button.
6. If the connection was successfully established, the status of the connection changes to "Connected" and the "Connect to server" button changes to "Check connection". You can reset the connection via "Reset configuration".

---

**See also**

[Managing multiple projects in the SIMATIC Runtime Manager (RT Unified)](#managing-multiple-projects-in-the-simatic-runtime-manager-rt-unified)

#### Simulating a central user management (RT Unified)

You want to simulate a project in which a central user management is configured for a customer. You have two options if you do not have access to the central user management of the customer:

- Configure your own central user management.
- Configure a local user management.

##### Requirement

- You know which groups and their function rights are contained in the central user management of the customer.

##### Configuring a central user management

Configure a central user management for the simulation project.

1. Create the users.
2. Create the user groups according to the customer project.
3. Assign the users to the groups.
4. Establish the connection to the central user management.
5. Start the simulation.
6. Log on in runtime.

Changes can be downloaded.

##### Configuring a local user management

Configure a local user management.

1. Create one or more users.
2. Assign the roles to the users.
3. Start the simulation.

Changes cannot be downloaded.

#### SwacLogin: Errors after complete download (RT Unified)

After complete download of a project to a Unified PC, an error can occur when you open the WinCC Unified home page. The error can occur regardless of whether you open the home page locally on the PC or from a different device.

A possible cause of the error is the deletion of the browser cache.

##### Error description

In "Chrome" and "MS Edge", the error is displayed with the following alarm:

![Error description](images/142866988171_DV_resource.Stream@PNG-en-US.png)

In "Firefox", the error is displayed with the following alarm:

![Error description](images/142866998283_DV_resource.Stream@PNG-en-US.png)

After accepting the warning of a potential security risk, the page remains empty in Firefox. Only the background screen is visible.

##### Remedy the error in "Chrome" and "MS Edge"

To fix the error in "Chrome" and "MS Edge", proceed as follows:

1. Open a new tab.
2. Enter the URL address of the identity provider of the UMC server in the address line of the browser. The URL is the same as the one in the error message without "/swaclogin", for example, "https://uadtbf-01.asrd-lab.net/umc-sso".
3. The page with a warning regarding the secure connection is displayed.

   ![Remedy the error in "Chrome" and "MS Edge"](images/145919451659_DV_resource.Stream@PNG-en-US.png)
4. Accept the warning by clicking on "Proceed to uadtbf-01.asrd-lab.net (unsafe)".
5. The home page with the "User login" dialog is displayed.

   ![Remedy the error in "Chrome" and "MS Edge"](images/142879972107_DV_resource.Stream@PNG-en-US.png)

##### Remedy the error in "Firefox"

To remedy the error in "Firefox", follow these steps:

1. Open a new tab.
2. Enter the URL address of the identity provider of the UMC server (ring server) in the address line of the browser, for example, "https://uadtbf-01.asrd-lab.net/umc-sso".
3. A blank page opens. Close the page.
4. Refresh the home page with the function key <F5>. The home page with the "User login" dialog is displayed.

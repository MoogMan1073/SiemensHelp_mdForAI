---
title: "SIMATIC Runtime Manager (RT Unified)"
package: WinCCUnifiedRTMan_enUS
topics: 18
devices: [RT Unified]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# SIMATIC Runtime Manager (RT Unified)

This section contains information on the following topics:

- [SIMATIC Runtime Manager functions (RT Unified)](#simatic-runtime-manager-functions-rt-unified)
- [Start Runtime Manager (RT Unified)](#start-runtime-manager-rt-unified)
- [The Runtime Manager user interface (RT Unified)](#the-runtime-manager-user-interface-rt-unified)
- [Starting the project (RT Unified)](#starting-the-project-rt-unified)
- [Adding a project (RT Unified)](#adding-a-project-rt-unified)
- [Selecting an autostart project (RT Unified)](#selecting-an-autostart-project-rt-unified)
- [Restoring and deleting log segments (RT Unified)](#restoring-and-deleting-log-segments-rt-unified)
- [Enter password (RT Unified)](#enter-password-rt-unified)
- [Setting general settings (RT Unified)](#setting-general-settings-rt-unified)
- [Activating automatic login (RT Unified)](#activating-automatic-login-rt-unified)
- [Configuring security settings (RT Unified)](#configuring-security-settings-rt-unified)
- [Managing certificates (RT Unified)](#managing-certificates-rt-unified)
- [Exporting tags via the OPC UA server (RT Unified)](#exporting-tags-via-the-opc-ua-server-rt-unified)
- [Activating user management (RT Unified)](#activating-user-management-rt-unified)
- [Setting the Runtime Script Debugger settings (RT Unified)](#setting-the-runtime-script-debugger-settings-rt-unified)
- [Enabling telemetry service (RT Unified)](#enabling-telemetry-service-rt-unified)
- [Operation via command line (RT Unified)](#operation-via-command-line-rt-unified)

## SIMATIC Runtime Manager functions (RT Unified)

### Introduction

The SIMATIC Runtime Manager offers the following options for WinCC Unified PC:

- Use the project list to get an overview of the projects loaded into the Runtime and their properties.

  See [The Runtime Manager user interface](#the-runtime-manager-user-interface-rt-unified).
- Manually start and stop a project loaded into the Runtime.

  See [Starting the project](#starting-the-project-rt-unified).
- Define a project that is started automatically when the HMI device starts up.

  See [Selecting an autostart project](#selecting-an-autostart-project-rt-unified).
- Restore log segments in Runtime and delete restored segments.

  See [Restoring and deleting log segments](#restoring-and-deleting-log-segments-rt-unified).
- Load a project from an external storage medium into Runtime.

  See [Adding a project](#adding-a-project-rt-unified).
- Make the following settings, if required:

  |  |  |  |
  | --- | --- | --- |
  | Password | Enter the password that is used by the Runtime Manager for secure communication with Runtime. | See [Enter password](#enter-password-rt-unified). |
  | Autoscaling | Enable automatic adaptation of the HMI screens to the window size of the browser in which the Runtime project is displayed (autoscale). | See [Setting general settings](#setting-general-settings-rt-unified). |
  | Language | Change the user interface language of the Runtime Manager. |  |
  | Automatic login | Enable automatic login for a local web client of a Unified PC. | See [Activating automatic login](#activating-automatic-login-rt-unified). |
  | Start external processes | Enable the start of external processes from runtime. | See [Configuring security settings](#configuring-security-settings-rt-unified). |
  | OPC UA Export | Export the tags of the project running in Runtime into an XML file via the OPC UA server. | See [Exporting tags via the OPC UA server](#exporting-tags-via-the-opc-ua-server-rt-unified). |
  | User management | Enable the user administration of the project running in Runtime. | See [Activating user management](#activating-user-management-rt-unified). |
  | Certificates | Manage and distribute certificates of external communication partners and manage and distribute the root certificate of the Unified PC. | See [Managing certificates](#managing-certificates-rt-unified). |
  | Runtime script debugger | Configure and enable the Runtime script debugger (screen debugger and scheduler debugger). | See [Setting the Runtime Script Debugger settings](#setting-the-runtime-script-debugger-settings-rt-unified). |

## Start Runtime Manager (RT Unified)

### Requirement

WinCC Unified Runtime for PC is installed on the device.

### Procedure

Double-click the desktop link of SIMATIC Runtime Manage created during the installation of WinCC Unified Runtime.

Alternatively, start the Runtime Manager from a file explorer by double-clicking the following file: "<Path to the Unified installation directory>\bin\SIMATICRuntimeManager.exe"

For example C:\Program Files\Siemens\Automation\WinCCUnified\bin\SIMATICRuntimeManager.exe

> **Note**
>
> **Starting the Runtime Manager as administrator**
>
> Some settings under "Settings" require the Runtime Manager to be started as administrator. Right-click on the .exe and select "Run as administrator".

## The Runtime Manager user interface (RT Unified)

> **Note**
>
> **User interface language**
>
> The SIMATIC Runtime Manager starts with the language configured in the general settings. You can change the interface language. See also [Setting general settings](#setting-general-settings-rt-unified).

### Structure

The Runtime Manager has the following structure:

![Structure](images/157835756427_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Information about the server on which the Runtime is installed |
| ② | Toolbar |
| ③ | Project list |
| ④ | Button to start the project is selected in the project list |
| ⑤ | Button to stop the project is selected in the project list |
| ⑥ | Information bar |
| ⑦ | "Restore/remove database segments for logs" button |
| ⑧ | "SIMATIC Runtime Manager settings" button |

### Toolbar

The toolbar has the following buttons:

| Icon | Function |
| --- | --- |
| ![Toolbar](images/127465678347_DV_resource.Stream@PNG-de-DE.png) | Loads a project from an external storage medium into the Runtime. |
| ![Toolbar](images/127465686923_DV_resource.Stream@PNG-de-DE.png) | Deletes from the Runtime the project selected in the project list.  The project folder and the log folders are deleted. |
| ![Toolbar](images/127465759499_DV_resource.Stream@PNG-de-DE.png) | Updates the project list. |

### Content of the project list.

The project list shows all projects loaded into the Runtime.

The list provides the following information on the projects:

| Project details | Description |
| --- | --- |
| Project | Project name |
| Autostart | Indicates whether the "Autostart" option is enabled. |
| Device name | Device name |
| State | State of the associated Runtime service   Possible status values:   - Running - Partly running - Shutting down - Stopped - Unknown |
| Type | Type of the Runtime service   Project: Runtime mode  Simulation: Simulation mode |
| ID | Project-ID |

## Starting the project (RT Unified)

### Requirement

A project is loaded in runtime that does not have the "Running" state.

### Start without reset

Proceed as follows to start the project in a state that existed before the last project stop:

1. Click on the project in the project list.
2. Click the "Start" button ![Start without reset](images/134448358411_DV_resource.Stream@PNG-de-DE.png).
3. Select "Start".

### Start with reset

Proceed as follows to start the project in a state that existed during the first project start:

1. Click on the project in the project list.
2. Click the "Start" button ![Start with reset](images/134448358411_DV_resource.Stream@PNG-de-DE.png).
3. Select "Start with options".
4. Enable the options "Reset logging data" and/or "Reset Runtime data" in the "Start project options" dialog.
5. Click "Start".

### "Partly running" status

If it is not possible to start the simulation or the Unified Runtime and the status of the project is displayed as "partly running", check the following:

- Does the user currently logged on in Runtime have sufficient rights? Is the user registered in the following Windows user groups:

  - PlcSimUsers
  - RTIL Tracing Users
  - Siemens TIA Engineer
  - SIMATIC HMI
  - SIMATIC HMI VIEWER
- Is the computer name no longer than 15 characters?
- Is the "OPC UA" activated in the Runtime settings and is a certificate is available?

### Result

- The project is started.

  > **Note**
  >
  > **Activating user management**
  >
  > The login to the Runtime project requires that its user management is active in Runtime.
  >
  > After starting a project manually, you have to activate its user management manually.
- If the "Reset logging data" option was enabled, the following data is deleted when Runtime is started:

  - Logging tags
  - Logging alarms
  - Logged context values
- If the "Reset Runtime data" option was enabled, the following data originating from the last runtime of the project is deleted when Runtime is started:

  - The last values of internal, persistent tags
  - The last alarm states
  - The persistent attributes of the alarm system
  - The persistent attributes for the last logging cycle of the logging tags.

---

**See also**

[Activating user management (RT Unified)](#activating-user-management-rt-unified)

## Adding a project (RT Unified)

You have the option of loading projects from an external storage medium into Runtime with the SIMATIC Runtime Manager.

### Requirement

- The external storage medium with the Runtime project is connected to the computer.
- The Runtime Manager is open.
- To download a project for which only the changes to the project have been downloaded to the external storage medium, the following additional requirements must be met:

  - The project that is to receive the changes is running on the HMI device.
  - The Runtime ID of the running project and the project on the external storage medium match.

### Procedure

1. In the toolbar, click "Add project from offline transmission": ![Procedure](images/126350654859_DV_resource.Stream@PNG-de-DE.png)

   The "Add projects" dialog box opens.
2. Under "Select project log", click "...".

   A selection dialog opens.
3. Select the compressed ZIP folder of the Runtime project on the storage medium.
4. Click "Open".

   Under "Project information" you can see details of the selected project.
5. For a project that has been completely loaded onto the external storage medium, set the following options:

   - To start the project in Runtime after loading, select the "Start Runtime with project" option under "Options".

     Alternatively, you can start the project later in Runtime Manager.
   - Define whether project data is reset on startup.

     To start the project in a state that existed when the project was first started, activate the options "Reset logging data" or "Reset Runtime data".

     Disable these options to start the project in a state that existed before the last project stop.

     For more information on which data is reset with these options, see section [Starting the project](#starting-the-project-rt-unified).
   - Under "Check IDs", determine whether or not to check the synchronization of IDs between engineering data and runtime data.

     Check activated: If inconsistent IDs are reported, the download is canceled. The IDs are then not synchronized.

     Check not activated: The project is loaded without checking. The system cannot guarantee that the data loaded from the Engineering System match the data present in Runtime.
6. To overwrite the Runtime UMC data with UMC data from the project, select the "Overwrite UMC data with the context of the offline loading" option under "Options".
7. Confirm with "Add project".

**Note**

**Restart Runtime**

To prevent data inconsistencies, restart Runtime when you select "Do not Sync".

### Result

- The project is downloaded to Runtime and appears in the project list.
- When "Start Runtime with project" is activated: The running project is stopped and the downloaded project is started. Depending on your settings, the Runtime data and log data of the project is reset and the Runtime UMC data is overwritten by the UMC data from the project.

> **Note**
>
> When you load a project from an external storage medium, the Runtime Manager extracts the repository to a temporary folder on the target system. The transfer to Runtime takes place from this folder, which is then deleted again.

## Selecting an autostart project (RT Unified)

### Requirements

- At least one project is loaded into Runtime.
- The SIMATIC Runtime Manager is open.

### Procedure

In the project list for the desired project, select the option in the "Autostart" column.

> **Note**
>
> **Restrictions**
>
> - You can only select one project for autostart at a time.
> - The project must not have the "Simulation" project type.

### Result

The project is started automatically when the device on which the Runtime is installed is started.

## Restoring and deleting log segments (RT Unified)

In Runtime you have the option of restoring segments from logs for which a backup was created.

You can visualize the restored data in a trend control, for example.

> **Note**
>
> **Database types for backups**
>
> - Microsoft SQL
>
>   Must support the "Microsoft ODBC Driver 17 for SQL Server" driver in Version 17.9.
> - SQLite
>
>   Must support the "SQLite3" driver.

You can find more information on logs in the help of the TIA Portal.

### Requirement

- At least one backup of a tag or alarm log is available.
- A project is loaded into Runtime and is in the "Running" state.
- The SIMATIC Runtime Manager is open.

### Restoring log segments

1. Select the project.
2. Click "Restore/delete database segments for logs".

   A dialog opens.
3. Select the log type:

   - "Alarm" for alarm logs
   - "Tag" for data log
4. If required, select the relevant log in the selection menu.
5. If required, define a start time or end time.

   If you define a start time, all entries from this point in time are restored.

   If you define an end time, all entries up to this point in time are restored.

   If you define a start time and an end time, all entries between the defined points in time are restored.
6. If you have moved the backup of the log to be restored, enter the changed storage path of the backup under "Backup path".
7. Click "Restore segments".

   The selected segments are restored.

   If you have selected a time period, data may be restored beyond the selected period, as the restoration is carried out segment by segment.

   Information on the restoration can be found under "Status".

**Note**

Only one log can be restored using the "Backup path" option.

### Delete log segments

To delete all previously restored segments of the tag logs or alarm logs, follow these steps:

1. Select the log type:

   - "Alarm" for alarm logs
   - "Tag" for data log
2. Click "Delete segments".

   Information on the deletion process can be found under "Status".

**Note**

All restored segments of the selected log type are deleted regardless of the log or the defined period.

## Enter password (RT Unified)

For secure communication with Runtime, the same password must be stored in the SIMATIC Runtime Manager as in Runtime.

### Requirement

The Runtime uses secure communication.

> **Note**
>
> **Enabling secure communication**
>
> Secure communication for Runtime can be enabled as follows:
>
> - During the installation of the Runtime, in the step "Secure Download";
>
>   Or after the installation in the application "WinCC Unified Configuration".
> - In the Engineering System, if encrypted transmission is configured in the Runtime settings of a device and the option "Allow initial password transfer via unencrypted download" is enabled when downloading the device to Runtime.
>
>   After the first, unencrypted transmission, the Runtime switches to secure communication.

### Enter password for secure communication

1. Click the ![Enter password for secure communication](images/140347454603_DV_resource.Stream@PNG-de-DE.png) button in the toolbar.
2. Select the "General" tab.
3. Under "Secure connection", enter the same password that is used by Runtime for secure communication.

   For more information, refer to the "SIMATIC Unified PC Installation" user help under "Secure download".

> **Note**
>
> If Runtime does not use secure communication, the password entered here is ignored during communication with Runtime.

## Setting general settings (RT Unified)

### Enable Autoscale

Proceed as follows to automatically adapt the size of HMI screens to the window size of the browser in which a Runtime project is open:

1. Click the ![Enable Autoscale](images/140347454603_DV_resource.Stream@PNG-de-DE.png) button in the toolbar.
2. Select the "General" tab.
3. Under "Autoscale", select the "Adapt screen to window" check box.
4. Restart the currently running project or start another project that is loaded into the Runtime.

When users zoom in or out of the browser window, the HMI screens automatically adapt. Users always see the entire screen.

### Changing the user interface language

Proceed as follows:

1. Click the ![Changing the user interface language](images/140347454603_DV_resource.Stream@PNG-de-DE.png) button in the toolbar.
2. Select the "General" tab.
3. Select a language under "Language > Select language".
4. Click "OK".

   Changing the interface language requires you to restart the SIMATIC Runtime Manager. To restart the Runtime Manager directly, confirm the message that opens with "OK".

## Activating automatic login (RT Unified)

### Introduction

Automatic login to Runtime can be enabled for local web clients of a Unified PC.

A local web client is a web client located on the same HMI device as Unified Runtime.

### Requirement

- The HMI device is a Unified PC.

### Procedure

1. On the HMI device, open the SIMATIC Runtime Manager as administrator.
2. Click the button ![Procedure](images/140347454603_DV_resource.Stream@PNG-de-DE.png) in the toolbar.
3. Select the "General" tab.
4. Under "Automatic login", activate the "Enable automatic login" option.
5. Enter the user name and password of the UMC user that automatic login is to use if no UMC user is logged into Runtime via UMC Desktop Single Sign-on yet when the local web client is started or on login to Runtime.
6. Confirm your entries with "OK".
7. Restart Runtime.

### Result

- On the start of a local web client or on connection to Runtime, the web client automatically authenticates itself with the following user data:

  | A UMC user is already logged in on the HMI device via UMC Desktop Single Sign-on (DSSO) |  |
  | --- | --- |
  | Yes | The logged-in user is used. |
  | No | The user configured in SIMATIC Runtime Manager is used.  If no user has been configured in SIMATIC Runtime Manager, a hard-coded default user without function rights is used. |

  All local web clients use the same logged-in user.
- Operators see the start screen of the project running in Runtime.
- If the logged-in user does not have the authorization to operate a screen element, a login dialog opens.

  To operate the screen element, the operator must log in with a user with corresponding function rights. The open process screens remain open.
- After logout of the user used for automatic login, for example, via the "LogOff" system function, or after switchover to another user, automatic login is only possible again after Runtime is restarted.

  Logout takes effect in all applications that use DSSO. The local web client switches to the hard-coded default user without function rights. The open process screens remain open.

## Configuring security settings (RT Unified)

### Allowing start of external processes

System functions that start an external process in Runtime can be configured in the engineering.

Example: The `OpenTIAPortalProject` system function, which starts the TIA Portal, can be called in Runtime in the process diagnostics.

To allow Runtime to start an external process when such a system function is called, follow these steps:

1. On the HMI device, open the SIMATIC Runtime Manager.
2. Click the ![Allowing start of external processes](images/140347454603_DV_resource.Stream@PNG-de-DE.png) button in the toolbar.
3. Select the "Security" tab.
4. Enable the "Allow start of external processes via Unified Runtime" option.

### Enabling and disabling automatic logout

If the user management is configured accordingly, users who have been inactive in Runtime for too long are automatically logged out of Runtime. The login page is displayed.

You have the option to completely disable or re-enable the automatic logout for the HMI device.

**Requirement**

The user logged into Windows belongs to the SIMATIC HMI Windows user group.

**Procedure**

1. On the HMI device, open the SIMATIC Runtime Manager.
2. Click the ![Enabling and disabling automatic logout](images/140347454603_DV_resource.Stream@PNG-de-DE.png) button in the toolbar.
3. Select the "Security" tab.
4. Enable or disable the "Auto logout" option under "Enable automatic logout".

By default, the automatic logout is disabled.

For additional information on the configuration of the automatic logout in the user management, please refer to the help "Configuring users and roles".

---

**See also**

[Configuring automatic logoff (RT Unified)](Configuring%20users%20and%20roles%20%28RT%20Unified%29.md#configuring-automatic-logoff-rt-unified)

## Managing certificates (RT Unified)

### Introduction

Data exchange between WinCC Unified Runtime and its communication partners can be protected by certificates. The communication partners use self-signed certificates or certificates issued by a certificate authority (CA-based certificates).

In the SIMATIC Runtime Manager, you manage the certificates of the communication partners of the Unified PC (third-party certificates) in the "Certificates" tab.

You have the following options:

- Importing certificates, root certificates and CRL files
- Trust, reject, or delete certificates and root certificates already in the certificate store
- Exporting certificates, root certificates and CRL files to distribute them to other devices

  > **Note**
  >
  > **Alternative**
  >
  > If the Unified PC has its own CA-based certificates, you can also export the root certificate and CRL file of its Unified Certificate Authority using the WinCC Unified Certificate Manager application.

> **Note**
>
> **Import and export of root certificates and CRL files**
>
> A root certificate and its CRL file must be imported separately.
>
> If you have exported a root certificate, its CRL file is also exported. If required, you can also export the CRL files individually.

> **Note**
>
> Certificates of S7 controllers with an integrated connection to the Unified PC are managed system-internally. They are not visible in the SIMATIC Runtime Manager.

### Structure

![Structure](images/153675591179_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Button for importing a certificate or CRL file |
| ② | "Certificates" area  A list of the third-party certificates available in the certificate store (self-signed certificates, CA-based certificates and their root certificate). If the PC has its own CA-based certificates, you can also find the root certificate of the Unified Certificate Authority here. |
| ③ | "State" column  Shows whether the Unified PC trusts a certificate. |
| ④ | "Certificate Revocation Lists (CRL)" area  A list of the root certificate CRL files from "Certificates" |

### Requirement

- The Runtime Manager is open.
- The certificates and CRL files to be imported are located in a folder to which the Unified PC has access.

### Managing certificates

| 1. Click the ![Managing certificates](images/140347454603_DV_resource.Stream@PNG-de-DE.png) button in the toolbar. 2. Select the "Certificates" tab. 3. You can perform the following actions:       | Action | Procedure |    | --- | --- |    | Import and trust | | Symbol | Meaning | | --- | --- | | 1. Click "Import new certificate or certificate revocation list (CRL)":               ![Managing certificates](images/143169617931_DV_resource.Stream@PNG-de-DE.png)         ![Managing certificates](images/143169617931_DV_resource.Stream@PNG-de-DE.png) 2. Select the location where the certificate is stored, for example, an external data carrier, and select the certificate. 3. Confirm your input. |  |  The certificate is imported and copied to the "trusted" folder on the PC. Or the CRL file is imported. |    | Trust | Right-click on a certificate and select "Trust". The certificate is moved to the "trusted" folder on the PC. |    | Reject | Right-click the certificate and select "Reject". The certificate is moved to the "untrusted" folder on the PC. |    | Display | Right-click on a certificate and select "Show". A window with detailed information on the certificate opens. |    | Delete | Right-click on a certificate and select "Delete". The certificate is deleted from the certificate store on the PC. |    | Export | | Symbol | Meaning | | --- | --- | | 1. Right-click the certificate and select "Export". 2. If you have selected a root certificate, select the file format. 3. Select the target folder, for example, an external data storage medium. 4. Confirm your input. |  |  The certificate is copied to the target folder. If you have selected a root certificate, its CRL file is also copied. Distribute the files to the desired devices. To do this, proceed as described in the application help of the device. | |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

### Managing CRL files

| 1. Click the ![Managing CRL files](images/140347454603_DV_resource.Stream@PNG-de-DE.png) button in the toolbar. 2. Select the "Certificates" tab. 3. You can perform the following actions:       | Action | Procedure |    | --- | --- |    | Import | | Symbol | Meaning | | --- | --- | | 1. Click "Import new certificate or certificate revocation list (CRL)":               ![Managing CRL files](images/143169617931_DV_resource.Stream@PNG-de-DE.png)         ![Managing CRL files](images/143169617931_DV_resource.Stream@PNG-de-DE.png) 2. Select the location of the CRL file, e.g. an external data storage medium, and select the file. 3. Confirm your input. |  |  The file is imported and copied in the "trusted" folder on the PC. |    | Delete | Right-click on a CRL file and select "Delete". The file is deleted from the "trusted" folder on the PC. |    | Export | | Symbol | Meaning | | --- | --- | | 1. Right-click on the CRL file and select "Export". 2. Select the file format. 3. Select the target folder, for example, an external data storage medium. 4. Confirm your input. |  |  The CRL file is copied to the target folder. Distribute the files to the desired devices. To do this, proceed as described in the application help of the device. | |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## Exporting tags via the OPC UA server (RT Unified)

In the "OPC UA Export" tab, you can export the tags of the project running in Runtime via the OPC UA server into an XML file. The exported data can then be imported into another application, e.g. the TIA Portal, without the need for a connection to the OPC UA server.

The export makes it easier for you to apply an existing configuration to a new Runtime system.

You can find a detailed description in the help "OPC UA - Open Platform Communications". To do this, open the following file after installing Runtime: "<Path to the Unified installation directory>\Documentation\<Language folder>\OPCWCCU<Language code>.pdf"

For example C:\Program Files\Siemens\Automation\WinCCUnified\Documentation\English\OPCWCCUenUS.pdf

## Activating user management (RT Unified)

### Introduction

Several projects can be loaded on one Unified PC. The configuration of their user management may differ. For a successful login to a project in Runtime, the project must be running in Runtime and the appropriate user management must be active.

In the "User administration" tab, activate the appropriate user administration. For a project with central user management, you can also adapt the connection settings to the UMC server, e.g. to add missing settings in the TIA Portal or to use different settings.

**Configuring the user administration**

The user management of a project is configured in the TIA Portal under "Runtime settings > User management". In the SIMATIC Runtime Manager, it is not possible to switch a project from local to central user management.

You can find information on configuring the user management in the TIA Portal in the TIA Portal online help.

You can find information on how to configure the runtime system settings for user management during runtime installation or later with WinCC Unified Configuration here.

### Requirement

- In the Runtime system settings, it has been specified that Runtime uses the user management configuration downloaded from the TIA Portal.
- At least one user has been configured with an HMI function right for the user management active in Runtime.
- At least one user has been configured with an HMI function right for the user management that you want to activate.
- The Runtime Manager is open.
- A project is running in Runtime, and:

  - The active user management does not match the user management configured for the project.
  - For projects with central user management: The connection settings configured in the TIA Portal for the project are incomplete, or you want to use different settings.

### Procedure

| Symbol | Meaning |
| --- | --- |
| 1. Click the button ![Procedure](images/140347454603_DV_resource.Stream@PNG-de-DE.png) in the toolbar. 2. Select the "User management" tab. 3. Under "Select configuration", in the "From" list, select the project whose user management configuration you want to activate in Runtime.    Default setting after starting the Runtime Manager: The project running in Runtime 4. Confirm the confirmation prompt.    The "Operating mode" area shows the operating mode of the user management of the selected project. The displayed options are read-only. 5. If the project selected under "From" uses local user management, click "Load user management".    User management is activated in Runtime:    - The user data pre-configured in the TIA Portal for the project is loaded into the local user management.    - Runtime uses the local user management.    - The "Status" field shows the status of the user management.     | Symbol | Meaning |    | --- | --- |    |  | **Notice** |    | **Possible data loss** The user data configured in the TIA Portal overwrites the user data added or changed on the HMI device in the local user management. Data loss can occur. |  | 6. If the project selected under "From" uses central user management, proceed as follows:    - Add missing or incorrect information about the connection settings.       By default, the identity provider address is automatically generated based on the UMC server address.      To enter the address of the identity provider manually, deactivate the option "Generate the address of the identity provider automatically".      To set all fields to empty, click "Reset configuration".    - Click "Connect to server".      The system will notify you if the configured server ID and the server ID reported during the connection attempt are different from each other. To continue with the ID reported online, click "Yes"; to continue with the configured server ID, click "No".User management is activated in Runtime:    - A connection to the UMC server is established using the connection settings from the Runtime Manager.    - Runtime uses the UMC server for user management.    - If you later select the project under "From", the connection settings you entered are loaded. |  |

## Setting the Runtime Script Debugger settings (RT Unified)

The scripts of the screens and jobs of a Runtime project can be tested using the Google Chrome script debugger.

To this end, the debugger must be configured and enabled in advance in the "Script debugger" tab in the SIMATIC Runtime Manager.

---

**See also**

[Enabling the debugger (RT Unified)](Operating%20Unified%20PC%20%28RT%20Unified%29.md#enabling-the-debugger-rt-unified)

## Enabling telemetry service (RT Unified)

### Introduction

The telemetry service is used to analyze problems occurring in Runtime projects. It helps the Siemens support team to support you in analyzing and correcting such problems in the best possible way. The service generates an encrypted ECD file that combines the visual recording of the process running in runtime with the recording of detailed internal system information about the process.

The ECD file records the following information from the project running in runtime:

- Screen configuration of the visible screens
- User input with mouse and keyboard
- IO addresses of all connections
- Property values of the underlying CHROM objects

> **Note**
>
> - Enable the telemetry service only after being requested by the Siemens support team.
> - The size of the ECD file depends on the length of the recording, the number of connections and the events in the process.
> - The ECD file contains machine-specific and user-specific data such as user names, but not passwords.
>
>   This data is visible to the Siemens support team. The data is not processed or stored longer than necessary.

### Requirement

SIMATIC Runtime Manager has been started in admin mode.

### Enabling telemetry service

1. Click the ![Enabling telemetry service](images/140347454603_DV_resource.Stream@PNG-de-DE.png) button in the toolbar.
2. Select the "Telemetry settings" tab.
3. Under "Storage directory", specify the path to the directory where the ECD file is to be stored.

   Use an already existing directory.
4. Enable the "Enable telemetry" option.
5. Restart Runtime.

The telemetry service will be enabled for the currently running project.

### Next steps

1. Reproduce the error scenario in Runtime.
2. Stop the telemetry service by disabling the "Enable telemetry" option and restarting Runtime.
3. Submit the ECD file to the Siemens Support team.

## Operation via command line (RT Unified)

The SIMATIC Runtime Manager has an interface with which you can start numerous functions of the Runtime Manager via a command line program:

### Requirement

- Runtime and command line program are installed on the same device.
- For starting/stopping projects: Projects have been loaded into Runtime.

### Procedure

1. Start the command line program.
2. Enter the command line call. Separate the individual elements of the call with spaces.

   - Enter the path to the SIMATIC Runtime Manager.exe:

     "<Runtime installation directory>\bin> start /wait SIMATICRuntimeManager.exe"

     Example: C:\Program Files\Siemens\Automation\WinCCUnified\bin> start /wait SIMATICRuntimeManager.exe
   - Enter the options with which the command line program calls the Runtime Manager.

     The last option must be "-c".

     | Option | Description |
     | --- | --- |
     | `-s` | Option for starting the Runtime Manager in silent mode.  Without this option, the UI of the Runtime Manager is started when the command line call is processed. |
     | `-u` | Option to enable help messages that assist you in operating the Runtime Manager via the command line program. |
     | `-sim` | Only use this option if you call the option "-c" with the command `projectstate`, `start`, `stop` or `remove`. |
     | `-quiet` | Option for calling the Runtime Manager without output. |
     | `-o` | Option for diverting the output into an Output.txt file that is stored parallel to SIMATICRuntimeManager.exe.  You can redirect the output to another folder. The Unified Administrator must have write access to the folder.  Example:    `-o “C:\Program Files\Siemens\Automation\WinCCUnified\bin\MyOutput.txt"`   If an error occurs during the write and -quiet is not set, the error indication appears on the console. |
     | `-keepUmc` | Optional  Only in combination with the `fulldownload` command  Set the option to keep the Runtime UMC data. |
     | `-overwriteUmc` | Optional  Only in combination with the `fulldownload` command  Set this option to replace the UMC data of the Runtime with the UMC data from the project. |
     | `-c` | Option for inputting the commands that are transmitted to the Runtime Manager. |
   - After the option "-c", enter the command that the Runtime Manager should run and the argument that is transmitted to the command:

     | Command | Argument | Description |
     | --- | --- | --- |
     | `start` | <Project ID> | Starts the project. |
     | `stop` | <Project ID> | Stops the project. |
     | `projectlist` | [ALL] or [RUNNING]  Default: [ALL] | `[ALL]`: Returns a list of projects loaded in the Runtime.   `[RUNNING]`: Returns the project running in Runtime. |
     | `projectstate` | <Project ID> | Returns the state of the project running in Runtime. |
     | `remove` | <Project ID> | Removes the project from Runtime.  If the autostart option was previously set for the project: Removes the autostart option. |
     | `securemode` | <Password> | Sets the password for secure communication with SCS.  Enter the same password that Runtime uses for secure communication. |
     | `setautostart` | <Project ID> | The project is started when the device is booted.  The project must have the Project type.   The option can only be set for 1 project. |
     | `removeautostart` | <Project ID> | Removes the autostart of the project. |
     | `fulldownload` | <Log path> | Starts the full download of a TIA Portal log.  If the project is already running in Runtime, it is stopped first before the full download.  To start the project after successful download, use the command `start`. |
     | `deltadownload` | <Log path> | Starts the change loading of a TIA Portal log.  Check in advance if the corresponding project is downloaded and running in Runtime. |

     To run multiple commands, use multiple command line calls.
3. Press Enter.

### Result

- The command is executed.
- A return code with description is output in the console.

  List of possible return codes:

  | Return code | Description |
  | --- | --- |
  | 0x00000000 | Success |
  | 0x0080400b | Project already running |
  | 0x0080400c | Project started |
  | 0x0080400d | Project already stopped |
  | 0x0080400e | Project stopped |
  | 0x80000000 | General error |
  | 0x80000001 | Not supported (e. g. wrong command) |
  | 0x80000003 | Timeout during communication with SCS |
  | 0x80000004 | Invalid arguments |
  | 0x80000005 | Access denied – password required for secure connection |
  | 0x8000000C | Another project is currently flagged as autostart project, remove autostart from the other project |
  | 0x80000016 | Unable to connect to SCS |
  | 0x80804019 | Project not found |
  | 0x80B0412E | Write output file error |
  | 0x80B0412F | Autostart option cannot be set on simulation project |
  | 0x80B04130 | Empty command value |
  | 0x80B04131 | archive target path could not be created |
  | 0x80B04132 | project archive can not be extracted |
  | 0x80B04133 | DownloadTask file can not be read |
  | 0x80B04134 | Could not change UMC Data override option |
  | 0x80B04135 | Missing config folder in archive |
  | 0x80B04136 | Missing delta folder in archive |
- An output is written to the console or to the output file.

  Requirement: The command was called without the -quiet option.

### Examples

- Call a list of all projects loaded into Runtime:

  - Input: `C:\Program Files\Siemens\Automation\WinCCUnified\bin> start /wait SIMATICRuntimeManager.exe -s -c projectlist [ALL]`
  - Example output:

    `[1]`

    `Project name: T1`

    `Device name: T1`

    `Project type: Project`

    `Project ID: 0B527D12-6BBD-4F2F-BEB9-23E3C37A8932`

    `Autostart: 0`

    `[2]`

    `Project name: T2`

    `Device name: T2`

    `Project type: Project`

    `Project ID: 29DCBA1D-C615-4560-AFB4-94EB9565682C`

    `Autostart: 0`

    `[3]`

    `Project name: T3`

    `Device name: T3`

    `Project type: Project`

    `Project ID: 96FE68D0-5337-4072-A96C-F7C1D7525CAF`

    `Autostart: 0`
- Call the project running in Runtime:

  Input:

  `C:\Program Files\Siemens\Automation\WinCCUnified\bin> start /wait SIMATiCRuntimeManager.exe -s -c projectlist RUNNING`
- Query project state:

  Input:

  `C:\Program Files\Siemens\Automation\WinCCUnified\bin> start /wait SIMATICRuntimeManager.exe -s -c projectstate 96FE68D0-5337-4072-A96C-F7C1D7525CAF`
- Start a project:

  Input:

  `C:\Program Files\Siemens\Automation\WinCCUnified\bin> start /wait SIMATICRuntimeManager.exe -s -c start 96FE68D0-5337-4072-A96C-F7C1D7525CAF`
- Stop a project:

  Input:

  `C:\Program Files\Siemens\Automation\WinCCUnified\bin> start /wait SIMATICRuntimeManager.exe -s -c stop 96FE68D0-5337-4072-A96C-F7C1D7525CAF`
- Remove a project from Runtime:

  Input:

  `C:\Program Files\Siemens\Automation\WinCCUnified\bin> start /wait SIMATICRuntimeManager.exe -s -c remove 96FE68D0-5337-4072-A96C-F7C1D7525CAF`
- Example of a query regarding the state of a simulation project:

  Input:

  `C:\Program Files\Siemens\Automation\WinCCUnified\bin>SIMATICRuntimeManager.exe -s -sim -c projectstate 96FE68D0-5337-4072-A96C-F7C1D7525CAF`
- Set password for secure communication with Runtime:

  Input:

  `C:\Program Files\Siemens\Automation\WinCCUnified\bin> start /wait SIMATICRuntimeManager.exe -s -c securemode <`
  `password`
  `>`
- Enable autostart for a project:

  Input:

  `C:\Program Files\Siemens\Automation\WinCCUnified\bin> start /wait SIMATICRuntimeManager.exe -s -c setautostart 28AC5BD5-0741-42D1-B3C6-503359F32B7E`
- Disable autostart for a project:

  `C:\Program Files\Siemens\Automation\WinCCUnified\bin> start /wait SIMATICRuntimeManager.exe -s -c removeautostart 28AC5BD5-0741-42D1-B3C6-503359F32B7E`
- Perform a full download of a TIA Portal log:

  Input:

  `C:\Program Files\Siemens\Automation\WinCCUnified\bin> start /wait SIMATICRuntimeManager.exe -s -c fulldownload "C:\Users\admin\Desktop\ HMI_RT_1[Project1] - Full 2019-10-21 - 08.00.22.zip`"
- Download only the changes of a TIA Portal log (delta download):

  Input:

  `C:\Program Files\Siemens\Automation\WinCCUnified\bin> start /wait SIMATICRuntimeManager.exe -s -keepUmc -c fulldownload "C:\Users\admin\Desktop\HMI_RT_1[Project1] - Full 2020-03-27 - 11.39.51.zip"`
- Retain UMC data during full download:

  Input:

  `C:\Program Files\Siemens\Automation\WinCCUnified\bin> start /wait SIMATICRuntimeManager.exe -s -c deltadownload "C:\Users\admin\Desktop\ HMI_RT_1[Project1] - Delta 2019-10-21 - 08.03.18.zip"`
- Replace UMC data during full download:

  Input:

  `C:\Program Files\Siemens\Automation\WinCCUnified\bin> start /wait SIMATICRuntimeManager.exe -s -overwriteUmc -c fulldownload "C:\Users\admin\Desktop\HMI_RT_1[Project1] - Full 2020-03-27 - 11.39.51.zip"`
- Enable help messages:

  Input:

  `C:\Program Files\Siemens\Automation\WinCCUnified\bin> start /wait SIMATICRuntimeManager.exe -s – u`

---

**See also**

[Enabling the debugger (RT Unified)](Operating%20Unified%20PC%20%28RT%20Unified%29.md#enabling-the-debugger-rt-unified)
